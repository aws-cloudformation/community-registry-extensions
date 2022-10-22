# Community Registry Extension Release Process

_Note that this is a work in progress and we welcome your feedback!_

_The final step in the release process, publishing, will not activated until
we complete an appsec review internally_

See the tracking issue [here](https://github.com/aws-cloudformation/community-registry-extensions/issues/22)

This document covers the release process for registry extensions in the
`AwsCommunity::` namespace, published by the AWS Community Engagement Program
(CEP) team.  


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
`resources/buildspec-{language}.yml`.

There are some changes that need to be made to the `release/cicd.yml` template
when adding a new resource. Each resource gets is own build action, and any 
permissions that are needed to run the setup template and make SDK calls 
during contract testing need to be added to the project policy.

Each extension type and each language has its own build spec within each environment. 
For example, `resources/cicd-buildspec-python.yml` is used in the CICD account
when building Python resources.

### Beta account

An account controlled by AWS that runs end-to-end integration tests with sample
templates that cover all published resources. These tests go beyond contract
testing to make sure that resources created by prior versions can be
successfully updated by the new default version. The resource developer creates
`test/integ.yml`, a template that fully exercises their resource. This template
should create all needed resources, and does not rely on the `test/setup.yml`
template.

The `test/integ.yml` template is created and deleted, and a second copy is
created once and never deleted (TODO), to make sure that updates to the
resource don't cause issues.  In the integ template, no hard-coded names should
be used, to avoid issues with multiple stacks being deployed from the same
template in the same account.

TODO: What about Alpha resources? It's Ok for them to break backwards
compatibility, so we shouldn't fail the release process, but how do we tell the
difference between this kind of failure and something we want to catch?

The beta account uses the same CloudFormation template, `release/cicd.yml`, as 
the CICD account, since the pipeline and permissions are very similar. The pipeline 
is started by a commit being made on the `release` branch.

The beta pipeline has one extra stage which copies the source zip to a bucket in the 
prod account to start the publishing process, if all beta tests succeed. (TODO)


### Prod account

An account controlled by AWS that is the publisher for the registry extensions.
If all integ tests succeed in the beta account, the prod pipeline is invoked by copying the build to an S3 bucket that starts the pipeline in each configured region. A stack set is used to deploy `cicd-prod-regional.yml` across regions. The pipeline invokes a CodeBuild job that runs `release/publish.sh`.

### Development

If you need to make changes to the release process, deploy the CICD stacks to
your own sandbox account for development and testing. 

First, create a secret in Secrets Manager for the GitHub webhook secret. 
It should be a plaintext string that you determine. Note the ARN of the secret.

Make copies of the `scripts/deploy-*.sh` scripts in the git-ignored `local/`
folder and deploy each of them after changing the environment variables. 

Deploy them in this order:

1. `deploy-cicd.sh`
2. `deploy-prod.sh`
3. `deploy-beta.sh`

Manually create an ECR repository called cep-cicd in your account.

Deploying the build image will take a while from outside the PROD network,
so it's recommended to do this from a Cloud9 instance in your account.

Once `deploy-cicd.sh` has run, you will need to manually confgure a GitHub
webhook from your fork to point to the API Gateway `prod` stage that is created
by the `cicd.yml` template. Set the content-type to `application-json` and
leave the default of "Just the push event". The "Recent Deliveries" tab on the
webhook screen can be used to re-deliver payloads if you are troubleshooting
it.

### 3rd party resources

If we want to publish namespaces other than `AwsCommunity`, we can still use
this release process and publish the extensions via AWS accounts. This
will require making copies of the template files and template deployment
scripts. Example for a third party called "Oktank".

- `cicd.yml` -> `oktank/cicd.yml`
- `cicd-prod.yml` -> `oktank/cicd-prod.yml`
- `cicd-prod-regional.yml` -> `oktank/cicd-prod-regional.yml`

Copy-pasting templates is not ideal, but they are full of extension-specific stuff
that is not easily abstracted without use of something like CDK, which we are not using
here on purpose, in order to dogfood CloudFormation tools as much as possible.

These templates are deployed to the same accounts as `AwsCommunity`. This is required 
since we need these all to be published by us from a single account.





