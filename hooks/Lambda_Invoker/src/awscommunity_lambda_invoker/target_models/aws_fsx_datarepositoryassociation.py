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
class AwsFsxDatarepositoryassociation(BaseModel):
    AssociationId: Optional[str]
    ResourceARN: Optional[str]
    FileSystemId: Optional[str]
    FileSystemPath: Optional[str]
    DataRepositoryPath: Optional[str]
    BatchImportMetaDataOnCreate: Optional[bool]
    ImportedFileChunkSize: Optional[int]
    S3: Optional["_S3"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFsxDatarepositoryassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFsxDatarepositoryassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssociationId=json_data.get("AssociationId"),
            ResourceARN=json_data.get("ResourceARN"),
            FileSystemId=json_data.get("FileSystemId"),
            FileSystemPath=json_data.get("FileSystemPath"),
            DataRepositoryPath=json_data.get("DataRepositoryPath"),
            BatchImportMetaDataOnCreate=json_data.get("BatchImportMetaDataOnCreate"),
            ImportedFileChunkSize=json_data.get("ImportedFileChunkSize"),
            S3=S3._deserialize(json_data.get("S3")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFsxDatarepositoryassociation = AwsFsxDatarepositoryassociation


@dataclass
class S3(BaseModel):
    AutoImportPolicy: Optional["_AutoImportPolicy"]
    AutoExportPolicy: Optional["_AutoExportPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            AutoImportPolicy=AutoImportPolicy._deserialize(json_data.get("AutoImportPolicy")),
            AutoExportPolicy=AutoExportPolicy._deserialize(json_data.get("AutoExportPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


@dataclass
class AutoImportPolicy(BaseModel):
    Events: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoImportPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoImportPolicy"]:
        if not json_data:
            return None
        return cls(
            Events=set_or_none(json_data.get("Events")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoImportPolicy = AutoImportPolicy


@dataclass
class AutoExportPolicy(BaseModel):
    Events: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoExportPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoExportPolicy"]:
        if not json_data:
            return None
        return cls(
            Events=set_or_none(json_data.get("Events")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoExportPolicy = AutoExportPolicy


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


