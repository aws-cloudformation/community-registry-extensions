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
class AwsCognitoUserpooldomain(BaseModel):
    CloudFrontDistribution: Optional[str]
    UserPoolId: Optional[str]
    Id: Optional[str]
    Domain: Optional[str]
    CustomDomainConfig: Optional["_CustomDomainConfigType"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpooldomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpooldomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CloudFrontDistribution=json_data.get("CloudFrontDistribution"),
            UserPoolId=json_data.get("UserPoolId"),
            Id=json_data.get("Id"),
            Domain=json_data.get("Domain"),
            CustomDomainConfig=CustomDomainConfigType._deserialize(json_data.get("CustomDomainConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpooldomain = AwsCognitoUserpooldomain


@dataclass
class CustomDomainConfigType(BaseModel):
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDomainConfigType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDomainConfigType"]:
        if not json_data:
            return None
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDomainConfigType = CustomDomainConfigType


