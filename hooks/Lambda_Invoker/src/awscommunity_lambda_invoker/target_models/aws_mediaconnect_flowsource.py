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
class AwsMediaconnectFlowsource(BaseModel):
    FlowArn: Optional[str]
    SourceArn: Optional[str]
    Decryption: Optional["_Encryption"]
    Description: Optional[str]
    EntitlementArn: Optional[str]
    GatewayBridgeSource: Optional["_GatewayBridgeSource"]
    IngestIp: Optional[str]
    IngestPort: Optional[int]
    MaxBitrate: Optional[int]
    MaxLatency: Optional[int]
    MinLatency: Optional[int]
    Name: Optional[str]
    Protocol: Optional[str]
    SenderIpAddress: Optional[str]
    SenderControlPort: Optional[int]
    StreamId: Optional[str]
    SourceIngestPort: Optional[str]
    SourceListenerAddress: Optional[str]
    SourceListenerPort: Optional[int]
    VpcInterfaceName: Optional[str]
    WhitelistCidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectFlowsource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectFlowsource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FlowArn=json_data.get("FlowArn"),
            SourceArn=json_data.get("SourceArn"),
            Decryption=Encryption._deserialize(json_data.get("Decryption")),
            Description=json_data.get("Description"),
            EntitlementArn=json_data.get("EntitlementArn"),
            GatewayBridgeSource=GatewayBridgeSource._deserialize(json_data.get("GatewayBridgeSource")),
            IngestIp=json_data.get("IngestIp"),
            IngestPort=json_data.get("IngestPort"),
            MaxBitrate=json_data.get("MaxBitrate"),
            MaxLatency=json_data.get("MaxLatency"),
            MinLatency=json_data.get("MinLatency"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            SenderIpAddress=json_data.get("SenderIpAddress"),
            SenderControlPort=json_data.get("SenderControlPort"),
            StreamId=json_data.get("StreamId"),
            SourceIngestPort=json_data.get("SourceIngestPort"),
            SourceListenerAddress=json_data.get("SourceListenerAddress"),
            SourceListenerPort=json_data.get("SourceListenerPort"),
            VpcInterfaceName=json_data.get("VpcInterfaceName"),
            WhitelistCidr=json_data.get("WhitelistCidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectFlowsource = AwsMediaconnectFlowsource


@dataclass
class Encryption(BaseModel):
    Algorithm: Optional[str]
    ConstantInitializationVector: Optional[str]
    DeviceId: Optional[str]
    KeyType: Optional[str]
    Region: Optional[str]
    ResourceId: Optional[str]
    RoleArn: Optional[str]
    SecretArn: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            ConstantInitializationVector=json_data.get("ConstantInitializationVector"),
            DeviceId=json_data.get("DeviceId"),
            KeyType=json_data.get("KeyType"),
            Region=json_data.get("Region"),
            ResourceId=json_data.get("ResourceId"),
            RoleArn=json_data.get("RoleArn"),
            SecretArn=json_data.get("SecretArn"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


@dataclass
class GatewayBridgeSource(BaseModel):
    BridgeArn: Optional[str]
    VpcInterfaceAttachment: Optional["_VpcInterfaceAttachment"]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayBridgeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayBridgeSource"]:
        if not json_data:
            return None
        return cls(
            BridgeArn=json_data.get("BridgeArn"),
            VpcInterfaceAttachment=VpcInterfaceAttachment._deserialize(json_data.get("VpcInterfaceAttachment")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayBridgeSource = GatewayBridgeSource


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


