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
class AwsMediaconnectBridgeoutput(BaseModel):
    BridgeArn: Optional[str]
    NetworkOutput: Optional["_BridgeNetworkOutput"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectBridgeoutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectBridgeoutput"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BridgeArn=json_data.get("BridgeArn"),
            NetworkOutput=BridgeNetworkOutput._deserialize(json_data.get("NetworkOutput")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectBridgeoutput = AwsMediaconnectBridgeoutput


@dataclass
class BridgeNetworkOutput(BaseModel):
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
            Protocol=json_data.get("Protocol"),
            IpAddress=json_data.get("IpAddress"),
            Port=json_data.get("Port"),
            NetworkName=json_data.get("NetworkName"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BridgeNetworkOutput = BridgeNetworkOutput


