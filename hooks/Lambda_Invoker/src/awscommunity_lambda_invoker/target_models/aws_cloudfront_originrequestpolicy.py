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
class AwsCloudfrontOriginrequestpolicy(BaseModel):
    Id: Optional[str]
    LastModifiedTime: Optional[str]
    OriginRequestPolicyConfig: Optional["_OriginRequestPolicyConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontOriginrequestpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontOriginrequestpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            OriginRequestPolicyConfig=OriginRequestPolicyConfig._deserialize(json_data.get("OriginRequestPolicyConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontOriginrequestpolicy = AwsCloudfrontOriginrequestpolicy


@dataclass
class OriginRequestPolicyConfig(BaseModel):
    Comment: Optional[str]
    CookiesConfig: Optional["_CookiesConfig"]
    HeadersConfig: Optional["_HeadersConfig"]
    Name: Optional[str]
    QueryStringsConfig: Optional["_QueryStringsConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_OriginRequestPolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginRequestPolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            CookiesConfig=CookiesConfig._deserialize(json_data.get("CookiesConfig")),
            HeadersConfig=HeadersConfig._deserialize(json_data.get("HeadersConfig")),
            Name=json_data.get("Name"),
            QueryStringsConfig=QueryStringsConfig._deserialize(json_data.get("QueryStringsConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginRequestPolicyConfig = OriginRequestPolicyConfig


@dataclass
class CookiesConfig(BaseModel):
    CookieBehavior: Optional[str]
    Cookies: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookiesConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookiesConfig"]:
        if not json_data:
            return None
        return cls(
            CookieBehavior=json_data.get("CookieBehavior"),
            Cookies=json_data.get("Cookies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookiesConfig = CookiesConfig


@dataclass
class HeadersConfig(BaseModel):
    HeaderBehavior: Optional[str]
    Headers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersConfig"]:
        if not json_data:
            return None
        return cls(
            HeaderBehavior=json_data.get("HeaderBehavior"),
            Headers=json_data.get("Headers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersConfig = HeadersConfig


@dataclass
class QueryStringsConfig(BaseModel):
    QueryStringBehavior: Optional[str]
    QueryStrings: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringsConfig"]:
        if not json_data:
            return None
        return cls(
            QueryStringBehavior=json_data.get("QueryStringBehavior"),
            QueryStrings=json_data.get("QueryStrings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringsConfig = QueryStringsConfig


