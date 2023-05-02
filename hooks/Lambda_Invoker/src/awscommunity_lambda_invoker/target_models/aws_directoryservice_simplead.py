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
class AwsDirectoryserviceSimplead(BaseModel):
    DirectoryId: Optional[str]
    Alias: Optional[str]
    DnsIpAddresses: Optional[Sequence[str]]
    CreateAlias: Optional[bool]
    Description: Optional[str]
    EnableSso: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    ShortName: Optional[str]
    Size: Optional[str]
    VpcSettings: Optional["_VpcSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDirectoryserviceSimplead"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDirectoryserviceSimplead"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DirectoryId=json_data.get("DirectoryId"),
            Alias=json_data.get("Alias"),
            DnsIpAddresses=json_data.get("DnsIpAddresses"),
            CreateAlias=json_data.get("CreateAlias"),
            Description=json_data.get("Description"),
            EnableSso=json_data.get("EnableSso"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ShortName=json_data.get("ShortName"),
            Size=json_data.get("Size"),
            VpcSettings=VpcSettings._deserialize(json_data.get("VpcSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDirectoryserviceSimplead = AwsDirectoryserviceSimplead


@dataclass
class VpcSettings(BaseModel):
    SubnetIds: Optional[AbstractSet[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSettings"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSettings = VpcSettings


