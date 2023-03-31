# AwsCommunity::DynamoDB::Item

This resource will manage the lifecycle of items in a DynamoDB table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::DynamoDB::Item",
    "Properties" : {
        "<a href="#item" title="Item">Item</a>" : <i><a href="item.md">Item</a></i>,
        "<a href="#keys" title="Keys">Keys</a>" : <i>[ <a href="key.md">Key</a>, ... ]</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::DynamoDB::Item
Properties:
    <a href="#item" title="Item">Item</a>: <i><a href="item.md">Item</a></i>
    <a href="#keys" title="Keys">Keys</a>: <i>
      - <a href="key.md">Key</a></i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
</pre>

## Properties

#### Item

_Required_: No

_Type_: <a href="item.md">Item</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keys

_Required_: Yes

_Type_: List of <a href="key.md">Key</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

The table to put the item into

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### CompositeKey

Composite Key is a combination of the partition and sort key values

