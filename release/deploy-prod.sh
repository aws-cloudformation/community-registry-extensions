#!/bin/sh
#
# Deploy the publishing process to the prod account.
#
# Supply a list of regions as the command line arguments to this script.
# All other variables have to be set in the environment.
# See scripts/deploy-prod.sh

set -eou pipefail

cfn-lint release/cicd-prod.yml
cfn-lint release/cicd-prod-regional.yml

rain --profile $PROFILE deploy -y\
    --params SourceBucketName=$SOURCE_BUCKET_NAME,TypeRegistrationLogBucketName=$TYPE_REGISTRATION_BUCKET_NAME,HandlerBucketName=$HANDLER_BUCKET_NAME,PublishBuildBucketName=$PUBLISH_BUILD_BUCKET_NAME \
    release/cicd-prod.yml cep-prod

echo "cep-prod deployed, about to deploy stack sets"

STACK_SET_NAME="cep-prod-pipelines"
PARAMETERS=[{"ParameterKey":"Prefix","ParameterValue":"AwsCommunity"},{"ParameterKey":"PrefixLower","ParameterValue":"awscommunity"},{"ParameterKey":"PublishBuildBucketName","ParameterValue":"$PUBLISH_BUILD_BUCKET_NAME"},{"ParameterKey":"HandlerBucketName","ParameterValue":"$HANDLER_BUCKET_NAME"}]

if ! aws --profile $PROFILE --no-cli-pager cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME 2>&1 > /dev/null ; then
    echo "Creating $STACK_SET_NAME"

    aws --profile $PROFILE cloudformation create-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://cicd-prod-regional.yml \
        --parameters $PARAMETERS 

else
    
    echo "Updating $STACK_SET_NAME"

    aws --profile $PROFILE cloudformation update-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://cicd-prod-regional.yml \
        --parameters $PARAMETERS 

fi

echo "About to poll for status"

STATUS="IN_PROGRESS"
check_status() {
    if ! STATUS=$(aws --profile $PROFILE --no-cli-pager \
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

echo "About to create or update stack instances"

for region in "$@" 
do
    echo "$region"

    if ! aws --profile $PROFILE cloudformation describe-stack-instance \
        --stack-set-name $STACK_SET_NAME \
        --stack-instance-account "$ACCOUNT" \
        --stack-instance-region "$region" > /dev/null 2>&1 ; 
    then
        echo "Creating stack instance in $region"
        aws --profile $PROFILE cloudformation create-stack-instances \
            --stack-set-name $STACK_SET_NAME \
            --accounts "$ACCOUNT" \
            --regions "$region"
    else
        echo "Stack instance already exists in $region"
    fi

done



