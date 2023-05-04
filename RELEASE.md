# Community Registry Extension Release Process

_Note that this is a work in progress and we welcome your feedback!_

_The final step in the release process, publishing, will not activated until
we complete an appsec review internally_

This document covers the release process for registry extensions in the
`AwsCommunity::` namespace, published by the AWS Community Engagement Program
(CEP) team.

See the tracking issue [here](https://github.com/aws-cloudformation/community-registry-extensions/issues/22)

<img src="https://github.com/aws-cloudformation/community-registry-extensions/blob/main/release/ceparch.png?raw=true" width="80%" />


## Accounts

### Developer sandbox account

This is the account that belongs to a resource developer, where extensions are
submitted to the private registry for integration testing. Extensions should be
clearly documented so that a new developer can quickly deploy and test an
extension in their account. Developers can also deploy the CICD pipelines to a
single sandbox account in order to test changes to the release process.

### Alpha account

An account controlled by AWS to perform integration testing on resources.
Runs contract tests.

In each extension project, there must be an `inputs` folder, renamed from the
`example_inputs` folder created by `cfn init`. When contract tests are run, if
there are files in the `inputs` folder, these inputs are used instead of
randomly generated characters which are not useful for real resource testing.
Since these inputs are not full templates and cannot create prerequisite
resources, a template must be provided in each project to create those
prerequisites. The resource developer creates `test/setup.yml` to create any
resources that are needed in order for contract testing to succeed. See
https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html)
for documentation on the input files and how to reference CloudFormation export
names. Keep in mind that `cfn test` will ignore the files if there are special
characters in the export names.

When a PR is merged to the `main` branch in the repo, a CodePipeline pipeline is
started via a GitHub webhook. The webhook is handled by a Lambda function that
invokes a CodeBuild job. The CodeBuild job clones the repo and places a zip
file into a bucket, which is detected by CodePipeline. The pipeline starts
parallel CodeBuild jobs for each resource. The jobs for resource types run
`resources/{env}-buildspec-{language}.yml`.

There are some changes that need to be made to the `release/cicd.yml` template
when adding a new resource. Each resource gets is own build action, and any
permissions that are needed to run the setup template and make SDK calls
during contract testing need to be added to the project policy.

Each extension type and each language has its own build spec within each environment.
For example, `resources/alpha-buildspec-python.yml` is used in the alpha account
when building Python resources.

### Beta account

An account controlled by AWS that runs end-to-end integration tests with sample
templates that cover all published resources. These tests go beyond contract
testing to make sure that resources created by prior versions can be
successfully updated by the new default version. The resource developer creates
`test/integ.yml`, a template that fully exercises their resource. This template
should create all needed resources, and does not rely on the `test/setup.yml`
template.

In the integ template, no hard-coded names should be used, to avoid issues with
multiple stacks being deployed from the same template in the same account.

The beta account uses the same CloudFormation template, `release/cicd.yml`, as
the alpha account, since the pipeline and permissions are very similar. The pipeline
is started by creating a release in the GitHub repo and then copying the zip file to the `cep-source-${ACCOUNT_ID}-beta-awscommunity` bucket in the beta account. There is a script to do this here:  `release/awscommunity/release.sh`.

The beta pipeline has one extra stage which copies the source zip to a bucket in the
prod account to start the publishing process, if all beta tests succeed.

The beta pipeline can be triggered by a push to the release branch, or a release zip
can be copied to the beta bucket using `release/release.sh`, which is preferred.

### Prod account

An account controlled by AWS that is the publisher for the registry extensions.
If all integ tests succeed in the beta account, the prod pipeline is invoked by
copying the build to an S3 bucket that starts the pipeline. A stack set is used
to publish the extension to all regions. The prod account uses the same
`cicd.yml` template as the alpha and beta accounts, with different parameter
values and different build specs.

### Development

*Note that you do not have to follow these steps to create a new extension, or
to fix a bug that is not related to the release process.  See the
[CONTRIBUTOR](./CONTRIBUTOR.md) guide for instructions instead.*

If you need to make changes to the release process, deploy the CICD stacks to
your own sandbox account for development and testing.

**Pre-Requisites**

***In your sandbox AWS Account***
- Create a secret in Secrets Manager for the GitHub webhook secret.
*This should be a plaintext string that you determine. Note the ARN of the secret.*

- Create S3 buckets for `alpha`, `beta`, `prod` environments

***Local Machine***
You will need to have the following software installed

- [cfn-lint](https://github.com/aws-cloudformation/cfn-lint)
- [aws](https://aws.amazon.com/cli/)
- [rain](https://github.com/aws-cloudformation/rain)
- `docker`

Make copies of the `scripts/deploy-*.sh` scripts in the git-ignored `local/`
folder and update the environment variables in the shell scripts you will be
using.  To set up the sandbox pipelines you would update the
`deploy-sandbox-pipeline.sh` file.

Change to the `release` directory and run

1. `../local/deploy-sandbox-pipeline.sh`

Building the image for the first time will take a fair amount of time.  We recommend
doing this from a Cloud9 instance in your account if that is a concern.

Once `deploy-sandbox-pipeline.sh` has completed, you will need to confgure a GitHub
webhook from your fork to point to the API Gateway `prod` stage that is created
by the `cicd.yml` template. Set the content-type to `application-json` and
leave the default of "Just the push event". Add, in the "Secret" field, the plaintext
string value you created earlier and stored in Secrets Manager.

The Webhook URL is in the output of the `cep-common-alpha`
CloudFormation stack.  The "Recent Deliveries" tab on the webhook
screen can be used to re-deliver payloads if you are troubleshooting
it.

### 3rd party resources

We use this release process for third parties as well as `AwsCommunity`. The
base CICD template in each account handles some things centrally, such as the
GitHub webhook to start an alpha build. But most of the resources have to be
replicated into a distint pipeline for each namespace (GitHub, Okta, etc.)

Run this script to generate the CICD template for a 3rd party:

```
cd scripts
python get_3p_template.py Oktank MyResource
```

Additional resources beyond the first one will have to be added manually.

The template can be deployed to the accounts like this, from the `release/` directory:

```sh
cd release
../scripts/deploy-3p.sh alpha oktank
../scripts/deploy-3p.sh prod oktank
../scripts/deploy-3p.sh beta oktank
```

In the 3rd party repo, what's needed here is somewhat dependent on the layout of the
project, and if there is more than one resource in the namespace. These are the files
that will typically need to be added, beyond what the cfn cli generates for you.

```
publish.sh
alpha-buildspec.yml
beta-buildspec.yml
prod-buildspec.yml
deregister-all.sh
otkank-resource/setup.sh
oktank-resource/cleanup.sh
oktank-resource/get_type_configuration.py
oktank-resouce/resource-role-prod.yml
oktank-resource/test/integ.yml
oktank-resource/inputs/*
```

Copy-pasting templates is not ideal, but they are full of extension-specific stuff
that is not easily abstracted without use of something like CDK, which we are not using
here on purpose, in order to dogfood CloudFormation tools as much as possible.

These templates are deployed to the same accounts as `AwsCommunity`. This is required
since we need these all to be published by us from a single account.

## Publishing a release (this is done by AWS staff)

For now, when we do a release, all resources are published. In the future we will look at
publishing only those resources that have changed.

Go to the GitHub repo, `Code` -> `Releases` -> `Draft a new release`.

Choose a new release number, incrementing from the last one. For example `release-0.1.2`.

Add release notes that cover any changes made since the last release.

`Publish release`

Run the `release/release.sh` script to copy the zip from GitHub to the beta pipeline bucket.
