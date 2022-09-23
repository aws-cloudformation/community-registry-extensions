# AwsCommunity::IAM::PasswordPolicy

Configure IAM Password Policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AwsCommunity::IAM::PasswordPolicy",
    "Properties" : {
        "<a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>" : <i>Boolean</i>,
        "<a href="#hardexpiry" title="HardExpiry">HardExpiry</a>" : <i>Boolean</i>,
        "<a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>" : <i>Integer</i>,
        "<a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>" : <i>Integer</i>,
        "<a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>" : <i>Integer</i>,
        "<a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>" : <i>Boolean</i>,
        "<a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>" : <i>Boolean</i>,
        "<a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>" : <i>Boolean</i>,
        "<a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: AwsCommunity::IAM::PasswordPolicy
Properties:
    <a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>: <i>Boolean</i>
    <a href="#hardexpiry" title="HardExpiry">HardExpiry</a>: <i>Boolean</i>
    <a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>: <i>Integer</i>
    <a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>: <i>Integer</i>
    <a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>: <i>Integer</i>
    <a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>: <i>Boolean</i>
    <a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>: <i>Boolean</i>
    <a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>: <i>Boolean</i>
    <a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowUsersToChangePassword

Allows all IAM users in your account to use the AWS Management Console to change their own passwords.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardExpiry

Prevents IAM users who are accessing the account via the AWS Management Console from setting a new console password after their password has expired.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordAge

The number of days that an IAM user password is valid.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumPasswordLength

The minimum number of characters allowed in an IAM user password.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReusePrevention

Specifies the number of previous passwords that IAM users are prevented from reusing.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireLowercaseCharacters

Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireNumbers

Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSymbols

Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters: ! @ # $ % ^ & * ( ) _ + - = [ ] { } | '.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireUppercaseCharacters

Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the AccountId.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### AccountId

Returns the <code>AccountId</code> value.

