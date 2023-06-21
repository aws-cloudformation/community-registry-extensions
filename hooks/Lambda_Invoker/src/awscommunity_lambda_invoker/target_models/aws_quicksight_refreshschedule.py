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
class AwsQuicksightRefreshschedule(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    DataSetId: Optional[str]
    Schedule: Optional["_RefreshScheduleMap"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightRefreshschedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightRefreshschedule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            DataSetId=json_data.get("DataSetId"),
            Schedule=RefreshScheduleMap._deserialize(json_data.get("Schedule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightRefreshschedule = AwsQuicksightRefreshschedule


@dataclass
class RefreshScheduleMap(BaseModel):
    ScheduleId: Optional[str]
    ScheduleFrequency: Optional["_ScheduleFrequency"]
    StartAfterDateTime: Optional[str]
    RefreshType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefreshScheduleMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefreshScheduleMap"]:
        if not json_data:
            return None
        return cls(
            ScheduleId=json_data.get("ScheduleId"),
            ScheduleFrequency=ScheduleFrequency._deserialize(json_data.get("ScheduleFrequency")),
            StartAfterDateTime=json_data.get("StartAfterDateTime"),
            RefreshType=json_data.get("RefreshType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefreshScheduleMap = RefreshScheduleMap


@dataclass
class ScheduleFrequency(BaseModel):
    Interval: Optional[str]
    RefreshOnDay: Optional["_RefreshOnDay"]
    TimeZone: Optional[str]
    TimeOfTheDay: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleFrequency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleFrequency"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            RefreshOnDay=RefreshOnDay._deserialize(json_data.get("RefreshOnDay")),
            TimeZone=json_data.get("TimeZone"),
            TimeOfTheDay=json_data.get("TimeOfTheDay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleFrequency = ScheduleFrequency


@dataclass
class RefreshOnDay(BaseModel):
    DayOfWeek: Optional[str]
    DayOfMonth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefreshOnDay"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefreshOnDay"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            DayOfMonth=json_data.get("DayOfMonth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefreshOnDay = RefreshOnDay


