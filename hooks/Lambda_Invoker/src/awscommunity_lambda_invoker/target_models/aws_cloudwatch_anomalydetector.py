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
class AwsCloudwatchAnomalydetector(BaseModel):
    MetricName: Optional[str]
    Stat: Optional[str]
    Configuration: Optional["_Configuration"]
    MetricMathAnomalyDetector: Optional["_MetricMathAnomalyDetector"]
    Dimensions: Optional[Sequence["_Dimension"]]
    Id: Optional[str]
    Namespace: Optional[str]
    SingleMetricAnomalyDetector: Optional["_SingleMetricAnomalyDetector"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchAnomalydetector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchAnomalydetector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MetricName=json_data.get("MetricName"),
            Stat=json_data.get("Stat"),
            Configuration=Configuration._deserialize(json_data.get("Configuration")),
            MetricMathAnomalyDetector=MetricMathAnomalyDetector._deserialize(json_data.get("MetricMathAnomalyDetector")),
            Dimensions=deserialize_list(json_data.get("Dimensions"), Dimension),
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
            SingleMetricAnomalyDetector=SingleMetricAnomalyDetector._deserialize(json_data.get("SingleMetricAnomalyDetector")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchAnomalydetector = AwsCloudwatchAnomalydetector


@dataclass
class Configuration(BaseModel):
    MetricTimeZone: Optional[str]
    ExcludedTimeRanges: Optional[Sequence["_Range"]]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            MetricTimeZone=json_data.get("MetricTimeZone"),
            ExcludedTimeRanges=deserialize_list(json_data.get("ExcludedTimeRanges"), Range),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


@dataclass
class Range(BaseModel):
    EndTime: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Range"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Range"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Range = Range


@dataclass
class MetricMathAnomalyDetector(BaseModel):
    MetricDataQueries: Optional[Sequence["_MetricDataQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricMathAnomalyDetector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricMathAnomalyDetector"]:
        if not json_data:
            return None
        return cls(
            MetricDataQueries=deserialize_list(json_data.get("MetricDataQueries"), MetricDataQuery),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricMathAnomalyDetector = MetricMathAnomalyDetector


@dataclass
class MetricDataQuery(BaseModel):
    AccountId: Optional[str]
    ReturnData: Optional[bool]
    Expression: Optional[str]
    MetricStat: Optional["_MetricStat"]
    Label: Optional[str]
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
            MetricStat=MetricStat._deserialize(json_data.get("MetricStat")),
            Label=json_data.get("Label"),
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
class SingleMetricAnomalyDetector(BaseModel):
    MetricName: Optional[str]
    Dimensions: Optional[Sequence["_Dimension"]]
    Stat: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleMetricAnomalyDetector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleMetricAnomalyDetector"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), Dimension),
            Stat=json_data.get("Stat"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleMetricAnomalyDetector = SingleMetricAnomalyDetector


