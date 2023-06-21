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
class AwsGlueConnection(BaseModel):
    ConnectionInput: Optional["_ConnectionInput"]
    CatalogId: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueConnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueConnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectionInput=ConnectionInput._deserialize(json_data.get("ConnectionInput")),
            CatalogId=json_data.get("CatalogId"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueConnection = AwsGlueConnection


@dataclass
class ConnectionInput(BaseModel):
    Description: Optional[str]
    ConnectionType: Optional[str]
    MatchCriteria: Optional[Sequence[str]]
    PhysicalConnectionRequirements: Optional["_PhysicalConnectionRequirements"]
    ConnectionProperties: Optional[MutableMapping[str, Any]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionInput"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            ConnectionType=json_data.get("ConnectionType"),
            MatchCriteria=json_data.get("MatchCriteria"),
            PhysicalConnectionRequirements=PhysicalConnectionRequirements._deserialize(json_data.get("PhysicalConnectionRequirements")),
            ConnectionProperties=json_data.get("ConnectionProperties"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionInput = ConnectionInput


@dataclass
class PhysicalConnectionRequirements(BaseModel):
    AvailabilityZone: Optional[str]
    SecurityGroupIdList: Optional[Sequence[str]]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhysicalConnectionRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhysicalConnectionRequirements"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            SecurityGroupIdList=json_data.get("SecurityGroupIdList"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhysicalConnectionRequirements = PhysicalConnectionRequirements


