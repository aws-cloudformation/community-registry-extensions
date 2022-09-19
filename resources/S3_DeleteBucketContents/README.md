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

## Development

Open two tabs in your terminal.

Create a virtual environment.

```sh
cd resources/BucketNotification
python3 -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
```

In the other tab, run SAM local:

```sh
cd resources/BucketNotification
source .env/bin/activaate
sam local start-lambda
```

Keep in mind that SAM local testing only simulates lambda locally, it will make SDK 
calls into your account and create resources!

Create the setup stack so that contract tests have something to interact with in your account.

```sh
aws cloudformation create-stack --stack-name bucketnotification-setup \
    --template-body file://test/setup.yml
```

In the first tab:

```sh
./run-test.sh
```

If you don't have a default profile set up on your machine, you can do this:

```sh
AWS_PROFILE=my-profile ./run-test.sh
```

The `run-test.sh` script runs pylint and does a `cfn submit --dry-run`, which is necessary to create the build folder that SAM relies on.

There is also an integ test you can run to test the SDK calls without using SAM.
It also creates resources in your account.

```sh
cd src
python3 run_integ_test.py --profile your-aws-profile-name
```

