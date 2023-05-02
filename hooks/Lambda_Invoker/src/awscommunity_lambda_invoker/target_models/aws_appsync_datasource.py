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
class AwsAppsyncDatasource(BaseModel):
    OpenSearchServiceConfig: Optional["_OpenSearchServiceConfig"]
    Description: Optional[str]
    ServiceRoleArn: Optional[str]
    Name: Optional[str]
    DataSourceArn: Optional[str]
    Type: Optional[str]
    EventBridgeConfig: Optional["_EventBridgeConfig"]
    HttpConfig: Optional["_HttpConfig"]
    RelationalDatabaseConfig: Optional["_RelationalDatabaseConfig"]
    LambdaConfig: Optional["_LambdaConfig"]
    Id: Optional[str]
    ApiId: Optional[str]
    DynamoDBConfig: Optional["_DynamoDBConfig"]
    ElasticsearchConfig: Optional["_ElasticsearchConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncDatasource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncDatasource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OpenSearchServiceConfig=OpenSearchServiceConfig._deserialize(json_data.get("OpenSearchServiceConfig")),
            Description=json_data.get("Description"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            Name=json_data.get("Name"),
            DataSourceArn=json_data.get("DataSourceArn"),
            Type=json_data.get("Type"),
            EventBridgeConfig=EventBridgeConfig._deserialize(json_data.get("EventBridgeConfig")),
            HttpConfig=HttpConfig._deserialize(json_data.get("HttpConfig")),
            RelationalDatabaseConfig=RelationalDatabaseConfig._deserialize(json_data.get("RelationalDatabaseConfig")),
            LambdaConfig=LambdaConfig._deserialize(json_data.get("LambdaConfig")),
            Id=json_data.get("Id"),
            ApiId=json_data.get("ApiId"),
            DynamoDBConfig=DynamoDBConfig._deserialize(json_data.get("DynamoDBConfig")),
            ElasticsearchConfig=ElasticsearchConfig._deserialize(json_data.get("ElasticsearchConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncDatasource = AwsAppsyncDatasource


@dataclass
class OpenSearchServiceConfig(BaseModel):
    AwsRegion: Optional[str]
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenSearchServiceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenSearchServiceConfig"]:
        if not json_data:
            return None
        return cls(
            AwsRegion=json_data.get("AwsRegion"),
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenSearchServiceConfig = OpenSearchServiceConfig


@dataclass
class EventBridgeConfig(BaseModel):
    EventBusArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeConfig"]:
        if not json_data:
            return None
        return cls(
            EventBusArn=json_data.get("EventBusArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeConfig = EventBridgeConfig


@dataclass
class HttpConfig(BaseModel):
    Endpoint: Optional[str]
    AuthorizationConfig: Optional["_AuthorizationConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfig"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            AuthorizationConfig=AuthorizationConfig._deserialize(json_data.get("AuthorizationConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfig = HttpConfig


@dataclass
class AuthorizationConfig(BaseModel):
    AuthorizationType: Optional[str]
    AwsIamConfig: Optional["_AwsIamConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationConfig"]:
        if not json_data:
            return None
        return cls(
            AuthorizationType=json_data.get("AuthorizationType"),
            AwsIamConfig=AwsIamConfig._deserialize(json_data.get("AwsIamConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationConfig = AuthorizationConfig


@dataclass
class AwsIamConfig(BaseModel):
    SigningRegion: Optional[str]
    SigningServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamConfig"]:
        if not json_data:
            return None
        return cls(
            SigningRegion=json_data.get("SigningRegion"),
            SigningServiceName=json_data.get("SigningServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamConfig = AwsIamConfig


@dataclass
class RelationalDatabaseConfig(BaseModel):
    RdsHttpEndpointConfig: Optional["_RdsHttpEndpointConfig"]
    RelationalDatabaseSourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationalDatabaseConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationalDatabaseConfig"]:
        if not json_data:
            return None
        return cls(
            RdsHttpEndpointConfig=RdsHttpEndpointConfig._deserialize(json_data.get("RdsHttpEndpointConfig")),
            RelationalDatabaseSourceType=json_data.get("RelationalDatabaseSourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationalDatabaseConfig = RelationalDatabaseConfig


@dataclass
class RdsHttpEndpointConfig(BaseModel):
    DatabaseName: Optional[str]
    AwsRegion: Optional[str]
    DbClusterIdentifier: Optional[str]
    AwsSecretStoreArn: Optional[str]
    Schema: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RdsHttpEndpointConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RdsHttpEndpointConfig"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            AwsRegion=json_data.get("AwsRegion"),
            DbClusterIdentifier=json_data.get("DbClusterIdentifier"),
            AwsSecretStoreArn=json_data.get("AwsSecretStoreArn"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RdsHttpEndpointConfig = RdsHttpEndpointConfig


@dataclass
class LambdaConfig(BaseModel):
    LambdaFunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfig"]:
        if not json_data:
            return None
        return cls(
            LambdaFunctionArn=json_data.get("LambdaFunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfig = LambdaConfig


@dataclass
class DynamoDBConfig(BaseModel):
    TableName: Optional[str]
    DeltaSyncConfig: Optional["_DeltaSyncConfig"]
    UseCallerCredentials: Optional[bool]
    AwsRegion: Optional[str]
    Versioned: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDBConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDBConfig"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            DeltaSyncConfig=DeltaSyncConfig._deserialize(json_data.get("DeltaSyncConfig")),
            UseCallerCredentials=json_data.get("UseCallerCredentials"),
            AwsRegion=json_data.get("AwsRegion"),
            Versioned=json_data.get("Versioned"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDBConfig = DynamoDBConfig


@dataclass
class DeltaSyncConfig(BaseModel):
    BaseTableTTL: Optional[str]
    DeltaSyncTableTTL: Optional[str]
    DeltaSyncTableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeltaSyncConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeltaSyncConfig"]:
        if not json_data:
            return None
        return cls(
            BaseTableTTL=json_data.get("BaseTableTTL"),
            DeltaSyncTableTTL=json_data.get("DeltaSyncTableTTL"),
            DeltaSyncTableName=json_data.get("DeltaSyncTableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeltaSyncConfig = DeltaSyncConfig


@dataclass
class ElasticsearchConfig(BaseModel):
    AwsRegion: Optional[str]
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfig"]:
        if not json_data:
            return None
        return cls(
            AwsRegion=json_data.get("AwsRegion"),
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfig = ElasticsearchConfig


