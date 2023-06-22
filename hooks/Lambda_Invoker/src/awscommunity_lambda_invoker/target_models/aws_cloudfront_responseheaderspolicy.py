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
class AwsCloudfrontResponseheaderspolicy(BaseModel):
    Id: Optional[str]
    LastModifiedTime: Optional[str]
    ResponseHeadersPolicyConfig: Optional["_ResponseHeadersPolicyConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontResponseheaderspolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontResponseheaderspolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            ResponseHeadersPolicyConfig=ResponseHeadersPolicyConfig._deserialize(json_data.get("ResponseHeadersPolicyConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontResponseheaderspolicy = AwsCloudfrontResponseheaderspolicy


@dataclass
class ResponseHeadersPolicyConfig(BaseModel):
    Comment: Optional[str]
    CorsConfig: Optional["_CorsConfig"]
    CustomHeadersConfig: Optional["_CustomHeadersConfig"]
    Name: Optional[str]
    RemoveHeadersConfig: Optional["_RemoveHeadersConfig"]
    SecurityHeadersConfig: Optional["_SecurityHeadersConfig"]
    ServerTimingHeadersConfig: Optional["_ServerTimingHeadersConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeadersPolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeadersPolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            CorsConfig=CorsConfig._deserialize(json_data.get("CorsConfig")),
            CustomHeadersConfig=CustomHeadersConfig._deserialize(json_data.get("CustomHeadersConfig")),
            Name=json_data.get("Name"),
            RemoveHeadersConfig=RemoveHeadersConfig._deserialize(json_data.get("RemoveHeadersConfig")),
            SecurityHeadersConfig=SecurityHeadersConfig._deserialize(json_data.get("SecurityHeadersConfig")),
            ServerTimingHeadersConfig=ServerTimingHeadersConfig._deserialize(json_data.get("ServerTimingHeadersConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeadersPolicyConfig = ResponseHeadersPolicyConfig


@dataclass
class CorsConfig(BaseModel):
    AccessControlAllowCredentials: Optional[bool]
    AccessControlAllowHeaders: Optional["_AccessControlAllowHeaders"]
    AccessControlAllowMethods: Optional["_AccessControlAllowMethods"]
    AccessControlAllowOrigins: Optional["_AccessControlAllowOrigins"]
    AccessControlExposeHeaders: Optional["_AccessControlExposeHeaders"]
    AccessControlMaxAgeSec: Optional[int]
    OriginOverride: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CorsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsConfig"]:
        if not json_data:
            return None
        return cls(
            AccessControlAllowCredentials=json_data.get("AccessControlAllowCredentials"),
            AccessControlAllowHeaders=AccessControlAllowHeaders._deserialize(json_data.get("AccessControlAllowHeaders")),
            AccessControlAllowMethods=AccessControlAllowMethods._deserialize(json_data.get("AccessControlAllowMethods")),
            AccessControlAllowOrigins=AccessControlAllowOrigins._deserialize(json_data.get("AccessControlAllowOrigins")),
            AccessControlExposeHeaders=AccessControlExposeHeaders._deserialize(json_data.get("AccessControlExposeHeaders")),
            AccessControlMaxAgeSec=json_data.get("AccessControlMaxAgeSec"),
            OriginOverride=json_data.get("OriginOverride"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsConfig = CorsConfig


@dataclass
class AccessControlAllowHeaders(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlAllowHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlAllowHeaders"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlAllowHeaders = AccessControlAllowHeaders


@dataclass
class AccessControlAllowMethods(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlAllowMethods"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlAllowMethods"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlAllowMethods = AccessControlAllowMethods


@dataclass
class AccessControlAllowOrigins(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlAllowOrigins"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlAllowOrigins"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlAllowOrigins = AccessControlAllowOrigins


@dataclass
class AccessControlExposeHeaders(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlExposeHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlExposeHeaders"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlExposeHeaders = AccessControlExposeHeaders


@dataclass
class CustomHeadersConfig(BaseModel):
    Items: Optional[Sequence["_CustomHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeadersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeadersConfig"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), CustomHeader),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeadersConfig = CustomHeadersConfig


@dataclass
class CustomHeader(BaseModel):
    Header: Optional[str]
    Override: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeader"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Override=json_data.get("Override"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeader = CustomHeader


@dataclass
class RemoveHeadersConfig(BaseModel):
    Items: Optional[AbstractSet["_RemoveHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoveHeadersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoveHeadersConfig"]:
        if not json_data:
            return None
        return cls(
            Items=set_or_none(json_data.get("Items")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoveHeadersConfig = RemoveHeadersConfig


@dataclass
class RemoveHeader(BaseModel):
    Header: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoveHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoveHeader"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoveHeader = RemoveHeader


@dataclass
class SecurityHeadersConfig(BaseModel):
    ContentSecurityPolicy: Optional["_ContentSecurityPolicy"]
    ContentTypeOptions: Optional["_ContentTypeOptions"]
    FrameOptions: Optional["_FrameOptions"]
    ReferrerPolicy: Optional["_ReferrerPolicy"]
    StrictTransportSecurity: Optional["_StrictTransportSecurity"]
    XSSProtection: Optional["_XSSProtection"]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityHeadersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityHeadersConfig"]:
        if not json_data:
            return None
        return cls(
            ContentSecurityPolicy=ContentSecurityPolicy._deserialize(json_data.get("ContentSecurityPolicy")),
            ContentTypeOptions=ContentTypeOptions._deserialize(json_data.get("ContentTypeOptions")),
            FrameOptions=FrameOptions._deserialize(json_data.get("FrameOptions")),
            ReferrerPolicy=ReferrerPolicy._deserialize(json_data.get("ReferrerPolicy")),
            StrictTransportSecurity=StrictTransportSecurity._deserialize(json_data.get("StrictTransportSecurity")),
            XSSProtection=XSSProtection._deserialize(json_data.get("XSSProtection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityHeadersConfig = SecurityHeadersConfig


@dataclass
class ContentSecurityPolicy(BaseModel):
    ContentSecurityPolicy: Optional[str]
    Override: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContentSecurityPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentSecurityPolicy"]:
        if not json_data:
            return None
        return cls(
            ContentSecurityPolicy=json_data.get("ContentSecurityPolicy"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentSecurityPolicy = ContentSecurityPolicy


@dataclass
class ContentTypeOptions(BaseModel):
    Override: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContentTypeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentTypeOptions"]:
        if not json_data:
            return None
        return cls(
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentTypeOptions = ContentTypeOptions


@dataclass
class FrameOptions(BaseModel):
    FrameOption: Optional[str]
    Override: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FrameOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameOptions"]:
        if not json_data:
            return None
        return cls(
            FrameOption=json_data.get("FrameOption"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameOptions = FrameOptions


@dataclass
class ReferrerPolicy(BaseModel):
    Override: Optional[bool]
    ReferrerPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferrerPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferrerPolicy"]:
        if not json_data:
            return None
        return cls(
            Override=json_data.get("Override"),
            ReferrerPolicy=json_data.get("ReferrerPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferrerPolicy = ReferrerPolicy


@dataclass
class StrictTransportSecurity(BaseModel):
    AccessControlMaxAgeSec: Optional[int]
    IncludeSubdomains: Optional[bool]
    Override: Optional[bool]
    Preload: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StrictTransportSecurity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrictTransportSecurity"]:
        if not json_data:
            return None
        return cls(
            AccessControlMaxAgeSec=json_data.get("AccessControlMaxAgeSec"),
            IncludeSubdomains=json_data.get("IncludeSubdomains"),
            Override=json_data.get("Override"),
            Preload=json_data.get("Preload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrictTransportSecurity = StrictTransportSecurity


@dataclass
class XSSProtection(BaseModel):
    ModeBlock: Optional[bool]
    Override: Optional[bool]
    Protection: Optional[bool]
    ReportUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XSSProtection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XSSProtection"]:
        if not json_data:
            return None
        return cls(
            ModeBlock=json_data.get("ModeBlock"),
            Override=json_data.get("Override"),
            Protection=json_data.get("Protection"),
            ReportUri=json_data.get("ReportUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XSSProtection = XSSProtection


@dataclass
class ServerTimingHeadersConfig(BaseModel):
    Enabled: Optional[bool]
    SamplingRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServerTimingHeadersConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerTimingHeadersConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            SamplingRate=json_data.get("SamplingRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerTimingHeadersConfig = ServerTimingHeadersConfig


