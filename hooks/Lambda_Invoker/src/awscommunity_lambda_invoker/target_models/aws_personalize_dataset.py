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
class AwsPersonalizeDataset(BaseModel):
    Name: Optional[str]
    DatasetArn: Optional[str]
    DatasetType: Optional[str]
    DatasetGroupArn: Optional[str]
    SchemaArn: Optional[str]
    DatasetImportJob: Optional["_DatasetImportJob"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPersonalizeDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPersonalizeDataset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            DatasetArn=json_data.get("DatasetArn"),
            DatasetType=json_data.get("DatasetType"),
            DatasetGroupArn=json_data.get("DatasetGroupArn"),
            SchemaArn=json_data.get("SchemaArn"),
            DatasetImportJob=DatasetImportJob._deserialize(json_data.get("DatasetImportJob")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPersonalizeDataset = AwsPersonalizeDataset


@dataclass
class DatasetImportJob(BaseModel):
    JobName: Optional[str]
    DatasetImportJobArn: Optional[str]
    DatasetArn: Optional[str]
    DataSource: Optional["_DataSource"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetImportJob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetImportJob"]:
        if not json_data:
            return None
        return cls(
            JobName=json_data.get("JobName"),
            DatasetImportJobArn=json_data.get("DatasetImportJobArn"),
            DatasetArn=json_data.get("DatasetArn"),
            DataSource=DataSource._deserialize(json_data.get("DataSource")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetImportJob = DatasetImportJob


@dataclass
class DataSource(BaseModel):
    DataLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSource"]:
        if not json_data:
            return None
        return cls(
            DataLocation=json_data.get("DataLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSource = DataSource


