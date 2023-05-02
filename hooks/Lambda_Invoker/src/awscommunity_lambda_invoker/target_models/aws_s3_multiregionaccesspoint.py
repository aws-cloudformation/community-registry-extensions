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
class AwsS3Multiregionaccesspoint(BaseModel):
    Name: Optional[str]
    Alias: Optional[str]
    CreatedAt: Optional[str]
    PublicAccessBlockConfiguration: Optional["_PublicAccessBlockConfiguration"]
    Regions: Optional[Sequence["_Region"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Multiregionaccesspoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Multiregionaccesspoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Alias=json_data.get("Alias"),
            CreatedAt=json_data.get("CreatedAt"),
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration._deserialize(json_data.get("PublicAccessBlockConfiguration")),
            Regions=deserialize_list(json_data.get("Regions"), Region),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Multiregionaccesspoint = AwsS3Multiregionaccesspoint


@dataclass
class PublicAccessBlockConfiguration(BaseModel):
    BlockPublicAcls: Optional[bool]
    IgnorePublicAcls: Optional[bool]
    BlockPublicPolicy: Optional[bool]
    RestrictPublicBuckets: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessBlockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessBlockConfiguration"]:
        if not json_data:
            return None
        return cls(
            BlockPublicAcls=json_data.get("BlockPublicAcls"),
            IgnorePublicAcls=json_data.get("IgnorePublicAcls"),
            BlockPublicPolicy=json_data.get("BlockPublicPolicy"),
            RestrictPublicBuckets=json_data.get("RestrictPublicBuckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessBlockConfiguration = PublicAccessBlockConfiguration


@dataclass
class Region(BaseModel):
    Bucket: Optional[str]
    BucketAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Region"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Region"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            BucketAccountId=json_data.get("BucketAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Region = Region


