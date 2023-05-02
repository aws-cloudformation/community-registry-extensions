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
class AwsKinesisanalyticsApplicationreferencedatasource(BaseModel):
    Id: Optional[str]
    ApplicationName: Optional[str]
    ReferenceDataSource: Optional["_ReferenceDataSource"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisanalyticsApplicationreferencedatasource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisanalyticsApplicationreferencedatasource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApplicationName=json_data.get("ApplicationName"),
            ReferenceDataSource=ReferenceDataSource._deserialize(json_data.get("ReferenceDataSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisanalyticsApplicationreferencedatasource = AwsKinesisanalyticsApplicationreferencedatasource


@dataclass
class ReferenceDataSource(BaseModel):
    ReferenceSchema: Optional["_ReferenceSchema"]
    TableName: Optional[str]
    S3ReferenceDataSource: Optional["_S3ReferenceDataSource"]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceDataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceDataSource"]:
        if not json_data:
            return None
        return cls(
            ReferenceSchema=ReferenceSchema._deserialize(json_data.get("ReferenceSchema")),
            TableName=json_data.get("TableName"),
            S3ReferenceDataSource=S3ReferenceDataSource._deserialize(json_data.get("S3ReferenceDataSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceDataSource = ReferenceDataSource


@dataclass
class ReferenceSchema(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumns: Optional[Sequence["_RecordColumn"]]
    RecordFormat: Optional["_RecordFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceSchema"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumns=deserialize_list(json_data.get("RecordColumns"), RecordColumn),
            RecordFormat=RecordFormat._deserialize(json_data.get("RecordFormat")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceSchema = ReferenceSchema


@dataclass
class RecordColumn(BaseModel):
    Mapping: Optional[str]
    SqlType: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumn"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            SqlType=json_data.get("SqlType"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumn = RecordColumn


@dataclass
class RecordFormat(BaseModel):
    MappingParameters: Optional["_MappingParameters"]
    RecordFormatType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormat"]:
        if not json_data:
            return None
        return cls(
            MappingParameters=MappingParameters._deserialize(json_data.get("MappingParameters")),
            RecordFormatType=json_data.get("RecordFormatType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormat = RecordFormat


@dataclass
class MappingParameters(BaseModel):
    JSONMappingParameters: Optional["_JSONMappingParameters"]
    CSVMappingParameters: Optional["_CSVMappingParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParameters"]:
        if not json_data:
            return None
        return cls(
            JSONMappingParameters=JSONMappingParameters._deserialize(json_data.get("JSONMappingParameters")),
            CSVMappingParameters=CSVMappingParameters._deserialize(json_data.get("CSVMappingParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParameters = MappingParameters


@dataclass
class JSONMappingParameters(BaseModel):
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JSONMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JSONMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JSONMappingParameters = JSONMappingParameters


@dataclass
class CSVMappingParameters(BaseModel):
    RecordRowDelimiter: Optional[str]
    RecordColumnDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CSVMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CSVMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CSVMappingParameters = CSVMappingParameters


@dataclass
class S3ReferenceDataSource(BaseModel):
    BucketARN: Optional[str]
    FileKey: Optional[str]
    ReferenceRoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ReferenceDataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ReferenceDataSource"]:
        if not json_data:
            return None
        return cls(
            BucketARN=json_data.get("BucketARN"),
            FileKey=json_data.get("FileKey"),
            ReferenceRoleARN=json_data.get("ReferenceRoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ReferenceDataSource = S3ReferenceDataSource


