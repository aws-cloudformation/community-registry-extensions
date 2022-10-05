#!/bin/bash

set -euo pipefail

echo "About to run cfn submit --dry-run to create the package"
echo ""

cfn submit --dry-run
echo ""

ZIPFILE="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]').zip"
echo "ZIPFILE is $ZIPFILE"

ROLE_STACK_NAME="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')-role-stack"
echo "ROLE_STACK_NAME is $ROLE_STACK_NAME"
echo ""

echo "Copying schema package handler to $HANDLER_BUCKET"
aws s3 cp $ZIPFILE s3://$HANDLER_BUCKET/$ZIPFILE

# Create or update the role stack
if ! aws cloudformation describe-stacks --stack-name $ROLE_STACK_NAME 2>&1 ; then
    echo "Creating role stack"
    aws cloudformation create-stack --stack-name $ROLE_STACK_NAME --template-body file://resource-role.yaml --capabilities CAPABILITY_IAM
    echo ""
    aws cloudformation wait stack-create-complete --stack-name $ROLE_STACK_NAME
else
    echo "Updating role stack"
    update_output=$(aws cloudformation update-stack --stack-name $ROLE_STACK_NAME --template-body file://resource-role.yaml --capabilities CAPABILITY_IAM 2>&1 || [ $? -ne 0 ])
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

echo "About to run register-type"
echo ""
TOKEN=$(aws cloudformation register-type --type RESOURCE --type-name $TYPE_NAME --schema-handler-package s3://$HANDLER_BUCKET/$ZIPFILE --execution-role-arn $ROLE_ARN | jq -r .RegistrationToken)

echo "Registration token is $TOKEN"

STATUS="IN_PROGRESS"

check_status() {
    echo "Checking status for $TOKEN..."
    STATUS=$(aws cloudformation describe-type-registration --registration-token $TOKEN | jq -r .ProgressStatus)
    echo $STATUS
}

# TODO Check status
while [ "$STATUS" == "IN_PROGRESS" ]
do
    check_status
done

echo "About to get latest version id"
VERSION_ID=$(aws cloudformation describe-type --type RESOURCE --type-name $TYPE_NAME | jq -r .Arn | awk -F/ '{print $NF}')
echo ""
echo "VERSION_ID is $VERSION_ID"
echo ""

echo "About to set-type-default-version"
aws cloudformation set-type-default-version --type RESOURCE --type-name $TYPE_NAME --version-id $VERSION_ID
echo ""

echo "About to run test-type"
echo ""
TYPE_VERSION_ARN=$(aws cloudformation test-type --type RESOURCE --type-name $TYPE_NAME --log-delivery-bucket $HANDLER_BUCKET | jq .TypeVersionArn | sed s/\"//g)
echo "TYPE_VERSION_ARN is $TYPE_VERSION_ARN"
echo ""

echo "About to run decribe-type to check test status"
echo ""
aws cloudformation describe-type --arn $TYPE_VERSION_ARN 



