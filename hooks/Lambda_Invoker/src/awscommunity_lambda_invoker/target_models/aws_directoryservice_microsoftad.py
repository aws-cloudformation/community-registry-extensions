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
class AwsDirectoryserviceMicrosoftad(BaseModel):
    Id: Optional[str]
    Alias: Optional[str]
    DnsIpAddresses: Optional[Sequence[str]]
    CreateAlias: Optional[bool]
    Edition: Optional[str]
    EnableSso: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    ShortName: Optional[str]
    VpcSettings: Optional["_VpcSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDirectoryserviceMicrosoftad"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDirectoryserviceMicrosoftad"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Alias=json_data.get("Alias"),
            DnsIpAddresses=json_data.get("DnsIpAddresses"),
            CreateAlias=json_data.get("CreateAlias"),
            Edition=json_data.get("Edition"),
            EnableSso=json_data.get("EnableSso"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ShortName=json_data.get("ShortName"),
            VpcSettings=VpcSettings._deserialize(json_data.get("VpcSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDirectoryserviceMicrosoftad = AwsDirectoryserviceMicrosoftad


@dataclass
class VpcSettings(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSettings"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSettings = VpcSettings


