# AwsLabs::S3::BucketNotification

Configure bucket notifications for a variety of targets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsLabs::S3::BucketNotification",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#events" title="Events">Events</a>" : <i>[ String, ... ]</i>,
        "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="keyval.md">KeyVal</a>, ... ]</i>,
        "<a href="#bucketarn" title="BucketArn">BucketArn</a>" : <i>String</i>,
        "<a href="#targetarn" title="TargetArn">TargetArn</a>" : <i>String</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: AwsLabs::S3::BucketNotification
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#events" title="Events">Events</a>: <i>
      - String</i>
    <a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="keyval.md">KeyVal</a></i>
    <a href="#bucketarn" title="BucketArn">BucketArn</a>: <i>String</i>
    <a href="#targetarn" title="TargetArn">TargetArn</a>: <i>String</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### Id

A unique identifier for the notification. This is required, since we have to query all notifications configured on the bucket in order to leave any of them not defined here intact.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Events

The S3 event types. See https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-event-types

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

The filters to apply to events

_Required_: No

_Type_: List of <a href="keyval.md">KeyVal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketArn

The ARN of the bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetArn

The ARN to the Lambda Function, SQS Queue, or SNS Topic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The target type, Function, Queue, or Topic

_Required_: Yes

_Type_: String

_Allowed Values_: <code>Function</code> | <code>Queue</code> | <code>Topic</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

