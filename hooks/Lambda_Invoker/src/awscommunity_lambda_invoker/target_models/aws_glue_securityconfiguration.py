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
class AwsGlueSecurityconfiguration(BaseModel):
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    Name: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueSecurityconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueSecurityconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            Name=json_data.get("Name"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueSecurityconfiguration = AwsGlueSecurityconfiguration


@dataclass
class EncryptionConfiguration(BaseModel):
    S3Encryptions: Optional[MutableMapping[str, Any]]
    JobBookmarksEncryption: Optional["_JobBookmarksEncryption"]
    CloudWatchEncryption: Optional["_CloudWatchEncryption"]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3Encryptions=json_data.get("S3Encryptions"),
            JobBookmarksEncryption=JobBookmarksEncryption._deserialize(json_data.get("JobBookmarksEncryption")),
            CloudWatchEncryption=CloudWatchEncryption._deserialize(json_data.get("CloudWatchEncryption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class JobBookmarksEncryption(BaseModel):
    KmsKeyArn: Optional[str]
    JobBookmarksEncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobBookmarksEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobBookmarksEncryption"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            JobBookmarksEncryptionMode=json_data.get("JobBookmarksEncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobBookmarksEncryption = JobBookmarksEncryption


@dataclass
class CloudWatchEncryption(BaseModel):
    KmsKeyArn: Optional[str]
    CloudWatchEncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchEncryption"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            CloudWatchEncryptionMode=json_data.get("CloudWatchEncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchEncryption = CloudWatchEncryption


