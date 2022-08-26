# AwsLabs::S3::BucketNotification

This CloudFormation registry extension resource type allows you to specify S3
bucket notifications one at a time, in a way that does not result in a circular
dependency error in your template.

Note that this resource intentionally introduces drift into your template,
since the official way to configure bucket notifications is to specify them as
part of the `AWS::S3::Bucket` resource.

## Sample template

```yml
Resources:
  Queue:
    Type: AWS::SQS::Queue
  Bucket:
    Type: AWS::S3::Bucket
  Notification:
    Type: AwsCommunity::S3::BucketNotification
    Properties:
      Id: MyNotification
      Events: 
        - s3:ObjectCreated:*
      Filters:
        - Name: suffix
          Value: gif
      BucketArn: !GetAtt Bucket.Arn
      TargetType: Queue
      TargetArn: !GetAtt Queue.Arn
    DependsOn:
      - Bucket
      - Queue
```

## Development

Open two tabs in your terminal.

Create a virtual environment.

```sh
cd resources/BucketNotification
python3 -m venv .env
source .env/bin/activaate
cd src
pip install -r requirements.txt
cd ..
```

In the other tab, run SAM local:

```sh
cd resources/BucketNotification
source .env/bin/activaate
sam local start-lambda
```

In the first tab:

```sh
./run-test.sh
```

