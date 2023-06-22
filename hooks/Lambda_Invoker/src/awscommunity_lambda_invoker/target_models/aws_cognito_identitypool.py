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
class AwsCognitoIdentitypool(BaseModel):
    PushSync: Optional["_PushSync"]
    CognitoIdentityProviders: Optional[Sequence["_CognitoIdentityProvider"]]
    DeveloperProviderName: Optional[str]
    CognitoStreams: Optional["_CognitoStreams"]
    SupportedLoginProviders: Optional[MutableMapping[str, Any]]
    Name: Optional[str]
    CognitoEvents: Optional[MutableMapping[str, Any]]
    Id: Optional[str]
    IdentityPoolName: Optional[str]
    AllowUnauthenticatedIdentities: Optional[bool]
    SamlProviderARNs: Optional[Sequence[str]]
    OpenIdConnectProviderARNs: Optional[Sequence[str]]
    AllowClassicFlow: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoIdentitypool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoIdentitypool"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PushSync=PushSync._deserialize(json_data.get("PushSync")),
            CognitoIdentityProviders=deserialize_list(json_data.get("CognitoIdentityProviders"), CognitoIdentityProvider),
            DeveloperProviderName=json_data.get("DeveloperProviderName"),
            CognitoStreams=CognitoStreams._deserialize(json_data.get("CognitoStreams")),
            SupportedLoginProviders=json_data.get("SupportedLoginProviders"),
            Name=json_data.get("Name"),
            CognitoEvents=json_data.get("CognitoEvents"),
            Id=json_data.get("Id"),
            IdentityPoolName=json_data.get("IdentityPoolName"),
            AllowUnauthenticatedIdentities=json_data.get("AllowUnauthenticatedIdentities"),
            SamlProviderARNs=json_data.get("SamlProviderARNs"),
            OpenIdConnectProviderARNs=json_data.get("OpenIdConnectProviderARNs"),
            AllowClassicFlow=json_data.get("AllowClassicFlow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoIdentitypool = AwsCognitoIdentitypool


@dataclass
class PushSync(BaseModel):
    ApplicationArns: Optional[Sequence[str]]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PushSync"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PushSync"]:
        if not json_data:
            return None
        return cls(
            ApplicationArns=json_data.get("ApplicationArns"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PushSync = PushSync


@dataclass
class CognitoIdentityProvider(BaseModel):
    ServerSideTokenCheck: Optional[bool]
    ProviderName: Optional[str]
    ClientId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoIdentityProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoIdentityProvider"]:
        if not json_data:
            return None
        return cls(
            ServerSideTokenCheck=json_data.get("ServerSideTokenCheck"),
            ProviderName=json_data.get("ProviderName"),
            ClientId=json_data.get("ClientId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoIdentityProvider = CognitoIdentityProvider


@dataclass
class CognitoStreams(BaseModel):
    StreamingStatus: Optional[str]
    StreamName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoStreams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoStreams"]:
        if not json_data:
            return None
        return cls(
            StreamingStatus=json_data.get("StreamingStatus"),
            StreamName=json_data.get("StreamName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoStreams = CognitoStreams


