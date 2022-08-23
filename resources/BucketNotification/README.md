# AwsLabs::S3::BucketNotification

This CloudFormation registry extension resource type allows you to specify S3 bucket notifications one at a time, in a way that does not result in a circular dependency error in your template.

Note that this resource intentionally introduces drift into your template, since the official way to configure bucket notifications is to specify them as part of the `AWS::S3::Bucket` resource.

In this project, we deviate slightly from the boilerplate provided by the CFN CLI. In order to support publishing the resource under the `CommunityAlpha::` namespace before making an extension generally available, we changed the source folder name to `bucketnotification` and create a soft link to the schema in `bucketnotification.json`.

## Development

```sh
cd resources/BucketNotification
python3 -m venv .env
source .env/bin/activate
cd src
pip install -r requirements.txt
pip install -e .
```

