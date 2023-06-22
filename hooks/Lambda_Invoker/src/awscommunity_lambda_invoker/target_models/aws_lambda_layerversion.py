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
class AwsLambdaLayerversion(BaseModel):
    CompatibleRuntimes: Optional[Sequence[str]]
    LicenseInfo: Optional[str]
    Description: Optional[str]
    LayerName: Optional[str]
    Content: Optional["_Content"]
    LayerVersionArn: Optional[str]
    CompatibleArchitectures: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaLayerversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaLayerversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CompatibleRuntimes=json_data.get("CompatibleRuntimes"),
            LicenseInfo=json_data.get("LicenseInfo"),
            Description=json_data.get("Description"),
            LayerName=json_data.get("LayerName"),
            Content=Content._deserialize(json_data.get("Content")),
            LayerVersionArn=json_data.get("LayerVersionArn"),
            CompatibleArchitectures=json_data.get("CompatibleArchitectures"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaLayerversion = AwsLambdaLayerversion


@dataclass
class Content(BaseModel):
    S3ObjectVersion: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Content"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Content"]:
        if not json_data:
            return None
        return cls(
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Content = Content


