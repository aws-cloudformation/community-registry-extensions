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
class AwsPinpointApplicationsettings(BaseModel):
    Id: Optional[str]
    QuietTime: Optional["_QuietTime"]
    Limits: Optional["_Limits"]
    ApplicationId: Optional[str]
    CampaignHook: Optional["_CampaignHook"]
    CloudWatchMetricsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointApplicationsettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointApplicationsettings"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            QuietTime=QuietTime._deserialize(json_data.get("QuietTime")),
            Limits=Limits._deserialize(json_data.get("Limits")),
            ApplicationId=json_data.get("ApplicationId"),
            CampaignHook=CampaignHook._deserialize(json_data.get("CampaignHook")),
            CloudWatchMetricsEnabled=json_data.get("CloudWatchMetricsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointApplicationsettings = AwsPinpointApplicationsettings


@dataclass
class QuietTime(BaseModel):
    Start: Optional[str]
    End: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuietTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuietTime"]:
        if not json_data:
            return None
        return cls(
            Start=json_data.get("Start"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuietTime = QuietTime


@dataclass
class Limits(BaseModel):
    Daily: Optional[int]
    MaximumDuration: Optional[int]
    Total: Optional[int]
    MessagesPerSecond: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            Daily=json_data.get("Daily"),
            MaximumDuration=json_data.get("MaximumDuration"),
            Total=json_data.get("Total"),
            MessagesPerSecond=json_data.get("MessagesPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class CampaignHook(BaseModel):
    Mode: Optional[str]
    WebUrl: Optional[str]
    LambdaFunctionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignHook"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            WebUrl=json_data.get("WebUrl"),
            LambdaFunctionName=json_data.get("LambdaFunctionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignHook = CampaignHook


