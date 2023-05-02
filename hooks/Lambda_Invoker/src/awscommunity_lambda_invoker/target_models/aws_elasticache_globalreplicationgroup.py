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
class AwsElasticacheGlobalreplicationgroup(BaseModel):
    GlobalReplicationGroupIdSuffix: Optional[str]
    AutomaticFailoverEnabled: Optional[bool]
    CacheNodeType: Optional[str]
    EngineVersion: Optional[str]
    CacheParameterGroupName: Optional[str]
    GlobalNodeGroupCount: Optional[int]
    GlobalReplicationGroupDescription: Optional[str]
    GlobalReplicationGroupId: Optional[str]
    Members: Optional[Sequence["_GlobalReplicationGroupMember"]]
    Status: Optional[str]
    RegionalConfigurations: Optional[Sequence["_RegionalConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticacheGlobalreplicationgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticacheGlobalreplicationgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GlobalReplicationGroupIdSuffix=json_data.get("GlobalReplicationGroupIdSuffix"),
            AutomaticFailoverEnabled=json_data.get("AutomaticFailoverEnabled"),
            CacheNodeType=json_data.get("CacheNodeType"),
            EngineVersion=json_data.get("EngineVersion"),
            CacheParameterGroupName=json_data.get("CacheParameterGroupName"),
            GlobalNodeGroupCount=json_data.get("GlobalNodeGroupCount"),
            GlobalReplicationGroupDescription=json_data.get("GlobalReplicationGroupDescription"),
            GlobalReplicationGroupId=json_data.get("GlobalReplicationGroupId"),
            Members=deserialize_list(json_data.get("Members"), GlobalReplicationGroupMember),
            Status=json_data.get("Status"),
            RegionalConfigurations=deserialize_list(json_data.get("RegionalConfigurations"), RegionalConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticacheGlobalreplicationgroup = AwsElasticacheGlobalreplicationgroup


@dataclass
class GlobalReplicationGroupMember(BaseModel):
    ReplicationGroupId: Optional[str]
    ReplicationGroupRegion: Optional[str]
    Role: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalReplicationGroupMember"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalReplicationGroupMember"]:
        if not json_data:
            return None
        return cls(
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            ReplicationGroupRegion=json_data.get("ReplicationGroupRegion"),
            Role=json_data.get("Role"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalReplicationGroupMember = GlobalReplicationGroupMember


@dataclass
class RegionalConfiguration(BaseModel):
    ReplicationGroupId: Optional[str]
    ReplicationGroupRegion: Optional[str]
    ReshardingConfigurations: Optional[Sequence["_ReshardingConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_RegionalConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionalConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            ReplicationGroupRegion=json_data.get("ReplicationGroupRegion"),
            ReshardingConfigurations=deserialize_list(json_data.get("ReshardingConfigurations"), ReshardingConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionalConfiguration = RegionalConfiguration


@dataclass
class ReshardingConfiguration(BaseModel):
    NodeGroupId: Optional[str]
    PreferredAvailabilityZones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ReshardingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReshardingConfiguration"]:
        if not json_data:
            return None
        return cls(
            NodeGroupId=json_data.get("NodeGroupId"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReshardingConfiguration = ReshardingConfiguration


