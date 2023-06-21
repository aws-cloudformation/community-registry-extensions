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
class AwsLogsMetricfilter(BaseModel):
    FilterName: Optional[str]
    FilterPattern: Optional[str]
    LogGroupName: Optional[str]
    MetricTransformations: Optional[Sequence["_MetricTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLogsMetricfilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLogsMetricfilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FilterName=json_data.get("FilterName"),
            FilterPattern=json_data.get("FilterPattern"),
            LogGroupName=json_data.get("LogGroupName"),
            MetricTransformations=deserialize_list(json_data.get("MetricTransformations"), MetricTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLogsMetricfilter = AwsLogsMetricfilter


@dataclass
class MetricTransformation(BaseModel):
    DefaultValue: Optional[float]
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    MetricValue: Optional[str]
    Unit: Optional[str]
    Dimensions: Optional[AbstractSet["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTransformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTransformation"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            MetricValue=json_data.get("MetricValue"),
            Unit=json_data.get("Unit"),
            Dimensions=set_or_none(json_data.get("Dimensions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTransformation = MetricTransformation


@dataclass
class Dimension(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimension"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimension = Dimension


