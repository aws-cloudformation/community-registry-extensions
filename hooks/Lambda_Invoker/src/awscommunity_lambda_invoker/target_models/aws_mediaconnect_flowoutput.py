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
class AwsMediaconnectFlowoutput(BaseModel):
    FlowArn: Optional[str]
    OutputArn: Optional[str]
    CidrAllowList: Optional[Sequence[str]]
    Encryption: Optional["_Encryption"]
    Description: Optional[str]
    Destination: Optional[str]
    MaxLatency: Optional[int]
    MinLatency: Optional[int]
    Name: Optional[str]
    Port: Optional[int]
    Protocol: Optional[str]
    RemoteId: Optional[str]
    SmoothingLatency: Optional[int]
    StreamId: Optional[str]
    VpcInterfaceAttachment: Optional["_VpcInterfaceAttachment"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectFlowoutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectFlowoutput"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FlowArn=json_data.get("FlowArn"),
            OutputArn=json_data.get("OutputArn"),
            CidrAllowList=json_data.get("CidrAllowList"),
            Encryption=Encryption._deserialize(json_data.get("Encryption")),
            Description=json_data.get("Description"),
            Destination=json_data.get("Destination"),
            MaxLatency=json_data.get("MaxLatency"),
            MinLatency=json_data.get("MinLatency"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            RemoteId=json_data.get("RemoteId"),
            SmoothingLatency=json_data.get("SmoothingLatency"),
            StreamId=json_data.get("StreamId"),
            VpcInterfaceAttachment=VpcInterfaceAttachment._deserialize(json_data.get("VpcInterfaceAttachment")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectFlowoutput = AwsMediaconnectFlowoutput


@dataclass
class Encryption(BaseModel):
    Algorithm: Optional[str]
    KeyType: Optional[str]
    RoleArn: Optional[str]
    SecretArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            KeyType=json_data.get("KeyType"),
            RoleArn=json_data.get("RoleArn"),
            SecretArn=json_data.get("SecretArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


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


