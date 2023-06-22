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
class AwsEmrInstancegroupconfig(BaseModel):
    JobFlowId: Optional[str]
    AutoScalingPolicy: Optional["_AutoScalingPolicy"]
    BidPrice: Optional[str]
    InstanceCount: Optional[int]
    EbsConfiguration: Optional["_EbsConfiguration"]
    InstanceRole: Optional[str]
    CustomAmiId: Optional[str]
    Id: Optional[str]
    Configurations: Optional[Sequence["_Configuration"]]
    InstanceType: Optional[str]
    Market: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrInstancegroupconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrInstancegroupconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            JobFlowId=json_data.get("JobFlowId"),
            AutoScalingPolicy=AutoScalingPolicy._deserialize(json_data.get("AutoScalingPolicy")),
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            EbsConfiguration=EbsConfiguration._deserialize(json_data.get("EbsConfiguration")),
            InstanceRole=json_data.get("InstanceRole"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Id=json_data.get("Id"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            InstanceType=json_data.get("InstanceType"),
            Market=json_data.get("Market"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrInstancegroupconfig = AwsEmrInstancegroupconfig


@dataclass
class AutoScalingPolicy(BaseModel):
    Rules: Optional[Sequence["_ScalingRule"]]
    Constraints: Optional["_ScalingConstraints"]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingPolicy"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), ScalingRule),
            Constraints=ScalingConstraints._deserialize(json_data.get("Constraints")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingPolicy = AutoScalingPolicy


@dataclass
class ScalingRule(BaseModel):
    Action: Optional["_ScalingAction"]
    Description: Optional[str]
    Trigger: Optional["_ScalingTrigger"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingRule"]:
        if not json_data:
            return None
        return cls(
            Action=ScalingAction._deserialize(json_data.get("Action")),
            Description=json_data.get("Description"),
            Trigger=ScalingTrigger._deserialize(json_data.get("Trigger")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingRule = ScalingRule


@dataclass
class ScalingAction(BaseModel):
    Market: Optional[str]
    SimpleScalingPolicyConfiguration: Optional["_SimpleScalingPolicyConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingAction"]:
        if not json_data:
            return None
        return cls(
            Market=json_data.get("Market"),
            SimpleScalingPolicyConfiguration=SimpleScalingPolicyConfiguration._deserialize(json_data.get("SimpleScalingPolicyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingAction = ScalingAction


@dataclass
class SimpleScalingPolicyConfiguration(BaseModel):
    ScalingAdjustment: Optional[int]
    CoolDown: Optional[int]
    AdjustmentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
            CoolDown=json_data.get("CoolDown"),
            AdjustmentType=json_data.get("AdjustmentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleScalingPolicyConfiguration = SimpleScalingPolicyConfiguration


@dataclass
class ScalingTrigger(BaseModel):
    CloudWatchAlarmDefinition: Optional["_CloudWatchAlarmDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingTrigger"]:
        if not json_data:
            return None
        return cls(
            CloudWatchAlarmDefinition=CloudWatchAlarmDefinition._deserialize(json_data.get("CloudWatchAlarmDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingTrigger = ScalingTrigger


@dataclass
class CloudWatchAlarmDefinition(BaseModel):
    MetricName: Optional[str]
    ComparisonOperator: Optional[str]
    Statistic: Optional[str]
    Dimensions: Optional[Sequence["_MetricDimension"]]
    Period: Optional[int]
    EvaluationPeriods: Optional[int]
    Unit: Optional[str]
    Namespace: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchAlarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchAlarmDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistic=json_data.get("Statistic"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), MetricDimension),
            Period=json_data.get("Period"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchAlarmDefinition = CloudWatchAlarmDefinition


@dataclass
class MetricDimension(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


@dataclass
class ScalingConstraints(BaseModel):
    MinCapacity: Optional[int]
    MaxCapacity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConstraints"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConstraints = ScalingConstraints


@dataclass
class EbsConfiguration(BaseModel):
    EbsBlockDeviceConfigs: Optional[Sequence["_EbsBlockDeviceConfig"]]
    EbsOptimized: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfiguration"]:
        if not json_data:
            return None
        return cls(
            EbsBlockDeviceConfigs=deserialize_list(json_data.get("EbsBlockDeviceConfigs"), EbsBlockDeviceConfig),
            EbsOptimized=json_data.get("EbsOptimized"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfiguration = EbsConfiguration


@dataclass
class EbsBlockDeviceConfig(BaseModel):
    VolumeSpecification: Optional["_VolumeSpecification"]
    VolumesPerInstance: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceConfig"]:
        if not json_data:
            return None
        return cls(
            VolumeSpecification=VolumeSpecification._deserialize(json_data.get("VolumeSpecification")),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceConfig = EbsBlockDeviceConfig


@dataclass
class VolumeSpecification(BaseModel):
    SizeInGB: Optional[int]
    VolumeType: Optional[str]
    Iops: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeSpecification"]:
        if not json_data:
            return None
        return cls(
            SizeInGB=json_data.get("SizeInGB"),
            VolumeType=json_data.get("VolumeType"),
            Iops=json_data.get("Iops"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeSpecification = VolumeSpecification


@dataclass
class Configuration(BaseModel):
    ConfigurationProperties: Optional[MutableMapping[str, str]]
    Configurations: Optional[Sequence["_Configuration"]]
    Classification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationProperties=json_data.get("ConfigurationProperties"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            Classification=json_data.get("Classification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


