# AwsCommunity::Lambda::Invoker

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
                "<a href="#registrationtablearn" title="RegistrationTableArn">RegistrationTableArn</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### RegistrationTableArn

Arn for the DynamoDB table that will hold the list of Lambda functions to invoke. The table must have a partition key called 'pk', and sort key called 'sk'. Entries should have a single additional attribute called 'lambda_arn'. You must create the table as a prerequisite to installing this hook.

_Required_: No

_Type_: String


---

## Targets

* `AWS::Lambda::Alias`
* `AWS::Lambda::CodeSigningConfig`
* `AWS::Lambda::EventInvokeConfig`
* `AWS::Lambda::EventSourceMapping`
* `AWS::Lambda::Function`
* `AWS::Lambda::LayerVersion`
* `AWS::Lambda::LayerVersionPermission`
* `AWS::Lambda::Permission`
* `AWS::Lambda::Url`
* `AWS::Lambda::Version`
* `AWS::S3::AccessPoint`
* `AWS::S3::Bucket`
* `AWS::S3::BucketPolicy`
* `AWS::S3::MultiRegionAccessPoint`
* `AWS::S3::MultiRegionAccessPointPolicy`
* `AWS::S3::StorageLens`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

