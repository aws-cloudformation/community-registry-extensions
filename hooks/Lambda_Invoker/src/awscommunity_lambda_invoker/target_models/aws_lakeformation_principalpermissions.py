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
class AwsLakeformationPrincipalpermissions(BaseModel):
    Catalog: Optional[str]
    Principal: Optional["_DataLakePrincipal"]
    Resource: Optional["_Resource"]
    Permissions: Optional[Sequence[str]]
    PermissionsWithGrantOption: Optional[Sequence[str]]
    PrincipalIdentifier: Optional[str]
    ResourceIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLakeformationPrincipalpermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLakeformationPrincipalpermissions"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Catalog=json_data.get("Catalog"),
            Principal=DataLakePrincipal._deserialize(json_data.get("Principal")),
            Resource=Resource._deserialize(json_data.get("Resource")),
            Permissions=json_data.get("Permissions"),
            PermissionsWithGrantOption=json_data.get("PermissionsWithGrantOption"),
            PrincipalIdentifier=json_data.get("PrincipalIdentifier"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLakeformationPrincipalpermissions = AwsLakeformationPrincipalpermissions


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
class Resource(BaseModel):
    Catalog: Optional[MutableMapping[str, Any]]
    Database: Optional["_DatabaseResource"]
    Table: Optional["_TableResource"]
    TableWithColumns: Optional["_TableWithColumnsResource"]
    DataLocation: Optional["_DataLocationResource"]
    DataCellsFilter: Optional["_DataCellsFilterResource"]
    LFTag: Optional["_LFTagKeyResource"]
    LFTagPolicy: Optional["_LFTagPolicyResource"]

    @classmethod
    def _deserialize(
        cls: Type["_Resource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resource"]:
        if not json_data:
            return None
        return cls(
            Catalog=json_data.get("Catalog"),
            Database=DatabaseResource._deserialize(json_data.get("Database")),
            Table=TableResource._deserialize(json_data.get("Table")),
            TableWithColumns=TableWithColumnsResource._deserialize(json_data.get("TableWithColumns")),
            DataLocation=DataLocationResource._deserialize(json_data.get("DataLocation")),
            DataCellsFilter=DataCellsFilterResource._deserialize(json_data.get("DataCellsFilter")),
            LFTag=LFTagKeyResource._deserialize(json_data.get("LFTag")),
            LFTagPolicy=LFTagPolicyResource._deserialize(json_data.get("LFTagPolicy")),
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
class TableResource(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Name: Optional[str]
    TableWildcard: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_TableResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Name=json_data.get("Name"),
            TableWildcard=json_data.get("TableWildcard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableResource = TableResource


@dataclass
class TableWithColumnsResource(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Name: Optional[str]
    ColumnNames: Optional[Sequence[str]]
    ColumnWildcard: Optional["_ColumnWildcard"]

    @classmethod
    def _deserialize(
        cls: Type["_TableWithColumnsResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableWithColumnsResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Name=json_data.get("Name"),
            ColumnNames=json_data.get("ColumnNames"),
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
class DataLocationResource(BaseModel):
    CatalogId: Optional[str]
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataLocationResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLocationResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLocationResource = DataLocationResource


@dataclass
class DataCellsFilterResource(BaseModel):
    TableCatalogId: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataCellsFilterResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCellsFilterResource"]:
        if not json_data:
            return None
        return cls(
            TableCatalogId=json_data.get("TableCatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCellsFilterResource = DataCellsFilterResource


@dataclass
class LFTagKeyResource(BaseModel):
    CatalogId: Optional[str]
    TagKey: Optional[str]
    TagValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LFTagKeyResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LFTagKeyResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            TagKey=json_data.get("TagKey"),
            TagValues=json_data.get("TagValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LFTagKeyResource = LFTagKeyResource


@dataclass
class LFTagPolicyResource(BaseModel):
    CatalogId: Optional[str]
    ResourceType: Optional[str]
    Expression: Optional[Sequence["_LFTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_LFTagPolicyResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LFTagPolicyResource"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            ResourceType=json_data.get("ResourceType"),
            Expression=deserialize_list(json_data.get("Expression"), LFTag),
        )


# work around possible type aliasing issues when variable has same name as a model
_LFTagPolicyResource = LFTagPolicyResource


@dataclass
class LFTag(BaseModel):
    TagKey: Optional[str]
    TagValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LFTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LFTag"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValues=json_data.get("TagValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LFTag = LFTag


