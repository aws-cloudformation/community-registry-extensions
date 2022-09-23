# AwsCommunity::CloudFront::WebACLAssociation

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::CloudFront::WebACLAssociation",
    "Properties" : {
        "<a href="#DistributionArn" title="DistributionArn">DistributionArn</a>" : <i>String</i>,
        "<a href="#WebAclArn" title="WebAclArn">WebAclArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::CloudFront::WebACLAssociation
Properties:
    <a href="#DistributionArn" title="DistributionArn">Title</a>: <i>String</i>
    <a href="#WebAclArn" title="WebAclArn">WebAclArn</a>: <i>String</i>
</pre>

## Properties

#### DistributionArn

ARN of the CloudFront Distribution to which the webACL needs to be associatied. 

_Required_: Yes

_Type_: String

_Minimum_: <code>20</code>

_Maximum_: <code>250</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAclArn

ARN of the WebACL that needs to be associated with the CloudFront Distribution. 

_Required_: Yes

_Type_: String 

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

