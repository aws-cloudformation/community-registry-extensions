# AwsCommunity::S3::DeleteBucketContents

This registry extension resource type deletes all contents of a bucket when the resource is deleted. 

Use this resource with caution! In the sample below we show how to incorporate a condition to avoid deleting contents from a production environment.

## Sample template

```yml
Parameters:
  EnvType:
    Description: Environment type.
    Default: alpha
    Type: String
    AllowedValues:
      - alpha
      - beta
      - gamma
      - prod
    ConstraintDescription: Specify alpha, beta, gamma, or prod
Conditions:
  IsNotProd: !Not 
    - !Equals
      - !Ref EnvType
      - prod
Resources:
  Bucket:
    Type: AWS::S3::Bucket
  Deleter:
    DependsOn: Bucket
    Condition: IsNotProd
    Type: AwsCommunity::S3::DeleteBucketContents
    Properties:
      BucketName: !Ref Bucket
```

