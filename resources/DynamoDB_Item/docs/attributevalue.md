# AwsCommunity::DynamoDB::Item AttributeValue

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bool" title="BOOL">BOOL</a>" : <i>Boolean</i>,
    "<a href="#l" title="L">L</a>" : <i>[ <a href="attributevalue.md">AttributeValue</a>, ... ]</i>,
    "<a href="#m" title="M">M</a>" : <i><a href="attributevalue-m.md">M</a></i>,
    "<a href="#n" title="N">N</a>" : <i>String</i>,
    "<a href="#ns" title="NS">NS</a>" : <i>[ String, ... ]</i>,
    "<a href="#null" title="NULL">NULL</a>" : <i>Boolean</i>,
    "<a href="#s" title="S">S</a>" : <i>String</i>,
    "<a href="#ss" title="SS">SS</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bool" title="BOOL">BOOL</a>: <i>Boolean</i>
<a href="#l" title="L">L</a>: <i>
      - <a href="attributevalue.md">AttributeValue</a></i>
<a href="#m" title="M">M</a>: <i><a href="attributevalue-m.md">M</a></i>
<a href="#n" title="N">N</a>: <i>String</i>
<a href="#ns" title="NS">NS</a>: <i>
      - String</i>
<a href="#null" title="NULL">NULL</a>: <i>Boolean</i>
<a href="#s" title="S">S</a>: <i>String</i>
<a href="#ss" title="SS">SS</a>: <i>
      - String</i>
</pre>

## Properties

#### BOOL

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L

_Required_: Yes

_Type_: List of <a href="attributevalue.md">AttributeValue</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### M

_Required_: Yes

_Type_: <a href="attributevalue-m.md">M</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NS

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NULL

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SS

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

