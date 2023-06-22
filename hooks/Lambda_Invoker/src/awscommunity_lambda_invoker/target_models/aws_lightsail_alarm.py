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
class AwsLightsailAlarm(BaseModel):
    AlarmName: Optional[str]
    MonitoredResourceName: Optional[str]
    MetricName: Optional[str]
    ComparisonOperator: Optional[str]
    ContactProtocols: Optional[AbstractSet[str]]
    AlarmArn: Optional[str]
    DatapointsToAlarm: Optional[int]
    EvaluationPeriods: Optional[int]
    NotificationEnabled: Optional[bool]
    NotificationTriggers: Optional[AbstractSet[str]]
    Threshold: Optional[float]
    TreatMissingData: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailAlarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailAlarm"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AlarmName=json_data.get("AlarmName"),
            MonitoredResourceName=json_data.get("MonitoredResourceName"),
            MetricName=json_data.get("MetricName"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            ContactProtocols=set_or_none(json_data.get("ContactProtocols")),
            AlarmArn=json_data.get("AlarmArn"),
            DatapointsToAlarm=json_data.get("DatapointsToAlarm"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            NotificationEnabled=json_data.get("NotificationEnabled"),
            NotificationTriggers=set_or_none(json_data.get("NotificationTriggers")),
            Threshold=json_data.get("Threshold"),
            TreatMissingData=json_data.get("TreatMissingData"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailAlarm = AwsLightsailAlarm


