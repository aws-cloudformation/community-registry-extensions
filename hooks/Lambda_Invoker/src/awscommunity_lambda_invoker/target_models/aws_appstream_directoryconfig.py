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
class AwsAppstreamDirectoryconfig(BaseModel):
    OrganizationalUnitDistinguishedNames: Optional[Sequence[str]]
    ServiceAccountCredentials: Optional["_ServiceAccountCredentials"]
    DirectoryName: Optional[str]
    CertificateBasedAuthProperties: Optional["_CertificateBasedAuthProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamDirectoryconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamDirectoryconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OrganizationalUnitDistinguishedNames=json_data.get("OrganizationalUnitDistinguishedNames"),
            ServiceAccountCredentials=ServiceAccountCredentials._deserialize(json_data.get("ServiceAccountCredentials")),
            DirectoryName=json_data.get("DirectoryName"),
            CertificateBasedAuthProperties=CertificateBasedAuthProperties._deserialize(json_data.get("CertificateBasedAuthProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamDirectoryconfig = AwsAppstreamDirectoryconfig


@dataclass
class ServiceAccountCredentials(BaseModel):
    AccountName: Optional[str]
    AccountPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceAccountCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceAccountCredentials"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            AccountPassword=json_data.get("AccountPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceAccountCredentials = ServiceAccountCredentials


@dataclass
class CertificateBasedAuthProperties(BaseModel):
    Status: Optional[str]
    CertificateAuthorityArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateBasedAuthProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateBasedAuthProperties"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateBasedAuthProperties = CertificateBasedAuthProperties


