#!/usr/local/bin/bash
# Run this script from the `hooks/Lambda_Invoker` directory
set -eoux pipefail
TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)
if [ "$TYPE_NAME" != "AwsCommunity::Lambda::Invoker" ]; then
    echo "This script should be run from the Lambda_Invoker directory"
    exit 1
fi
export STACK_NAME=lambda-invoker-rain-sample
rain pkg samples/rain/compliance.yaml > samples/rain/compliance-pkg.yaml
rain deploy samples/rain/compliance-pkg.yaml $STACK_NAME 
# Get the table arn from output
TABLE_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME \
    --query 'Stacks[0].Outputs[?OutputKey==`RegistrationTableArn`].OutputValue' \
    --output text)
echo $TABLE_ARN
# Copy the type configuration into the location where cfn expects it
cat samples/rain/type-config.json | sed "s/REGISTRATION_TABLE_ARN/${TABLE_ARN}/g" > ~/.cfn-cli/typeConfiguration.json
# Submit the extension with the new configuration
cfn submit --dry-run

