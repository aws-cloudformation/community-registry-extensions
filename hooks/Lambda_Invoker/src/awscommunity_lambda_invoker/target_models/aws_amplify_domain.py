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
class AwsAmplifyDomain(BaseModel):
    AppId: Optional[str]
    Arn: Optional[str]
    AutoSubDomainCreationPatterns: Optional[Sequence[str]]
    AutoSubDomainIAMRole: Optional[str]
    CertificateRecord: Optional[str]
    DomainName: Optional[str]
    DomainStatus: Optional[str]
    EnableAutoSubDomain: Optional[bool]
    StatusReason: Optional[str]
    SubDomainSettings: Optional[Sequence["_SubDomainSetting"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppId=json_data.get("AppId"),
            Arn=json_data.get("Arn"),
            AutoSubDomainCreationPatterns=json_data.get("AutoSubDomainCreationPatterns"),
            AutoSubDomainIAMRole=json_data.get("AutoSubDomainIAMRole"),
            CertificateRecord=json_data.get("CertificateRecord"),
            DomainName=json_data.get("DomainName"),
            DomainStatus=json_data.get("DomainStatus"),
            EnableAutoSubDomain=json_data.get("EnableAutoSubDomain"),
            StatusReason=json_data.get("StatusReason"),
            SubDomainSettings=deserialize_list(json_data.get("SubDomainSettings"), SubDomainSetting),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyDomain = AwsAmplifyDomain


@dataclass
class SubDomainSetting(BaseModel):
    Prefix: Optional[str]
    BranchName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubDomainSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubDomainSetting"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            BranchName=json_data.get("BranchName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubDomainSetting = SubDomainSetting


