# AwsCommunity::S3::PublicAccessControlsRestricted

Validates any resource of type `AWS::S3::Bucket` has the public access controls restricted.

## Configuration

```bash
# Create a basic type configuration json
cat <<EOF > typeConfiguration.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://typeConfiguration.json \
  --type HOOK \
  --type-name AwsCommunity::S3::PublicAccessControlsRestricted
```

## Example templates

The Hook will find this template to be non-compliant.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  S3BucketWithNoProperties:
    Type: 'AWS::S3::Bucket'
  S3BucketWithNoProperties:
    Type: 'AWS::S3::Bucket'
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: True
        BlockPublicPolicy: False
        IgnorePublicAcls: True
        RestrictPublicBuckets: True
```

This template will be found as compliant and deploy successfully.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  S3BucketCompliant:
    Type: 'AWS::S3::Bucket'
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: True
        BlockPublicPolicy: True
        IgnorePublicAcls: True
        RestrictPublicBuckets: True
```
