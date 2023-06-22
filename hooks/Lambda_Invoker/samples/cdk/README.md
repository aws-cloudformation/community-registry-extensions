# AwsCommunity::Lambda::Invoker Hook CDK Sample

This is a sample of the constructs and stacks that a CCoE team might 
create using CDK to implement compliance checks that will apply 
to all stack operations in the environment (account/region) where 
this app is deployed. Writing and deploying a CDK application like this 
is much simpler than authoring and publishing a hook for the registry.

## Prerequisites

This sample assumes that you have already activated the hook, and that 
you have separately created the DynamoDB table to hold the Lambda function
ARNs. The table ARN must be configured in app.py.


