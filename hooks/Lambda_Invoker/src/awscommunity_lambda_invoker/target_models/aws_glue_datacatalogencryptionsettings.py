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
class AwsGlueDatacatalogencryptionsettings(BaseModel):
    Id: Optional[str]
    DataCatalogEncryptionSettings: Optional["_DataCatalogEncryptionSettings"]
    CatalogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueDatacatalogencryptionsettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueDatacatalogencryptionsettings"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            DataCatalogEncryptionSettings=DataCatalogEncryptionSettings._deserialize(json_data.get("DataCatalogEncryptionSettings")),
            CatalogId=json_data.get("CatalogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueDatacatalogencryptionsettings = AwsGlueDatacatalogencryptionsettings


@dataclass
class DataCatalogEncryptionSettings(BaseModel):
    ConnectionPasswordEncryption: Optional["_ConnectionPasswordEncryption"]
    EncryptionAtRest: Optional["_EncryptionAtRest"]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogEncryptionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogEncryptionSettings"]:
        if not json_data:
            return None
        return cls(
            ConnectionPasswordEncryption=ConnectionPasswordEncryption._deserialize(json_data.get("ConnectionPasswordEncryption")),
            EncryptionAtRest=EncryptionAtRest._deserialize(json_data.get("EncryptionAtRest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogEncryptionSettings = DataCatalogEncryptionSettings


@dataclass
class ConnectionPasswordEncryption(BaseModel):
    ReturnConnectionPasswordEncrypted: Optional[bool]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionPasswordEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionPasswordEncryption"]:
        if not json_data:
            return None
        return cls(
            ReturnConnectionPasswordEncrypted=json_data.get("ReturnConnectionPasswordEncrypted"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionPasswordEncryption = ConnectionPasswordEncryption


@dataclass
class EncryptionAtRest(BaseModel):
    CatalogEncryptionMode: Optional[str]
    SseAwsKmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionAtRest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionAtRest"]:
        if not json_data:
            return None
        return cls(
            CatalogEncryptionMode=json_data.get("CatalogEncryptionMode"),
            SseAwsKmsKeyId=json_data.get("SseAwsKmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionAtRest = EncryptionAtRest


