# AwsCommunity::Lambda::Invoker

This hook serves as a central control point for any number of compliance checks
that you implement as Lambda functions, so you only have to install and
configure one hook, and you don't have to do any custom coding inside the hook
itself. Since Lambda functions can be invoked in a variety of ways, it is easier 
to incorporate those checks into development workflows to move security checks "left"
so that developers catch problems with their templates sooner.

## Configuration

To use this hook, you must create a DynamoDB table to use for registering your
compliance Lambda functions. The table can be created with the following
CloudFormation or manually via the CLI or AWS console. It must have a primary
key consiting of two attributes, 'pk' and 'sk'. The 'pk' field is the Lambda
Arn. The 'sk' field is a string used to order the invocation of those
functions.

```yaml
  RegistrationTable:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - 
          AttributeName: "pk"
          AttributeType: "S"
        - 
          AttributeName: "sk"
          AttributeType: "S"
      KeySchema:
        -
          AttributeName: "pk"
          KeyType: "HASH"
        -
          AttributeName: "sk"
          KeyType: "RANGE"
```

The compliance Lambda functions will be invoked with a payload that looks like this:

```json
{
    "resource_name": "AWS::S3::Bucket",
    "resource_properties": {
        "BucketName": "ABC"
    }
}
```

It's up to you to create and maintain those Lambda functions.

