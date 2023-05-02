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
class AwsElasticbeanstalkApplicationversion(BaseModel):
    Id: Optional[str]
    ApplicationName: Optional[str]
    Description: Optional[str]
    SourceBundle: Optional["_SourceBundle"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticbeanstalkApplicationversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticbeanstalkApplicationversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApplicationName=json_data.get("ApplicationName"),
            Description=json_data.get("Description"),
            SourceBundle=SourceBundle._deserialize(json_data.get("SourceBundle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticbeanstalkApplicationversion = AwsElasticbeanstalkApplicationversion


@dataclass
class SourceBundle(BaseModel):
    S3Bucket: Optional[str]
    S3Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceBundle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceBundle"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceBundle = SourceBundle


