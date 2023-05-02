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
class AwsOpsworksApp(BaseModel):
    Id: Optional[str]
    AppSource: Optional["_Source"]
    Attributes: Optional[MutableMapping[str, str]]
    DataSources: Optional[Sequence["_DataSource"]]
    Description: Optional[str]
    Domains: Optional[Sequence[str]]
    EnableSsl: Optional[bool]
    Environment: Optional[Sequence["_EnvironmentVariable"]]
    Name: Optional[str]
    Shortname: Optional[str]
    SslConfiguration: Optional["_SslConfiguration"]
    StackId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpsworksApp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpsworksApp"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            AppSource=Source._deserialize(json_data.get("AppSource")),
            Attributes=json_data.get("Attributes"),
            DataSources=deserialize_list(json_data.get("DataSources"), DataSource),
            Description=json_data.get("Description"),
            Domains=json_data.get("Domains"),
            EnableSsl=json_data.get("EnableSsl"),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentVariable),
            Name=json_data.get("Name"),
            Shortname=json_data.get("Shortname"),
            SslConfiguration=SslConfiguration._deserialize(json_data.get("SslConfiguration")),
            StackId=json_data.get("StackId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpsworksApp = AwsOpsworksApp


@dataclass
class Source(BaseModel):
    Password: Optional[str]
    Revision: Optional[str]
    SshKey: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Revision=json_data.get("Revision"),
            SshKey=json_data.get("SshKey"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class DataSource(BaseModel):
    Arn: Optional[str]
    DatabaseName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSource"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            DatabaseName=json_data.get("DatabaseName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSource = DataSource


@dataclass
class EnvironmentVariable(BaseModel):
    Key: Optional[str]
    Secure: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Secure=json_data.get("Secure"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariable = EnvironmentVariable


@dataclass
class SslConfiguration(BaseModel):
    Certificate: Optional[str]
    Chain: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfiguration"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Chain=json_data.get("Chain"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfiguration = SslConfiguration


