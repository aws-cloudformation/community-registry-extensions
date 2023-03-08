# AwsCommunity::KMS::EncryptionSettings

## Activation

To activate a hook in your account, use the following JSON as the `Configuration` request parameter for [`SetTypeConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) API request.

### Configuration

<pre>
{
    "CloudFormationConfiguration": {
        "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-hook-configuration" title="HookConfiguration">HookConfiguration</a>": {
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">TargetStacks</a>":  <a href="#footnote-1">"ALL" | "NONE"</a>,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>": <a href="#footnote-1">"FAIL" | "WARN"</a> ,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-properties" title="Properties">Properties</a>" : {
                "<a href="#usegetebsencryptionbydefaultasfallback" title="UseGetEbsEncryptionByDefaultAsFallback">UseGetEbsEncryptionByDefaultAsFallback</a>" : <i>String</i>,
                "<a href="#validateamiblockdevicemappingencryptionsettings" title="ValidateAmiBlockDeviceMappingEncryptionSettings">ValidateAmiBlockDeviceMappingEncryptionSettings</a>" : <i>String</i>,
                "<a href="#validatebucketkeyenabled" title="ValidateBucketKeyEnabled">ValidateBucketKeyEnabled</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### UseGetEbsEncryptionByDefaultAsFallback

Whether or not to instruct this hook to call the `GetEbsEncryptionByDefault` API to determine if EBS encryption by default is enabled for your account in the current Region.  If EBS encryption by default is enabled for your account in the current Region, this hook does not perform additional policy-as-code validation checks for a number of resource type properties, except for certain regular expression pattern checks or for certain missing mandatory property checks.  For more information on which resource type properties use this configuration option, see `Supported resource types and properties` in this hook's documentation.  If you wish to activate this policy-as-code validation as a fallback strategy, choose `yes`; otherwise, choose `no` (default).

_Required_: No

_Type_: String

_Allowed Values_: <code>no</code> | <code>yes</code>

#### ValidateAmiBlockDeviceMappingEncryptionSettings

When you specify an Amazon Machine Image (AMI) ID for the `ImageId` property, whether to validate its BlockDeviceMapping encryption settings.  If you wish to activate this policy-as-code validation check, choose `yes`; otherwise, choose `no` (default).

_Required_: No

_Type_: String

_Allowed Values_: <code>no</code> | <code>yes</code>

#### ValidateBucketKeyEnabled

Whether to validate if the BucketKeyEnabled property for the Amazon S3 bucket resource type is set to `true`.  If you wish to activate this policy-as-code validation check, choose `yes`; otherwise, choose `no` (default).

_Required_: No

_Type_: String

_Allowed Values_: <code>no</code> | <code>yes</code>


---

## Targets

* `AWS::AutoScaling::LaunchConfiguration`
* `AWS::CloudTrail::Trail`
* `AWS::DynamoDB::GlobalTable`
* `AWS::DynamoDB::Table`
* `AWS::EC2::Instance`
* `AWS::EC2::LaunchTemplate`
* `AWS::EC2::Volume`
* `AWS::EFS::FileSystem`
* `AWS::Kinesis::Stream`
* `AWS::Logs::LogGroup`
* `AWS::RDS::DBCluster`
* `AWS::RDS::DBInstance`
* `AWS::RDS::GlobalCluster`
* `AWS::Redshift::Cluster`
* `AWS::S3::Bucket`
* `AWS::SNS::Topic`
* `AWS::SQS::Queue`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

