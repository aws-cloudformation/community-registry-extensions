# AwsCommunity::CloudFront::LoggingEnabled

Validates all CloudFront distributions created with CloudFormation stacks to ensure that they have access logs enabled.

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
  --type-name AwsCommunity::CloudFront::LoggingEnabled
```

## Example templates

The Hook will find this template to be non-compliant.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  CloudFrontDistributionLoggingNonCompliant:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - DomainName: !GetAtt
              - S3BucketOriginSupporting
              - DomainName
            Id: S3Origin
            CustomOriginConfig:
              OriginProtocolPolicy: https-only
        DefaultCacheBehavior:
          TargetOriginId: S3Origin
          ViewerProtocolPolicy: https-only
          ForwardedValues:
            QueryString: false
```

This template will be found as compliant and deploy successfully.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  CloudFrontDistributionLoggingCompliant:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Logging:
          Bucket: !GetAtt
            - S3BucketLoggingSupporting
            - DomainName
        Origins:
          - DomainName: !GetAtt
              - S3BucketOriginSupporting
              - DomainName
            Id: S3Origin
            CustomOriginConfig:
              OriginProtocolPolicy: https-only
        DefaultCacheBehavior:
          TargetOriginId: S3Origin
          ViewerProtocolPolicy: https-only
          ForwardedValues:
            QueryString: false
```