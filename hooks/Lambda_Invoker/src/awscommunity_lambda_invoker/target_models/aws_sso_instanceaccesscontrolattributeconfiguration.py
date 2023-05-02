# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsSsoInstanceaccesscontrolattributeconfiguration(BaseModel):
    InstanceArn: Optional[str]
    InstanceAccessControlAttributeConfiguration: Optional["_InstanceAccessControlAttributeConfiguration"]
    AccessControlAttributes: Optional[Sequence["_AccessControlAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsoInstanceaccesscontrolattributeconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsoInstanceaccesscontrolattributeconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            InstanceAccessControlAttributeConfiguration=InstanceAccessControlAttributeConfiguration._deserialize(json_data.get("InstanceAccessControlAttributeConfiguration")),
            AccessControlAttributes=deserialize_list(json_data.get("AccessControlAttributes"), AccessControlAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsoInstanceaccesscontrolattributeconfiguration = AwsSsoInstanceaccesscontrolattributeconfiguration


@dataclass
class InstanceAccessControlAttributeConfiguration(BaseModel):
    AccessControlAttributes: Optional[Sequence["_AccessControlAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceAccessControlAttributeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceAccessControlAttributeConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccessControlAttributes=deserialize_list(json_data.get("AccessControlAttributes"), AccessControlAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceAccessControlAttributeConfiguration = InstanceAccessControlAttributeConfiguration


@dataclass
class AccessControlAttribute(BaseModel):
    Key: Optional[str]
    Value: Optional["_AccessControlAttributeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlAttribute"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=AccessControlAttributeValue._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlAttribute = AccessControlAttribute


@dataclass
class AccessControlAttributeValue(BaseModel):
    Source: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlAttributeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlAttributeValue"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlAttributeValue = AccessControlAttributeValue


