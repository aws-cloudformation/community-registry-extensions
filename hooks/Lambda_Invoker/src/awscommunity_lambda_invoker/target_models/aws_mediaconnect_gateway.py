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
class AwsMediaconnectGateway(BaseModel):
    Name: Optional[str]
    GatewayArn: Optional[str]
    GatewayState: Optional[str]
    EgressCidrBlocks: Optional[Sequence[str]]
    Networks: Optional[Sequence["_GatewayNetwork"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectGateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectGateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            GatewayArn=json_data.get("GatewayArn"),
            GatewayState=json_data.get("GatewayState"),
            EgressCidrBlocks=json_data.get("EgressCidrBlocks"),
            Networks=deserialize_list(json_data.get("Networks"), GatewayNetwork),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectGateway = AwsMediaconnectGateway


@dataclass
class GatewayNetwork(BaseModel):
    Name: Optional[str]
    CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayNetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayNetwork"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            CidrBlock=json_data.get("CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayNetwork = GatewayNetwork


