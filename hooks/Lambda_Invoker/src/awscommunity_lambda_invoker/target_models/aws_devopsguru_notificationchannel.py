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
class AwsDevopsguruNotificationchannel(BaseModel):
    Config: Optional["_NotificationChannelConfig"]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDevopsguruNotificationchannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDevopsguruNotificationchannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Config=NotificationChannelConfig._deserialize(json_data.get("Config")),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDevopsguruNotificationchannel = AwsDevopsguruNotificationchannel


@dataclass
class NotificationChannelConfig(BaseModel):
    Sns: Optional["_SnsChannelConfig"]
    Filters: Optional["_NotificationFilterConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationChannelConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationChannelConfig"]:
        if not json_data:
            return None
        return cls(
            Sns=SnsChannelConfig._deserialize(json_data.get("Sns")),
            Filters=NotificationFilterConfig._deserialize(json_data.get("Filters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationChannelConfig = NotificationChannelConfig


@dataclass
class SnsChannelConfig(BaseModel):
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsChannelConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsChannelConfig"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsChannelConfig = SnsChannelConfig


@dataclass
class NotificationFilterConfig(BaseModel):
    Severities: Optional[Sequence[str]]
    MessageTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationFilterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationFilterConfig"]:
        if not json_data:
            return None
        return cls(
            Severities=json_data.get("Severities"),
            MessageTypes=json_data.get("MessageTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationFilterConfig = NotificationFilterConfig


