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
class AwsAutoscalingplansScalingplan(BaseModel):
    Id: Optional[str]
    ScalingPlanName: Optional[str]
    ScalingPlanVersion: Optional[str]
    ApplicationSource: Optional["_ApplicationSource"]
    ScalingInstructions: Optional[Sequence["_ScalingInstruction"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingplansScalingplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingplansScalingplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ScalingPlanName=json_data.get("ScalingPlanName"),
            ScalingPlanVersion=json_data.get("ScalingPlanVersion"),
            ApplicationSource=ApplicationSource._deserialize(json_data.get("ApplicationSource")),
            ScalingInstructions=deserialize_list(json_data.get("ScalingInstructions"), ScalingInstruction),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingplansScalingplan = AwsAutoscalingplansScalingplan


@dataclass
class ApplicationSource(BaseModel):
    CloudFormationStackARN: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSource"]:
        if not json_data:
            return None
        return cls(
            CloudFormationStackARN=json_data.get("CloudFormationStackARN"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSource = ApplicationSource


@dataclass
class TagFilter(BaseModel):
    Values: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilter"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilter = TagFilter


@dataclass
class ScalingInstruction(BaseModel):
    DisableDynamicScaling: Optional[bool]
    ServiceNamespace: Optional[str]
    PredictiveScalingMaxCapacityBehavior: Optional[str]
    ScalableDimension: Optional[str]
    ScalingPolicyUpdateBehavior: Optional[str]
    MinCapacity: Optional[int]
    TargetTrackingConfigurations: Optional[Sequence["_TargetTrackingConfiguration"]]
    PredictiveScalingMaxCapacityBuffer: Optional[int]
    CustomizedLoadMetricSpecification: Optional["_CustomizedLoadMetricSpecification"]
    PredefinedLoadMetricSpecification: Optional["_PredefinedLoadMetricSpecification"]
    ResourceId: Optional[str]
    ScheduledActionBufferTime: Optional[int]
    MaxCapacity: Optional[int]
    PredictiveScalingMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingInstruction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingInstruction"]:
        if not json_data:
            return None
        return cls(
            DisableDynamicScaling=json_data.get("DisableDynamicScaling"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            PredictiveScalingMaxCapacityBehavior=json_data.get("PredictiveScalingMaxCapacityBehavior"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ScalingPolicyUpdateBehavior=json_data.get("ScalingPolicyUpdateBehavior"),
            MinCapacity=json_data.get("MinCapacity"),
            TargetTrackingConfigurations=deserialize_list(json_data.get("TargetTrackingConfigurations"), TargetTrackingConfiguration),
            PredictiveScalingMaxCapacityBuffer=json_data.get("PredictiveScalingMaxCapacityBuffer"),
            CustomizedLoadMetricSpecification=CustomizedLoadMetricSpecification._deserialize(json_data.get("CustomizedLoadMetricSpecification")),
            PredefinedLoadMetricSpecification=PredefinedLoadMetricSpecification._deserialize(json_data.get("PredefinedLoadMetricSpecification")),
            ResourceId=json_data.get("ResourceId"),
            ScheduledActionBufferTime=json_data.get("ScheduledActionBufferTime"),
            MaxCapacity=json_data.get("MaxCapacity"),
            PredictiveScalingMode=json_data.get("PredictiveScalingMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingInstruction = ScalingInstruction


@dataclass
class TargetTrackingConfiguration(BaseModel):
    ScaleOutCooldown: Optional[int]
    TargetValue: Optional[float]
    PredefinedScalingMetricSpecification: Optional["_PredefinedScalingMetricSpecification"]
    DisableScaleIn: Optional[bool]
    ScaleInCooldown: Optional[int]
    EstimatedInstanceWarmup: Optional[int]
    CustomizedScalingMetricSpecification: Optional["_CustomizedScalingMetricSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
            PredefinedScalingMetricSpecification=PredefinedScalingMetricSpecification._deserialize(json_data.get("PredefinedScalingMetricSpecification")),
            DisableScaleIn=json_data.get("DisableScaleIn"),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            CustomizedScalingMetricSpecification=CustomizedScalingMetricSpecification._deserialize(json_data.get("CustomizedScalingMetricSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfiguration = TargetTrackingConfiguration


@dataclass
class PredefinedScalingMetricSpecification(BaseModel):
    ResourceLabel: Optional[str]
    PredefinedScalingMetricType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedScalingMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedScalingMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceLabel=json_data.get("ResourceLabel"),
            PredefinedScalingMetricType=json_data.get("PredefinedScalingMetricType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedScalingMetricSpecification = PredefinedScalingMetricSpecification


@dataclass
class CustomizedScalingMetricSpecification(BaseModel):
    MetricName: Optional[str]
    Statistic: Optional[str]
    Dimensions: Optional[Sequence["_MetricDimension"]]
    Unit: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedScalingMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedScalingMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Statistic=json_data.get("Statistic"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), MetricDimension),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedScalingMetricSpecification = CustomizedScalingMetricSpecification


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
class CustomizedLoadMetricSpecification(BaseModel):
    MetricName: Optional[str]
    Statistic: Optional[str]
    Dimensions: Optional[Sequence["_MetricDimension"]]
    Unit: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedLoadMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedLoadMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Statistic=json_data.get("Statistic"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), MetricDimension),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedLoadMetricSpecification = CustomizedLoadMetricSpecification


@dataclass
class PredefinedLoadMetricSpecification(BaseModel):
    PredefinedLoadMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedLoadMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedLoadMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            PredefinedLoadMetricType=json_data.get("PredefinedLoadMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedLoadMetricSpecification = PredefinedLoadMetricSpecification


