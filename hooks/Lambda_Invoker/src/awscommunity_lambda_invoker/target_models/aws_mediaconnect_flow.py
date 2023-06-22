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
class AwsMediaconnectFlow(BaseModel):
    FlowArn: Optional[str]
    Name: Optional[str]
    AvailabilityZone: Optional[str]
    FlowAvailabilityZone: Optional[str]
    Source: Optional["_Source"]
    SourceFailoverConfig: Optional["_FailoverConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectFlow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectFlow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FlowArn=json_data.get("FlowArn"),
            Name=json_data.get("Name"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            FlowAvailabilityZone=json_data.get("FlowAvailabilityZone"),
            Source=Source._deserialize(json_data.get("Source")),
            SourceFailoverConfig=FailoverConfig._deserialize(json_data.get("SourceFailoverConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectFlow = AwsMediaconnectFlow


@dataclass
class Source(BaseModel):
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
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
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
_Source = Source


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


@dataclass
class FailoverConfig(BaseModel):
    State: Optional[str]
    RecoveryWindow: Optional[int]
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
            RecoveryWindow=json_data.get("RecoveryWindow"),
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


