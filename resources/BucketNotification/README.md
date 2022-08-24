# AwsLabs::S3::BucketNotification

This CloudFormation registry extension resource type allows you to specify S3
bucket notifications one at a time, in a way that does not result in a circular
dependency error in your template.

Note that this resource intentionally introduces drift into your template,
since the official way to configure bucket notifications is to specify them as
part of the `AWS::S3::Bucket` resource.

## Development

```sh
cd resources/BucketNotification
python3 -m venv .env
source .env/bin/activate
cd src
pip install -r requirements.txt
pip install -e .
cd awscommunity_s3_bucketnotification
pylint *.py
python3 config_integ.py --profile YOUR_PROFILE_NAME
```

