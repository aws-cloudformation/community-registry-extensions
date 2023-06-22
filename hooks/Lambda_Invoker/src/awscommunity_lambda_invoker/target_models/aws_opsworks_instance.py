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
class AwsOpsworksInstance(BaseModel):
    Id: Optional[str]
    AvailabilityZone: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIp: Optional[str]
    PublicDnsName: Optional[str]
    PublicIp: Optional[str]
    AgentVersion: Optional[str]
    AmiId: Optional[str]
    Architecture: Optional[str]
    AutoScalingType: Optional[str]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMapping"]]
    EbsOptimized: Optional[bool]
    ElasticIps: Optional[Sequence[str]]
    Hostname: Optional[str]
    InstallUpdatesOnBoot: Optional[bool]
    InstanceType: Optional[str]
    LayerIds: Optional[Sequence[str]]
    Os: Optional[str]
    RootDeviceType: Optional[str]
    SshKeyName: Optional[str]
    StackId: Optional[str]
    SubnetId: Optional[str]
    Tenancy: Optional[str]
    TimeBasedAutoScaling: Optional["_TimeBasedAutoScaling"]
    VirtualizationType: Optional[str]
    Volumes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpsworksInstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpsworksInstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDnsName=json_data.get("PublicDnsName"),
            PublicIp=json_data.get("PublicIp"),
            AgentVersion=json_data.get("AgentVersion"),
            AmiId=json_data.get("AmiId"),
            Architecture=json_data.get("Architecture"),
            AutoScalingType=json_data.get("AutoScalingType"),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMapping),
            EbsOptimized=json_data.get("EbsOptimized"),
            ElasticIps=json_data.get("ElasticIps"),
            Hostname=json_data.get("Hostname"),
            InstallUpdatesOnBoot=json_data.get("InstallUpdatesOnBoot"),
            InstanceType=json_data.get("InstanceType"),
            LayerIds=json_data.get("LayerIds"),
            Os=json_data.get("Os"),
            RootDeviceType=json_data.get("RootDeviceType"),
            SshKeyName=json_data.get("SshKeyName"),
            StackId=json_data.get("StackId"),
            SubnetId=json_data.get("SubnetId"),
            Tenancy=json_data.get("Tenancy"),
            TimeBasedAutoScaling=TimeBasedAutoScaling._deserialize(json_data.get("TimeBasedAutoScaling")),
            VirtualizationType=json_data.get("VirtualizationType"),
            Volumes=json_data.get("Volumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpsworksInstance = AwsOpsworksInstance


@dataclass
class BlockDeviceMapping(BaseModel):
    DeviceName: Optional[str]
    Ebs: Optional["_EbsBlockDevice"]
    NoDevice: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMapping"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            Ebs=EbsBlockDevice._deserialize(json_data.get("Ebs")),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMapping = BlockDeviceMapping


@dataclass
class EbsBlockDevice(BaseModel):
    DeleteOnTermination: Optional[bool]
    Iops: Optional[int]
    SnapshotId: Optional[str]
    VolumeSize: Optional[int]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Iops=json_data.get("Iops"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDevice = EbsBlockDevice


@dataclass
class TimeBasedAutoScaling(BaseModel):
    Friday: Optional[MutableMapping[str, str]]
    Monday: Optional[MutableMapping[str, str]]
    Saturday: Optional[MutableMapping[str, str]]
    Sunday: Optional[MutableMapping[str, str]]
    Thursday: Optional[MutableMapping[str, str]]
    Tuesday: Optional[MutableMapping[str, str]]
    Wednesday: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedAutoScaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedAutoScaling"]:
        if not json_data:
            return None
        return cls(
            Friday=json_data.get("Friday"),
            Monday=json_data.get("Monday"),
            Saturday=json_data.get("Saturday"),
            Sunday=json_data.get("Sunday"),
            Thursday=json_data.get("Thursday"),
            Tuesday=json_data.get("Tuesday"),
            Wednesday=json_data.get("Wednesday"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedAutoScaling = TimeBasedAutoScaling


