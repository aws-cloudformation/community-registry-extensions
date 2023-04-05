# AwsCommunity::Time::Sleep

Sleep a provided number of seconds between create, update, or delete operations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::Time::Sleep",
    "Properties" : {
        "<a href="#seconds" title="Seconds">Seconds</a>" : <i>Integer</i>,
        "<a href="#sleeponcreate" title="SleepOnCreate">SleepOnCreate</a>" : <i>Boolean</i>,
        "<a href="#sleeponupdate" title="SleepOnUpdate">SleepOnUpdate</a>" : <i>Boolean</i>,
        "<a href="#sleepondelete" title="SleepOnDelete">SleepOnDelete</a>" : <i>Boolean</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::Time::Sleep
Properties:
    <a href="#seconds" title="Seconds">Seconds</a>: <i>Integer</i>
    <a href="#sleeponcreate" title="SleepOnCreate">SleepOnCreate</a>: <i>Boolean</i>
    <a href="#sleeponupdate" title="SleepOnUpdate">SleepOnUpdate</a>: <i>Boolean</i>
    <a href="#sleepondelete" title="SleepOnDelete">SleepOnDelete</a>: <i>Boolean</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
</pre>

## Properties

#### Seconds

The number of seconds to sleep for.

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SleepOnCreate

If we should sleep on a create.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SleepOnUpdate

If we should sleep on an update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SleepOnDelete

If we should sleep on a delete.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

A value to represent when a sleep should occur. Any time this is updated this resource will sleep.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Id

Id is a unique identifier that is auto generated.

