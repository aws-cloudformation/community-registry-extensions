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
class AwsAutoscalingScalingpolicy(BaseModel):
    MetricAggregationType: Optional[str]
    PolicyName: Optional[str]
    PolicyType: Optional[str]
    PredictiveScalingConfiguration: Optional["_PredictiveScalingConfiguration"]
    ScalingAdjustment: Optional[int]
    Cooldown: Optional[str]
    StepAdjustments: Optional[AbstractSet["_StepAdjustment"]]
    AutoScalingGroupName: Optional[str]
    MinAdjustmentMagnitude: Optional[int]
    TargetTrackingConfiguration: Optional["_TargetTrackingConfiguration"]
    EstimatedInstanceWarmup: Optional[int]
    AdjustmentType: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingScalingpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingScalingpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MetricAggregationType=json_data.get("MetricAggregationType"),
            PolicyName=json_data.get("PolicyName"),
            PolicyType=json_data.get("PolicyType"),
            PredictiveScalingConfiguration=PredictiveScalingConfiguration._deserialize(json_data.get("PredictiveScalingConfiguration")),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
            Cooldown=json_data.get("Cooldown"),
            StepAdjustments=set_or_none(json_data.get("StepAdjustments")),
            AutoScalingGroupName=json_data.get("AutoScalingGroupName"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            TargetTrackingConfiguration=TargetTrackingConfiguration._deserialize(json_data.get("TargetTrackingConfiguration")),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            AdjustmentType=json_data.get("AdjustmentType"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingScalingpolicy = AwsAutoscalingScalingpolicy


@dataclass
class PredictiveScalingConfiguration(BaseModel):
    MetricSpecifications: Optional[AbstractSet["_PredictiveScalingMetricSpecification"]]
    MaxCapacityBreachBehavior: Optional[str]
    MaxCapacityBuffer: Optional[int]
    SchedulingBufferTime: Optional[int]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingConfiguration"]:
        if not json_data:
            return None
        return cls(
            MetricSpecifications=set_or_none(json_data.get("MetricSpecifications")),
            MaxCapacityBreachBehavior=json_data.get("MaxCapacityBreachBehavior"),
            MaxCapacityBuffer=json_data.get("MaxCapacityBuffer"),
            SchedulingBufferTime=json_data.get("SchedulingBufferTime"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingConfiguration = PredictiveScalingConfiguration


@dataclass
class PredictiveScalingMetricSpecification(BaseModel):
    CustomizedCapacityMetricSpecification: Optional["_PredictiveScalingCustomizedCapacityMetric"]
    CustomizedLoadMetricSpecification: Optional["_PredictiveScalingCustomizedLoadMetric"]
    CustomizedScalingMetricSpecification: Optional["_PredictiveScalingCustomizedScalingMetric"]
    PredefinedLoadMetricSpecification: Optional["_PredictiveScalingPredefinedLoadMetric"]
    TargetValue: Optional[float]
    PredefinedScalingMetricSpecification: Optional["_PredictiveScalingPredefinedScalingMetric"]
    PredefinedMetricPairSpecification: Optional["_PredictiveScalingPredefinedMetricPair"]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            CustomizedCapacityMetricSpecification=PredictiveScalingCustomizedCapacityMetric._deserialize(json_data.get("CustomizedCapacityMetricSpecification")),
            CustomizedLoadMetricSpecification=PredictiveScalingCustomizedLoadMetric._deserialize(json_data.get("CustomizedLoadMetricSpecification")),
            CustomizedScalingMetricSpecification=PredictiveScalingCustomizedScalingMetric._deserialize(json_data.get("CustomizedScalingMetricSpecification")),
            PredefinedLoadMetricSpecification=PredictiveScalingPredefinedLoadMetric._deserialize(json_data.get("PredefinedLoadMetricSpecification")),
            TargetValue=json_data.get("TargetValue"),
            PredefinedScalingMetricSpecification=PredictiveScalingPredefinedScalingMetric._deserialize(json_data.get("PredefinedScalingMetricSpecification")),
            PredefinedMetricPairSpecification=PredictiveScalingPredefinedMetricPair._deserialize(json_data.get("PredefinedMetricPairSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingMetricSpecification = PredictiveScalingMetricSpecification


@dataclass
class PredictiveScalingCustomizedCapacityMetric(BaseModel):
    MetricDataQueries: Optional[AbstractSet["_MetricDataQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingCustomizedCapacityMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingCustomizedCapacityMetric"]:
        if not json_data:
            return None
        return cls(
            MetricDataQueries=set_or_none(json_data.get("MetricDataQueries")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingCustomizedCapacityMetric = PredictiveScalingCustomizedCapacityMetric


@dataclass
class MetricDataQuery(BaseModel):
    Label: Optional[str]
    MetricStat: Optional["_MetricStat"]
    Id: Optional[str]
    ReturnData: Optional[bool]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDataQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDataQuery"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            MetricStat=MetricStat._deserialize(json_data.get("MetricStat")),
            Id=json_data.get("Id"),
            ReturnData=json_data.get("ReturnData"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDataQuery = MetricDataQuery


@dataclass
class MetricStat(BaseModel):
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
            Metric=Metric._deserialize(json_data.get("Metric")),
            Stat=json_data.get("Stat"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStat = MetricStat


@dataclass
class Metric(BaseModel):
    MetricName: Optional[str]
    Dimensions: Optional[AbstractSet["_MetricDimension"]]
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
            Dimensions=set_or_none(json_data.get("Dimensions")),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class MetricDimension(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


@dataclass
class PredictiveScalingCustomizedLoadMetric(BaseModel):
    MetricDataQueries: Optional[AbstractSet["_MetricDataQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingCustomizedLoadMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingCustomizedLoadMetric"]:
        if not json_data:
            return None
        return cls(
            MetricDataQueries=set_or_none(json_data.get("MetricDataQueries")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingCustomizedLoadMetric = PredictiveScalingCustomizedLoadMetric


@dataclass
class PredictiveScalingCustomizedScalingMetric(BaseModel):
    MetricDataQueries: Optional[AbstractSet["_MetricDataQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingCustomizedScalingMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingCustomizedScalingMetric"]:
        if not json_data:
            return None
        return cls(
            MetricDataQueries=set_or_none(json_data.get("MetricDataQueries")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingCustomizedScalingMetric = PredictiveScalingCustomizedScalingMetric


@dataclass
class PredictiveScalingPredefinedLoadMetric(BaseModel):
    ResourceLabel: Optional[str]
    PredefinedMetricType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingPredefinedLoadMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingPredefinedLoadMetric"]:
        if not json_data:
            return None
        return cls(
            ResourceLabel=json_data.get("ResourceLabel"),
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingPredefinedLoadMetric = PredictiveScalingPredefinedLoadMetric


@dataclass
class PredictiveScalingPredefinedScalingMetric(BaseModel):
    ResourceLabel: Optional[str]
    PredefinedMetricType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingPredefinedScalingMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingPredefinedScalingMetric"]:
        if not json_data:
            return None
        return cls(
            ResourceLabel=json_data.get("ResourceLabel"),
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingPredefinedScalingMetric = PredictiveScalingPredefinedScalingMetric


@dataclass
class PredictiveScalingPredefinedMetricPair(BaseModel):
    ResourceLabel: Optional[str]
    PredefinedMetricType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingPredefinedMetricPair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingPredefinedMetricPair"]:
        if not json_data:
            return None
        return cls(
            ResourceLabel=json_data.get("ResourceLabel"),
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingPredefinedMetricPair = PredictiveScalingPredefinedMetricPair


@dataclass
class StepAdjustment(BaseModel):
    MetricIntervalUpperBound: Optional[float]
    MetricIntervalLowerBound: Optional[float]
    ScalingAdjustment: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StepAdjustment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepAdjustment"]:
        if not json_data:
            return None
        return cls(
            MetricIntervalUpperBound=json_data.get("MetricIntervalUpperBound"),
            MetricIntervalLowerBound=json_data.get("MetricIntervalLowerBound"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepAdjustment = StepAdjustment


@dataclass
class TargetTrackingConfiguration(BaseModel):
    CustomizedMetricSpecification: Optional["_CustomizedMetricSpecification"]
    TargetValue: Optional[float]
    DisableScaleIn: Optional[bool]
    PredefinedMetricSpecification: Optional["_PredefinedMetricSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomizedMetricSpecification=CustomizedMetricSpecification._deserialize(json_data.get("CustomizedMetricSpecification")),
            TargetValue=json_data.get("TargetValue"),
            DisableScaleIn=json_data.get("DisableScaleIn"),
            PredefinedMetricSpecification=PredefinedMetricSpecification._deserialize(json_data.get("PredefinedMetricSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfiguration = TargetTrackingConfiguration


@dataclass
class CustomizedMetricSpecification(BaseModel):
    MetricName: Optional[str]
    Dimensions: Optional[AbstractSet["_MetricDimension"]]
    Statistic: Optional[str]
    Unit: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Dimensions=set_or_none(json_data.get("Dimensions")),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecification = CustomizedMetricSpecification


@dataclass
class PredefinedMetricSpecification(BaseModel):
    ResourceLabel: Optional[str]
    PredefinedMetricType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceLabel=json_data.get("ResourceLabel"),
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedMetricSpecification = PredefinedMetricSpecification


