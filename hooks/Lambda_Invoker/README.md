# AwsCommunity::Lambda::Invoker

This hook serves as a central control point for any number of compliance checks
that you implement as AWS Lambda functions, so you only have to install and
configure one hook, and you don't have to do any custom coding inside the hook
itself. Since Lambda functions can be invoked in a variety of ways, it is easier 
to incorporate those checks into development workflows to move security checks "left"
so that developers catch problems with their templates sooner.

## Configuration

To use this hook, you must create an Amazon DynamoDB table to use for registering your
compliance Lambda functions. The table can be created with the following
CloudFormation template snippet, or manually via the CLI or AWS console. It must have a primary
key consiting of one attribute, 'lambda\_arn'.

```yaml
  RegistrationTable:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - 
          AttributeName: "lambda_arn"
          AttributeType: "S"
      KeySchema:
        -
          AttributeName: "lambda_arn"
          KeyType: "HASH"
```

The compliance Lambda functions will be invoked with a payload that looks like this:

```json
{
    "type_name": "AWS::S3::Bucket",
    "resource_properties": {
        "BucketName": "ABC"
    }, 
    "operation": "create|update|delete"
}
```

It's up to you to create and maintain those Lambda functions. If the resource 
fails your compliance checks, raise an Exception in your Lambda function.
The Hook will summarize all function errors in the error message returned by 
CloudFormation when the stack operation fails.


