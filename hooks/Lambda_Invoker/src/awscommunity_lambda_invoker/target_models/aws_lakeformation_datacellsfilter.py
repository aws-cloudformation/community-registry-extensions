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
class AwsLakeformationDatacellsfilter(BaseModel):
    TableCatalogId: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    Name: Optional[str]
    RowFilter: Optional["_RowFilter"]
    ColumnNames: Optional[Sequence[str]]
    ColumnWildcard: Optional["_ColumnWildcard"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLakeformationDatacellsfilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLakeformationDatacellsfilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TableCatalogId=json_data.get("TableCatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            Name=json_data.get("Name"),
            RowFilter=RowFilter._deserialize(json_data.get("RowFilter")),
            ColumnNames=json_data.get("ColumnNames"),
            ColumnWildcard=ColumnWildcard._deserialize(json_data.get("ColumnWildcard")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLakeformationDatacellsfilter = AwsLakeformationDatacellsfilter


@dataclass
class RowFilter(BaseModel):
    FilterExpression: Optional[str]
    AllRowsWildcard: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_RowFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RowFilter"]:
        if not json_data:
            return None
        return cls(
            FilterExpression=json_data.get("FilterExpression"),
            AllRowsWildcard=json_data.get("AllRowsWildcard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RowFilter = RowFilter


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


