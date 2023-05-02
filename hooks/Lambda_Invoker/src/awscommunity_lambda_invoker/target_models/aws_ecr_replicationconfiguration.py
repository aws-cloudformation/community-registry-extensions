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
class AwsEcrReplicationconfiguration(BaseModel):
    ReplicationConfiguration: Optional["_ReplicationConfiguration"]
    RegistryId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcrReplicationconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcrReplicationconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicationConfiguration=ReplicationConfiguration._deserialize(json_data.get("ReplicationConfiguration")),
            RegistryId=json_data.get("RegistryId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcrReplicationconfiguration = AwsEcrReplicationconfiguration


@dataclass
class ReplicationConfiguration(BaseModel):
    Rules: Optional[Sequence["_ReplicationRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), ReplicationRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfiguration = ReplicationConfiguration


@dataclass
class ReplicationRule(BaseModel):
    RepositoryFilters: Optional[Sequence["_RepositoryFilter"]]
    Destinations: Optional[Sequence["_ReplicationDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRule"]:
        if not json_data:
            return None
        return cls(
            RepositoryFilters=deserialize_list(json_data.get("RepositoryFilters"), RepositoryFilter),
            Destinations=deserialize_list(json_data.get("Destinations"), ReplicationDestination),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRule = ReplicationRule


@dataclass
class RepositoryFilter(BaseModel):
    Filter: Optional[str]
    FilterType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryFilter"]:
        if not json_data:
            return None
        return cls(
            Filter=json_data.get("Filter"),
            FilterType=json_data.get("FilterType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryFilter = RepositoryFilter


@dataclass
class ReplicationDestination(BaseModel):
    Region: Optional[str]
    RegistryId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationDestination"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            RegistryId=json_data.get("RegistryId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationDestination = ReplicationDestination


