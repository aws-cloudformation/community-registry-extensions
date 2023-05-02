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
class AwsRedshiftEndpointaccess(BaseModel):
    Address: Optional[str]
    ClusterIdentifier: Optional[str]
    VpcSecurityGroups: Optional[Sequence["_VpcSecurityGroup"]]
    ResourceOwner: Optional[str]
    EndpointStatus: Optional[str]
    EndpointName: Optional[str]
    EndpointCreateTime: Optional[str]
    SubnetGroupName: Optional[str]
    Port: Optional[int]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    VpcEndpoint: Optional["_VpcEndpoint"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftEndpointaccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftEndpointaccess"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Address=json_data.get("Address"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            VpcSecurityGroups=deserialize_list(json_data.get("VpcSecurityGroups"), VpcSecurityGroup),
            ResourceOwner=json_data.get("ResourceOwner"),
            EndpointStatus=json_data.get("EndpointStatus"),
            EndpointName=json_data.get("EndpointName"),
            EndpointCreateTime=json_data.get("EndpointCreateTime"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Port=json_data.get("Port"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            VpcEndpoint=VpcEndpoint._deserialize(json_data.get("VpcEndpoint")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftEndpointaccess = AwsRedshiftEndpointaccess


@dataclass
class VpcSecurityGroup(BaseModel):
    VpcSecurityGroupId: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSecurityGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSecurityGroup"]:
        if not json_data:
            return None
        return cls(
            VpcSecurityGroupId=json_data.get("VpcSecurityGroupId"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSecurityGroup = VpcSecurityGroup


@dataclass
class VpcEndpoint(BaseModel):
    VpcEndpointId: Optional[str]
    VpcId: Optional[str]
    NetworkInterfaces: Optional[Sequence["_NetworkInterface"]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcEndpoint"]:
        if not json_data:
            return None
        return cls(
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcId=json_data.get("VpcId"),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterface),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcEndpoint = VpcEndpoint


@dataclass
class NetworkInterface(BaseModel):
    NetworkInterfaceId: Optional[str]
    SubnetId: Optional[str]
    PrivateIpAddress: Optional[str]
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            SubnetId=json_data.get("SubnetId"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


