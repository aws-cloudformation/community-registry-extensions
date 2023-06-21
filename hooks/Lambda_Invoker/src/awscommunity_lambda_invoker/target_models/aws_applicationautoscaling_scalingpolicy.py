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
class AwsApplicationautoscalingScalingpolicy(BaseModel):
    Id: Optional[str]
    PolicyName: Optional[str]
    PolicyType: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    ScalingTargetId: Optional[str]
    ServiceNamespace: Optional[str]
    StepScalingPolicyConfiguration: Optional["_StepScalingPolicyConfiguration"]
    TargetTrackingScalingPolicyConfiguration: Optional["_TargetTrackingScalingPolicyConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApplicationautoscalingScalingpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApplicationautoscalingScalingpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            PolicyName=json_data.get("PolicyName"),
            PolicyType=json_data.get("PolicyType"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ScalingTargetId=json_data.get("ScalingTargetId"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StepScalingPolicyConfiguration=StepScalingPolicyConfiguration._deserialize(json_data.get("StepScalingPolicyConfiguration")),
            TargetTrackingScalingPolicyConfiguration=TargetTrackingScalingPolicyConfiguration._deserialize(json_data.get("TargetTrackingScalingPolicyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApplicationautoscalingScalingpolicy = AwsApplicationautoscalingScalingpolicy


@dataclass
class StepScalingPolicyConfiguration(BaseModel):
    AdjustmentType: Optional[str]
    Cooldown: Optional[int]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[int]
    StepAdjustments: Optional[Sequence["_StepAdjustment"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdjustmentType=json_data.get("AdjustmentType"),
            Cooldown=json_data.get("Cooldown"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            StepAdjustments=deserialize_list(json_data.get("StepAdjustments"), StepAdjustment),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepScalingPolicyConfiguration = StepScalingPolicyConfiguration


@dataclass
class StepAdjustment(BaseModel):
    MetricIntervalLowerBound: Optional[float]
    MetricIntervalUpperBound: Optional[float]
    ScalingAdjustment: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StepAdjustment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepAdjustment"]:
        if not json_data:
            return None
        return cls(
            MetricIntervalLowerBound=json_data.get("MetricIntervalLowerBound"),
            MetricIntervalUpperBound=json_data.get("MetricIntervalUpperBound"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepAdjustment = StepAdjustment


@dataclass
class TargetTrackingScalingPolicyConfiguration(BaseModel):
    CustomizedMetricSpecification: Optional["_CustomizedMetricSpecification"]
    DisableScaleIn: Optional[bool]
    PredefinedMetricSpecification: Optional["_PredefinedMetricSpecification"]
    ScaleInCooldown: Optional[int]
    ScaleOutCooldown: Optional[int]
    TargetValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomizedMetricSpecification=CustomizedMetricSpecification._deserialize(json_data.get("CustomizedMetricSpecification")),
            DisableScaleIn=json_data.get("DisableScaleIn"),
            PredefinedMetricSpecification=PredefinedMetricSpecification._deserialize(json_data.get("PredefinedMetricSpecification")),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingScalingPolicyConfiguration = TargetTrackingScalingPolicyConfiguration


@dataclass
class CustomizedMetricSpecification(BaseModel):
    Dimensions: Optional[Sequence["_MetricDimension"]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            Dimensions=deserialize_list(json_data.get("Dimensions"), MetricDimension),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecification = CustomizedMetricSpecification


@dataclass
class MetricDimension(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


@dataclass
class PredefinedMetricSpecification(BaseModel):
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedMetricSpecification = PredefinedMetricSpecification


