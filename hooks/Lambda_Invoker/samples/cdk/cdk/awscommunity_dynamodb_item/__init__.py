import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnItem(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="1bc04b5291c26a46d918139138b992d2de976d6851d0893b0476b85bfbdfc6e6.CfnItem",
):
    '''A CloudFormation ``AwsCommunity::DynamoDB::Item``.

    :cloudformationResource: AwsCommunity::DynamoDB::Item
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        keys: typing.Sequence[typing.Union["Key", typing.Dict[builtins.str, typing.Any]]],
        table_name: builtins.str,
        item: typing.Any = None,
    ) -> None:
        '''Create a new ``AwsCommunity::DynamoDB::Item``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param keys: 
        :param table_name: The table to put the item into.
        :param item: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8fbb2e593de411134d1a7b20ea8bf0bc5ffb7a2c864c2addc5567d602959231)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnItemProps(keys=keys, table_name=table_name, item=item)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCompositeKey")
    def attr_composite_key(self) -> builtins.str:
        '''Attribute ``AwsCommunity::DynamoDB::Item.CompositeKey``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCompositeKey"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnItemProps":
        '''Resource props.'''
        return typing.cast("CfnItemProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="1bc04b5291c26a46d918139138b992d2de976d6851d0893b0476b85bfbdfc6e6.CfnItemProps",
    jsii_struct_bases=[],
    name_mapping={"keys": "keys", "table_name": "tableName", "item": "item"},
)
class CfnItemProps:
    def __init__(
        self,
        *,
        keys: typing.Sequence[typing.Union["Key", typing.Dict[builtins.str, typing.Any]]],
        table_name: builtins.str,
        item: typing.Any = None,
    ) -> None:
        '''This resource will manage the lifecycle of items in a DynamoDB table.

        :param keys: 
        :param table_name: The table to put the item into.
        :param item: 

        :schema: CfnItemProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a30b4f9e79ee0873e7a4c1ea495b0960a7bef4d3679f0748dc4366de4ae0b4bf)
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument item", value=item, expected_type=type_hints["item"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keys": keys,
            "table_name": table_name,
        }
        if item is not None:
            self._values["item"] = item

    @builtins.property
    def keys(self) -> typing.List["Key"]:
        '''
        :schema: CfnItemProps#Keys
        '''
        result = self._values.get("keys")
        assert result is not None, "Required property 'keys' is missing"
        return typing.cast(typing.List["Key"], result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The table to put the item into.

        :schema: CfnItemProps#TableName
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def item(self) -> typing.Any:
        '''
        :schema: CfnItemProps#Item
        '''
        result = self._values.get("item")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnItemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="1bc04b5291c26a46d918139138b992d2de976d6851d0893b0476b85bfbdfc6e6.Key",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_type": "attributeType",
        "attribute_value": "attributeValue",
    },
)
class Key:
    def __init__(
        self,
        *,
        attribute_name: builtins.str,
        attribute_type: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_name: 
        :param attribute_type: 
        :param attribute_value: 

        :schema: Key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98dfa9db288f67bae78a35c6ff964df81563381e5abb3885da62fbcf32c21a12)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_type", value=attribute_type, expected_type=type_hints["attribute_type"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_name": attribute_name,
            "attribute_type": attribute_type,
            "attribute_value": attribute_value,
        }

    @builtins.property
    def attribute_name(self) -> builtins.str:
        '''
        :schema: Key#AttributeName
        '''
        result = self._values.get("attribute_name")
        assert result is not None, "Required property 'attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_type(self) -> builtins.str:
        '''
        :schema: Key#AttributeType
        '''
        result = self._values.get("attribute_type")
        assert result is not None, "Required property 'attribute_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_value(self) -> builtins.str:
        '''
        :schema: Key#AttributeValue
        '''
        result = self._values.get("attribute_value")
        assert result is not None, "Required property 'attribute_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Key(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnItem",
    "CfnItemProps",
    "Key",
]

publication.publish()

def _typecheckingstub__f8fbb2e593de411134d1a7b20ea8bf0bc5ffb7a2c864c2addc5567d602959231(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    keys: typing.Sequence[typing.Union[Key, typing.Dict[builtins.str, typing.Any]]],
    table_name: builtins.str,
    item: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30b4f9e79ee0873e7a4c1ea495b0960a7bef4d3679f0748dc4366de4ae0b4bf(
    *,
    keys: typing.Sequence[typing.Union[Key, typing.Dict[builtins.str, typing.Any]]],
    table_name: builtins.str,
    item: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98dfa9db288f67bae78a35c6ff964df81563381e5abb3885da62fbcf32c21a12(
    *,
    attribute_name: builtins.str,
    attribute_type: builtins.str,
    attribute_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
