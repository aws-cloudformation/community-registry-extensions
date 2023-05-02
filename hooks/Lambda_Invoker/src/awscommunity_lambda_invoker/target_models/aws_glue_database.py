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
class AwsGlueDatabase(BaseModel):
    CatalogId: Optional[str]
    DatabaseInput: Optional["_DatabaseInput"]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueDatabase"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueDatabase"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseInput=DatabaseInput._deserialize(json_data.get("DatabaseInput")),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueDatabase = AwsGlueDatabase


@dataclass
class DatabaseInput(BaseModel):
    LocationUri: Optional[str]
    CreateTableDefaultPermissions: Optional[Sequence["_PrincipalPrivileges"]]
    Description: Optional[str]
    Parameters: Optional[MutableMapping[str, Any]]
    TargetDatabase: Optional["_DatabaseIdentifier"]
    FederatedDatabase: Optional["_FederatedDatabase"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseInput"]:
        if not json_data:
            return None
        return cls(
            LocationUri=json_data.get("LocationUri"),
            CreateTableDefaultPermissions=deserialize_list(json_data.get("CreateTableDefaultPermissions"), PrincipalPrivileges),
            Description=json_data.get("Description"),
            Parameters=json_data.get("Parameters"),
            TargetDatabase=DatabaseIdentifier._deserialize(json_data.get("TargetDatabase")),
            FederatedDatabase=FederatedDatabase._deserialize(json_data.get("FederatedDatabase")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseInput = DatabaseInput


@dataclass
class PrincipalPrivileges(BaseModel):
    Permissions: Optional[Sequence[str]]
    Principal: Optional["_DataLakePrincipal"]

    @classmethod
    def _deserialize(
        cls: Type["_PrincipalPrivileges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrincipalPrivileges"]:
        if not json_data:
            return None
        return cls(
            Permissions=json_data.get("Permissions"),
            Principal=DataLakePrincipal._deserialize(json_data.get("Principal")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrincipalPrivileges = PrincipalPrivileges


@dataclass
class DataLakePrincipal(BaseModel):
    DataLakePrincipalIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataLakePrincipal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLakePrincipal"]:
        if not json_data:
            return None
        return cls(
            DataLakePrincipalIdentifier=json_data.get("DataLakePrincipalIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLakePrincipal = DataLakePrincipal


@dataclass
class DatabaseIdentifier(BaseModel):
    DatabaseName: Optional[str]
    CatalogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseIdentifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseIdentifier"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            CatalogId=json_data.get("CatalogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseIdentifier = DatabaseIdentifier


@dataclass
class FederatedDatabase(BaseModel):
    ConnectionName: Optional[str]
    Identifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FederatedDatabase"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FederatedDatabase"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Identifier=json_data.get("Identifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FederatedDatabase = FederatedDatabase


