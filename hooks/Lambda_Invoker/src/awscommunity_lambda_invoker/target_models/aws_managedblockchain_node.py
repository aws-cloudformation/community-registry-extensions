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
class AwsManagedblockchainNode(BaseModel):
    NodeId: Optional[str]
    MemberId: Optional[str]
    Arn: Optional[str]
    NetworkId: Optional[str]
    NodeConfiguration: Optional["_NodeConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsManagedblockchainNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsManagedblockchainNode"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NodeId=json_data.get("NodeId"),
            MemberId=json_data.get("MemberId"),
            Arn=json_data.get("Arn"),
            NetworkId=json_data.get("NetworkId"),
            NodeConfiguration=NodeConfiguration._deserialize(json_data.get("NodeConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsManagedblockchainNode = AwsManagedblockchainNode


@dataclass
class NodeConfiguration(BaseModel):
    InstanceType: Optional[str]
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfiguration"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfiguration = NodeConfiguration


