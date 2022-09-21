# AwsCommunity::S3::DeleteBucketContents

 Currently, CloudFormation ‘AWS::WAFv2::WebACLAssociation’ resource has a limitation that a new WebACL provisioned using CloudFormation cannot be associated to an existing CloudFront distribution (created outside of the CloudFormation template). For associating a web ACL to resources in CloudFormation, we can create a resource ‘AWS::WAFv2::WebACLAssociation’. However, this resource type only supports below ResourceArn values for Application Load Balancer, API Gateway and AppSync GraphQL API. This registry extension resource type associates a WebACL to a CloudFront distribution ARN. 


## Sample template

```yml
AWSTemplateFormatVersion: "2010-09-09"
Description: "This is to protect the CloudFront"
Parameters : 
  DistributionARN : 
    Type : String 
  WebAclARN : 
    Type : String 
Resources:
  CFwebACLAssociation:
    Type : AwsCommunity::CloudFront::WebACLAssociation
    Properties :
      DistributionArn: !Ref DistributionARN
      WebAclArn: !Ref WebAclARN
```

## Development

Open two tabs in your terminal.

Create a virtual environment.

```sh
cd resources/CloudFront_WebACLAssociation
python3 -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
```

In the other tab, run SAM local:

```sh
cd resources/CloudFront_WebACLAssociation
source .env/bin/activaate
sam local start-lambda
```

Keep in mind that SAM local testing only simulates lambda locally, it will make SDK 
calls into your account and create resources!

Create the setup stack so that contract tests have something to interact with in your account.

```sh
aws cloudformation create-stack --stack-name cloudfront-webacl-association-setup \
    --template-body file://test/setup.yml
```

