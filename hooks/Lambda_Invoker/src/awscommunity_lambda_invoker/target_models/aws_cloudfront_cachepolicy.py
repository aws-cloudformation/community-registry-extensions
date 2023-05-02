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
class AwsCloudfrontCachepolicy(BaseModel):
    CachePolicyConfig: Optional["_CachePolicyConfig"]
    Id: Optional[str]
    LastModifiedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontCachepolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontCachepolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CachePolicyConfig=CachePolicyConfig._deserialize(json_data.get("CachePolicyConfig")),
            Id=json_data.get("Id"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontCachepolicy = AwsCloudfrontCachepolicy


@dataclass
class CachePolicyConfig(BaseModel):
    Comment: Optional[str]
    DefaultTTL: Optional[float]
    MaxTTL: Optional[float]
    MinTTL: Optional[float]
    Name: Optional[str]
    ParametersInCacheKeyAndForwardedToOrigin: Optional["_ParametersInCacheKeyAndForwardedToOrigin"]

    @classmethod
    def _deserialize(
        cls: Type["_CachePolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CachePolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            DefaultTTL=json_data.get("DefaultTTL"),
            MaxTTL=json_data.get("MaxTTL"),
            MinTTL=json_data.get("MinTTL"),
            Name=json_data.get("Name"),
            ParametersInCacheKeyAndForwardedToOrigin=ParametersInCacheKeyAndForwardedToOrigin._deserialize(json_data.get("ParametersInCacheKeyAndForwardedToOrigin")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CachePolicyConfig = CachePolicyConfig


@dataclass
class ParametersInCacheKeyAndForwardedToOrigin(BaseModel):
    CookiesConfig: Optional["_CookiesConfig"]
    EnableAcceptEncodingBrotli: Optional[bool]
    EnableAcceptEncodingGzip: Optional[bool]
    HeadersConfig: Optional["_HeadersConfig"]
    QueryStringsConfig: Optional["_QueryStringsConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersInCacheKeyAndForwardedToOrigin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersInCacheKeyAndForwardedToOrigin"]:
        if not json_data:
            return None
        return cls(
            CookiesConfig=CookiesConfig._deserialize(json_data.get("CookiesConfig")),
            EnableAcceptEncodingBrotli=json_data.get("EnableAcceptEncodingBrotli"),
            EnableAcceptEncodingGzip=json_data.get("EnableAcceptEncodingGzip"),
            HeadersConfig=HeadersConfig._deserialize(json_data.get("HeadersConfig")),
            QueryStringsConfig=QueryStringsConfig._deserialize(json_data.get("QueryStringsConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersInCacheKeyAndForwardedToOrigin = ParametersInCacheKeyAndForwardedToOrigin


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


