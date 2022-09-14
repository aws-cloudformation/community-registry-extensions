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

[![Join our Discord](https://discordapp.com/api/guilds/981586120448020580/widget.png?style=banner3)](https://discord.gg/9zpd7TTRwq)

## Open Discussions

This repository is part of an initiative to improve open source community
engagement around Infrastructure as Code at AWS. We are still in early phases,
so we would like community input on the direction we take.

* Linting. Hooks and resources can be authored in a variety of languages.
  Should we enforce a coding standard at the top level for all projects (for
  example, a single .pylintrc)? Or let each project dictate its own standards?
* What’s our “swim lane”? Do we allow contributions that patch gaps in
  CloudFormation resource coverage, which may later be handled by the AWS
  service team? Do we allow someone to basically re-write an AWS resource from
  scratch, for example AwsCommunity::S3::Bucket with different behavior from
  the original?
* Experimental extensions. Do we have a variation on the namespace to give
  people freedom to experiment? AwsCommunityAlpha:: ? There may be a registry
  feature coming soon to give a resource an ‘Alpha’ badge or ‘GA’ badge, and
  also another high level category in the middle of “AWS” and “3rd Party”. We
  want to avoid a situation where customers install experimental extensions in
  production and then get surprised by a breaking change because it wasn't
  obvious.
* Testing. We need to make sure that the resources we publish remain stable
  over time, especially after we designate one as "GA". We expect these
  resources to be used in production by customers, and a change that leads to
  the lambda handler code behind a resource failing could lead to outages for
  customer release pipelines. Running "local" tests with SAM still results in
  SDK calls being made in an AWS account, which requires a certain amount of
  setup to be done beforehand. And these tests only cover the resource handlers
  themselves, not an actual template that uses the resource. Full integration
  testing requires even more setup, which is difficult to automate. We need to
  decide what tests are run when new PRs are submitted, and which tests we
  reserve for releases. And what the release branching strategy will be.

## How to use these extensions

Log in to your AWS account and go to the CloudFormation console. Under Registry
in the menu, select Public extensions. Search under Third Party publishers for
the AwsCommunity:: namespace. These extensions can be used from any template
you author in a region where they are available and activated. Unlike public
extensions under the AWS:: namespace, each of these community extensions must
first be activated using the instructions [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Catalog of community extensions

|Name|Type|Version|Description|
|----|----|-------|-----------|
|[./resources/BucketNotification](AwsCommunity::S3::BucketNotification)|Resource|Alpha|Configure bucket notifications|
|[./resources/DeleteBucketContents](AwsCommunity::S3::DeleteBucketContents)|Resource|Alpha|Delete all objects in a bucket|
|[./hooks/S3_BucketVersioningEnabled](AwsCommunity::S3::BucketVersioningEnabled)|Hook|Alpha|Validate an AWS::S3::Bucket has versioning enabled|

## Contributing

See the contributer guide: [./CONTRIBUTING.md](CONTRIBUTING.md)

Also check out how our release process works here: [./RELEASE.md](RELEASE.md)




