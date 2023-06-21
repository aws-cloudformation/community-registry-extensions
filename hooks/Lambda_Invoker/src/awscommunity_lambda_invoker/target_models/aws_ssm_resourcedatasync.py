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
class AwsSsmResourcedatasync(BaseModel):
    S3Destination: Optional["_S3Destination"]
    KMSKeyArn: Optional[str]
    SyncSource: Optional["_SyncSource"]
    BucketName: Optional[str]
    BucketRegion: Optional[str]
    SyncFormat: Optional[str]
    SyncName: Optional[str]
    SyncType: Optional[str]
    BucketPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmResourcedatasync"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmResourcedatasync"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            S3Destination=S3Destination._deserialize(json_data.get("S3Destination")),
            KMSKeyArn=json_data.get("KMSKeyArn"),
            SyncSource=SyncSource._deserialize(json_data.get("SyncSource")),
            BucketName=json_data.get("BucketName"),
            BucketRegion=json_data.get("BucketRegion"),
            SyncFormat=json_data.get("SyncFormat"),
            SyncName=json_data.get("SyncName"),
            SyncType=json_data.get("SyncType"),
            BucketPrefix=json_data.get("BucketPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmResourcedatasync = AwsSsmResourcedatasync


@dataclass
class S3Destination(BaseModel):
    KMSKeyArn: Optional[str]
    BucketPrefix: Optional[str]
    BucketName: Optional[str]
    BucketRegion: Optional[str]
    SyncFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Destination"]:
        if not json_data:
            return None
        return cls(
            KMSKeyArn=json_data.get("KMSKeyArn"),
            BucketPrefix=json_data.get("BucketPrefix"),
            BucketName=json_data.get("BucketName"),
            BucketRegion=json_data.get("BucketRegion"),
            SyncFormat=json_data.get("SyncFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Destination = S3Destination


@dataclass
class SyncSource(BaseModel):
    IncludeFutureRegions: Optional[bool]
    SourceRegions: Optional[Sequence[str]]
    SourceType: Optional[str]
    AwsOrganizationsSource: Optional["_AwsOrganizationsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_SyncSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyncSource"]:
        if not json_data:
            return None
        return cls(
            IncludeFutureRegions=json_data.get("IncludeFutureRegions"),
            SourceRegions=json_data.get("SourceRegions"),
            SourceType=json_data.get("SourceType"),
            AwsOrganizationsSource=AwsOrganizationsSource._deserialize(json_data.get("AwsOrganizationsSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyncSource = SyncSource


@dataclass
class AwsOrganizationsSource(BaseModel):
    OrganizationalUnits: Optional[Sequence[str]]
    OrganizationSourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOrganizationsSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOrganizationsSource"]:
        if not json_data:
            return None
        return cls(
            OrganizationalUnits=json_data.get("OrganizationalUnits"),
            OrganizationSourceType=json_data.get("OrganizationSourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOrganizationsSource = AwsOrganizationsSource


