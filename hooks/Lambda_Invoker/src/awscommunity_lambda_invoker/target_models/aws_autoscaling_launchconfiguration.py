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
class AwsAutoscalingLaunchconfiguration(BaseModel):
    AssociatePublicIpAddress: Optional[bool]
    BlockDeviceMappings: Optional[AbstractSet["_BlockDeviceMapping"]]
    ClassicLinkVPCId: Optional[str]
    ClassicLinkVPCSecurityGroups: Optional[Sequence[str]]
    EbsOptimized: Optional[bool]
    IamInstanceProfile: Optional[str]
    ImageId: Optional[str]
    InstanceId: Optional[str]
    InstanceMonitoring: Optional[bool]
    InstanceType: Optional[str]
    KernelId: Optional[str]
    KeyName: Optional[str]
    LaunchConfigurationName: Optional[str]
    MetadataOptions: Optional["_MetadataOptions"]
    PlacementTenancy: Optional[str]
    RamDiskId: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SpotPrice: Optional[str]
    UserData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingLaunchconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingLaunchconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            BlockDeviceMappings=set_or_none(json_data.get("BlockDeviceMappings")),
            ClassicLinkVPCId=json_data.get("ClassicLinkVPCId"),
            ClassicLinkVPCSecurityGroups=json_data.get("ClassicLinkVPCSecurityGroups"),
            EbsOptimized=json_data.get("EbsOptimized"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            ImageId=json_data.get("ImageId"),
            InstanceId=json_data.get("InstanceId"),
            InstanceMonitoring=json_data.get("InstanceMonitoring"),
            InstanceType=json_data.get("InstanceType"),
            KernelId=json_data.get("KernelId"),
            KeyName=json_data.get("KeyName"),
            LaunchConfigurationName=json_data.get("LaunchConfigurationName"),
            MetadataOptions=MetadataOptions._deserialize(json_data.get("MetadataOptions")),
            PlacementTenancy=json_data.get("PlacementTenancy"),
            RamDiskId=json_data.get("RamDiskId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotPrice=json_data.get("SpotPrice"),
            UserData=json_data.get("UserData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingLaunchconfiguration = AwsAutoscalingLaunchconfiguration


@dataclass
class BlockDeviceMapping(BaseModel):
    NoDevice: Optional[bool]
    VirtualName: Optional[str]
    Ebs: Optional["_BlockDevice"]
    DeviceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMapping"]:
        if not json_data:
            return None
        return cls(
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=BlockDevice._deserialize(json_data.get("Ebs")),
            DeviceName=json_data.get("DeviceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMapping = BlockDeviceMapping


@dataclass
class BlockDevice(BaseModel):
    SnapshotId: Optional[str]
    VolumeType: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[int]
    VolumeSize: Optional[int]
    DeleteOnTermination: Optional[bool]
    Throughput: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDevice"]:
        if not json_data:
            return None
        return cls(
            SnapshotId=json_data.get("SnapshotId"),
            VolumeType=json_data.get("VolumeType"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Throughput=json_data.get("Throughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDevice = BlockDevice


@dataclass
class MetadataOptions(BaseModel):
    HttpPutResponseHopLimit: Optional[int]
    HttpTokens: Optional[str]
    HttpEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataOptions"]:
        if not json_data:
            return None
        return cls(
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
            HttpEndpoint=json_data.get("HttpEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataOptions = MetadataOptions


