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
class AwsLexBotversion(BaseModel):
    BotId: Optional[str]
    BotVersion: Optional[str]
    Description: Optional[str]
    BotVersionLocaleSpecification: Optional[Sequence["_BotVersionLocaleSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLexBotversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLexBotversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BotId=json_data.get("BotId"),
            BotVersion=json_data.get("BotVersion"),
            Description=json_data.get("Description"),
            BotVersionLocaleSpecification=deserialize_list(json_data.get("BotVersionLocaleSpecification"), BotVersionLocaleSpecification),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLexBotversion = AwsLexBotversion


@dataclass
class BotVersionLocaleSpecification(BaseModel):
    LocaleId: Optional[str]
    BotVersionLocaleDetails: Optional["_BotVersionLocaleDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_BotVersionLocaleSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotVersionLocaleSpecification"]:
        if not json_data:
            return None
        return cls(
            LocaleId=json_data.get("LocaleId"),
            BotVersionLocaleDetails=BotVersionLocaleDetails._deserialize(json_data.get("BotVersionLocaleDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotVersionLocaleSpecification = BotVersionLocaleSpecification


@dataclass
class BotVersionLocaleDetails(BaseModel):
    SourceBotVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BotVersionLocaleDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotVersionLocaleDetails"]:
        if not json_data:
            return None
        return cls(
            SourceBotVersion=json_data.get("SourceBotVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotVersionLocaleDetails = BotVersionLocaleDetails


