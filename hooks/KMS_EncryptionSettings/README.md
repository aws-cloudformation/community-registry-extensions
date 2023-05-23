# AwsCommunity::KMS::EncryptionSettings

- [Overview](#Overview)
    - [Supported resource types and properties in this hook](#Supported-resource-types-and-properties-in-this-hook)
- [Usage](#Usage)
- [Configuration options](#Configuration-options)
    - [UseGetEbsEncryptionByDefaultAsFallback](#UseGetEbsEncryptionByDefaultAsFallback)
    - [ValidateAmiBlockDeviceMappingEncryptionSettings](#ValidateAmiBlockDeviceMappingEncryptionSettings)
    - [ValidateBucketKeyEnabled](#ValidateBucketKeyEnabled)
- [Hook registry submission with StackSets](#Hook-registry-submission-with-StackSets)
- [Example templates](#Example-templates)
- [Tests](#Tests)
    - [Unit tests](#Unit-tests)
    - [Contract tests](#Contract-tests)
- [Hook development](#Hook-development)
    - [Notes](#Notes)

## Overview
This hook for [AWS CloudFormation](https://aws.amazon.com/cloudformation/) performs policy-as-code validation of [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) encryption-related, user-provided configuration settings for a number of [AWS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) with which KMS [integrates](https://aws.amazon.com/kms/features/#AWS_Service_Integration) that are supported in this hook.

This hook also includes [configuration options](#Configuration-options) that you can choose to enable/use to perform additional validation operations (for example, determine if EBS [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) is enabled for your account in the current Region, whether to validate the BlockDeviceMapping encryption settings of an [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) ID you specify).

### Supported resource types and properties in this hook
AWS resource types and properties supported in this hook include the following (see also the [configuration options](#Configuration-options) section shown next in this document):

- [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html)
    - [BlockDeviceMappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-blockdevicemappings): validates that the [Ebs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html#cfn-autoscaling-launchconfiguration-blockdevicemapping-ebs) property for [BlockDevice](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html) list items are configured as following:
        - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-encrypted): validates that it is set to a boolean value of `true`.
        - For additional, opt-in configuration options, see also:
            - [UseGetEbsEncryptionByDefaultAsFallback](#UseGetEbsEncryptionByDefaultAsFallback)
            - [ValidateAmiBlockDeviceMappingEncryptionSettings](#ValidateAmiBlockDeviceMappingEncryptionSettings)
- [AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html)
    - [KMSKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid): validates that this property is set, and runs a regex pattern validation on its value.
- [AWS::DynamoDB::GlobalTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html)
    - [SSESpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification) properties configured as follows:
        - [SSEEnabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-sseenabled): validates that it is set to a boolean value of `true`.
        - [SSEType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-ssetype): validates that it is set to `KMS`.
    - [ReplicaSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html) properties underneath the [Replicas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas) property are configured as follows:
        - [KMSMasterKeyID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid): (property underneath [SSESpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-ssespecification)) runs a regex pattern validation if this property has a value set.
- [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html)
    - [SSESpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html) properties configured as follows:
        - [SSEEnabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled): validates that it is set to a boolean value of `true`.
        - [SSEType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-ssetype): validates that it is set to `KMS`.
        - [KMSMasterKeyID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-kmsmasterkeyid): runs a regex pattern validation if this property has a value set.
- [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)
    - [BlockDeviceMappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-blockdevicemappings): validates that the [Ebs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html) property for [BlockDeviceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html) list items are configured as following:
        - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-encrypted): validates that it is set to a boolean value of `true`.
        - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-instance-ebs-kmskeyid): runs a regex pattern validation if this property has a value set.
        - For additional, opt-in configuration options, see also:
            - [UseGetEbsEncryptionByDefaultAsFallback](#UseGetEbsEncryptionByDefaultAsFallback)
            - [ValidateAmiBlockDeviceMappingEncryptionSettings](#ValidateAmiBlockDeviceMappingEncryptionSettings)
- [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html)
    - [BlockDeviceMappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-blockdevicemappings) of [LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html): validates that the [Ebs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html) property for [BlockDeviceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html) list items are configured as following:
        - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-encrypted): validates that it is set to a boolean value of `true`.
        - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-kmskeyid): runs a regex pattern validation if this property has a value set.
        - For additional, opt-in configuration options, see also:
            - [UseGetEbsEncryptionByDefaultAsFallback](#UseGetEbsEncryptionByDefaultAsFallback)
            - [ValidateAmiBlockDeviceMappingEncryptionSettings](#ValidateAmiBlockDeviceMappingEncryptionSettings)
- [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html)
    - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-encrypted): validates that it is set to a boolean value of `true`.
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-kmskeyid): runs a regex pattern validation if this property has a value set.
        - For additional, opt-in configuration options, see also:
            - [UseGetEbsEncryptionByDefaultAsFallback](#UseGetEbsEncryptionByDefaultAsFallback)
- [AWS::EFS::FileSystem](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html)
    - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-encrypted): validates that it is set to a boolean value of `true`.
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-kmskeyid): runs a regex pattern validation if this property has a value set.
- [AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html)
    - [StreamEncryption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-streamencryption) items are configured as following:
        - [EncryptionType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-encryptiontype): validates that it is set to `KMS`.
        - [KeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-keyid): validates that this property is set, and runs a regex pattern validation on its value.
- [AWS::Logs::LogGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html)
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid): validates that this property is set, and runs a regex pattern validation on its value.
- [AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html)
    - [StorageEncrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-storageencrypted): validates that this property is set to a boolean value of `true` in the following cases:
        - when the following properties are not specified:
            - `SnapshotIdentifier`
            - `SourceDBClusterIdentifier`
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-kmskeyid): runs a regex pattern validation if this property has a value set.
- [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html)
    - [StorageEncrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-storageencrypted): validates that this property is set to a boolean value of `true` in the following cases:
        - when the `Engine` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-engine) value does not start with the `aurora` occurrence: as per this documentation [page](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-storageencrypted), the encryption for Amazon Aurora DB instances is managed by the RDS DB cluster;
        - when the following properties are not specified:
            - `DBClusterSnapshotIdentifier`
            - `SnapshotIdentifier`
            - `SourceDBInstanceIdentifier`
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-kmskeyid): runs a regex pattern validation if this property has a value set.
- [AWS::RDS::GlobalCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html)
    - [StorageEncrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted): validates that this property is set to a boolean value of `true`.
- [AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html)
    - [Encrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-encrypted): validates that it is set to a boolean value of `true`.
    - [KmsKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-kmskeyid): runs a regex pattern validation if this property has a value set.
- [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)
    - [BucketEncryption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-bucketencryption): validates that the [ServerSideEncryptionRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html) structure for [ServerSideEncryptionByDefault](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html#cfn-s3-bucket-serversideencryptionrule-serversideencryptionbydefault) is configured as following:
        - [SSEAlgorithm](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html#cfn-s3-bucket-serversideencryptionbydefault-ssealgorithm): validates that it is set to `aws:kms`.
        - [KMSMasterKeyID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html#cfn-s3-bucket-serversideencryptionbydefault-kmsmasterkeyid): runs a regex pattern validation if this property has a value set.
        - For additional, opt-in configuration options, see also:
            - [ValidateBucketKeyEnabled](#ValidateBucketKeyEnabled)
- [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html)
    - [KmsMasterKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-kmsmasterkeyid): validates that this property is set, and runs a regex pattern validation on its value.
- [AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html)
    - [SqsManagedSseEnabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-sqsmanagedsseenabled): validates that this property is either set to a boolean `false`, or that is not set: you can either enable [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) (that is the intent of this hook), or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html);
    - [KmsMasterKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-kmsmasterkeyid): validates that this property is set, and runs a regex pattern validation on its value.

## Usage
To get started, follow the steps shown next:

- Install [Apache Maven](https://maven.apache.org/install.html), that you'll need to build this hook that uses Java.  You'll also need to install the JDK 8 or JDK 11; for more information, see [Prerequisites for developing hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-walkthrough-java.html#prerequisites-developing-hooks-java).
- Install the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
- Run the following commands to build and [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) it as a private extension to the CloudFormation registry in the AWS region(s) of your choice.  The following example uses the `us-east-1` region; you will need to make a separate `cfn submit` registry submission for each region you want to use (alternatively, see [Hook registry submission with StackSets](#Hook-registry-submission-with-StackSets) to submit the hook as a private extension to the registry in multiple regions with one operation):

```shell
cfn generate && mvn clean verify && cfn submit --set-default --region us-east-1
```

- Configure this hook: create a `type_config.json` file as shown next (for more information on `Properties` defined for this hook, see [Configuration options](#Configuration-options)):

```shell
cat <<EOF > type_config.json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                "UseGetEbsEncryptionByDefaultAsFallback": "no",
                "ValidateAmiBlockDeviceMappingEncryptionSettings": "no",
                "ValidateBucketKeyEnabled": "no"
            }
        }
    }
}
EOF
```

- By default, all the [supported resource type targets in this hook](#Supported-resource-types-and-properties-in-this-hook) are included.  You can, optionally, choose to only include the supported targets you require (thus, excluding the others) by adding the `TargetFilters` section to the type configuration that you will apply (as shown later on in this file).  For example, if you only want to trigger the hook for `AWS::S3::Bucket` and `AWS::SQS::Queue` resource types on pre-create and pre-update operations, add the `TargetFilters` section as follows (for more information on configuring hooks, see the [Hooks structure](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html) page):

```json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                [...omitted for brevity...]
            },
            "TargetFilters":{
                "TargetNames": [
                    "AWS::S3::Bucket",
                    "AWS::SQS::Queue"
                ],
                "Actions": [
                    "CREATE",
                    "UPDATE"
                ],
                "InvocationPoints": [
                    "PRE_PROVISION"
                ]
            }
        }
    }
}
```

- Get the [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) for this hook:

```shell
aws cloudformation list-types \
  --type HOOK \
  --filters TypeNamePrefix=AwsCommunity::KMS::EncryptionSettings \
  --query 'TypeSummaries[?TypeName==`AwsCommunity::KMS::EncryptionSettings`].TypeArn' \
  --output text
```

- Find the ARN in the output of the command above, and use it with this command you'll run next:

```shell
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type-arn 'YOUR_HOOK_ARN'
```

## Configuration options
### UseGetEbsEncryptionByDefaultAsFallback
Whether or not to instruct this hook to call the `GetEbsEncryptionByDefault` API to determine if EBS [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) is enabled for your account in the current Region.  If EBS encryption by default is enabled for your account in the current Region, this hook does not perform additional policy-as-code validation checks for a number of resource type properties, except for certain regular expression pattern checks (such as for this `KmsKeyId` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-kmskeyid) values) or for certain missing mandatory property checks (such as for `LaunchTemplateData` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html) values).

For more information on which resource type properties use this configuration option, see [Supported resource types and properties in this hook](#Supported-resource-types-and-properties-in-this-hook).  If you wish to activate this policy-as-code validation as a fallback strategy, choose `yes`; otherwise, choose `no` (default).

### ValidateAmiBlockDeviceMappingEncryptionSettings
When you specify an [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) ID for the `ImageId` property of resource types such as `AWS::AutoScaling::LaunchConfiguration`, `AWS::EC2::Instance`, and `AWS::EC2::LaunchTemplate`, or when this hook determines the AMI ID via the instance ID property value by calling e.g., the `DescribeInstances` EC2 API (for example, the `InstanceId` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instanceid)), whether to validate the `BlockDeviceMapping` encryption settings of the AMI.  If you wish to activate this policy-as-code validation check, choose `yes`; otherwise, choose `no` (default).

### ValidateBucketKeyEnabled
Whether to validate if the `BucketKeyEnabled` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html#cfn-s3-bucket-serversideencryptionrule-bucketkeyenabled) for the Amazon S3 bucket resource type is set to `true`.  If you wish to activate this policy-as-code validation check, choose `yes`; otherwise, choose `no` (default).

## Hook registry submission with StackSets
This section will guide you through the process of submitting the hook to the registry as a private extension using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html), to multiple regions with one operation.

To get started, use the command below to build and package the hook in an `awscommunity-kms-encryptionsettings.zip` ZIP archive:

```shell
mvn clean verify && cfn submit --dry-run
```

Upload the ZIP archive to a bucket you own; later on, you'll need to reference the object URL of this ZIP file you uploaded, so make a note of it.

Following steps assume you'll choose to use the [self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html) to operate with StackSets.  To get started, prepare your account by following [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html): follow steps in [Set up basic permissions for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html#stacksets-prereqs-accountsetup), and create both the `AWSCloudFormationStackSetAdministrationRole` and `AWSCloudFormationStackSetExecutionRole` resources in your account.

Once ready, you'll use the AWS CloudFormation [console](https://console.aws.amazon.com/cloudformation/) to [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html), for which you'll choose to use self-managed permissions:

- In the CloudFormation console, choose **StackSets**.
- Choose **Create StackSet**.
- In the **Choose a template** page, choose **Self-service permissions**.
- Specify the admin **IAM role name** you created earlier: `AWSCloudFormationStackSetAdministrationRole`.
- Specify the **IAM execution role name** you created earlier: `AWSCloudFormationStackSetExecutionRole`.
- Go to the **Prerequisite - Prepare template** section.
- Choose **Template is ready**.
- Specify the template to use in the **Specify template** section: choose to upload the `templates/private-registry-submit.yaml` template; alternatively, first upload the template to a bucket you own, and then provide the Amazon S3 template URL.  **Note that by using this template you'll also create a KMS key for each region you'll choose**, and use each key with [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) log group resources that the template describes: whilst you are not required to use KMS with log group resources, the template describes a key for such resources so that the `AwsCommunity::KMS::EncryptionSettings` hook will find them to be compliant (this hook encompasses log groups) as you update the stack set in the future.
- Choose **Next**.
- In **Specify StackSet details**, specify the StackSet name and description.
- In **Parameters**, specify values you need.  In `SchemaHandlerPackage` parameter, specify the object URL of the ZIP archive you uploaded earlier.  Choose **Next**.
- In **Execution configuration**, choose the **Active** managed execution.  Choose **Next**.
- In **Accounts**, specify your [AWS account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId) in **Account numbers**.
- In the **Regions** section, specify the regions you need.
- In **Deployment options**, choose **Parallel** for **Region Concurrency**.  Choose **Next**.
- In the **Review** page, review your choices, and select **I acknowledge that AWS CloudFormation might create IAM resources**.
- Choose **Submit** to start the StackSet creation process.

## Example templates
Templates in this section are marked as:

- Non-compliant: this hook will find the given template to be non-compliant, and
- Compliant: the template will be found to be compliant, and should deploy successfully.

Notes:
- example templates shown next:
    - assume this hook is configured with the default [Configuration options](#Configuration-options) values;
    - might include additional resource types on which a target resource would depend on, and that are added here to show additional context;
- there are also templates called `integ-succeed.yml` and `integ-fail.yml` in the `test` directory, that can be used to create a stack for testing: resources described in these templates are expected to be created either successfully or not, respectively.

### AWS::AutoScaling::LaunchConfiguration
Non-compliant (`Encrypted` in `BlockDeviceMappings` is set to `false`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  LaunchConfigurationInstanceType:
    Description: Amazon EC2 instance type to use for the LaunchConfiguration resource.
    Type: String
    AllowedValues:
      - a1.large
    Default: a1.large
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            Encrypted: false
            VolumeSize: 1
            VolumeType: gp3
        - DeviceName: /dev/sdk
          Ebs:
            Encrypted: false
            VolumeSize: 1
            VolumeType: gp3
      ImageId: !Ref 'LatestAmiId'
      InstanceType: !Ref 'LaunchConfigurationInstanceType'
```

Compliant (`Encrypted` in `BlockDeviceMappings` is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  LaunchConfigurationInstanceType:
    Description: Amazon EC2 instance type to use for the LaunchConfiguration resource.
    Type: String
    AllowedValues:
      - a1.large
    Default: a1.large
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            Encrypted: true
            VolumeSize: 1
            VolumeType: gp3
        - DeviceName: /dev/sdk
          Ebs:
            Encrypted: true
            VolumeSize: 1
            VolumeType: gp3
      ImageId: !Ref 'LatestAmiId'
      InstanceType: !Ref 'LaunchConfigurationInstanceType'
```

### AWS::CloudTrail::Trail
Note that in the example shown next the `IsLogging` property is set to `false` to turn off logging for this test-only use case; independently of the setting of this property, CloudTrail will create an S3 object whose prefix starts with `AWSLogs/YOUR_ACCOUNT_ID/CloudTrail/`.

Non-compliant (the `AWS::CloudTrail::Trail` resource type is not set up to use `KMSKeyId`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  CloudTrailTrail:
    Type: AWS::CloudTrail::Trail
    Properties:
      EventSelectors:
        - IncludeManagementEvents: true
          ReadWriteType: All
      IsLogging: false
      S3BucketName: !Ref 'CloudTrailTrailS3Bucket'
      TrailName: !Sub '${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
  CloudTrailTrailS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
  CloudTrailTrailS3BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref 'CloudTrailTrailS3Bucket'
      PolicyDocument:
        Statement:
          - Action: s3:GetBucketAcl
            Condition:
              StringEquals:
                AWS:SourceArn: !Sub 'arn:${AWS::Partition}:cloudtrail:${AWS::Region}:${AWS::AccountId}:trail/${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: !GetAtt CloudTrailTrailS3Bucket.Arn
            Sid: AWSCloudTrailAclCheck20150319
          - Action: s3:PutObject
            Condition:
              StringEquals:
                AWS:SourceArn: !Sub 'arn:${AWS::Partition}:cloudtrail:${AWS::Region}:${AWS::AccountId}:trail/${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
                s3:x-amz-acl: bucket-owner-full-control
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: !Sub '${CloudTrailTrailS3Bucket.Arn}/AWSLogs/${AWS::AccountId}/*'
            Sid: AWSCloudTrailWrite20150319
        Version: "2012-10-17"
```

Note that in the example shown next:
- the `IsLogging` property is set to `false` to turn off logging for this test-only use case; independently of the setting of this property, CloudTrail will create an S3 object whose prefix starts with `AWSLogs/YOUR_ACCOUNT_ID/CloudTrail/`;
- an example KMS key policy is shown; for more information, see [Configure AWS KMS key policies for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html).

Compliant (the `AWS::CloudTrail::Trail` resource type is set up to use `KMSKeyId`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  CloudTrailTrailKmsKey:
    Type: AWS::KMS::Key
    Properties:
      EnableKeyRotation: true
      KeyPolicy:
        Id: key-default-1
        Statement:
          - Action: kms:*
            Effect: Allow
            Principal:
              AWS: !Sub 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
            Resource: '*'
            Sid: Enable IAM User Permissions
          - Action: kms:GenerateDataKey*
            Condition:
              StringEquals:
                AWS:SourceArn: !Sub 'arn:${AWS::Partition}:cloudtrail:${AWS::Region}:${AWS::AccountId}:trail/${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
              StringLike:
                kms:EncryptionContext:aws:cloudtrail:arn: !Sub 'arn:${AWS::Partition}:cloudtrail:*:${AWS::AccountId}:trail/*'
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: '*'
            Sid: Allow CloudTrail to encrypt logs
          - Action: kms:DescribeKey
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: '*'
            Sid: Allow CloudTrail to describe key
          - Action:
              - kms:Decrypt
              - kms:ReEncryptFrom
            Condition:
              StringEquals:
                kms:CallerAccount: !Ref 'AWS::AccountId'
              StringLike:
                kms:EncryptionContext:aws:cloudtrail:arn: !Sub 'arn:${AWS::Partition}:cloudtrail:*:${AWS::AccountId}:trail/*'
            Effect: Allow
            Principal:
              AWS: '*'
            Resource: '*'
            Sid: Allow principals in the account to decrypt log files
        Version: "2012-10-17"
      PendingWindowInDays: 7
  CloudTrailTrail:
    Type: AWS::CloudTrail::Trail
    Properties:
      EventSelectors:
        - IncludeManagementEvents: true
          ReadWriteType: All
      IsLogging: false
      KMSKeyId: !Ref 'CloudTrailTrailKmsKey'
      S3BucketName: !Ref 'CloudTrailTrailS3Bucket'
      TrailName: !Sub '${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
  CloudTrailTrailS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
  CloudTrailTrailS3BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref 'CloudTrailTrailS3Bucket'
      PolicyDocument:
        Statement:
          - Action: s3:GetBucketAcl
            Condition:
              StringEquals:
                AWS:SourceArn: !Sub 'arn:${AWS::Partition}:cloudtrail:${AWS::Region}:${AWS::AccountId}:trail/${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: !GetAtt CloudTrailTrailS3Bucket.Arn
            Sid: AWSCloudTrailAclCheck20150319
          - Action: s3:PutObject
            Condition:
              StringEquals:
                AWS:SourceArn: !Sub 'arn:${AWS::Partition}:cloudtrail:${AWS::Region}:${AWS::AccountId}:trail/${AWS::Partition}-${AWS::AccountId}-${AWS::Region}-test-only-trail'
                s3:x-amz-acl: bucket-owner-full-control
            Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Resource: !Sub '${CloudTrailTrailS3Bucket.Arn}/AWSLogs/${AWS::AccountId}/*'
            Sid: AWSCloudTrailWrite20150319
        Version: "2012-10-17"
```

### AWS::DynamoDB::GlobalTable
Non-compliant (`SSESpecification` properties are missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  DynamoDbGlobalTable:
    Type: AWS::DynamoDB::GlobalTable
    Properties:
      AttributeDefinitions:
        - AttributeName: Book
          AttributeType: S
        - AttributeName: Author
          AttributeType: S
      BillingMode: PAY_PER_REQUEST
      KeySchema:
        - AttributeName: Book
          KeyType: HASH
        - AttributeName: Author
          KeyType: RANGE
      Replicas:
        - Region: !Ref 'AWS::Region'
          TableClass: STANDARD
```

Compliant (`SSESpecification` properties are present, and are set up to use KMS encryption):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  DynamoDbGlobalTable:
    Type: AWS::DynamoDB::GlobalTable
    Properties:
      AttributeDefinitions:
        - AttributeName: Book
          AttributeType: S
        - AttributeName: Author
          AttributeType: S
      BillingMode: PAY_PER_REQUEST
      KeySchema:
        - AttributeName: Book
          KeyType: HASH
        - AttributeName: Author
          KeyType: RANGE
      Replicas:
        - Region: !Ref 'AWS::Region'
          TableClass: STANDARD
      SSESpecification:
        SSEEnabled: true
        SSEType: KMS
```

### AWS::DynamoDB::Table
Non-compliant (`SSESpecification` properties are missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  DynamoDbTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: Book
          AttributeType: S
        - AttributeName: Author
          AttributeType: S
      KeySchema:
        - AttributeName: Book
          KeyType: HASH
        - AttributeName: Author
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: 1
        WriteCapacityUnits: 1
```

Compliant (`SSESpecification` properties are present, and are set up to use KMS encryption):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  DynamoDbTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: Book
          AttributeType: S
        - AttributeName: Author
          AttributeType: S
      KeySchema:
        - AttributeName: Book
          KeyType: HASH
        - AttributeName: Author
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: 1
        WriteCapacityUnits: 1
      SSESpecification:
        SSEEnabled: true
        SSEType: KMS
```

### AWS::EC2::Instance
Non-compliant (`Encrypted` in `BlockDeviceMappings` is set to `false`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  InstanceType:
    Description: Amazon EC2 instance type to use.
    Type: String
    AllowedValues:
      - t2.micro
      - t2.small
    Default: t2.micro
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  Instance:
    Type: AWS::EC2::Instance
    Properties:
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            Encrypted: false
            VolumeSize: 1
            VolumeType: gp3
        - DeviceName: /dev/sdk
          Ebs:
            Encrypted: false
            VolumeSize: 1
            VolumeType: gp3
      ImageId: !Ref 'LatestAmiId'
      InstanceType: !Ref 'InstanceType'
```

Compliant (`Encrypted` in `BlockDeviceMappings` is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  InstanceType:
    Description: Amazon EC2 instance type to use.
    Type: String
    AllowedValues:
      - t2.micro
      - t2.small
    Default: t2.micro
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  Instance:
    Type: AWS::EC2::Instance
    Properties:
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            Encrypted: true
            VolumeSize: 1
            VolumeType: gp3
        - DeviceName: /dev/sdk
          Ebs:
            Encrypted: true
            VolumeSize: 1
            VolumeType: gp3
      ImageId: !Ref 'LatestAmiId'
      InstanceType: !Ref 'InstanceType'
```

### AWS::EC2::LaunchTemplate
Non-compliant (`Encrypted` in `BlockDeviceMappings` is set to `false`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  InstanceType:
    Description: Amazon EC2 instance type to use.
    Type: String
    AllowedValues:
      - t2.micro
      - t2.small
    Default: t2.micro
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        BlockDeviceMappings:
          - DeviceName: /dev/sdm
            Ebs:
              Encrypted: false
              VolumeSize: 1
              VolumeType: gp3
          - DeviceName: /dev/sdk
            Ebs:
              Encrypted: false
              VolumeSize: 1
              VolumeType: gp3
        ImageId: !Ref 'LatestAmiId'
        InstanceType: !Ref 'InstanceType'
```

Compliant (`Encrypted` in `BlockDeviceMappings` is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Parameters:
  InstanceType:
    Description: Amazon EC2 instance type to use.
    Type: String
    AllowedValues:
      - t2.micro
      - t2.small
    Default: t2.micro
  LatestAmiId:
    Description: Region-specific image to use.
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        BlockDeviceMappings:
          - DeviceName: /dev/sdm
            Ebs:
              Encrypted: true
              VolumeSize: 1
              VolumeType: gp3
          - DeviceName: /dev/sdk
            Ebs:
              Encrypted: true
              VolumeSize: 1
              VolumeType: gp3
        ImageId: !Ref 'LatestAmiId'
        InstanceType: !Ref 'InstanceType'
```

### AWS::EC2::Volume
Non-compliant (`Encrypted` is set to `false`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  Volume:
    Type: AWS::EC2::Volume
    Properties:
      AvailabilityZone: !Sub '${AWS::Region}a'
      Encrypted: false
      Size: 1
```

Compliant (`Encrypted` is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  Volume:
    Type: AWS::EC2::Volume
    Properties:
      AvailabilityZone: !Sub '${AWS::Region}a'
      Encrypted: true
      Size: 1
```

### AWS::EFS::FileSystem
Non-compliant (`Encrypted` is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  EfsFileSystem:
    Type: AWS::EFS::FileSystem
```

Compliant (`Encrypted` is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  EfsFileSystem:
    Type: AWS::EFS::FileSystem
    Properties:
      Encrypted: true
```

### AWS::Kinesis::Stream
Non-compliant (`StreamEncryption` properties are missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  KinesisStream:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
```

Compliant (`StreamEncryption` properties are present, and are set up to use KMS encryption):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  KinesisStream:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
      StreamEncryption:
        EncryptionType: KMS
        KeyId: alias/aws/kinesis
```

### AWS::Logs::LogGroup
Non-compliant (the `AWS::Logs::LogGroup` resource type is not set up to use `KmsKeyId`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  LogsLogGroup:
    Type: AWS::Logs::LogGroup
```

Compliant (the `AWS::Logs::LogGroup` resource type is set up to use `KmSKeyId`.  Note that the example below uses a sample configuration for the KMS key; for more information on configuration options you can use, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html) and [AWS::KMS::Key](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html)):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  LogsLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      KmsKeyId: !GetAtt LogsLogGroupKmsKey.Arn
      RetentionInDays: 365
  LogsLogGroupKmsKey:
    Type: AWS::KMS::Key
    Properties:
      EnableKeyRotation: true
      KeyPolicy:
        Id: key-default-1
        Statement:
          - Action: kms:*
            Effect: Allow
            Principal:
              AWS: !Sub 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
            Resource: '*'
            Sid: Enable IAM User Permissions
          - Action:
              - kms:Decrypt*
              - kms:Describe*
              - kms:Encrypt*
              - kms:GenerateDataKey*
              - kms:ReEncrypt*
            Condition:
              ArnLike:
                kms:EncryptionContext:aws:logs:arn: !Sub 'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*'
            Effect: Allow
            Principal:
              Service: !Sub 'logs.${AWS::Region}.amazonaws.com'
            Resource: '*'
        Version: "2012-10-17"
      PendingWindowInDays: 7
```

### AWS::RDS::DBCluster
Non-compliant (`StorageEncrypted` for the `AWS::RDS::DBCluster` resource type is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsDbCluster:
    Type: AWS::RDS::DBCluster
    Properties:
      Engine: aurora
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RdsDbClusterSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RdsDbClusterSecretsManagerSecret}::username}}'
  RdsDbClusterSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"@/'
        GenerateStringKey: password
        PasswordLength: 30
        SecretStringTemplate: '{"username": "admin"}'
  RdsDbClusterSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RdsDbClusterSecretsManagerSecret'
      TargetId: !Ref 'RdsDbCluster'
      TargetType: AWS::RDS::DBCluster
```

Compliant (`StorageEncrypted` for the `AWS::RDS::DBCluster` resource type is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsDbCluster:
    Type: AWS::RDS::DBCluster
    Properties:
      Engine: aurora
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RdsDbClusterSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RdsDbClusterSecretsManagerSecret}::username}}'
      StorageEncrypted: true
  RdsDbClusterSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"@/'
        GenerateStringKey: password
        PasswordLength: 30
        SecretStringTemplate: '{"username": "admin"}'
  RdsDbClusterSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RdsDbClusterSecretsManagerSecret'
      TargetId: !Ref 'RdsDbCluster'
      TargetType: AWS::RDS::DBCluster
```

### AWS::RDS::DBInstance
Non-compliant (`StorageEncrypted` for the `AWS::RDS::DBInstance` resource type is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsDbInstance:
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: 20
      DBInstanceClass: db.t3.micro
      DBName: testdbinstance
      Engine: MySQL
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RdsDbInstanceSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RdsDbInstanceSecretsManagerSecret}::username}}'
      PubliclyAccessible: false
  RdsDbInstanceSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"@/'
        GenerateStringKey: password
        PasswordLength: 30
        SecretStringTemplate: '{"username": "admin"}'
  RdsDbInstanceSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RdsDbInstanceSecretsManagerSecret'
      TargetId: !Ref 'RdsDbInstance'
      TargetType: AWS::RDS::DBInstance
```

Compliant (`StorageEncrypted` for the `AWS::RDS::DBInstance` resource type is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsDbInstance:
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: 20
      DBInstanceClass: db.t3.micro
      DBName: testdbinstance
      Engine: MySQL
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RdsDbInstanceSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RdsDbInstanceSecretsManagerSecret}::username}}'
      PubliclyAccessible: false
      StorageEncrypted: true
  RdsDbInstanceSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"@/'
        GenerateStringKey: password
        PasswordLength: 30
        SecretStringTemplate: '{"username": "admin"}'
  RdsDbInstanceSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RdsDbInstanceSecretsManagerSecret'
      TargetId: !Ref 'RdsDbInstance'
      TargetType: AWS::RDS::DBInstance
```

### AWS::RDS::GlobalCluster
Non-compliant (`StorageEncrypted` for the `AWS::RDS::GlobalCluster` resource type is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsGlobalCluster:
    Type: AWS::RDS::GlobalCluster
    Properties:
      Engine: aurora
```

Compliant (`StorageEncrypted` for the `AWS::RDS::GlobalCluster` resource type is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RdsGlobalCluster:
    Type: AWS::RDS::GlobalCluster
    Properties:
      Engine: aurora
      StorageEncrypted: true
```

### AWS::Redshift::Cluster
Non-compliant (`Encrypted` for the `AWS::Redshift::Cluster` resource type is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RedshiftCluster:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      DBName: testdb
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RedshiftClusterSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RedshiftClusterSecretsManagerSecret}::username}}'
      NodeType: dc2.large
      PubliclyAccessible: false
  RedshiftClusterSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"''@/\'
        GenerateStringKey: password
        PasswordLength: 64
        SecretStringTemplate: '{"username": "admin"}'
  RedshiftClusterSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RedshiftClusterSecretsManagerSecret'
      TargetId: !Ref 'RedshiftCluster'
      TargetType: AWS::Redshift::Cluster
```

Compliant (`Encrypted` for the `AWS::Redshift::Cluster` resource type is set to `true`):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  RedshiftCluster:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      DBName: testdb
      Encrypted: true
      MasterUserPassword: !Sub '{{resolve:secretsmanager:${RedshiftClusterSecretsManagerSecret}::password}}'
      MasterUsername: !Sub '{{resolve:secretsmanager:${RedshiftClusterSecretsManagerSecret}::username}}'
      NodeType: dc2.large
      PubliclyAccessible: false
  RedshiftClusterSecretsManagerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        ExcludeCharacters: '"''@/\'
        GenerateStringKey: password
        PasswordLength: 64
        SecretStringTemplate: '{"username": "admin"}'
  RedshiftClusterSecretsManagerSecretAttachment:
    Type: AWS::SecretsManager::SecretTargetAttachment
    Properties:
      SecretId: !Ref 'RedshiftClusterSecretsManagerSecret'
      TargetId: !Ref 'RedshiftCluster'
      TargetType: AWS::Redshift::Cluster
```

### AWS::S3::Bucket
Non-compliant (`ServerSideEncryptionConfiguration` properties are missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
```

Compliant (`ServerSideEncryptionConfiguration` properties are are present, and are set up to use KMS encryption):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
```

### AWS::SNS::Topic
Non-compliant (`KmsMasterKeyId` is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  SnsTopic:
    Type: AWS::SNS::Topic
```

Compliant (`KmsMasterKeyId` is present):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  SnsTopic:
    Type: AWS::SNS::Topic
    Properties:
      KmsMasterKeyId: alias/aws/sns
```

### AWS::SQS::Queue
Non-compliant (`KmsMasterKeyId` is missing):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  SqsQueue:
    Type: AWS::SQS::Queue
    Properties:
      SqsManagedSseEnabled: false
```

Compliant (`KmsMasterKeyId` is present):

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Example AWS CloudFormation template.
Resources:
  SqsQueue:
    Type: AWS::SQS::Queue
    Properties:
      KmsMasterKeyId: alias/aws/sqs
      SqsManagedSseEnabled: false
```

## Tests

### Unit tests
To run unit tests, and verify code coverage, use the following command:

```shell
mvn clean verify
```

### Contract tests
Contract tests help you validate hooks you develop work as expected, and must pass before you publish a hook you write, should you elect to publish your hook as a public extension.  Your hook does not have to pass contract tests for being registered as a private extension, but it is highly recommended you implement contract test inputs and strive to pass them anyway.

For more information, see [Testing registered hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-publishing.html#hooks-testing-registered-hooks).

To run contract tests, start with setting up a retry configuration in your `~/.aws/config` global AWS configuration file, should it be needed.  For more information, see [AWS CLI retries](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html).  Assuming you use a `default` profile, add this content to your file:

```
[default]
retry_mode = standard
max_attempts = 15
```

Next, open a new terminal window, and run:

```shell
sam local start-lambda
```

For more information, see [Testing resource types locally using AWS SAM](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html#resource-type-develop-test).

Open a another terminal window, and create a `~/.cfn-cli/` directory in your home directory:

```shell
mkdir ~/.cfn-cli/
```

Next, set up the configuration file for this hook, by copying the existing `type_config.json` file you created in the usage section above into a new `~/.cfn-cli/typeConfiguration.json` file

```shell
cp type_config.json ~/.cfn-cli/typeConfiguration.json
```

Next, build this hook, and run contract tests:

```shell
cfn generate && mvn clean verify && cfn test -v --enforce-timeout 90
```

## Hook development
For more information on developing CloudFormation Hooks, see [Developing hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html).

To extend this hook with additional resource types whose KMS-related, user-specified configuration settings you want to validate (recommendations shown below to follow the alphabetical order, where indicated, as well as other style notes, are meant to help with code maintenance):

- add the resource type name (e.g., `AWS::SQS::Queue`) to the `awscommunity-kms-encryptionsettings.json` schema, for both the `preCreate` and `preUpdate` handlers:
    - add the resource by following the alphabetical order;
    - if you plan to make API calls from the hook to the relevant AWS service, add the needed IAM permissions in `permissions` for the handlers as well, by following the alphabetical order;
- if you plan to make API calls from the hook to the relevant AWS service: update the `pom.xml` file, and add the dependency for the relevant AWS service in the `<dependencies>` section (such as, the dependency for `ec2` that is already in the POM file).  Follow the alphabetical order of the `<artifactId>` values to add the dependency;
- run `cfn generate` to generate the hook input model, so to include the schema changes above;
- update the [supported resource types in this hook](#Supported-resource-types-in-this-hook) section on this file accordingly;
- if you plan to add hook configuration options:
    - update the [usage](#Usage) and [configuration options](#Configuration-options) sections on this file accordingly, and follow the alphabetical order for entries in [configuration options](#Configuration-options);
    - do the same for the `type_config.json` file, that you can find at the root level of the project;
- update the contents of the templates called `integ-succeed.yml` and `integ-fail.yml` in the `test` directory, by adding the new resource: follow the alphabetical order of the relevant resource type: assign the logical ID of the resource a name that includes the second and the third segment of the resource type name, without the `::` delimiters and in pascal case (e.g., `S3Bucket` for `AWS::S3::Bucket`).  Resources described in these templates are expected to be created either successfully or not, respectively: reflect these intents in both templates;
- update the [example templates](#Example-templates) section on this file accordingly:
    - follow the alphabetical order of the relevant resource type;
    - add both use cases for both _Non-compliant_ and _Compliant_ cases, and add a brief description on why resources will be found to be _Non-compliant_ or _Compliant_;
- add the class where you will implement the support for the resource type:
    - as needed, create a new directory in `main/java/com/awscommunity/kms/encryptionsettings/services`, and add the relevant `package-info.java` file to it: see the `package-info.java` file for an existing service directory on this hook, and set the content for the new file accordingly;
    - add the new class file to the designated directory: mimic the name convention and method sorting that other relevant class files in other directories are using;
    - make sure the class implements the `AwsKmsIntegratedService` interface;
    - add the implementation of the class;
    - if needed, consider adding helper methods such as the existing ones in the classes inside the `helpers` package, and service-specific helpers in classes inside packages like `ebs`, `ec2`, `rds`;
- wire up the class to the `factory` in the `AwsKmsIntegratedServiceFactoryImpl` class, by following the alphabetical order;
- implement unit tests:
    - create a test model in the `Mocks` class for the resource type to cover: follow the existing methods whose names end in `MockTargetModel`;
    - consume the test model in unit tests you'll implement in the `PreCreatePreUpdateHookHandlerCommonTests` class;
    - add unit tests by following the alphabetical order of the relevant resource type;
    - wire up unit tests:
        - add the wire-up methods to both the `PreCreateHookHandlerTest` and `PreUpdateHookHandlerTest` classes;
        - when you add the wire-up methods, follow the alphabetical order of the relevant resource type;
- run `mvn clean verify` to verify unit test coverage for this hook is met;
- update contract tests inputs in the `inputs` directory: follow the alphabetical order of the relevant resource type;
- make sure all [contract tests](#Contract-tests) pass;
- submit the hook to the private registry in your account and for a given region, and test the changes.

### Notes
The RPDK will automatically generate the correct hook input model from the schema whenever the project is built via Maven. You can also do this manually with the following command: `cfn generate`.

> Please don't modify files under `target/generated-sources/rpdk`, as they will be automatically overwritten.

The code uses [Lombok](https://projectlombok.org/), and [you may have to install IDE integrations](https://projectlombok.org/) to enable auto-complete for Lombok-annotated classes.
