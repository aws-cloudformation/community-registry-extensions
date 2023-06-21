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
class AwsLakeformationPermissions(BaseModel):
    Resource: Optional["_Resource"]
    Permissions: Optional[Sequence[str]]
    Id: Optional[str]
    DataLakePrincipal: Optional["_DataLakePrincipal"]
    PermissionsWithGrantOption: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLakeformationPermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLakeformationPermissions"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Resource=Resource._deserialize(json_data.get("Resource")),
            Permissions=json_data.get("Permissions"),
            Id=json_data.get("Id"),
            DataLakePrincipal=DataLakePrincipal._deserialize(json_data.get("DataLakePrincipal")),
            PermissionsWithGrantOption=json_data.get("PermissionsWithGrantOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLakeformationPermissions = AwsLakeformationPermissions


@dataclass
class Resource(BaseModel):
    DatabaseResource: Optional["_DatabaseResource"]
    DataLocationResource: Optional["_DataLocationResource"]
    TableWithColumnsResource: Optional["_TableWithColumnsResource"]
    TableResource: Optional["_TableResource"]

    @classmethod
    def _deserialize(
        cls: Type["_Resource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resource"]:
        if not json_data:
            return None
        return cls(
            DatabaseResource=DatabaseResource._deserialize(json_data.get("DatabaseResource")),
            DataLocationResource=DataLocationResource._deserialize(json_data.get("DataLocationResource")),
            TableWithColumnsResource=TableWithColumnsResource._deserialize(json_data.get("TableWithColumnsResource")),
            TableResource=TableResource._deserialize(json_data.get("TableResource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resource = Resource


@dataclass
class DatabaseResource(BaseModel):
    CatalogId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseResource = DatabaseResource


@dataclass
class DataLocationResource(BaseModel):
    S3Resource: Optional[str]
    CatalogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataLocationResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLocationResource"]:
        if not json_data:
            return None
        return cls(
            S3Resource=json_data.get("S3Resource"),
            CatalogId=json_data.get("CatalogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLocationResource = DataLocationResource


@dataclass
class TableWithColumnsResource(BaseModel):
    DatabaseName: Optional[str]
    ColumnNames: Optional[Sequence[str]]
    CatalogId: Optional[str]
    Name: Optional[str]
    ColumnWildcard: Optional["_ColumnWildcard"]

    @classmethod
    def _deserialize(
        cls: Type["_TableWithColumnsResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableWithColumnsResource"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            ColumnNames=json_data.get("ColumnNames"),
            CatalogId=json_data.get("CatalogId"),
            Name=json_data.get("Name"),
            ColumnWildcard=ColumnWildcard._deserialize(json_data.get("ColumnWildcard")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableWithColumnsResource = TableWithColumnsResource


@dataclass
class ColumnWildcard(BaseModel):
    ExcludedColumnNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnWildcard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnWildcard"]:
        if not json_data:
            return None
        return cls(
            ExcludedColumnNames=json_data.get("ExcludedColumnNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnWildcard = ColumnWildcard


@dataclass
class TableResource(BaseModel):
    DatabaseName: Optional[str]
    CatalogId: Optional[str]
    TableWildcard: Optional[MutableMapping[str, Any]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableResource"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            CatalogId=json_data.get("CatalogId"),
            TableWildcard=json_data.get("TableWildcard"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableResource = TableResource


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


