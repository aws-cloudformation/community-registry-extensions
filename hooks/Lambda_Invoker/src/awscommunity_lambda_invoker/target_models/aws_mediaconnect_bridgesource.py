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
class AwsMediaconnectBridgesource(BaseModel):
    Name: Optional[str]
    BridgeArn: Optional[str]
    FlowSource: Optional["_BridgeFlowSource"]
    NetworkSource: Optional["_BridgeNetworkSource"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectBridgesource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectBridgesource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            BridgeArn=json_data.get("BridgeArn"),
            FlowSource=BridgeFlowSource._deserialize(json_data.get("FlowSource")),
            NetworkSource=BridgeNetworkSource._deserialize(json_data.get("NetworkSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectBridgesource = AwsMediaconnectBridgesource


@dataclass
class BridgeFlowSource(BaseModel):
    FlowArn: Optional[str]
    FlowVpcInterfaceAttachment: Optional["_VpcInterfaceAttachment"]

    @classmethod
    def _deserialize(
        cls: Type["_BridgeFlowSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BridgeFlowSource"]:
        if not json_data:
            return None
        return cls(
            FlowArn=json_data.get("FlowArn"),
            FlowVpcInterfaceAttachment=VpcInterfaceAttachment._deserialize(json_data.get("FlowVpcInterfaceAttachment")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeFlowSource = BridgeFlowSource


@dataclass
class VpcInterfaceAttachment(BaseModel):
    VpcInterfaceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcInterfaceAttachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcInterfaceAttachment"]:
        if not json_data:
            return None
        return cls(
            VpcInterfaceName=json_data.get("VpcInterfaceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcInterfaceAttachment = VpcInterfaceAttachment


@dataclass
class BridgeNetworkSource(BaseModel):
    Protocol: Optional[str]
    MulticastIp: Optional[str]
    Port: Optional[int]
    NetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BridgeNetworkSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BridgeNetworkSource"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            MulticastIp=json_data.get("MulticastIp"),
            Port=json_data.get("Port"),
            NetworkName=json_data.get("NetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeNetworkSource = BridgeNetworkSource


