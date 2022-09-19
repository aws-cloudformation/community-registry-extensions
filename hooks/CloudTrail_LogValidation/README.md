# AwsCommunity::CloudTrail::LogValidationEnabled

Validates all CloudTrail trails created with CloudFormation stacks to ensure that they have log file validation enabled.

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
  --type-name AwsCommunity::CloudTrail::LogValidationEnabled
```

## Example templates

The Hook will find this template to be non-compliant.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  CloudTrailTrailWithLogFileValidationFalseNonCompliant:
    Type: 'AWS::CloudTrail::Trail'
    Properties:
      TrailName: log-file-validation-disabled-non-compliant
      EnableLogFileValidation: false
      IsLogging: false
      S3BucketName: 'test'
  CloudTrailTrailWithoutLogFileValidationNonCompliant:
    Type: 'AWS::CloudTrail::Trail'
    Properties:
      TrailName: log-file-validation-disabled-non-compliant-2
      IsLogging: false
      S3BucketName: 'test'
```

This template will be found as compliant and deploy successfully.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  CloudTrailTrailWithoutLogFileValidationEnabledNonCompliant:
    Type: 'AWS::CloudTrail::Trail'
    Properties:
      TrailName: log-file-validation-disabled-compliant
      EnableLogFileValidation: true
      IsLogging: false
      S3BucketName: 'test'
```