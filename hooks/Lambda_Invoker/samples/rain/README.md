# Sample usage for AwsCommunity::Lambda::Invoker hook

This is a sample for how to write and deploy resources to enable compliance 
checks on CloudFormation templates using the `AwsCommunity::Lambda::Invoker` hook.
This hook is a central point for invoking a series of Lambda functions that you 
write to check templates before they are deployed. These lambda functions can 
also be easily invoked by template developers before deployment, to catch errors
early.

## Pre-requisites

Make sure you have activated the public resource type `AwsCommunity::DynamoDB::Item` 
in your account/region before deploying this sample.

## Files

### compliance.yaml

This template creates the registration table in DynamoDB to store the Arns of
your lambda functions. It also uses a
[rain](https://github.com/aws-cloudformation/rain) module to simplify the
template by encapsulating the CloudFormation code needed to register the
functions.

### deploy.sh

This script assumes you are privately registering the hook. It packages and deploys 
`compliance.yaml`, and then registers the hook with CloudFormation.

### module.yaml

This is a rain, module, which is a snippet of CloudFormation that inherits from 
`AWS::Lambda::Function` to simplify the code in `compliance.yaml`.

### type-config.json

CloudFormation registry extensions must be configured when they are registered. This 
file is used to tell the hook the Arn of the DynamoDB table that contains a list of
your compliance lambda functions.

