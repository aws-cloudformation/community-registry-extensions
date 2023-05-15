# AwsCommunity::ApplicationAutoscaling::ScheduledAction

Resource to create a Application Autoscaling Scheduled Action. Can be used with any resource that uses AWS Application Autoscaling Dimensions.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::ApplicationAutoscaling::ScheduledAction",
    "Properties" : {
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#scalabledimension" title="ScalableDimension">ScalableDimension</a>" : <i>String</i>,
        "<a href="#scalabletargetaction" title="ScalableTargetAction">ScalableTargetAction</a>" : <i><a href="scalabletargetaction.md">ScalableTargetAction</a></i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#scheduledactionname" title="ScheduledActionName">ScheduledActionName</a>" : <i>String</i>,
        "<a href="#servicenamespace" title="ServiceNamespace">ServiceNamespace</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::ApplicationAutoscaling::ScheduledAction
Properties:
    <a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#scalabledimension" title="ScalableDimension">ScalableDimension</a>: <i>String</i>
    <a href="#scalabletargetaction" title="ScalableTargetAction">ScalableTargetAction</a>: <i><a href="scalabletargetaction.md">ScalableTargetAction</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#scheduledactionname" title="ScheduledActionName">ScheduledActionName</a>: <i>String</i>
    <a href="#servicenamespace" title="ServiceNamespace">ServiceNamespace</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

Must be a valid resource as defined in https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html#autoscaling-PutScheduledAction-request-ResourceId

_Required_: Yes

_Type_: String

_Pattern_: <code>[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ScalableDimension

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ScalableTargetAction

_Required_: Yes

_Type_: <a href="scalabletargetaction.md">ScalableTargetAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Must be a valid schedule as defined in https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html#autoscaling-PutScheduledAction-request-ResourceId

_Required_: Yes

_Type_: String

_Pattern_: <code>[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledActionName

Must be a valid action name as defined in https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html#autoscaling-PutScheduledAction-request-ResourceId

_Required_: Yes

_Type_: String

_Pattern_: <code>(?!((^[ ]+.*)|(.*([\u0000-\u001f]|[\u007f-\u009f]|[:/|])+.*)|(.*[ ]+$))).+</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ServiceNamespace

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Must be a valid timestamp as defined in https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html#autoscaling-PutScheduledAction-request-ResourceId

_Required_: No

_Type_: String

_Pattern_: <code>[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ScheduledActionARN.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### ScheduledActionARN

Returns the <code>ScheduledActionARN</code> value.

