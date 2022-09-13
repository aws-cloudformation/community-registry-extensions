# Community Registry Extension Release Process

This document covers the release process for registry extensions in the
`AwsCommunity::` namespace, published by the AWS Community Engagement Program
(CEP) team.  

Our intention with this release process is for it to be useable by someone who
wants to publish their own public resources to all available regions from 
their own account.

## Accounts

### Developer sandbox account

This is the account that belongs to a resource developer, where extensions are
submitted to the private registry for integration testing. Extensions should be
clearly documented so that a new developer can quickly deploy and test an
extension in their account.

### CI/CD account

An account controlled by AWS to perform integration testing on resources.
Connected to the GitHub account. Runs contract tests.

In each extension project, there must be an `inputs` folder, renamed from the
`example_inputs` folder created by `cfn init`. When contract tests are run, if
there are files in the `inputs` folder, these inputs are used instead of
randomly generated characters which are not useful for real resource testing.
Since these inputs are not full templates and cannot create prerequisite
resources, a template must be provided in each project to create those
prerequisites. The resource developer creates `test/setup.yml` or
`test/setup.json` to create any resources that are needed in order for contract
testing to succeed. See
https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html)
for documentation on the input files and how to reference CloudFormation export
names. Keep in mind that `cfn test` will ignore the files if there are special
characters in the export names.

When a PR is merged to the main branch in the repo, a CodePipeline pipeline is
started. It starts parallel CodeBuild jobs for each resource. The jobs for
resource types run `resources/buildspec.yml`.

There are some changes that need to be made to the `release/cicd.yml` template
when adding a new resource. Each resource gets is own build action, and any 
permissions that are needed to run the setup template and make SDK calls 
during contract testing need to be added to the project policy.

### Beta account

An account controlled by AWS that runs end-to-end integration tests with sample
templates that cover all published resources. These tests go beyond contract
testing to make sure that resources created by prior versions can be
successfully updated by the new default version. The resource developer creates
`test/integ.yml`, a template that fully exercises their resource. This template
should create all needed resources, and does not rely on the `test/setup.yml`
template.

The `test/integ.yml` template is created and deleted, and a second copy is
created once and never deleted, to make sure that updates to the resource don't
cause issues.  In the integ template, no hard-coded names should be used, to
avoid issues with multiple stacks being deployed from the same template in the
same account.

TODO: What about Alpha resources? It's Ok for them to break backwards
compatibility, so we shouldn't fail the release process, but how do we tell the
difference between this kind of failure and something we want to catch?

### Prod account

An account controlled by AWS that is the publisher for the registry extensions.
We are planning to use a strategy that involves Systems Manager documents
instead of Stack Sets for deployment to all available regions.

