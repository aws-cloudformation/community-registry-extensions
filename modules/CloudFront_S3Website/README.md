# AwsCommunity::CloudFront::S3Website::MODULE

The module `AwsCommunity::CloudFront::S3Website::MODULE` creates a CloudFront distribution
that points at an S3 bucket. This module will also use ACM to create a certificate and set up a 
custom DNS name using Route53.

## Limitations

This module will only work in `us-east-1` because CloudFront can only use certificates from ACM in `us-east-1`

## Parameters

| Resource Name | Type | Description |
| ------------- | ------------- | ------------- |
| **Alias** | string  | The custom DNS alias for the CloudFront distribution
| **HostedZoneId**  | string  | The Route53 hosted zone ID for where to create the DNS record
| **AcmCertificateArn** | string | When provided will use this ACM Certificate instead of generating it

## Resources created

| Resource Name | Type | Description |
| ------------- | ------------- | ------------- |
| **Bucket**  | AWS::S3::Bucket  | Creates the bucket for the static content.
| **BucketPolicy** | AWS::S3::BucketPolicy  | Create a bucket policy for the content bucket in which CloudFront can do GetObject to the bucket.
| **Certificate**  | AWS::CertificateManager::Certificate  | Creates a certificate for the alias using ACM. Conditionally created based on if ***AcmCertificateArn*** parameter is specified or not.
| **Distribution** | AWS::CloudFront::Distribution | The CloudFront distribution.
| **Dns** | AWS::Route53::RecordSet  | A CNAME record set in the ***HostedZoneId***.
| **Oac** | AWS::CloudFront::OriginAccessControl  | Create a OAC for CloudFront to talk to S3.
