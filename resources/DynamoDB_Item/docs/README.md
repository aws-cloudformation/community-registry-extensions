# AwsCommunity::DynamoDB::Item

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::DynamoDB::Item",
    "Properties" : {
        "<a href="#item" title="Item">Item</a>" : <i><a href="item.md">Item</a></i>,
        "<a href="#key" title="Key">Key</a>" : <i><a href="key.md">Key</a></i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::DynamoDB::Item
Properties:
    <a href="#item" title="Item">Item</a>: <i><a href="item.md">Item</a></i>
    <a href="#key" title="Key">Key</a>: <i><a href="key.md">Key</a></i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
</pre>

## Properties

#### Item

_Required_: No

_Type_: <a href="item.md">Item</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: <a href="key.md">Key</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

The table to put the item into

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the TableName.
