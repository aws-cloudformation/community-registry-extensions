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
class AwsConfigDeliverychannel(BaseModel):
    S3KeyPrefix: Optional[str]
    ConfigSnapshotDeliveryProperties: Optional["_ConfigSnapshotDeliveryProperties"]
    S3BucketName: Optional[str]
    SnsTopicARN: Optional[str]
    Id: Optional[str]
    S3KmsKeyArn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigDeliverychannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigDeliverychannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            ConfigSnapshotDeliveryProperties=ConfigSnapshotDeliveryProperties._deserialize(json_data.get("ConfigSnapshotDeliveryProperties")),
            S3BucketName=json_data.get("S3BucketName"),
            SnsTopicARN=json_data.get("SnsTopicARN"),
            Id=json_data.get("Id"),
            S3KmsKeyArn=json_data.get("S3KmsKeyArn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigDeliverychannel = AwsConfigDeliverychannel


@dataclass
class ConfigSnapshotDeliveryProperties(BaseModel):
    DeliveryFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigSnapshotDeliveryProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigSnapshotDeliveryProperties"]:
        if not json_data:
            return None
        return cls(
            DeliveryFrequency=json_data.get("DeliveryFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigSnapshotDeliveryProperties = ConfigSnapshotDeliveryProperties


