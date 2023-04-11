# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (AbstractSet, Any, Generic, Mapping, MutableMapping,
                    Optional, Sequence, Type, TypeVar)

from cloudformation_cli_python_lib.interface import (
    BaseModel, BaseResourceHandlerRequest)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]
    typeConfiguration: Optional["TypeConfigurationModel"]


@dataclass
class ResourceModel(BaseModel):
    Item: Optional[MutableMapping[str, "_AttributeValue"]]
    Key: Optional[MutableMapping[str, "_AttributeValue"]]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Item=json_data.get("Item"),
            Key=json_data.get("Key"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttributeValue(BaseModel):
    BOOL: Optional[bool]
    L: Optional[Sequence["_AttributeValue"]]
    M: Optional[MutableMapping[str, "_AttributeValue"]]
    N: Optional[str]
    NS: Optional[Sequence[str]]
    NULL: Optional[bool]
    S: Optional[str]
    SS: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeValue"]:
        if not json_data:
            return None
        return cls(
            BOOL=json_data.get("BOOL"),
            L=deserialize_list(json_data.get("L"), AttributeValue),
            M=json_data.get("M"),
            N=json_data.get("N"),
            NS=json_data.get("NS"),
            NULL=json_data.get("NULL"),
            S=json_data.get("S"),
            SS=json_data.get("SS"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeValue = AttributeValue


@dataclass
class TypeConfigurationModel(BaseModel):
    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls()


# work around possible type aliasing issues when variable has same name as a model
_TypeConfigurationModel = TypeConfigurationModel
