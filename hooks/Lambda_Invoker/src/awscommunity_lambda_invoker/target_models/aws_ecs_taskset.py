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
class AwsEcsTaskset(BaseModel):
    Cluster: Optional[str]
    ExternalId: Optional[str]
    Id: Optional[str]
    LaunchType: Optional[str]
    LoadBalancers: Optional[Sequence["_LoadBalancer"]]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    PlatformVersion: Optional[str]
    Scale: Optional["_Scale"]
    Service: Optional[str]
    ServiceRegistries: Optional[Sequence["_ServiceRegistry"]]
    TaskDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsTaskset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsTaskset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Cluster=json_data.get("Cluster"),
            ExternalId=json_data.get("ExternalId"),
            Id=json_data.get("Id"),
            LaunchType=json_data.get("LaunchType"),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancer),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            PlatformVersion=json_data.get("PlatformVersion"),
            Scale=Scale._deserialize(json_data.get("Scale")),
            Service=json_data.get("Service"),
            ServiceRegistries=deserialize_list(json_data.get("ServiceRegistries"), ServiceRegistry),
            TaskDefinition=json_data.get("TaskDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsTaskset = AwsEcsTaskset


@dataclass
class LoadBalancer(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[int]
    LoadBalancerName: Optional[str]
    TargetGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancer"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancer = LoadBalancer


@dataclass
class NetworkConfiguration(BaseModel):
    AwsVpcConfiguration: Optional["_AwsVpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AwsVpcConfiguration=AwsVpcConfiguration._deserialize(json_data.get("AwsVpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class AwsVpcConfiguration(BaseModel):
    AssignPublicIp: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class Scale(BaseModel):
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Scale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scale"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scale = Scale


@dataclass
class ServiceRegistry(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[int]
    Port: Optional[int]
    RegistryArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRegistry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRegistry"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            Port=json_data.get("Port"),
            RegistryArn=json_data.get("RegistryArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRegistry = ServiceRegistry


