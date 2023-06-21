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
class AwsMediaconnectBridge(BaseModel):
    Name: Optional[str]
    BridgeArn: Optional[str]
    PlacementArn: Optional[str]
    BridgeState: Optional[str]
    SourceFailoverConfig: Optional["_FailoverConfig"]
    Outputs: Optional[Sequence["_BridgeOutput"]]
    Sources: Optional[Sequence["_BridgeSource"]]
    IngressGatewayBridge: Optional["_IngressGatewayBridge"]
    EgressGatewayBridge: Optional["_EgressGatewayBridge"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectBridge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectBridge"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            BridgeArn=json_data.get("BridgeArn"),
            PlacementArn=json_data.get("PlacementArn"),
            BridgeState=json_data.get("BridgeState"),
            SourceFailoverConfig=FailoverConfig._deserialize(json_data.get("SourceFailoverConfig")),
            Outputs=deserialize_list(json_data.get("Outputs"), BridgeOutput),
            Sources=deserialize_list(json_data.get("Sources"), BridgeSource),
            IngressGatewayBridge=IngressGatewayBridge._deserialize(json_data.get("IngressGatewayBridge")),
            EgressGatewayBridge=EgressGatewayBridge._deserialize(json_data.get("EgressGatewayBridge")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectBridge = AwsMediaconnectBridge


@dataclass
class FailoverConfig(BaseModel):
    State: Optional[str]
    FailoverMode: Optional[str]
    SourcePriority: Optional["_SourcePriority"]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverConfig"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
            FailoverMode=json_data.get("FailoverMode"),
            SourcePriority=SourcePriority._deserialize(json_data.get("SourcePriority")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverConfig = FailoverConfig


@dataclass
class SourcePriority(BaseModel):
    PrimarySource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePriority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePriority"]:
        if not json_data:
            return None
        return cls(
            PrimarySource=json_data.get("PrimarySource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePriority = SourcePriority


@dataclass
class BridgeOutput(BaseModel):
    NetworkOutput: Optional["_BridgeNetworkOutput"]

    @classmethod
    def _deserialize(
        cls: Type["_BridgeOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BridgeOutput"]:
        if not json_data:
            return None
        return cls(
            NetworkOutput=BridgeNetworkOutput._deserialize(json_data.get("NetworkOutput")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeOutput = BridgeOutput


@dataclass
class BridgeNetworkOutput(BaseModel):
    Name: Optional[str]
    Protocol: Optional[str]
    IpAddress: Optional[str]
    Port: Optional[int]
    NetworkName: Optional[str]
    Ttl: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BridgeNetworkOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BridgeNetworkOutput"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            IpAddress=json_data.get("IpAddress"),
            Port=json_data.get("Port"),
            NetworkName=json_data.get("NetworkName"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeNetworkOutput = BridgeNetworkOutput


@dataclass
class BridgeSource(BaseModel):
    FlowSource: Optional["_BridgeFlowSource"]
    NetworkSource: Optional["_BridgeNetworkSource"]

    @classmethod
    def _deserialize(
        cls: Type["_BridgeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BridgeSource"]:
        if not json_data:
            return None
        return cls(
            FlowSource=BridgeFlowSource._deserialize(json_data.get("FlowSource")),
            NetworkSource=BridgeNetworkSource._deserialize(json_data.get("NetworkSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeSource = BridgeSource


@dataclass
class BridgeFlowSource(BaseModel):
    Name: Optional[str]
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
            Name=json_data.get("Name"),
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
    Name: Optional[str]
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
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            MulticastIp=json_data.get("MulticastIp"),
            Port=json_data.get("Port"),
            NetworkName=json_data.get("NetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeNetworkSource = BridgeNetworkSource


@dataclass
class IngressGatewayBridge(BaseModel):
    MaxBitrate: Optional[int]
    MaxOutputs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IngressGatewayBridge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressGatewayBridge"]:
        if not json_data:
            return None
        return cls(
            MaxBitrate=json_data.get("MaxBitrate"),
            MaxOutputs=json_data.get("MaxOutputs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressGatewayBridge = IngressGatewayBridge


@dataclass
class EgressGatewayBridge(BaseModel):
    MaxBitrate: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EgressGatewayBridge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressGatewayBridge"]:
        if not json_data:
            return None
        return cls(
            MaxBitrate=json_data.get("MaxBitrate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressGatewayBridge = EgressGatewayBridge


