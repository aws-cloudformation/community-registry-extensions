# AWS CloudFormation Community Registry Extensions

This repository hosts [registry extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)
that are published under the `AwsCommunity::` namespace in AWS CloudFormation.
The CloudFormation Registry allows customers to create public and private
[resources
types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html),
[modules](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html),
and
[hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html).
Modules are authored as templates in either JSON or YAML. Resource types can be authored in Java, Go, Python, or Typescript, using the
[CloudFormation Command Line Interface (CFN
CLI)](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)
for project setup and testing. 

## Discord

Join us on Discord! Connect & interact with CloudFormation developers &
experts, find channels to discuss the CloudFormation registry, StackSets,
cfn-lint, Guard and more:

[![Join our Discord](https://discordapp.com/api/guilds/981586120448020580/widget.png?style=banner3)](https://discord.gg/9zpd7TTRwq)

## How to use these extensions

(Note that we are not yet actually publishing the extensions, pending approval 
of our release process)

Log in to your AWS account and go to the CloudFormation console. Under Registry
in the menu, select Public extensions. Search under Third Party publishers for
the `AwsCommunity::` namespace. These extensions can be used from any template
you author in a region where they are available and activated. Unlike public
extensions under the `AWS::` namespace, each of these community extensions must
first be activated using the instructions
[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Catalog of community extensions

|Name|Type|Version|Description|
|----|----|-------|-----------|
|[AwsCommunity::Account::AlternateContact](./resources/Account_AlternateContact)|Resource|Prod|An alternate contact attached to an Amazon Web Services account|
|[AwsCommunity::ApplicationAutoscaling::ScheduledAction](./resources/ApplicationAutoscaling_ScheduledAction)|Resource|Prod|Application Autoscaling Scheduled Action|
|[AwsCommunity::CloudFront::LoggingEnabled](./hooks/CloudFront_LoggingEnabled)|Hook|Alpha|Validate that a CloudFront distribution has logging enabled|
|[AwsCommunity::CloudFront::S3Website::MODULE](./modules/CloudFront_S3Website/)|Module|Prod|CloudFront backed by an S3 bucket with Route53 integration|
|[AwsCommunity::DynamoDB::Item](./resources/DynamoDB_Item)|Resource|Prod|Manage the lifecycle of items in a DynamoDB table|
|[AwsCommunity::EC2::SecurityGroupRestrictedSSH](./hooks/EC2_SecurityGroupRestrictedSSH)|Hook|Prod|Restrict SSH traffic from 0.0.0.0/0|
|[AwsCommunity::KMS::EncryptionSettings](./hooks/KMS_EncryptionSettings)|Hook|Prod|Validates AWS KMS encryption-related, user-provided configuration settings for a number of AWS resources|
|[AwsCommunity::Resource::Lookup](./resources/Resource_Lookup)|Resource|Prod|Uses AWS Cloud Control API to lookup a resource of a given type (such as, AWS::EC2::VPC)|
|[AwsCommunity::S3::Bucket::MODULE](./modules/S3_Bucket/)|Module|Prod|Create a standard S3 bucket|
|[AwsCommunity::SSM::ResizeVolume::MODULE](./modules/SSM_Document_ResizeVolume/)|Module|Prod|Create AWS SSM document to resize EBS volume and grow the filesystem on them|
|[AwsCommunity::IotAnalytics::Pipeline::MODULE](./modules/IOT_ANALYTICS_PIPELINE/)|Module|Prod|Create an IOT analytics pipeline|
|[AwsCommunity::S3::BucketAccessControlsRestricted](./hooks/S3_PublicAccessControlsRestricted)|Hook|Prod|Validates S3 Bucket is configured to block public access|
|[AwsCommunity::S3::BucketNotification](./resources/S3_BucketNotification)|Resource|Alpha|Configure bucket notifications|
|[AwsCommunity::S3::BucketVersioningEnabled](./hooks/S3_BucketVersioningEnabled)|Hook|Prod|Validate that an AWS::S3::Bucket has versioning enabled|
|[AwsCommunity::S3::DeleteBucketContents](./resources/S3_DeleteBucketContents)|Resource|Prod|Delete all objects in a bucket|
|[AwsCommunity::Time::Offset](./resources/Time_Offset)|Resource|Prod|Creates a time based resource with an offset from the provided time or now|
|[AwsCommunity::Time::Sleep](./resources/Time_Sleep)|Resource|Prod|Sleep a provided number of seconds between create, update, or delete operations.|
|[AwsCommunity::Time::Static](./resources/Time_Static)|Resource|Prod|Creates a static time stamp|


## Contributing

See the contributer guide: [./CONTRIBUTING.md](CONTRIBUTING.md)

Also check out how our release process works here: [./RELEASE.md](RELEASE.md)

## Related Repositories

### CloudFormation CLI and language plugins

The CloudFormation CLI (`cfn`), not to be confused with the `aws
cloudformation` commands, is used to initialize, build, test, and publish
registry extensions.

https://github.com/aws-cloudformation/cloudformation-cli

https://github.com/aws-cloudformation/cloudformation-cli-python-plugin

https://github.com/aws-cloudformation/cloudformation-cli-typescript-plugin

https://github.com/aws-cloudformation/cloudformation-cli-go-plugin

https://github.com/aws-cloudformation/cloudformation-cli-java-plugin

### cfn-lint

The CloudFormation linter is an indespensible tool for developing templates. It
does static analysis on your template to make sure it's valid before submitting
it, which saves a lot of wasted time waiting for the service to tell you the
same thing.

https://github.com/aws-cloudformation/cfn-lint

### rain

Rain is what happens when you have cloud formations... Rain is a CLI helper for
CloudFormation that makes it a lot easier to author and deploy stacks. Instead
of needing to string together `aws cloudformation` commands to check the status
of a stack before either creating or updating, rain does all of this with a
simple `deploy` command.

https://github.com/aws-cloudformation/rain

### 3p resources

We are working on a set of third party resources that will piggy-back on our release process and be published from our publisher account.

https://github.com/aws-ia/cloudformation-okta-resource-providers

https://github.com/aws-ia/cloudformation-github-resource-providers

https://github.com/aws-ia/cloudformation-rollbar-resource-providers

https://github.com/aws-ia/cloudformation-fastly-resource-providers

https://github.com/aws-ia/cloudformation-cloudflare-resource-providers

https://github.com/aws-ia/cloudformation-snowflake-resource-providers

https://github.com/aws-ia/cloudformation-pagerduty-resource-providers

https://github.com/aws-ia/cloudformation-gitlab-resource-providers

https://github.com/aws-ia/cloudformation-dynatrace-resource-providers

https://github.com/aws-ia/cloudformation-bigid-resource-providers

### cdk-import

Generates CDK constructs from external sources such as public CloudFormation Registry types and modules (L1s) as well as AWS Service Catalog product versions.

https://github.com/cdklabs/cdk-import

### cdk-cloudformation

A collection of L1 constructs created with `cdk-import`, based on registry resource types.

https://github.com/cdklabs/cdk-cloudformation

## Publishing packages

(Note that we decided to move these out to a separate repo, so they won't be here much longer)

We publish our python packages in `packages/` to pypi. When we publish a release a workflow is triggered to do the publishing. See the `CD.yml` workflows [here](./github/workflows)

For `cfn-guard-rs` we tag the release with `cfn-guard-rs-vX.X.X`
For `cfn-guard-rs-hook` we tag the release with `cfn-guard-rs-hook-vX.X.X`

## Maintainers

[![](https://github.com/ericzbeard.png?size=50)](https://github.com/ericzbeard)
[![](https://github.com/kddejong.png?size=50)](https://github.com/kddejong)
[![](https://github.com/mmaeng.png?size=50)](https://github.com/mmaeng)

