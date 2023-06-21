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
class AwsGameliftFleet(BaseModel):
    AnywhereConfiguration: Optional["_AnywhereConfiguration"]
    CertificateConfiguration: Optional["_CertificateConfiguration"]
    ComputeType: Optional[str]
    Description: Optional[str]
    DesiredEC2Instances: Optional[int]
    EC2InboundPermissions: Optional[Sequence["_IpPermission"]]
    EC2InstanceType: Optional[str]
    FleetType: Optional[str]
    InstanceRoleARN: Optional[str]
    Locations: Optional[Sequence["_LocationConfiguration"]]
    LogPaths: Optional[Sequence[str]]
    MaxSize: Optional[int]
    MetricGroups: Optional[Sequence[str]]
    MinSize: Optional[int]
    Name: Optional[str]
    NewGameSessionProtectionPolicy: Optional[str]
    PeerVpcAwsAccountId: Optional[str]
    PeerVpcId: Optional[str]
    ResourceCreationLimitPolicy: Optional["_ResourceCreationLimitPolicy"]
    FleetId: Optional[str]
    BuildId: Optional[str]
    ScriptId: Optional[str]
    RuntimeConfiguration: Optional["_RuntimeConfiguration"]
    ServerLaunchParameters: Optional[str]
    ServerLaunchPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftFleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftFleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AnywhereConfiguration=AnywhereConfiguration._deserialize(json_data.get("AnywhereConfiguration")),
            CertificateConfiguration=CertificateConfiguration._deserialize(json_data.get("CertificateConfiguration")),
            ComputeType=json_data.get("ComputeType"),
            Description=json_data.get("Description"),
            DesiredEC2Instances=json_data.get("DesiredEC2Instances"),
            EC2InboundPermissions=deserialize_list(json_data.get("EC2InboundPermissions"), IpPermission),
            EC2InstanceType=json_data.get("EC2InstanceType"),
            FleetType=json_data.get("FleetType"),
            InstanceRoleARN=json_data.get("InstanceRoleARN"),
            Locations=deserialize_list(json_data.get("Locations"), LocationConfiguration),
            LogPaths=json_data.get("LogPaths"),
            MaxSize=json_data.get("MaxSize"),
            MetricGroups=json_data.get("MetricGroups"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NewGameSessionProtectionPolicy=json_data.get("NewGameSessionProtectionPolicy"),
            PeerVpcAwsAccountId=json_data.get("PeerVpcAwsAccountId"),
            PeerVpcId=json_data.get("PeerVpcId"),
            ResourceCreationLimitPolicy=ResourceCreationLimitPolicy._deserialize(json_data.get("ResourceCreationLimitPolicy")),
            FleetId=json_data.get("FleetId"),
            BuildId=json_data.get("BuildId"),
            ScriptId=json_data.get("ScriptId"),
            RuntimeConfiguration=RuntimeConfiguration._deserialize(json_data.get("RuntimeConfiguration")),
            ServerLaunchParameters=json_data.get("ServerLaunchParameters"),
            ServerLaunchPath=json_data.get("ServerLaunchPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftFleet = AwsGameliftFleet


@dataclass
class AnywhereConfiguration(BaseModel):
    Cost: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnywhereConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnywhereConfiguration"]:
        if not json_data:
            return None
        return cls(
            Cost=json_data.get("Cost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnywhereConfiguration = AnywhereConfiguration


@dataclass
class CertificateConfiguration(BaseModel):
    CertificateType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateConfiguration"]:
        if not json_data:
            return None
        return cls(
            CertificateType=json_data.get("CertificateType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateConfiguration = CertificateConfiguration


@dataclass
class IpPermission(BaseModel):
    FromPort: Optional[int]
    IpRange: Optional[str]
    Protocol: Optional[str]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IpPermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPermission"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            IpRange=json_data.get("IpRange"),
            Protocol=json_data.get("Protocol"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPermission = IpPermission


@dataclass
class LocationConfiguration(BaseModel):
    Location: Optional[str]
    LocationCapacity: Optional["_LocationCapacity"]

    @classmethod
    def _deserialize(
        cls: Type["_LocationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            LocationCapacity=LocationCapacity._deserialize(json_data.get("LocationCapacity")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationConfiguration = LocationConfiguration


@dataclass
class LocationCapacity(BaseModel):
    DesiredEC2Instances: Optional[int]
    MinSize: Optional[int]
    MaxSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LocationCapacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationCapacity"]:
        if not json_data:
            return None
        return cls(
            DesiredEC2Instances=json_data.get("DesiredEC2Instances"),
            MinSize=json_data.get("MinSize"),
            MaxSize=json_data.get("MaxSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationCapacity = LocationCapacity


@dataclass
class ResourceCreationLimitPolicy(BaseModel):
    NewGameSessionsPerCreator: Optional[int]
    PolicyPeriodInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceCreationLimitPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceCreationLimitPolicy"]:
        if not json_data:
            return None
        return cls(
            NewGameSessionsPerCreator=json_data.get("NewGameSessionsPerCreator"),
            PolicyPeriodInMinutes=json_data.get("PolicyPeriodInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceCreationLimitPolicy = ResourceCreationLimitPolicy


@dataclass
class RuntimeConfiguration(BaseModel):
    GameSessionActivationTimeoutSeconds: Optional[int]
    MaxConcurrentGameSessionActivations: Optional[int]
    ServerProcesses: Optional[Sequence["_ServerProcess"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeConfiguration"]:
        if not json_data:
            return None
        return cls(
            GameSessionActivationTimeoutSeconds=json_data.get("GameSessionActivationTimeoutSeconds"),
            MaxConcurrentGameSessionActivations=json_data.get("MaxConcurrentGameSessionActivations"),
            ServerProcesses=deserialize_list(json_data.get("ServerProcesses"), ServerProcess),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeConfiguration = RuntimeConfiguration


@dataclass
class ServerProcess(BaseModel):
    ConcurrentExecutions: Optional[int]
    LaunchPath: Optional[str]
    Parameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerProcess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerProcess"]:
        if not json_data:
            return None
        return cls(
            ConcurrentExecutions=json_data.get("ConcurrentExecutions"),
            LaunchPath=json_data.get("LaunchPath"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerProcess = ServerProcess


