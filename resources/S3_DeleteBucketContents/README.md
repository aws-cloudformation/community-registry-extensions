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
    Condition: IsNotProd
    Type: AwsCommunity::S3::DeleteBucketContents
    Properties:
      BucketName: !Ref Bucket
```

### Activation

In order to use this resource, you will need to activate it in each account and region where you want to incorporate it into CloudFormation templates. 

1. Log in to the AWS Console
2. Got to CloudFormation and select `Public extensions` from the menu. Choose `Third party` under `Publisher`.
3. Select `AwsCommunity::S3::DeleteBucketContents`

<img src="https://github.com/aws-cloudformation/community-registry-extensions/blob/main/resources/S3_DeleteBucketContents/activation.png?raw=true" width="80%" />

4. Click on the `Activate` button.
5. On the following screen, you *must* enter an execution role ARN. It appears optional in the user interface, but it is not. Stack creation will fail if you do not create a role and enter the ARN here. The easiest way to create this role is to deploy the [resource-role-prod.yaml](./resource-role-prod.yaml) template, which creates a role with the necessary permissions. An Administrator role will not work, since it does not have the right trust policy, and is not recommended since it is not scoped down to only what is required for the resource handlers to work.
6. Click Activate Extension
7. Repeat this process for all other regions and accounts where you want to use the resource.

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

