# AwsCommunity::S3::DeleteBucketContents

Deletes all contents of the referenced bucket.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::S3::DeleteBucketContents",
    "Properties" : {
        "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::S3::DeleteBucketContents
Properties:
    <a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
</pre>

## Properties

#### BucketName

The name of the bucket

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the BucketName.
