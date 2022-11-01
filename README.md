# AWS CloudFormation Community Registry Extensions

This repository hosts [registry extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)
that are published under the `AwsCommunity::` namespace in AWS CloudFormation.
The CloudFormation Registry allows customers to create public and private
[resources
types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html),
[modules](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html),
and
[hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html).
Modules are authored as templates in either JSON or YAML. Resource types and
hooks can be authored in Java, Go, Python, or Typescript, using the
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
the AwsCommunity:: namespace. These extensions can be used from any template
you author in a region where they are available and activated. Unlike public
extensions under the `AWS::` namespace, each of these community extensions must
first be activated using the instructions
[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Catalog of community extensions

|Name|Type|Version|Description|
|----|----|-------|-----------|
|[AwsCommunity::S3::BucketNotification](./resources/S3_BucketNotification)|Resource|Alpha|Configure bucket notifications|
|[AwsCommunity::S3::DeleteBucketContents](./resources/S3_DeleteBucketContents)|Resource|Alpha|Delete all objects in a bucket|
|[AwsCommunity::S3::BucketVersioningEnabled](./hooks/S3_BucketVersioningEnabled)|Hook|Alpha|Validate that an AWS::S3::Bucket has versioning enabled|
|[AwsCommunity::CloudFront::LoggingEnabled](./hooks/CloudFront_LoggingEnabled)|Hook|Alpha|Validate that a CloudFront distribution has logging enabled|

## Contributing

See the contributer guide: [./CONTRIBUTING.md](CONTRIBUTING.md)

Also check out how our release process works here: [./RELEASE.md](RELEASE.md)

## Publishing packages

We publish our python packages in `packages/` to pypi. When we publish a release a workflow is triggered to do the publishing. See the `CD.yml` workflows [here](./github/workflows)

For `cfn-guard-rs` we tag the release with `cfn-guard-rs-vX.X.X`
For `cfn-guard-rs-hook` we tag the release with `cfn-guard-rs-hook-vX.X.X`

## Maintainers

[![](https://github.com/ericzbeard.png?size=50)](https://github.com/ericzbeard)
[![](https://github.com/kddejong.png?size=50)](https://github.com/kddejong)
[![](https://github.com/mmaeng.png?size=50)](https://github.com/mmaeng)

