#!/bin/bash
#
# Publish a resource type to all regions
# Run this from the resource directory, for example S3_DeleteBucketContents/
#
# See scripts/publish.sh for an example of how to call it
# 
# Environment:
#
#   AWS_PROFILE (If a default profile is not set)
#
# Args: 
#
#   $1 The region to publish to

set -eou pipefail

export AWS_REGION=$1
EXT_TYPE=$(cat .rpdk-config | jq -r .artifact_type)
TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

echo "About to publish $EXT_TYPE $TYPE_NAME to $AWS_REGION"

# Create or update the setup stack
SETUP_STACK_NAME="setup-prod-$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
if [ -f "test/setup.yml" ]
then
    rain deploy test/setup.yml $SETUP_STACK_NAME -y
else
    echo "Did not find test/setup.yml, skipping setup stack"
fi

# For example, awscommunity-s3-deletebucketcontents
TYPE_NAME_LOWER="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
echo "TYPE_NAME_LOWER is $TYPE_NAME_LOWER"

ZIPFILE="${TYPE_NAME_LOWER}.zip"
echo "ZIPFILE is $ZIPFILE"

# By default we won't actually publish, so that this script can be run in 
# sandbox accounts that are not the actual publishing account
PUBLISHING_ENABLED=0

ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)
echo "ACCOUNT_ID is $ACCOUNT_ID"

if [ "$ACCOUNT_ID" == "387586997764" ]
then
    PUBLISHING_ENABLED=1
fi

echo "PUBLISHING_ENABLED: $PUBLISHING_ENABLED"

HANDLER_BUCKET="cep-handler-${ACCOUNT_ID}"

# The execution role is not required by modules
if [ "$EXT_TYPE" != "MODULE" ]
then
    EXT_TYPE_LOWER="$(echo $EXT_TYPE | tr '[:upper:]' '[:lower:]')"
    echo "EXT_TYPE_LOWER is $EXT_TYPE_LOWER"
    # Overwrite the role stack to fix the broken Condition.
    # test-type does not use the role we register, it re-deploys the stack
    cp $EXT_TYPE_LOWER-role-prod.yaml $EXT_TYPE_LOWER-role.yaml

    ROLE_STACK_NAME="$(echo $TYPE_NAME | sed s/::/-/g | tr ‘[:upper:]’ ‘[:lower:]’)-prod-role-stack"
    echo "ROLE_STACK_NAME is $ROLE_STACK_NAME"
    echo ""

    # Create or update the role stack
    rain deploy $EXT_TYPE_LOWER-role.yaml $ROLE_STACK_NAME -y

    echo "About to describe stack to get the role arn"
    ROLE_ARN=$(aws --no-cli-pager cloudformation --region $AWS_REGION describe-stacks --stack-name $ROLE_STACK_NAME | jq ".Stacks|.[0]|.Outputs|.[0]|.OutputValue" | sed s/\"//g)
    echo ""
    echo "ROLE_ARN is $ROLE_ARN"
    echo ""

    # Register the resource or hook
    echo "About to run register-type"
    echo ""
    TOKEN=$(aws --no-cli-pager cloudformation --region $AWS_REGION register-type --type $EXT_TYPE --type-name $TYPE_NAME --schema-handler-package s3://$HANDLER_BUCKET/$ZIPFILE --execution-role-arn $ROLE_ARN | jq -r .RegistrationToken)

    echo "Registration token is $TOKEN"

else
    # Register the module
    echo "About to run register-type"
    echo ""
    TOKEN=$(aws --no-cli-pager cloudformation --region $AWS_REGION register-type --type $EXT_TYPE --type-name $TYPE_NAME --schema-handler-package s3://$HANDLER_BUCKET/$ZIPFILE | jq -r .RegistrationToken)

    echo "Registration token is $TOKEN"
fi

STATUS="IN_PROGRESS"

check_status() {
    STATUS=$(aws --no-cli-pager cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN | jq -r .ProgressStatus)
}

echo "About to poll status for $TOKEN"
# Check status
while [ "$STATUS" == "IN_PROGRESS" ]
do
    sleep 5
    check_status
done
echo $STATUS

echo "describe-type-registration"
aws --no-cli-pager cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN

echo "describe-type"
aws --no-cli-pager cloudformation --region $AWS_REGION describe-type --type $EXT_TYPE --type-name $TYPE_NAME

sleep 5

# Set this version to be the default
echo "About to get latest version id"
VERSION_ID=$(aws --no-cli-pager cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN | jq -r .TypeVersionArn | awk -F/ '{print $NF}')
echo ""
echo "VERSION_ID is $VERSION_ID"
echo ""

echo "About to set-type-default-version"
aws --no-cli-pager cloudformation --region $AWS_REGION set-type-default-version --type $EXT_TYPE --type-name $TYPE_NAME --version-id $VERSION_ID
echo ""

# Modules don't have type config
if [ "$EXT_TYPE" != "MODULE" ]
then
    # Set the type configuration
    if [ -f "get_type_configuration.py" ]
    then
        echo "About to set type configuration"
        TYPE_CONFIG_PATH=$(python get_type_configuration.py)
        echo "TYPE_CONFIG_PATH is $TYPE_CONFIG_PATH"
        aws --no-cli-pager cloudformation set-type-configuration --type $EXT_TYPE --type-name $TYPE_NAME --configuration-alias default --configuration $(cat ${TYPE_CONFIG_PATH} | jq -c "")
    else
        echo "Did not find get_type_configuration.py, skipping type configuration"
    fi
fi

TEST_STATUS=""

# Test the resource type
echo "About to run test-type"
echo ""
TYPE_VERSION_ARN=$(aws --no-cli-pager cloudformation --region $AWS_REGION test-type --type $EXT_TYPE --type-name $TYPE_NAME --log-delivery-bucket $HANDLER_BUCKET | jq .TypeVersionArn | sed s/\"//g)
echo "TYPE_VERSION_ARN is $TYPE_VERSION_ARN"
echo ""

TEST_STATUS="IN_PROGRESS"

echo "About to poll test status for $TYPE_VERSION_ARN"
check_test_status() {
    TEST_STATUS=$(aws --no-cli-pager cloudformation --region $AWS_REGION describe-type --arn $TYPE_VERSION_ARN | jq -r .TypeTestsStatus)
}

# Check status
while [ "$TEST_STATUS" == "IN_PROGRESS" ]
do
    sleep 5
    check_test_status
done

echo $TEST_STATUS

# Publish the type
if [ "$PUBLISHING_ENABLED" -eq 1 ]
then
    echo "About to publish $TYPE_NAME in $AWS_REGION"
    aws --no-cli-pager cloudformation --region $AWS_REGION publish-type --type $EXT_TYPE --type-name $TYPE_NAME
else
    echo "PUBLISHING_ENABLED is $PUBLISHING_ENABLED, not publishing"
fi

# Delete the setup stack
# This is mainly for sandbox accounts where it would conflict with alpha
if [ -f "test/setup.yml" ]
then
    rain rm $SETUP_STACK_NAME -y
fi

if [ "$TEST_STATUS" == "FAILED" ] 
then
    exit 1    
fi

echo "Done"


