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
class AwsSesReceiptfilter(BaseModel):
    Id: Optional[str]
    Filter: Optional["_Filter"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesReceiptfilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesReceiptfilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Filter=Filter._deserialize(json_data.get("Filter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesReceiptfilter = AwsSesReceiptfilter


@dataclass
class Filter(BaseModel):
    IpFilter: Optional["_IpFilter"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            IpFilter=IpFilter._deserialize(json_data.get("IpFilter")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class IpFilter(BaseModel):
    Policy: Optional[str]
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpFilter"]:
        if not json_data:
            return None
        return cls(
            Policy=json_data.get("Policy"),
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpFilter = IpFilter


