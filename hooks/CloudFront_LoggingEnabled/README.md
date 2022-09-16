# AwsCommunity::CloudFront::LoggingEnabled

Validates that CloudFront distribution has access logs enabled.

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

Hook will find this non-compliant
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

This will be found as compliant
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