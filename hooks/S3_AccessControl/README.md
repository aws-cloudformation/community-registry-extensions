# AwsCommunity::S3::AccessControl


- [Overview](#Overview)
- [Usage](#Usage)
- [Example templates](#example-templates)
- [Tests](#Tests)
    - [Unit tests](#Unit-tests)
    - [Contract tests](#Contract-tests)
- [Hook development notes](#Hook-development-notes)


## Overview
This hook for [AWS CloudFormation](https://aws.amazon.com/cloudformation/) validates that the legacy `AccessControl` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-accesscontrol) for an `AWS::S3::Bucket` [resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html) is either set to `Private`, or is not present.


## Usage
This hook is written in [Kotlin](https://kotlinlang.org/).  To build it on your machine, install [Apache Maven](https://maven.apache.org/install.html), and a JDK (8, or 11).  For more information, see [Prerequisites for developing hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-walkthrough-java.html#prerequisites-developing-hooks-java).

Next, you'll need to install the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html), that you'll use to run contract tests for this hook, and to [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) this hook to the CloudFormation registry, as a private extension, in the AWS account and Region(s) of your choice.

The following example shows how to build and submit the hook to the registry, in the `us-east-1` region for the account you use:

```shell
cfn generate && mvn clean verify && cfn submit --set-default --region us-east-1
```

After you submit the hook to the registry, you'll need to configure it.  One of the way of doing this is to first create a `type_config.json` file as shown next (for more information on `Properties` defined for this hook, see [Configuration options](#Configuration-options)):

```shell
cat <<EOF > type_config.json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
            }
        }
    }
}
EOF
```

and then submit the hook configuration using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/).  First, get the [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) for this hook, as follows (examples are for the `us-east-1` region):

```shell
aws cloudformation list-types \
  --type HOOK \
  --filters TypeNamePrefix=AwsCommunity::S3::AccessControl \
  --query 'TypeSummaries[?TypeName==`AwsCommunity::S3::AccessControl`].TypeArn' \
  --output text \
  --region us-east-1
```

Next, find the ARN value string in the output of the command above, and use it with this command by replacing the placeholder text below in upper case characters for `YOUR_HOOK_ARN`:

```shell
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type-arn 'YOUR_HOOK_ARN' \
  --region us-east-1
```


# Example templates

Templates in this section are marked as:
- _Non-compliant_: this hook will find the given template to be non-compliant, and
- _Compliant_: the template will be found to be compliant, and should deploy successfully.

Note that you'll also find templates called `integ-succeed.yml` and `integ-fail.yml` in the `test` directory, that can be used to create stacks for integration testing.

Non-compliant: the `AccessControl` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-accesscontrol) for the `AWS::S3::Bucket` [resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html) is present in the template, and with a value other than `Private`:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: Test-only template that describes an Amazon S3 bucket for integration tests.

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: PublicRead
```

Compliant, example 1: `AccessControl` is present in the template, and with a value of `Private`:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: Test-only template that describes an Amazon S3 bucket for integration tests.

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: Private
```

Compliant, example 2: `AccessControl` is not present in the template:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: Test-only template that describes an Amazon S3 bucket for integration tests.

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
```

## Tests


### Unit tests
Run unit tests, and verify code coverage with:

```shell
mvn clean verify
```


### Contract tests
Contract tests help you validate hooks you develop work as expected, and are required to pass when you submit a CloudFormation extension such as a hook to the public registry.  It is recommended to strive to pass contract tests also when you write a private extension, to help discover potential issues.

To run contract tests, open a new terminal window and run, from the root directory of this project:

```shell
sam local start-lambda
```

For more information, see [Testing resource types locally using AWS SAM](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html#resource-type-develop-test).

Open a another terminal window, build this hook, and run contract tests:

```shell
cfn generate && mvn clean verify && cfn test -v --enforce-timeout 90
```

## Hook development notes
The RPDK will automatically generate the correct hook input model from the schema whenever the project is built via Maven. You can also do this manually with the following command: `cfn generate`.

> Please don't modify files under `target/generated-sources/rpdk`, as they will be automatically overwritten.

The generated code uses [Lombok](https://projectlombok.org/) to annotate Java classes, including classes in the `target/generated-sources/rpdk` path mentioned above.  This hook -that is written in Kotlin- needs to consume such Lombok-annotated Java classes: one way to do this is to use [Delombok](https://projectlombok.org/features/delombok) to delombok relevant source files.  The `pom.xml` file, for this `AwsCommunity::S3::AccessControl` hook, uses the `delombok` goal for the [lombok.maven plugin](https://github.com/awhitford/lombok.maven) to delombok, during the `process-sources` phase, the `target/generated-sources/rpdk` generated classes into the `target/generated-sources/delombok` target directory that, in turn, is then added as a source with the `add-source` goal for the `build-helper-maven-plugin`.
