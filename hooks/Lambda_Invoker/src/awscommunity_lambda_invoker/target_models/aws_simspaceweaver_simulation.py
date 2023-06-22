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
class AwsSimspaceweaverSimulation(BaseModel):
    Name: Optional[str]
    RoleArn: Optional[str]
    SchemaS3Location: Optional["_S3Location"]
    DescribePayload: Optional[str]
    MaximumDuration: Optional[str]
    SnapshotS3Location: Optional["_S3Location"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSimspaceweaverSimulation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSimspaceweaverSimulation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            SchemaS3Location=S3Location._deserialize(json_data.get("SchemaS3Location")),
            DescribePayload=json_data.get("DescribePayload"),
            MaximumDuration=json_data.get("MaximumDuration"),
            SnapshotS3Location=S3Location._deserialize(json_data.get("SnapshotS3Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSimspaceweaverSimulation = AwsSimspaceweaverSimulation


@dataclass
class S3Location(BaseModel):
    BucketName: Optional[str]
    ObjectKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ObjectKey=json_data.get("ObjectKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


