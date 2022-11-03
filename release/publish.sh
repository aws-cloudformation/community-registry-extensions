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
#   PARAMETERS  Params for the stack set template
#       For example
#       [{"ParameterKey":"SchemaPackageURL","ParameterValue":"cep-handler-755952356119"}]
#
# Args: List of regions separated by spaces

set -eou pipefail

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

# Create a template specific to this resource for the stack set
cat ../publish.yml | sed "s/MyOrg::MyService::MyType/${TYPE_NAME}/g" > publish.yml

# Overwrite the role stack to fix the broken Condition.
# test-type does not use the role we register, it re-deploys the stack
cp resource-role-prod.yaml resource-role.yaml

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

ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)
HANDLER_BUCKET="cep-handler-${ACCOUNT_ID}"

# Copy the package to S3
echo "Copying schema package handler to $HANDLER_BUCKET"
aws s3 cp $ZIPFILE s3://$HANDLER_BUCKET/$ZIPFILE

# Create the stack set to register and publish the resource
STACK_SET_NAME="publish-${TYPE_NAME_LOWER}"

if ! aws --no-cli-pager cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME 2>&1 > /dev/null ; then
    echo "Creating $STACK_SET_NAME"

    aws cloudformation create-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://publish.yml \
        --parameters $PARAMETERS --capabilities CAPABILITY_NAMED_IAM

else
    
    echo "Updating $STACK_SET_NAME"

    aws cloudformation update-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://publish.yml \
        --parameters $PARAMETERS --capabilities CAPABILITY_NAMED_IAM 

fi

aws --no-cli-pager \
        cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME 

echo "About to poll for status"

STATUS="IN_PROGRESS"
check_status() {
    if ! STATUS=$(aws --no-cli-pager \
        cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME | jq .StackSet | jq -r .Status) ; then
        STATUS="IN_PROGRESS"
    fi
    echo $STATUS
}

while [ "$STATUS" != "ACTIVE" ]
do
    sleep 5
    check_status
done
echo $STATUS

echo "About to check detailed status of all instances"

IS_ANY_PENDING=1
while [ $IS_ANY_PENDING -eq 1 ]
do
    sleep 5
    IS_ANY_PENDING=0

    for region in "$@" 
    do
        echo "Checking $region"

        # Returns an error code if it hasn't been created yet
        if aws cloudformation describe-stack-instance \
            --stack-set-name $STACK_SET_NAME \
            --stack-instance-account "$ACCOUNT_ID" \
            --stack-instance-region "$region"
        then

            # Parse the detailed status if it was already created
            DETAILED_STATUS=$(aws cloudformation describe-stack-instance \
                --stack-set-name $STACK_SET_NAME \
                --stack-instance-account "$ACCOUNT_ID" \
                --stack-instance-region "$region" | jq .StackInstance | jq .StackInstanceStatus | jq -r .DetailedStatus)
            echo $DETAILED_STATUS
            if [ $DETAILED_STATUS == "PENDING" ] || [ $DETAILED_STATUS == "RUNNING" ]
            then
                IS_ANY_PENDING=1
            fi
        fi
    done
done


echo "About to create or update stack instances"

aws cloudformation create-stack-instances \
    --stack-set-name $STACK_SET_NAME \
    --accounts "$ACCOUNT_ID" \
    --regions "$@" 

