#!/bin/bash
#
# Deploy the publishing process to the prod account.
#
# Supply a list of regions as the command line arguments to this script.
# All other variables have to be set in the environment.
# See scripts/deploy-prod.sh

set -eou pipefail

cfn-lint cicd-prod.yml
cfn-lint cicd-prod-regional.yml

rain --profile $PROFILE deploy  \
    --params HandlerBucketName=$HANDLER_BUCKET_NAME,PublishBuildBucketName=$PUBLISH_BUILD_BUCKET_NAME,BetaAccountId=$BETA_ACCOUNT_ID \
    cicd-prod.yml cep-prod
#|| [ $? -eq 1 ]

echo "cep-prod deployed, about to deploy stack sets"

STACK_SET_NAME="cep-prod-pipelines"

if ! aws --profile $PROFILE --no-cli-pager cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME 2>&1 > /dev/null ; then
    echo "Creating $STACK_SET_NAME"

    aws --profile $PROFILE cloudformation create-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://cicd-prod-regional.yml \
        --parameters $PARAMETERS --capabilities CAPABILITY_NAMED_IAM

else
    
    echo "Updating $STACK_SET_NAME"

    aws --profile $PROFILE cloudformation update-stack-set --stack-set-name $STACK_SET_NAME \
        --template-body file://cicd-prod-regional.yml \
        --parameters $PARAMETERS --capabilities CAPABILITY_NAMED_IAM 

fi

aws --profile $PROFILE --no-cli-pager \
        cloudformation describe-stack-set --stack-set-name $STACK_SET_NAME 

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

echo "About to check detailed status of all instances"

IS_ANY_PENDING=1
while [ $IS_ANY_PENDING -eq 1 ]
do
    sleep 5
    IS_ANY_PENDING=0

    for region in "$@" 
    do
        echo "Checking $region"

        DETAILED_STATUS=$(aws --profile $PROFILE cloudformation describe-stack-instance \
            --stack-set-name $STACK_SET_NAME \
            --stack-instance-account "$ACCOUNT" \
            --stack-instance-region "$region" | jq .StackInstance | jq .StackInstanceStatus | jq -r .DetailedStatus)
        echo $DETAILED_STATUS
        if [ $DETAILED_STATUS == "PENDING" ] || [ $DETAILED_STATUS == "RUNNING" ]
        then
            IS_ANY_PENDING=1
        fi
    done
done


echo "About to create or update stack instances"

aws --profile $PROFILE cloudformation create-stack-instances \
    --stack-set-name $STACK_SET_NAME \
    --accounts "$ACCOUNT" \
    --regions "$@" 

#for region in "$@" 
#do
#    echo "$region"
#
#    if ! aws --profile $PROFILE cloudformation describe-stack-instance \
#        --stack-set-name $STACK_SET_NAME \
#        --stack-instance-account "$ACCOUNT" \
#        --stack-instance-region "$region" > /dev/null 2>&1 ; 
#    then
#        echo "Creating stack instance in $region"
#        aws --profile $PROFILE cloudformation create-stack-instances \
#            --stack-set-name $STACK_SET_NAME \
#            --accounts "$ACCOUNT" \
#            --regions "$region" 
#    else
#        echo "Updating stack instance in $region"
#        aws --profile $PROFILE cloudformation update-stack-instances \
#            --stack-set-name $STACK_SET_NAME \
#            --accounts "$ACCOUNT" \
#            --regions "$region" 
#    fi
#
#
#done



