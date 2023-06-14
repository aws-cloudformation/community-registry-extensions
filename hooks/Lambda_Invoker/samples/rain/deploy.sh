#!/usr/local/bin/bash
# 
# Run this script from the `hooks/Lambda_Invoker` directory
#
# This script assumes you are privately registering AwsCommunity::Lambda::Invoker
#

set -eoux pipefail

# Make sure we are in the correct directory
TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)
if [ "$TYPE_NAME" != "AwsCommunity::Lambda::Invoker" ]; then
    echo "This script should be run from the Lambda_Invoker directory"
    exit 1
fi
export STACK_NAME=lambda-invoker-rain-sample

# Install dependencies for the Python lambda function
mkdir -p samples/rain/lambda/dist
pip install -r samples/rain/lambda/requirements.txt --upgrade -t samples/rain/lambda/dist/ 
cp samples/rain/lambda/*py samples/rain/lambda/dist

# Package the template
rain pkg -x samples/rain/compliance.yaml > samples/rain/compliance-pkg.yaml

# Lint the packaged template
cfn-lint -i E3001 -- samples/rain/compliance-pkg.yaml

# Predict deployment failures
rain forecast -x samples/rain/compliance-pkg.yaml $STACK_NAME

# Deploy the packaged template
rain deploy samples/rain/compliance-pkg.yaml $STACK_NAME 

# Get the table arn from output
TABLE_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME \
    --query 'Stacks[0].Outputs[?OutputKey==`RegistrationTableArn`].OutputValue' \
    --output text)
echo $TABLE_ARN

# Copy the type configuration into the location where `cfn test` expects it
cat samples/rain/type-config.json | sed "s!REGISTRATION_TABLE_ARN!${TABLE_ARN}!g" > ~/.cfn-cli/typeConfiguration.json

# Submit the extension
cfn submit --set-default

# Set the configuration for this version
TYPE_CONFIG_PATH=~/.cfn-cli/typeConfiguration.json
echo "TYPE_CONFIG_PATH is $TYPE_CONFIG_PATH"
aws --no-cli-pager cloudformation set-type-configuration \
    --type HOOK --type-name $TYPE_NAME \
    --configuration-alias default \
    --configuration $(cat ${TYPE_CONFIG_PATH} | jq -c "")

