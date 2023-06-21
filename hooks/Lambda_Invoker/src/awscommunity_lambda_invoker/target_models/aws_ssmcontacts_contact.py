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
class AwsSsmcontactsContact(BaseModel):
    Alias: Optional[str]
    DisplayName: Optional[str]
    Type: Optional[str]
    Plan: Optional[Sequence["_Stage"]]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmcontactsContact"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmcontactsContact"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Alias=json_data.get("Alias"),
            DisplayName=json_data.get("DisplayName"),
            Type=json_data.get("Type"),
            Plan=deserialize_list(json_data.get("Plan"), Stage),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmcontactsContact = AwsSsmcontactsContact


@dataclass
class Stage(BaseModel):
    DurationInMinutes: Optional[int]
    Targets: Optional[Sequence["_Targets"]]
    RotationIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Stage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Stage"]:
        if not json_data:
            return None
        return cls(
            DurationInMinutes=json_data.get("DurationInMinutes"),
            Targets=deserialize_list(json_data.get("Targets"), Targets),
            RotationIds=json_data.get("RotationIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Stage = Stage


@dataclass
class Targets(BaseModel):
    ContactTargetInfo: Optional["_ContactTargetInfo"]
    ChannelTargetInfo: Optional["_ChannelTargetInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_Targets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Targets"]:
        if not json_data:
            return None
        return cls(
            ContactTargetInfo=ContactTargetInfo._deserialize(json_data.get("ContactTargetInfo")),
            ChannelTargetInfo=ChannelTargetInfo._deserialize(json_data.get("ChannelTargetInfo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Targets = Targets


@dataclass
class ContactTargetInfo(BaseModel):
    ContactId: Optional[str]
    IsEssential: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContactTargetInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContactTargetInfo"]:
        if not json_data:
            return None
        return cls(
            ContactId=json_data.get("ContactId"),
            IsEssential=json_data.get("IsEssential"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContactTargetInfo = ContactTargetInfo


@dataclass
class ChannelTargetInfo(BaseModel):
    ChannelId: Optional[str]
    RetryIntervalInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelTargetInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelTargetInfo"]:
        if not json_data:
            return None
        return cls(
            ChannelId=json_data.get("ChannelId"),
            RetryIntervalInMinutes=json_data.get("RetryIntervalInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelTargetInfo = ChannelTargetInfo


