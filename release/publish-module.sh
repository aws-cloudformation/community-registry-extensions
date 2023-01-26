#!/bin/bash
#
# Publish a module to all regions
# Run this from the module directory, for example modules/S3_Bucket/
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

cfn validate
cfn generate

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

# Create or update the setup stack
if [ -f "test/setup.yml" ]
then
    SETUP_STACK_NAME="setup-prod-$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
    if ! aws cloudformation --region $AWS_REGION describe-stacks --stack-name $SETUP_STACK_NAME 2>&1 ; then
        echo "Creating $SETUP_STACK_NAME"
        aws cloudformation --region $AWS_REGION create-stack --stack-name $SETUP_STACK_NAME --template-body file://test/setup.yml
        aws cloudformation --region $AWS_REGION wait stack-create-complete --stack-name $SETUP_STACK_NAME
    else
        echo "Updating $SETUP_STACK_NAME"
        update_output=$(aws cloudformation --region $AWS_REGION update-stack --stack-name $SETUP_STACK_NAME --template-body file://test/setup.yml --capabilities CAPABILITY_IAM 2>&1 || [ $? -ne 0 ])
        echo $update_output
        if [[ $update_output == *"ValidationError"* && $update_output == *"No updates"* ]] ; then
            echo "No updates to setup stack"
        else
            echo "Waiting for stack update to complete"
            aws cloudformation --region $AWS_REGION wait stack-update-complete --stack-name $SETUP_STACK_NAME
            # This just blocks forever if the previous command failed for another reason, 
            # since it never sees update stack complete
        fi
    fi
else
    echo "Did not find test/setup.yml, skipping setup stack"
fi

# Create the package
echo "About to run cfn submit --dry-run to create the package"
echo ""
cfn submit --dry-run
echo ""

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

if [ $"ACCOUNT_ID" == "387586997764" ]
then
    PUBLISHING_ENABLED=1
fi

HANDLER_BUCKET="cep-handler-${ACCOUNT_ID}"

# Copy the package to S3
echo "Copying schema package handler to $HANDLER_BUCKET"
aws s3 cp $ZIPFILE s3://$HANDLER_BUCKET/$ZIPFILE

# Register the type
echo "About to run register-type"
echo ""
TOKEN=$(aws cloudformation --region $AWS_REGION register-type --type MODULE --type-name $TYPE_NAME --schema-handler-package s3://$HANDLER_BUCKET/$ZIPFILE | jq -r .RegistrationToken)

echo "Registration token is $TOKEN"

STATUS="IN_PROGRESS"

check_status() {
    STATUS=$(aws cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN | jq -r .ProgressStatus)
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
aws cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN

echo "describe-type"
aws --no-cli-pager cloudformation --region $AWS_REGION describe-type --type MODULE --type-name $TYPE_NAME

sleep 5

# Set this version to be the default
echo "About to get latest version id"
VERSION_ID=$(aws cloudformation --region $AWS_REGION describe-type-registration --registration-token $TOKEN | jq -r .TypeVersionArn | awk -F/ '{print $NF}')
echo ""
echo "VERSION_ID is $VERSION_ID"
echo ""

echo "About to set-type-default-version"
aws cloudformation --region $AWS_REGION set-type-default-version --type MODULE --type-name $TYPE_NAME --version-id $VERSION_ID
echo ""

# Test the module
echo "About to run test-type"
echo ""
TYPE_VERSION_ARN=$(aws cloudformation --region $AWS_REGION test-type --type MODULE --type-name $TYPE_NAME --log-delivery-bucket $HANDLER_BUCKET | jq .TypeVersionArn | sed s/\"//g)
echo "TYPE_VERSION_ARN is $TYPE_VERSION_ARN"
echo ""

TEST_STATUS="IN_PROGRESS"

echo "About to poll test status for $TYPE_VERSION_ARN"
check_test_status() {
    TEST_STATUS=$(aws cloudformation --region $AWS_REGION describe-type --arn $TYPE_VERSION_ARN | jq -r .TypeTestsStatus)
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
    aws cloudformation --region $AWS_REGION publish-type --type MODULE --type-name $TYPE_NAME
else
    echo "PUBLISHING_ENABLED is $PUBLISHING_ENABLED, not publishing"
fi

# Delete the setup stack
# This is mainly for sandbox accounts where it would conflict with alpha
if [ -f "test/setup.yml" ]
then
    SETUP_STACK_NAME="setup-prod-$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
    aws cloudformation delete-stack --stack-name $SETUP_STACK_NAME
fi

echo "Done"


