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
class AwsEc2Spotfleet(BaseModel):
    Id: Optional[str]
    SpotFleetRequestConfigData: Optional["_SpotFleetRequestConfigData"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Spotfleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Spotfleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            SpotFleetRequestConfigData=SpotFleetRequestConfigData._deserialize(json_data.get("SpotFleetRequestConfigData")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Spotfleet = AwsEc2Spotfleet


@dataclass
class SpotFleetRequestConfigData(BaseModel):
    AllocationStrategy: Optional[str]
    Context: Optional[str]
    ExcessCapacityTerminationPolicy: Optional[str]
    IamFleetRole: Optional[str]
    InstanceInterruptionBehavior: Optional[str]
    InstancePoolsToUseCount: Optional[int]
    LaunchSpecifications: Optional[Sequence["_SpotFleetLaunchSpecification"]]
    LaunchTemplateConfigs: Optional[Sequence["_LaunchTemplateConfig"]]
    LoadBalancersConfig: Optional["_LoadBalancersConfig"]
    OnDemandAllocationStrategy: Optional[str]
    OnDemandMaxTotalPrice: Optional[str]
    OnDemandTargetCapacity: Optional[int]
    ReplaceUnhealthyInstances: Optional[bool]
    SpotMaintenanceStrategies: Optional["_SpotMaintenanceStrategies"]
    SpotMaxTotalPrice: Optional[str]
    SpotPrice: Optional[str]
    TargetCapacity: Optional[int]
    TerminateInstancesWithExpiration: Optional[bool]
    Type: Optional[str]
    ValidFrom: Optional[str]
    ValidUntil: Optional[str]
    TagSpecifications: Optional[Sequence["_SpotFleetTagSpecification"]]
    TargetCapacityUnitType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotFleetRequestConfigData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotFleetRequestConfigData"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            Context=json_data.get("Context"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            IamFleetRole=json_data.get("IamFleetRole"),
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
            LaunchSpecifications=deserialize_list(json_data.get("LaunchSpecifications"), SpotFleetLaunchSpecification),
            LaunchTemplateConfigs=deserialize_list(json_data.get("LaunchTemplateConfigs"), LaunchTemplateConfig),
            LoadBalancersConfig=LoadBalancersConfig._deserialize(json_data.get("LoadBalancersConfig")),
            OnDemandAllocationStrategy=json_data.get("OnDemandAllocationStrategy"),
            OnDemandMaxTotalPrice=json_data.get("OnDemandMaxTotalPrice"),
            OnDemandTargetCapacity=json_data.get("OnDemandTargetCapacity"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            SpotMaintenanceStrategies=SpotMaintenanceStrategies._deserialize(json_data.get("SpotMaintenanceStrategies")),
            SpotMaxTotalPrice=json_data.get("SpotMaxTotalPrice"),
            SpotPrice=json_data.get("SpotPrice"),
            TargetCapacity=json_data.get("TargetCapacity"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            Type=json_data.get("Type"),
            ValidFrom=json_data.get("ValidFrom"),
            ValidUntil=json_data.get("ValidUntil"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), SpotFleetTagSpecification),
            TargetCapacityUnitType=json_data.get("TargetCapacityUnitType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotFleetRequestConfigData = SpotFleetRequestConfigData


@dataclass
class SpotFleetLaunchSpecification(BaseModel):
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMapping"]]
    EbsOptimized: Optional[bool]
    IamInstanceProfile: Optional["_IamInstanceProfileSpecification"]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    KernelId: Optional[str]
    KeyName: Optional[str]
    Monitoring: Optional["_SpotFleetMonitoring"]
    NetworkInterfaces: Optional[Sequence["_InstanceNetworkInterfaceSpecification"]]
    Placement: Optional["_SpotPlacement"]
    RamdiskId: Optional[str]
    SecurityGroups: Optional[Sequence["_GroupIdentifier"]]
    SpotPrice: Optional[str]
    SubnetId: Optional[str]
    TagSpecifications: Optional[Sequence["_SpotFleetTagSpecification"]]
    UserData: Optional[str]
    WeightedCapacity: Optional[float]
    InstanceRequirements: Optional["_InstanceRequirementsRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_SpotFleetLaunchSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotFleetLaunchSpecification"]:
        if not json_data:
            return None
        return cls(
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMapping),
            EbsOptimized=json_data.get("EbsOptimized"),
            IamInstanceProfile=IamInstanceProfileSpecification._deserialize(json_data.get("IamInstanceProfile")),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            KernelId=json_data.get("KernelId"),
            KeyName=json_data.get("KeyName"),
            Monitoring=SpotFleetMonitoring._deserialize(json_data.get("Monitoring")),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), InstanceNetworkInterfaceSpecification),
            Placement=SpotPlacement._deserialize(json_data.get("Placement")),
            RamdiskId=json_data.get("RamdiskId"),
            SecurityGroups=deserialize_list(json_data.get("SecurityGroups"), GroupIdentifier),
            SpotPrice=json_data.get("SpotPrice"),
            SubnetId=json_data.get("SubnetId"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), SpotFleetTagSpecification),
            UserData=json_data.get("UserData"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            InstanceRequirements=InstanceRequirementsRequest._deserialize(json_data.get("InstanceRequirements")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotFleetLaunchSpecification = SpotFleetLaunchSpecification


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
    Encrypted: Optional[bool]
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
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDevice = EbsBlockDevice


@dataclass
class IamInstanceProfileSpecification(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamInstanceProfileSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamInstanceProfileSpecification"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamInstanceProfileSpecification = IamInstanceProfileSpecification


@dataclass
class SpotFleetMonitoring(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SpotFleetMonitoring"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotFleetMonitoring"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotFleetMonitoring = SpotFleetMonitoring


@dataclass
class InstanceNetworkInterfaceSpecification(BaseModel):
    AssociatePublicIpAddress: Optional[bool]
    DeleteOnTermination: Optional[bool]
    Description: Optional[str]
    DeviceIndex: Optional[int]
    Groups: Optional[Sequence[str]]
    Ipv6AddressCount: Optional[int]
    Ipv6Addresses: Optional[Sequence["_InstanceIpv6Address"]]
    NetworkInterfaceId: Optional[str]
    PrivateIpAddresses: Optional[Sequence["_PrivateIpAddressSpecification"]]
    SecondaryPrivateIpAddressCount: Optional[int]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceNetworkInterfaceSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceNetworkInterfaceSpecification"]:
        if not json_data:
            return None
        return cls(
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Description=json_data.get("Description"),
            DeviceIndex=json_data.get("DeviceIndex"),
            Groups=json_data.get("Groups"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Ipv6Addresses=deserialize_list(json_data.get("Ipv6Addresses"), InstanceIpv6Address),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            PrivateIpAddresses=deserialize_list(json_data.get("PrivateIpAddresses"), PrivateIpAddressSpecification),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceNetworkInterfaceSpecification = InstanceNetworkInterfaceSpecification


@dataclass
class InstanceIpv6Address(BaseModel):
    Ipv6Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceIpv6Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceIpv6Address"]:
        if not json_data:
            return None
        return cls(
            Ipv6Address=json_data.get("Ipv6Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceIpv6Address = InstanceIpv6Address


@dataclass
class PrivateIpAddressSpecification(BaseModel):
    Primary: Optional[bool]
    PrivateIpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateIpAddressSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateIpAddressSpecification"]:
        if not json_data:
            return None
        return cls(
            Primary=json_data.get("Primary"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateIpAddressSpecification = PrivateIpAddressSpecification


@dataclass
class SpotPlacement(BaseModel):
    AvailabilityZone: Optional[str]
    GroupName: Optional[str]
    Tenancy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotPlacement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotPlacement"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            GroupName=json_data.get("GroupName"),
            Tenancy=json_data.get("Tenancy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotPlacement = SpotPlacement


@dataclass
class GroupIdentifier(BaseModel):
    GroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupIdentifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupIdentifier"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupIdentifier = GroupIdentifier


@dataclass
class SpotFleetTagSpecification(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpotFleetTagSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotFleetTagSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotFleetTagSpecification = SpotFleetTagSpecification


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class InstanceRequirementsRequest(BaseModel):
    VCpuCount: Optional["_VCpuCountRangeRequest"]
    MemoryMiB: Optional["_MemoryMiBRequest"]
    CpuManufacturers: Optional[Sequence[str]]
    MemoryGiBPerVCpu: Optional["_MemoryGiBPerVCpuRequest"]
    AllowedInstanceTypes: Optional[Sequence[str]]
    ExcludedInstanceTypes: Optional[Sequence[str]]
    InstanceGenerations: Optional[Sequence[str]]
    SpotMaxPricePercentageOverLowestPrice: Optional[int]
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int]
    BareMetal: Optional[str]
    BurstablePerformance: Optional[str]
    RequireHibernateSupport: Optional[bool]
    NetworkBandwidthGbps: Optional["_NetworkBandwidthGbpsRequest"]
    NetworkInterfaceCount: Optional["_NetworkInterfaceCountRequest"]
    LocalStorage: Optional[str]
    LocalStorageTypes: Optional[Sequence[str]]
    TotalLocalStorageGB: Optional["_TotalLocalStorageGBRequest"]
    BaselineEbsBandwidthMbps: Optional["_BaselineEbsBandwidthMbpsRequest"]
    AcceleratorTypes: Optional[Sequence[str]]
    AcceleratorCount: Optional["_AcceleratorCountRequest"]
    AcceleratorManufacturers: Optional[Sequence[str]]
    AcceleratorNames: Optional[Sequence[str]]
    AcceleratorTotalMemoryMiB: Optional["_AcceleratorTotalMemoryMiBRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceRequirementsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceRequirementsRequest"]:
        if not json_data:
            return None
        return cls(
            VCpuCount=VCpuCountRangeRequest._deserialize(json_data.get("VCpuCount")),
            MemoryMiB=MemoryMiBRequest._deserialize(json_data.get("MemoryMiB")),
            CpuManufacturers=json_data.get("CpuManufacturers"),
            MemoryGiBPerVCpu=MemoryGiBPerVCpuRequest._deserialize(json_data.get("MemoryGiBPerVCpu")),
            AllowedInstanceTypes=json_data.get("AllowedInstanceTypes"),
            ExcludedInstanceTypes=json_data.get("ExcludedInstanceTypes"),
            InstanceGenerations=json_data.get("InstanceGenerations"),
            SpotMaxPricePercentageOverLowestPrice=json_data.get("SpotMaxPricePercentageOverLowestPrice"),
            OnDemandMaxPricePercentageOverLowestPrice=json_data.get("OnDemandMaxPricePercentageOverLowestPrice"),
            BareMetal=json_data.get("BareMetal"),
            BurstablePerformance=json_data.get("BurstablePerformance"),
            RequireHibernateSupport=json_data.get("RequireHibernateSupport"),
            NetworkBandwidthGbps=NetworkBandwidthGbpsRequest._deserialize(json_data.get("NetworkBandwidthGbps")),
            NetworkInterfaceCount=NetworkInterfaceCountRequest._deserialize(json_data.get("NetworkInterfaceCount")),
            LocalStorage=json_data.get("LocalStorage"),
            LocalStorageTypes=json_data.get("LocalStorageTypes"),
            TotalLocalStorageGB=TotalLocalStorageGBRequest._deserialize(json_data.get("TotalLocalStorageGB")),
            BaselineEbsBandwidthMbps=BaselineEbsBandwidthMbpsRequest._deserialize(json_data.get("BaselineEbsBandwidthMbps")),
            AcceleratorTypes=json_data.get("AcceleratorTypes"),
            AcceleratorCount=AcceleratorCountRequest._deserialize(json_data.get("AcceleratorCount")),
            AcceleratorManufacturers=json_data.get("AcceleratorManufacturers"),
            AcceleratorNames=json_data.get("AcceleratorNames"),
            AcceleratorTotalMemoryMiB=AcceleratorTotalMemoryMiBRequest._deserialize(json_data.get("AcceleratorTotalMemoryMiB")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceRequirementsRequest = InstanceRequirementsRequest


@dataclass
class VCpuCountRangeRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VCpuCountRangeRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VCpuCountRangeRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VCpuCountRangeRequest = VCpuCountRangeRequest


@dataclass
class MemoryMiBRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryMiBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryMiBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryMiBRequest = MemoryMiBRequest


@dataclass
class MemoryGiBPerVCpuRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryGiBPerVCpuRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryGiBPerVCpuRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryGiBPerVCpuRequest = MemoryGiBPerVCpuRequest


@dataclass
class NetworkBandwidthGbpsRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkBandwidthGbpsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkBandwidthGbpsRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkBandwidthGbpsRequest = NetworkBandwidthGbpsRequest


@dataclass
class NetworkInterfaceCountRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceCountRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceCountRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceCountRequest = NetworkInterfaceCountRequest


@dataclass
class TotalLocalStorageGBRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TotalLocalStorageGBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TotalLocalStorageGBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TotalLocalStorageGBRequest = TotalLocalStorageGBRequest


@dataclass
class BaselineEbsBandwidthMbpsRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BaselineEbsBandwidthMbpsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaselineEbsBandwidthMbpsRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaselineEbsBandwidthMbpsRequest = BaselineEbsBandwidthMbpsRequest


@dataclass
class AcceleratorCountRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorCountRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorCountRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorCountRequest = AcceleratorCountRequest


@dataclass
class AcceleratorTotalMemoryMiBRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorTotalMemoryMiBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorTotalMemoryMiBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorTotalMemoryMiBRequest = AcceleratorTotalMemoryMiBRequest


@dataclass
class LaunchTemplateConfig(BaseModel):
    LaunchTemplateSpecification: Optional["_FleetLaunchTemplateSpecification"]
    Overrides: Optional[Sequence["_LaunchTemplateOverrides"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfig"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=FleetLaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplateSpecification")),
            Overrides=deserialize_list(json_data.get("Overrides"), LaunchTemplateOverrides),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfig = LaunchTemplateConfig


@dataclass
class FleetLaunchTemplateSpecification(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FleetLaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetLaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetLaunchTemplateSpecification = FleetLaunchTemplateSpecification


@dataclass
class LaunchTemplateOverrides(BaseModel):
    AvailabilityZone: Optional[str]
    InstanceType: Optional[str]
    SpotPrice: Optional[str]
    SubnetId: Optional[str]
    WeightedCapacity: Optional[float]
    InstanceRequirements: Optional["_InstanceRequirementsRequest"]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateOverrides"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            InstanceType=json_data.get("InstanceType"),
            SpotPrice=json_data.get("SpotPrice"),
            SubnetId=json_data.get("SubnetId"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            InstanceRequirements=InstanceRequirementsRequest._deserialize(json_data.get("InstanceRequirements")),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateOverrides = LaunchTemplateOverrides


@dataclass
class LoadBalancersConfig(BaseModel):
    ClassicLoadBalancersConfig: Optional["_ClassicLoadBalancersConfig"]
    TargetGroupsConfig: Optional["_TargetGroupsConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancersConfig"]:
        if not json_data:
            return None
        return cls(
            ClassicLoadBalancersConfig=ClassicLoadBalancersConfig._deserialize(json_data.get("ClassicLoadBalancersConfig")),
            TargetGroupsConfig=TargetGroupsConfig._deserialize(json_data.get("TargetGroupsConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancersConfig = LoadBalancersConfig


@dataclass
class ClassicLoadBalancersConfig(BaseModel):
    ClassicLoadBalancers: Optional[Sequence["_ClassicLoadBalancer"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClassicLoadBalancersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassicLoadBalancersConfig"]:
        if not json_data:
            return None
        return cls(
            ClassicLoadBalancers=deserialize_list(json_data.get("ClassicLoadBalancers"), ClassicLoadBalancer),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassicLoadBalancersConfig = ClassicLoadBalancersConfig


@dataclass
class ClassicLoadBalancer(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClassicLoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassicLoadBalancer"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassicLoadBalancer = ClassicLoadBalancer


@dataclass
class TargetGroupsConfig(BaseModel):
    TargetGroups: Optional[Sequence["_TargetGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupsConfig"]:
        if not json_data:
            return None
        return cls(
            TargetGroups=deserialize_list(json_data.get("TargetGroups"), TargetGroup),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupsConfig = TargetGroupsConfig


@dataclass
class TargetGroup(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroup"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroup = TargetGroup


@dataclass
class SpotMaintenanceStrategies(BaseModel):
    CapacityRebalance: Optional["_SpotCapacityRebalance"]

    @classmethod
    def _deserialize(
        cls: Type["_SpotMaintenanceStrategies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotMaintenanceStrategies"]:
        if not json_data:
            return None
        return cls(
            CapacityRebalance=SpotCapacityRebalance._deserialize(json_data.get("CapacityRebalance")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotMaintenanceStrategies = SpotMaintenanceStrategies


@dataclass
class SpotCapacityRebalance(BaseModel):
    ReplacementStrategy: Optional[str]
    TerminationDelay: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SpotCapacityRebalance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotCapacityRebalance"]:
        if not json_data:
            return None
        return cls(
            ReplacementStrategy=json_data.get("ReplacementStrategy"),
            TerminationDelay=json_data.get("TerminationDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotCapacityRebalance = SpotCapacityRebalance


