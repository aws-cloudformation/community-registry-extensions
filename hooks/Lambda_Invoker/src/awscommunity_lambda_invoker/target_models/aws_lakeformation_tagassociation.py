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
class AwsLakeformationTagassociation(BaseModel):
    Resource: Optional["_Resource"]
    LFTags: Optional[Sequence["_LFTagPair"]]
    ResourceIdentifier: Optional[str]
    TagsIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLakeformationTagassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLakeformationTagassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Resource=Resource._deserialize(json_data.get("Resource")),
            LFTags=deserialize_list(json_data.get("LFTags"), LFTagPair),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            TagsIdentifier=json_data.get("TagsIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLakeformationTagassociation = AwsLakeformationTagassociation


@dataclass
class Resource(BaseModel):
    Catalog: Optional[MutableMapping[str, Any]]
    Database: Optional["_DatabaseResource"]
    Table: Optional["_TableResource"]
    TableWithColumns: Optional["_TableWithColumnsResource"]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TableWithColumnsResource = TableWithColumnsResource


@dataclass
class LFTagPair(BaseModel):
    CatalogId: Optional[str]
    TagKey: Optional[str]
    TagValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LFTagPair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LFTagPair"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            TagKey=json_data.get("TagKey"),
            TagValues=json_data.get("TagValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LFTagPair = LFTagPair


