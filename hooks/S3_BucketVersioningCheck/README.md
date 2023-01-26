# AwsCommunity::S3::VersioningCheck

Validates all S3 buckets created and updated with CloudFormation stacks to ensure that they have  versioning is enabled.

## Configuration

```bash


# enable the hook
aws cloudformation set-type-configuration 
  --configuration "{\"CloudFormationConfiguration\":{\"HookConfiguration\":{\"TargetStacks\":\"ALL\",\"FailureMode\":\"FAIL\",\"Properties\":{}}}}" \\n--type-arn <ARN of your hook>

```

## Example templates

The Hook will find this template to be non-compliant.
```json

{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "cfnhacktest01252023",
                "VersioningConfiguration": {
                    "Status": "Suspended"
                }
            }
        }
    }
}
```

This template will be found as compliant and deploy successfully.
```json
{
"AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "cfnhacktest01252023",
                "VersioningConfiguration": {
                    "Status": "Enabled"
                }
            }
        }
    }
}
```