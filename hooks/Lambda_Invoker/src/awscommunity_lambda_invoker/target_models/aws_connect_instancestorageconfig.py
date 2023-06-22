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
class AwsConnectInstancestorageconfig(BaseModel):
    InstanceArn: Optional[str]
    ResourceType: Optional[str]
    AssociationId: Optional[str]
    StorageType: Optional[str]
    S3Config: Optional["_S3Config"]
    KinesisVideoStreamConfig: Optional["_KinesisVideoStreamConfig"]
    KinesisStreamConfig: Optional["_KinesisStreamConfig"]
    KinesisFirehoseConfig: Optional["_KinesisFirehoseConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectInstancestorageconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectInstancestorageconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            ResourceType=json_data.get("ResourceType"),
            AssociationId=json_data.get("AssociationId"),
            StorageType=json_data.get("StorageType"),
            S3Config=S3Config._deserialize(json_data.get("S3Config")),
            KinesisVideoStreamConfig=KinesisVideoStreamConfig._deserialize(json_data.get("KinesisVideoStreamConfig")),
            KinesisStreamConfig=KinesisStreamConfig._deserialize(json_data.get("KinesisStreamConfig")),
            KinesisFirehoseConfig=KinesisFirehoseConfig._deserialize(json_data.get("KinesisFirehoseConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectInstancestorageconfig = AwsConnectInstancestorageconfig


@dataclass
class S3Config(BaseModel):
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    EncryptionConfig: Optional["_EncryptionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_S3Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Config"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            EncryptionConfig=EncryptionConfig._deserialize(json_data.get("EncryptionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Config = S3Config


@dataclass
class EncryptionConfig(BaseModel):
    EncryptionType: Optional[str]
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfig = EncryptionConfig


@dataclass
class KinesisVideoStreamConfig(BaseModel):
    Prefix: Optional[str]
    RetentionPeriodHours: Optional[float]
    EncryptionConfig: Optional["_EncryptionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisVideoStreamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisVideoStreamConfig"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            RetentionPeriodHours=json_data.get("RetentionPeriodHours"),
            EncryptionConfig=EncryptionConfig._deserialize(json_data.get("EncryptionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisVideoStreamConfig = KinesisVideoStreamConfig


@dataclass
class KinesisStreamConfig(BaseModel):
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamConfig"]:
        if not json_data:
            return None
        return cls(
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamConfig = KinesisStreamConfig


@dataclass
class KinesisFirehoseConfig(BaseModel):
    FirehoseArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseConfig"]:
        if not json_data:
            return None
        return cls(
            FirehoseArn=json_data.get("FirehoseArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseConfig = KinesisFirehoseConfig


