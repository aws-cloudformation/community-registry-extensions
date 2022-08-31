# Community Registry Extension Release Process

This document covers the release process for registry extensions in the
`AwsCommunity::` namespace by the AWS Community Engagement Program (CEP) team.
Our intention with this guide, and with the related code we write, is for it to
be useable by someone who wants to publish their own public resources to all
available regions.

## Accounts

### Developer sandbox account

This is the account that belongs to a resource developer, where extensions are submitted to the private registry for integration testing. Extensions should be clearly documented so that a new developer can quickly deploy and test an extension in their account.

### CI/CD account

An account controlled by AWS to perform integration testing on resources.
Connected to the GitHub account. Runs contract tests.

In each extension project, there is an `example_inputs` folder. When contract
tests are run, if there are files in the (git-ignored) `inputs` folder, these
inputs are used instead of randomly generated characters which are not useful
for real resource testing. Since these are not full templates and cannot create
prerequisite resources, a template must be provided in each project to create
those prerequisites.

### Beta account

An account controlled by AWS that runs end-to-end tests with sample templates
that cover all published resources. These tests go beyond contract testing to
make sure that resources created by prior versions can be successfully updated
by the new default version.

For each resource, a directory of E2E test templates is created. Each of those
templates is created from scratch and then deleted with a unique stack name
during each full test run. In addition, another stack is updated and never
deleted, to test backwards compatibility. These templates should create all of
their needed pre-requisites, and no hard-coded names should be used, to avoid
issues with multiple stacks being deployed from the same template in the same
account.

TODO: What about Alpha resources? It's Ok for them to break backwards compatibility.


### Prod account

An account controlled by AWS that is the publisher for the registry extensions.
