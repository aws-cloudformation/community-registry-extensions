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
class AwsCloudwatchAlarm(BaseModel):
    ThresholdMetricId: Optional[str]
    EvaluateLowSampleCountPercentile: Optional[str]
    ExtendedStatistic: Optional[str]
    ComparisonOperator: Optional[str]
    TreatMissingData: Optional[str]
    Dimensions: Optional[Sequence["_Dimension"]]
    Period: Optional[int]
    EvaluationPeriods: Optional[int]
    Unit: Optional[str]
    Namespace: Optional[str]
    OKActions: Optional[Sequence[str]]
    AlarmActions: Optional[Sequence[str]]
    MetricName: Optional[str]
    ActionsEnabled: Optional[bool]
    Metrics: Optional[Sequence["_MetricDataQuery"]]
    AlarmDescription: Optional[str]
    AlarmName: Optional[str]
    Statistic: Optional[str]
    InsufficientDataActions: Optional[Sequence[str]]
    Id: Optional[str]
    Arn: Optional[str]
    DatapointsToAlarm: Optional[int]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchAlarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchAlarm"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ThresholdMetricId=json_data.get("ThresholdMetricId"),
            EvaluateLowSampleCountPercentile=json_data.get("EvaluateLowSampleCountPercentile"),
            ExtendedStatistic=json_data.get("ExtendedStatistic"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            TreatMissingData=json_data.get("TreatMissingData"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), Dimension),
            Period=json_data.get("Period"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
            OKActions=json_data.get("OKActions"),
            AlarmActions=json_data.get("AlarmActions"),
            MetricName=json_data.get("MetricName"),
            ActionsEnabled=json_data.get("ActionsEnabled"),
            Metrics=deserialize_list(json_data.get("Metrics"), MetricDataQuery),
            AlarmDescription=json_data.get("AlarmDescription"),
            AlarmName=json_data.get("AlarmName"),
            Statistic=json_data.get("Statistic"),
            InsufficientDataActions=json_data.get("InsufficientDataActions"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            DatapointsToAlarm=json_data.get("DatapointsToAlarm"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchAlarm = AwsCloudwatchAlarm


@dataclass
class Dimension(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimension"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimension = Dimension


@dataclass
class MetricDataQuery(BaseModel):
    AccountId: Optional[str]
    ReturnData: Optional[bool]
    Expression: Optional[str]
    Label: Optional[str]
    MetricStat: Optional["_MetricStat"]
    Period: Optional[int]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDataQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDataQuery"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            ReturnData=json_data.get("ReturnData"),
            Expression=json_data.get("Expression"),
            Label=json_data.get("Label"),
            MetricStat=MetricStat._deserialize(json_data.get("MetricStat")),
            Period=json_data.get("Period"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDataQuery = MetricDataQuery


@dataclass
class MetricStat(BaseModel):
    Period: Optional[int]
    Metric: Optional["_Metric"]
    Stat: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStat"]:
        if not json_data:
            return None
        return cls(
            Period=json_data.get("Period"),
            Metric=Metric._deserialize(json_data.get("Metric")),
            Stat=json_data.get("Stat"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStat = MetricStat


@dataclass
class Metric(BaseModel):
    MetricName: Optional[str]
    Dimensions: Optional[Sequence["_Dimension"]]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), Dimension),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


