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
class AwsGluePartition(BaseModel):
    DatabaseName: Optional[str]
    TableName: Optional[str]
    Id: Optional[str]
    CatalogId: Optional[str]
    PartitionInput: Optional["_PartitionInput"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGluePartition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGluePartition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            Id=json_data.get("Id"),
            CatalogId=json_data.get("CatalogId"),
            PartitionInput=PartitionInput._deserialize(json_data.get("PartitionInput")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGluePartition = AwsGluePartition


@dataclass
class PartitionInput(BaseModel):
    StorageDescriptor: Optional["_StorageDescriptor"]
    Values: Optional[Sequence[str]]
    Parameters: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionInput"]:
        if not json_data:
            return None
        return cls(
            StorageDescriptor=StorageDescriptor._deserialize(json_data.get("StorageDescriptor")),
            Values=json_data.get("Values"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionInput = PartitionInput


@dataclass
class StorageDescriptor(BaseModel):
    StoredAsSubDirectories: Optional[bool]
    Parameters: Optional[MutableMapping[str, Any]]
    BucketColumns: Optional[Sequence[str]]
    NumberOfBuckets: Optional[int]
    OutputFormat: Optional[str]
    Columns: Optional[Sequence["_Column"]]
    SerdeInfo: Optional["_SerdeInfo"]
    SortColumns: Optional[Sequence["_Order"]]
    Compressed: Optional[bool]
    SchemaReference: Optional["_SchemaReference"]
    SkewedInfo: Optional["_SkewedInfo"]
    InputFormat: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDescriptor"]:
        if not json_data:
            return None
        return cls(
            StoredAsSubDirectories=json_data.get("StoredAsSubDirectories"),
            Parameters=json_data.get("Parameters"),
            BucketColumns=json_data.get("BucketColumns"),
            NumberOfBuckets=json_data.get("NumberOfBuckets"),
            OutputFormat=json_data.get("OutputFormat"),
            Columns=deserialize_list(json_data.get("Columns"), Column),
            SerdeInfo=SerdeInfo._deserialize(json_data.get("SerdeInfo")),
            SortColumns=deserialize_list(json_data.get("SortColumns"), Order),
            Compressed=json_data.get("Compressed"),
            SchemaReference=SchemaReference._deserialize(json_data.get("SchemaReference")),
            SkewedInfo=SkewedInfo._deserialize(json_data.get("SkewedInfo")),
            InputFormat=json_data.get("InputFormat"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDescriptor = StorageDescriptor


@dataclass
class Column(BaseModel):
    Comment: Optional[str]
    Type: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Column"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Column"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Column = Column


@dataclass
class SerdeInfo(BaseModel):
    Parameters: Optional[MutableMapping[str, Any]]
    SerializationLibrary: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SerdeInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerdeInfo"]:
        if not json_data:
            return None
        return cls(
            Parameters=json_data.get("Parameters"),
            SerializationLibrary=json_data.get("SerializationLibrary"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerdeInfo = SerdeInfo


@dataclass
class Order(BaseModel):
    Column: Optional[str]
    SortOrder: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Order"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Order"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            SortOrder=json_data.get("SortOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Order = Order


@dataclass
class SchemaReference(BaseModel):
    SchemaId: Optional["_SchemaId"]
    SchemaVersionId: Optional[str]
    SchemaVersionNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaReference"]:
        if not json_data:
            return None
        return cls(
            SchemaId=SchemaId._deserialize(json_data.get("SchemaId")),
            SchemaVersionId=json_data.get("SchemaVersionId"),
            SchemaVersionNumber=json_data.get("SchemaVersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaReference = SchemaReference


@dataclass
class SchemaId(BaseModel):
    RegistryName: Optional[str]
    SchemaName: Optional[str]
    SchemaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaId"]:
        if not json_data:
            return None
        return cls(
            RegistryName=json_data.get("RegistryName"),
            SchemaName=json_data.get("SchemaName"),
            SchemaArn=json_data.get("SchemaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaId = SchemaId


@dataclass
class SkewedInfo(BaseModel):
    SkewedColumnValues: Optional[Sequence[str]]
    SkewedColumnValueLocationMaps: Optional[MutableMapping[str, Any]]
    SkewedColumnNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SkewedInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkewedInfo"]:
        if not json_data:
            return None
        return cls(
            SkewedColumnValues=json_data.get("SkewedColumnValues"),
            SkewedColumnValueLocationMaps=json_data.get("SkewedColumnValueLocationMaps"),
            SkewedColumnNames=json_data.get("SkewedColumnNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkewedInfo = SkewedInfo


