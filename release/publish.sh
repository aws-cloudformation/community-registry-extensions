#!/bin/bash

# Publish a resource type.
# This runs from prod-buildspec.yml on CodeBuild but can also be run locally.
#
# Environment variables expected: TYPE_NAME, HANDLER_BUCKET

set -euo pipefail


cfn validate
cfn generate

# Create or update the setup stack
export SETUP_STACK_NAME="setup-prod-$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
if ! aws cloudformation describe-stacks --stack-name $SETUP_STACK_NAME 2>&1 ; then
    echo "Creating $SETUP_STACK_NAME"
    aws cloudformation create-stack --stack-name $SETUP_STACK_NAME --template-body file://test/setup.yml
    aws cloudformation wait stack-create-complete --stack-name $SETUP_STACK_NAME
else
    echo "Updating $SETUP_STACK_NAME"
    update_output=$(aws cloudformation update-stack --stack-name $SETUP_STACK_NAME --template-body file://test/setup.yml --capabilities CAPABILITY_IAM 2>&1 || [ $? -ne 0 ])
    echo $update_output
    if [[ $update_output == *"ValidationError"* && $update_output == *"No updates"* ]] ; then
        echo "No updates to setup stack"
    else
        echo "Waiting for stack update to complete"
        aws cloudformation wait stack-update-complete --stack-name $SETUP_STACK_NAME
        # This just blocks forever if the previous command failed for another reason, 
        # since it never sees update stack complete
    fi
fi

# Overwrite the role stack to fix the broken Condition.
# test-type does not use the role we register, it re-deploys the stack
cp resource-role-prod.yaml resource-role.yaml

# Create the package
echo "About to run cfn submit --dry-run to create the package"
echo ""
cfn submit --dry-run
echo ""

ZIPFILE="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]').zip"
echo "ZIPFILE is $ZIPFILE"

ROLE_STACK_NAME="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')-prod-role-stack"
echo "ROLE_STACK_NAME is $ROLE_STACK_NAME"
echo ""

# Copy the package to S3
echo "Copying schema package handler to $HANDLER_BUCKET"
aws s3 cp $ZIPFILE s3://$HANDLER_BUCKET/$ZIPFILE

# Create or update the role stack
if ! aws cloudformation describe-stacks --stack-name $ROLE_STACK_NAME 2>&1 ; then
    echo "Creating role stack"
    aws cloudformation create-stack --stack-name $ROLE_STACK_NAME --template-body file://resource-role-prod.yaml --capabilities CAPABILITY_IAM
    echo ""
    aws cloudformation wait stack-create-complete --stack-name $ROLE_STACK_NAME
else
    echo "Updating role stack"
    update_output=$(aws cloudformation update-stack --stack-name $ROLE_STACK_NAME --template-body file://resource-role-prod.yaml --capabilities CAPABILITY_IAM 2>&1 || [ $? -ne 0 ])
    echo $update_output
    if [[ $update_output == *"ValidationError"* && $update_output == *"No updates"* ]] ; then
        echo "No updates to role stack"
    else
        aws cloudformation wait stack-update-complete --stack-name $ROLE_STACK_NAME
    fi
fi

echo "About to describe stack to get the role arn"
ROLE_ARN=$(aws cloudformation describe-stacks --stack-name $ROLE_STACK_NAME | jq ".Stacks|.[0]|.Outputs|.[0]|.OutputValue" | sed s/\"//g)
echo ""
echo "ROLE_ARN is $ROLE_ARN"
echo ""

# Register the type
echo "About to run register-type"
echo ""
TOKEN=$(aws cloudformation register-type --type RESOURCE --type-name $TYPE_NAME --schema-handler-package s3://$HANDLER_BUCKET/$ZIPFILE --execution-role-arn $ROLE_ARN | jq -r .RegistrationToken)

echo "Registration token is $TOKEN"

STATUS="IN_PROGRESS"

check_status() {
    STATUS=$(aws cloudformation describe-type-registration --registration-token $TOKEN | jq -r .ProgressStatus)
}

echo "About to poll status for $TOKEN"
# Check status
while [ "$STATUS" == "IN_PROGRESS" ]
do
    sleep 5
    check_status
done
echo $STATUS

# Set this version to be the default
echo "About to get latest version id"
VERSION_ID=$(aws cloudformation describe-type --type RESOURCE --type-name $TYPE_NAME | jq -r .Arn | awk -F/ '{print $NF}')
echo ""
echo "VERSION_ID is $VERSION_ID"
echo ""

echo "About to set-type-default-version"
aws cloudformation set-type-default-version --type RESOURCE --type-name $TYPE_NAME --version-id $VERSION_ID
echo ""

# TODO: Eventually we will hit the 50 version limit, how do we work around it?

# Test the resource type
echo "About to run test-type"
echo ""
TYPE_VERSION_ARN=$(aws cloudformation test-type --type RESOURCE --type-name $TYPE_NAME --log-delivery-bucket $HANDLER_BUCKET | jq .TypeVersionArn | sed s/\"//g)
echo "TYPE_VERSION_ARN is $TYPE_VERSION_ARN"
echo ""

TEST_STATUS="IN_PROGRESS"

echo "About to poll test status for $TYPE_VERSION_ARN"
check_test_status() {
    TEST_STATUS=$(aws cloudformation describe-type --arn $TYPE_VERSION_ARN | jq -r .TypeTestsStatus)
}

# Check status
while [ "$TEST_STATUS" == "IN_PROGRESS" ]
do
    sleep 5
    check_test_status
done

echo $TEST_STATUS

echo "Done"


