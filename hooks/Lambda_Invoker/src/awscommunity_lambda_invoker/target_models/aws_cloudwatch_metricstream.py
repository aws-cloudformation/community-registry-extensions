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
class AwsCloudwatchMetricstream(BaseModel):
    CreationDate: Optional[str]
    StatisticsConfigurations: Optional[Sequence["_MetricStreamStatisticsConfiguration"]]
    FirehoseArn: Optional[str]
    OutputFormat: Optional[str]
    ExcludeFilters: Optional[Sequence["_MetricStreamFilter"]]
    RoleArn: Optional[str]
    Name: Optional[str]
    IncludeLinkedAccountsMetrics: Optional[bool]
    IncludeFilters: Optional[Sequence["_MetricStreamFilter"]]
    State: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]
    LastUpdateDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchMetricstream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchMetricstream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreationDate=json_data.get("CreationDate"),
            StatisticsConfigurations=deserialize_list(json_data.get("StatisticsConfigurations"), MetricStreamStatisticsConfiguration),
            FirehoseArn=json_data.get("FirehoseArn"),
            OutputFormat=json_data.get("OutputFormat"),
            ExcludeFilters=deserialize_list(json_data.get("ExcludeFilters"), MetricStreamFilter),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
            IncludeLinkedAccountsMetrics=json_data.get("IncludeLinkedAccountsMetrics"),
            IncludeFilters=deserialize_list(json_data.get("IncludeFilters"), MetricStreamFilter),
            State=json_data.get("State"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            LastUpdateDate=json_data.get("LastUpdateDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchMetricstream = AwsCloudwatchMetricstream


@dataclass
class MetricStreamStatisticsConfiguration(BaseModel):
    IncludeMetrics: Optional[Sequence["_MetricStreamStatisticsMetric"]]
    AdditionalStatistics: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamStatisticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamStatisticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            IncludeMetrics=deserialize_list(json_data.get("IncludeMetrics"), MetricStreamStatisticsMetric),
            AdditionalStatistics=json_data.get("AdditionalStatistics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamStatisticsConfiguration = MetricStreamStatisticsConfiguration


@dataclass
class MetricStreamStatisticsMetric(BaseModel):
    MetricName: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamStatisticsMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamStatisticsMetric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamStatisticsMetric = MetricStreamStatisticsMetric


@dataclass
class MetricStreamFilter(BaseModel):
    MetricNames: Optional[Sequence[str]]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamFilter"]:
        if not json_data:
            return None
        return cls(
            MetricNames=json_data.get("MetricNames"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamFilter = MetricStreamFilter


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


