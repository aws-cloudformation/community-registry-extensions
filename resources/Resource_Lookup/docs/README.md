# AwsCommunity::Resource::Lookup

This resource uses the `ListResources` and `GetResource` actions of AWS Cloud Control API to perform a lookup of a resource of a given type (such as, `AWS::EC2::VPC`) in your AWS account -and current region if you are using a regional AWS service- based on a query you specify.  If only one match is found, this resource returns the primary identifier of the resource (in the `AWS::EC2::VPC` example, the ID of the VPC), that you can then consume by referencing it in your template with the `Fn::GetAtt` intrinsic function.  Note: as this resource type uses Cloud Control API, you can specify resource type search targets -like `AWS::EC2::VPC`- that are supported by Cloud Control API; for more information, see `Determining if a resource type supports Cloud Control API`: https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-types.html#resource-types-determine-support .

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::Resource::Lookup",
    "Properties" : {
        "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
        "<a href="#jmespathquery" title="JmesPathQuery">JmesPathQuery</a>" : <i>String</i>,
        "<a href="#resourcelookuprolearn" title="ResourceLookupRoleArn">ResourceLookupRoleArn</a>" : <i>String</i>,
        "<a href="#resourcemodel" title="ResourceModel">ResourceModel</a>" : <i>String</i>,
        "<a href="#lookupserialnumber" title="LookupSerialNumber">LookupSerialNumber</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i><a href="tags.md">Tags</a></i>,
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::Resource::Lookup
Properties:
    <a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
    <a href="#jmespathquery" title="JmesPathQuery">JmesPathQuery</a>: <i>String</i>
    <a href="#resourcelookuprolearn" title="ResourceLookupRoleArn">ResourceLookupRoleArn</a>: <i>String</i>
    <a href="#resourcemodel" title="ResourceModel">ResourceModel</a>: <i>String</i>
    <a href="#lookupserialnumber" title="LookupSerialNumber">LookupSerialNumber</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i><a href="tags.md">Tags</a></i>
</pre>

## Properties

#### TypeName

The resource type name you wish to use for the lookup operation.

_Required_: Yes

_Type_: String

_Pattern_: <code>^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### JmesPathQuery

A query, in JMESPath (https://jmespath.org/) format, to perform the resource lookup (example: Tags[?Key==`Owner`&&Value==`contract-test-only-test-team`]).  When you specify a new value on resource updates (for example, when you update the stack that describes this resource), a new lookup will be performed.

_Required_: Yes

_Type_: String

_Minimum Length_: <code>1</code>

_Maximum Length_: <code>4096</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ResourceLookupRoleArn

The Amazon Resource Name (ARN) of the IAM role you wish to use for performing resource lookup operations in your AWS account on your behalf; for example: arn:aws:iam::111122223333:role/my-example-role.

_Required_: Yes

_Type_: String

_Pattern_: <code>^arn:aws(-[a-z]+)*:iam::[0-9]{12}:role\/[\w+=,.@-]{1,64}$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ResourceModel

The model of the resource you're using: this additional information is required if you're using a resource type shown in the `Resources that require additional information` page (https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html#resource-operations-list-containers).  Specify the required properties using the JSON format; for example, to specify `LoadBalancerArn` and its ARN value for `AWS::ElasticLoadBalancingV2::Listener` (that you specify in the `TypeName` property), use: {"LoadBalancerArn": "REPLACE_WITH_YOUR_LOAD_BALANCER_ARN"}.

_Required_: No

_Type_: String

_Pattern_: <code>^[\s\S]*$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### LookupSerialNumber

Optional, numeric integer value (such as `1`, `2`), that you can specify to induce a new search on e.g., stack updates without modifying the value for `JmesPathQuery`.  Specify a value that is different from the previous one to induce the update; note that either adding this property to the resource if not present before an update, or removing it if previously added to the resource, will yield the same effect of changing the property value and will induce an update.

_Required_: No

_Type_: String

_Pattern_: <code>^[0-9]*$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Tags

Optional key-value pairs object (such as, `Env: Dev`, `Name: Test`) to associate to the AWS Systems Manager Parameter Store parameter resource, that the implementation of this resource type creates in your account to persist the lookup result.

_Required_: No

_Type_: <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ResourceLookupId.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### ResourceIdentifier

The resource identifier.

#### ResourceLookupId

When this resource type finds only one match as the result of a lookup operation, it then creates an AWS Systems Manager Parameter Store parameter resource in your account and current region to persist the lookup result for subsequent use (for example, when its `Read` handler is invoked).  `ResourceLookupId` holds the name of the Parameter Store parameter.

