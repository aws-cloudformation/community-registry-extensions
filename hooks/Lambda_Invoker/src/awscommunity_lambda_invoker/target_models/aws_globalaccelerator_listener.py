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
class AwsGlobalacceleratorListener(BaseModel):
    ListenerArn: Optional[str]
    AcceleratorArn: Optional[str]
    PortRanges: Optional[Sequence["_PortRange"]]
    Protocol: Optional[str]
    ClientAffinity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlobalacceleratorListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlobalacceleratorListener"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ListenerArn=json_data.get("ListenerArn"),
            AcceleratorArn=json_data.get("AcceleratorArn"),
            PortRanges=deserialize_list(json_data.get("PortRanges"), PortRange),
            Protocol=json_data.get("Protocol"),
            ClientAffinity=json_data.get("ClientAffinity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlobalacceleratorListener = AwsGlobalacceleratorListener


@dataclass
class PortRange(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRange = PortRange


