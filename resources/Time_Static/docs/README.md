# AwsCommunity::Time::Static

Creates a static time stamp.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::Time::Static",
    "Properties" : {
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::Time::Static
Properties:
</pre>

## Properties

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Id

UTC returns the time in UTC format.

#### Day

Day returns the day of the month.

#### Hour

Hour returns the hour within the day, in the range [0, 23].

#### Minute

Minute returns the minute offset within the hour, in the range [0, 59].

#### Month

Month returns the month of the year.

#### Second

Second returns the second offset within the minute, in the range [0, 59].

#### Unix

Unix returns a Unix time, the number of seconds elapsed since January 1, 1970 UTC.

#### Year

Year returns the year.

