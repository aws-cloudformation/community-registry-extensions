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
class AwsAutoscalingScheduledaction(BaseModel):
    ScheduledActionName: Optional[str]
    MinSize: Optional[int]
    Recurrence: Optional[str]
    TimeZone: Optional[str]
    EndTime: Optional[str]
    AutoScalingGroupName: Optional[str]
    StartTime: Optional[str]
    DesiredCapacity: Optional[int]
    MaxSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingScheduledaction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingScheduledaction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ScheduledActionName=json_data.get("ScheduledActionName"),
            MinSize=json_data.get("MinSize"),
            Recurrence=json_data.get("Recurrence"),
            TimeZone=json_data.get("TimeZone"),
            EndTime=json_data.get("EndTime"),
            AutoScalingGroupName=json_data.get("AutoScalingGroupName"),
            StartTime=json_data.get("StartTime"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            MaxSize=json_data.get("MaxSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingScheduledaction = AwsAutoscalingScheduledaction


