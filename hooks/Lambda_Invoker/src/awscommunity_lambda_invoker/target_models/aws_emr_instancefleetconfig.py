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
class AwsEmrInstancefleetconfig(BaseModel):
    InstanceFleetType: Optional[str]
    TargetOnDemandCapacity: Optional[int]
    ClusterId: Optional[str]
    TargetSpotCapacity: Optional[int]
    LaunchSpecifications: Optional["_InstanceFleetProvisioningSpecifications"]
    Id: Optional[str]
    InstanceTypeConfigs: Optional[Sequence["_InstanceTypeConfig"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrInstancefleetconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrInstancefleetconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceFleetType=json_data.get("InstanceFleetType"),
            TargetOnDemandCapacity=json_data.get("TargetOnDemandCapacity"),
            ClusterId=json_data.get("ClusterId"),
            TargetSpotCapacity=json_data.get("TargetSpotCapacity"),
            LaunchSpecifications=InstanceFleetProvisioningSpecifications._deserialize(json_data.get("LaunchSpecifications")),
            Id=json_data.get("Id"),
            InstanceTypeConfigs=deserialize_list(json_data.get("InstanceTypeConfigs"), InstanceTypeConfig),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrInstancefleetconfig = AwsEmrInstancefleetconfig


@dataclass
class InstanceFleetProvisioningSpecifications(BaseModel):
    SpotSpecification: Optional["_SpotProvisioningSpecification"]
    OnDemandSpecification: Optional["_OnDemandProvisioningSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceFleetProvisioningSpecifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceFleetProvisioningSpecifications"]:
        if not json_data:
            return None
        return cls(
            SpotSpecification=SpotProvisioningSpecification._deserialize(json_data.get("SpotSpecification")),
            OnDemandSpecification=OnDemandProvisioningSpecification._deserialize(json_data.get("OnDemandSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceFleetProvisioningSpecifications = InstanceFleetProvisioningSpecifications


@dataclass
class SpotProvisioningSpecification(BaseModel):
    AllocationStrategy: Optional[str]
    TimeoutDurationMinutes: Optional[int]
    TimeoutAction: Optional[str]
    BlockDurationMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SpotProvisioningSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotProvisioningSpecification"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            TimeoutDurationMinutes=json_data.get("TimeoutDurationMinutes"),
            TimeoutAction=json_data.get("TimeoutAction"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotProvisioningSpecification = SpotProvisioningSpecification


@dataclass
class OnDemandProvisioningSpecification(BaseModel):
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandProvisioningSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandProvisioningSpecification"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandProvisioningSpecification = OnDemandProvisioningSpecification


@dataclass
class InstanceTypeConfig(BaseModel):
    BidPrice: Optional[str]
    WeightedCapacity: Optional[int]
    EbsConfiguration: Optional["_EbsConfiguration"]
    BidPriceAsPercentageOfOnDemandPrice: Optional[float]
    CustomAmiId: Optional[str]
    Configurations: Optional[Sequence["_Configuration"]]
    InstanceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypeConfig"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            EbsConfiguration=EbsConfiguration._deserialize(json_data.get("EbsConfiguration")),
            BidPriceAsPercentageOfOnDemandPrice=json_data.get("BidPriceAsPercentageOfOnDemandPrice"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            InstanceType=json_data.get("InstanceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypeConfig = InstanceTypeConfig


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


