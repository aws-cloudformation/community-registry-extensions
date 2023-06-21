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
class AwsAppflowConnectorprofile(BaseModel):
    ConnectorProfileArn: Optional[str]
    ConnectorLabel: Optional[str]
    ConnectorProfileName: Optional[str]
    KMSArn: Optional[str]
    ConnectorType: Optional[str]
    ConnectionMode: Optional[str]
    ConnectorProfileConfig: Optional["_ConnectorProfileConfig"]
    CredentialsArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppflowConnectorprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppflowConnectorprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectorProfileArn=json_data.get("ConnectorProfileArn"),
            ConnectorLabel=json_data.get("ConnectorLabel"),
            ConnectorProfileName=json_data.get("ConnectorProfileName"),
            KMSArn=json_data.get("KMSArn"),
            ConnectorType=json_data.get("ConnectorType"),
            ConnectionMode=json_data.get("ConnectionMode"),
            ConnectorProfileConfig=ConnectorProfileConfig._deserialize(json_data.get("ConnectorProfileConfig")),
            CredentialsArn=json_data.get("CredentialsArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppflowConnectorprofile = AwsAppflowConnectorprofile


@dataclass
class ConnectorProfileConfig(BaseModel):
    ConnectorProfileProperties: Optional["_ConnectorProfileProperties"]
    ConnectorProfileCredentials: Optional["_ConnectorProfileCredentials"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorProfileConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorProfileConfig"]:
        if not json_data:
            return None
        return cls(
            ConnectorProfileProperties=ConnectorProfileProperties._deserialize(json_data.get("ConnectorProfileProperties")),
            ConnectorProfileCredentials=ConnectorProfileCredentials._deserialize(json_data.get("ConnectorProfileCredentials")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorProfileConfig = ConnectorProfileConfig


@dataclass
class ConnectorProfileProperties(BaseModel):
    Datadog: Optional["_DatadogConnectorProfileProperties"]
    Dynatrace: Optional["_DynatraceConnectorProfileProperties"]
    InforNexus: Optional["_InforNexusConnectorProfileProperties"]
    Marketo: Optional["_MarketoConnectorProfileProperties"]
    Redshift: Optional["_RedshiftConnectorProfileProperties"]
    SAPOData: Optional["_SAPODataConnectorProfileProperties"]
    Salesforce: Optional["_SalesforceConnectorProfileProperties"]
    Pardot: Optional["_PardotConnectorProfileProperties"]
    ServiceNow: Optional["_ServiceNowConnectorProfileProperties"]
    Slack: Optional["_SlackConnectorProfileProperties"]
    Snowflake: Optional["_SnowflakeConnectorProfileProperties"]
    Veeva: Optional["_VeevaConnectorProfileProperties"]
    Zendesk: Optional["_ZendeskConnectorProfileProperties"]
    CustomConnector: Optional["_CustomConnectorProfileProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            Datadog=DatadogConnectorProfileProperties._deserialize(json_data.get("Datadog")),
            Dynatrace=DynatraceConnectorProfileProperties._deserialize(json_data.get("Dynatrace")),
            InforNexus=InforNexusConnectorProfileProperties._deserialize(json_data.get("InforNexus")),
            Marketo=MarketoConnectorProfileProperties._deserialize(json_data.get("Marketo")),
            Redshift=RedshiftConnectorProfileProperties._deserialize(json_data.get("Redshift")),
            SAPOData=SAPODataConnectorProfileProperties._deserialize(json_data.get("SAPOData")),
            Salesforce=SalesforceConnectorProfileProperties._deserialize(json_data.get("Salesforce")),
            Pardot=PardotConnectorProfileProperties._deserialize(json_data.get("Pardot")),
            ServiceNow=ServiceNowConnectorProfileProperties._deserialize(json_data.get("ServiceNow")),
            Slack=SlackConnectorProfileProperties._deserialize(json_data.get("Slack")),
            Snowflake=SnowflakeConnectorProfileProperties._deserialize(json_data.get("Snowflake")),
            Veeva=VeevaConnectorProfileProperties._deserialize(json_data.get("Veeva")),
            Zendesk=ZendeskConnectorProfileProperties._deserialize(json_data.get("Zendesk")),
            CustomConnector=CustomConnectorProfileProperties._deserialize(json_data.get("CustomConnector")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorProfileProperties = ConnectorProfileProperties


@dataclass
class DatadogConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogConnectorProfileProperties = DatadogConnectorProfileProperties


@dataclass
class DynatraceConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynatraceConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynatraceConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynatraceConnectorProfileProperties = DynatraceConnectorProfileProperties


@dataclass
class InforNexusConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InforNexusConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InforNexusConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InforNexusConnectorProfileProperties = InforNexusConnectorProfileProperties


@dataclass
class MarketoConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MarketoConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketoConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketoConnectorProfileProperties = MarketoConnectorProfileProperties


@dataclass
class RedshiftConnectorProfileProperties(BaseModel):
    DatabaseUrl: Optional[str]
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    RoleArn: Optional[str]
    IsRedshiftServerless: Optional[bool]
    DataApiRoleArn: Optional[str]
    ClusterIdentifier: Optional[str]
    WorkgroupName: Optional[str]
    DatabaseName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            DatabaseUrl=json_data.get("DatabaseUrl"),
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            RoleArn=json_data.get("RoleArn"),
            IsRedshiftServerless=json_data.get("IsRedshiftServerless"),
            DataApiRoleArn=json_data.get("DataApiRoleArn"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            WorkgroupName=json_data.get("WorkgroupName"),
            DatabaseName=json_data.get("DatabaseName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftConnectorProfileProperties = RedshiftConnectorProfileProperties


@dataclass
class SAPODataConnectorProfileProperties(BaseModel):
    ApplicationHostUrl: Optional[str]
    ApplicationServicePath: Optional[str]
    PortNumber: Optional[int]
    ClientNumber: Optional[str]
    LogonLanguage: Optional[str]
    PrivateLinkServiceName: Optional[str]
    OAuthProperties: Optional["_OAuthProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_SAPODataConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SAPODataConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            ApplicationHostUrl=json_data.get("ApplicationHostUrl"),
            ApplicationServicePath=json_data.get("ApplicationServicePath"),
            PortNumber=json_data.get("PortNumber"),
            ClientNumber=json_data.get("ClientNumber"),
            LogonLanguage=json_data.get("LogonLanguage"),
            PrivateLinkServiceName=json_data.get("PrivateLinkServiceName"),
            OAuthProperties=OAuthProperties._deserialize(json_data.get("OAuthProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SAPODataConnectorProfileProperties = SAPODataConnectorProfileProperties


@dataclass
class OAuthProperties(BaseModel):
    AuthCodeUrl: Optional[str]
    TokenUrl: Optional[str]
    OAuthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OAuthProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OAuthProperties"]:
        if not json_data:
            return None
        return cls(
            AuthCodeUrl=json_data.get("AuthCodeUrl"),
            TokenUrl=json_data.get("TokenUrl"),
            OAuthScopes=json_data.get("OAuthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OAuthProperties = OAuthProperties


@dataclass
class SalesforceConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]
    isSandboxEnvironment: Optional[bool]
    usePrivateLinkForMetadataAndAuthorization: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
            isSandboxEnvironment=json_data.get("isSandboxEnvironment"),
            usePrivateLinkForMetadataAndAuthorization=json_data.get("usePrivateLinkForMetadataAndAuthorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceConnectorProfileProperties = SalesforceConnectorProfileProperties


@dataclass
class PardotConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]
    IsSandboxEnvironment: Optional[bool]
    BusinessUnitId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PardotConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PardotConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
            IsSandboxEnvironment=json_data.get("IsSandboxEnvironment"),
            BusinessUnitId=json_data.get("BusinessUnitId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PardotConnectorProfileProperties = PardotConnectorProfileProperties


@dataclass
class ServiceNowConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowConnectorProfileProperties = ServiceNowConnectorProfileProperties


@dataclass
class SlackConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackConnectorProfileProperties = SlackConnectorProfileProperties


@dataclass
class SnowflakeConnectorProfileProperties(BaseModel):
    Warehouse: Optional[str]
    Stage: Optional[str]
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    PrivateLinkServiceName: Optional[str]
    AccountName: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnowflakeConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnowflakeConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            Warehouse=json_data.get("Warehouse"),
            Stage=json_data.get("Stage"),
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            PrivateLinkServiceName=json_data.get("PrivateLinkServiceName"),
            AccountName=json_data.get("AccountName"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnowflakeConnectorProfileProperties = SnowflakeConnectorProfileProperties


@dataclass
class VeevaConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VeevaConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VeevaConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VeevaConnectorProfileProperties = VeevaConnectorProfileProperties


@dataclass
class ZendeskConnectorProfileProperties(BaseModel):
    InstanceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            InstanceUrl=json_data.get("InstanceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskConnectorProfileProperties = ZendeskConnectorProfileProperties


@dataclass
class CustomConnectorProfileProperties(BaseModel):
    ProfileProperties: Optional[MutableMapping[str, str]]
    OAuth2Properties: Optional["_OAuth2Properties"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomConnectorProfileProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomConnectorProfileProperties"]:
        if not json_data:
            return None
        return cls(
            ProfileProperties=json_data.get("ProfileProperties"),
            OAuth2Properties=OAuth2Properties._deserialize(json_data.get("OAuth2Properties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomConnectorProfileProperties = CustomConnectorProfileProperties


@dataclass
class OAuth2Properties(BaseModel):
    TokenUrl: Optional[str]
    OAuth2GrantType: Optional[str]
    TokenUrlCustomProperties: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_OAuth2Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OAuth2Properties"]:
        if not json_data:
            return None
        return cls(
            TokenUrl=json_data.get("TokenUrl"),
            OAuth2GrantType=json_data.get("OAuth2GrantType"),
            TokenUrlCustomProperties=json_data.get("TokenUrlCustomProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OAuth2Properties = OAuth2Properties


@dataclass
class ConnectorProfileCredentials(BaseModel):
    Amplitude: Optional["_AmplitudeConnectorProfileCredentials"]
    Datadog: Optional["_DatadogConnectorProfileCredentials"]
    Dynatrace: Optional["_DynatraceConnectorProfileCredentials"]
    GoogleAnalytics: Optional["_GoogleAnalyticsConnectorProfileCredentials"]
    InforNexus: Optional["_InforNexusConnectorProfileCredentials"]
    Marketo: Optional["_MarketoConnectorProfileCredentials"]
    Redshift: Optional["_RedshiftConnectorProfileCredentials"]
    SAPOData: Optional["_SAPODataConnectorProfileCredentials"]
    Salesforce: Optional["_SalesforceConnectorProfileCredentials"]
    Pardot: Optional["_PardotConnectorProfileCredentials"]
    ServiceNow: Optional["_ServiceNowConnectorProfileCredentials"]
    Singular: Optional["_SingularConnectorProfileCredentials"]
    Slack: Optional["_SlackConnectorProfileCredentials"]
    Snowflake: Optional["_SnowflakeConnectorProfileCredentials"]
    Trendmicro: Optional["_TrendmicroConnectorProfileCredentials"]
    Veeva: Optional["_VeevaConnectorProfileCredentials"]
    Zendesk: Optional["_ZendeskConnectorProfileCredentials"]
    CustomConnector: Optional["_CustomConnectorProfileCredentials"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            Amplitude=AmplitudeConnectorProfileCredentials._deserialize(json_data.get("Amplitude")),
            Datadog=DatadogConnectorProfileCredentials._deserialize(json_data.get("Datadog")),
            Dynatrace=DynatraceConnectorProfileCredentials._deserialize(json_data.get("Dynatrace")),
            GoogleAnalytics=GoogleAnalyticsConnectorProfileCredentials._deserialize(json_data.get("GoogleAnalytics")),
            InforNexus=InforNexusConnectorProfileCredentials._deserialize(json_data.get("InforNexus")),
            Marketo=MarketoConnectorProfileCredentials._deserialize(json_data.get("Marketo")),
            Redshift=RedshiftConnectorProfileCredentials._deserialize(json_data.get("Redshift")),
            SAPOData=SAPODataConnectorProfileCredentials._deserialize(json_data.get("SAPOData")),
            Salesforce=SalesforceConnectorProfileCredentials._deserialize(json_data.get("Salesforce")),
            Pardot=PardotConnectorProfileCredentials._deserialize(json_data.get("Pardot")),
            ServiceNow=ServiceNowConnectorProfileCredentials._deserialize(json_data.get("ServiceNow")),
            Singular=SingularConnectorProfileCredentials._deserialize(json_data.get("Singular")),
            Slack=SlackConnectorProfileCredentials._deserialize(json_data.get("Slack")),
            Snowflake=SnowflakeConnectorProfileCredentials._deserialize(json_data.get("Snowflake")),
            Trendmicro=TrendmicroConnectorProfileCredentials._deserialize(json_data.get("Trendmicro")),
            Veeva=VeevaConnectorProfileCredentials._deserialize(json_data.get("Veeva")),
            Zendesk=ZendeskConnectorProfileCredentials._deserialize(json_data.get("Zendesk")),
            CustomConnector=CustomConnectorProfileCredentials._deserialize(json_data.get("CustomConnector")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorProfileCredentials = ConnectorProfileCredentials


@dataclass
class AmplitudeConnectorProfileCredentials(BaseModel):
    ApiKey: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmplitudeConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmplitudeConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmplitudeConnectorProfileCredentials = AmplitudeConnectorProfileCredentials


@dataclass
class DatadogConnectorProfileCredentials(BaseModel):
    ApiKey: Optional[str]
    ApplicationKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            ApplicationKey=json_data.get("ApplicationKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogConnectorProfileCredentials = DatadogConnectorProfileCredentials


@dataclass
class DynatraceConnectorProfileCredentials(BaseModel):
    ApiToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynatraceConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynatraceConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiToken=json_data.get("ApiToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynatraceConnectorProfileCredentials = DynatraceConnectorProfileCredentials


@dataclass
class GoogleAnalyticsConnectorProfileCredentials(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    AccessToken: Optional[str]
    RefreshToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleAnalyticsConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleAnalyticsConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            AccessToken=json_data.get("AccessToken"),
            RefreshToken=json_data.get("RefreshToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleAnalyticsConnectorProfileCredentials = GoogleAnalyticsConnectorProfileCredentials


@dataclass
class ConnectorOAuthRequest(BaseModel):
    AuthCode: Optional[str]
    RedirectUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorOAuthRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorOAuthRequest"]:
        if not json_data:
            return None
        return cls(
            AuthCode=json_data.get("AuthCode"),
            RedirectUri=json_data.get("RedirectUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorOAuthRequest = ConnectorOAuthRequest


@dataclass
class InforNexusConnectorProfileCredentials(BaseModel):
    AccessKeyId: Optional[str]
    UserId: Optional[str]
    SecretAccessKey: Optional[str]
    Datakey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InforNexusConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InforNexusConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            UserId=json_data.get("UserId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            Datakey=json_data.get("Datakey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InforNexusConnectorProfileCredentials = InforNexusConnectorProfileCredentials


@dataclass
class MarketoConnectorProfileCredentials(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    AccessToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_MarketoConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketoConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            AccessToken=json_data.get("AccessToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketoConnectorProfileCredentials = MarketoConnectorProfileCredentials


@dataclass
class RedshiftConnectorProfileCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftConnectorProfileCredentials = RedshiftConnectorProfileCredentials


@dataclass
class SAPODataConnectorProfileCredentials(BaseModel):
    BasicAuthCredentials: Optional["_BasicAuthCredentials"]
    OAuthCredentials: Optional["_OAuthCredentials"]

    @classmethod
    def _deserialize(
        cls: Type["_SAPODataConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SAPODataConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            BasicAuthCredentials=BasicAuthCredentials._deserialize(json_data.get("BasicAuthCredentials")),
            OAuthCredentials=OAuthCredentials._deserialize(json_data.get("OAuthCredentials")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SAPODataConnectorProfileCredentials = SAPODataConnectorProfileCredentials


@dataclass
class BasicAuthCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthCredentials = BasicAuthCredentials


@dataclass
class OAuthCredentials(BaseModel):
    AccessToken: Optional[str]
    RefreshToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OAuthCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OAuthCredentials"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            RefreshToken=json_data.get("RefreshToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OAuthCredentials = OAuthCredentials


@dataclass
class SalesforceConnectorProfileCredentials(BaseModel):
    AccessToken: Optional[str]
    RefreshToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]
    ClientCredentialsArn: Optional[str]
    OAuth2GrantType: Optional[str]
    JwtToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            RefreshToken=json_data.get("RefreshToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
            ClientCredentialsArn=json_data.get("ClientCredentialsArn"),
            OAuth2GrantType=json_data.get("OAuth2GrantType"),
            JwtToken=json_data.get("JwtToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceConnectorProfileCredentials = SalesforceConnectorProfileCredentials


@dataclass
class PardotConnectorProfileCredentials(BaseModel):
    AccessToken: Optional[str]
    RefreshToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]
    ClientCredentialsArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PardotConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PardotConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            RefreshToken=json_data.get("RefreshToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
            ClientCredentialsArn=json_data.get("ClientCredentialsArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PardotConnectorProfileCredentials = PardotConnectorProfileCredentials


@dataclass
class ServiceNowConnectorProfileCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowConnectorProfileCredentials = ServiceNowConnectorProfileCredentials


@dataclass
class SingularConnectorProfileCredentials(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingularConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingularConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingularConnectorProfileCredentials = SingularConnectorProfileCredentials


@dataclass
class SlackConnectorProfileCredentials(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    AccessToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_SlackConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            AccessToken=json_data.get("AccessToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackConnectorProfileCredentials = SlackConnectorProfileCredentials


@dataclass
class SnowflakeConnectorProfileCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnowflakeConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnowflakeConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnowflakeConnectorProfileCredentials = SnowflakeConnectorProfileCredentials


@dataclass
class TrendmicroConnectorProfileCredentials(BaseModel):
    ApiSecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrendmicroConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrendmicroConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiSecretKey=json_data.get("ApiSecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrendmicroConnectorProfileCredentials = TrendmicroConnectorProfileCredentials


@dataclass
class VeevaConnectorProfileCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VeevaConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VeevaConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VeevaConnectorProfileCredentials = VeevaConnectorProfileCredentials


@dataclass
class ZendeskConnectorProfileCredentials(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    AccessToken: Optional[str]
    ConnectorOAuthRequest: Optional["_ConnectorOAuthRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            AccessToken=json_data.get("AccessToken"),
            ConnectorOAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("ConnectorOAuthRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskConnectorProfileCredentials = ZendeskConnectorProfileCredentials


@dataclass
class CustomConnectorProfileCredentials(BaseModel):
    AuthenticationType: Optional[str]
    Basic: Optional["_BasicAuthCredentials"]
    Oauth2: Optional["_OAuth2Credentials"]
    ApiKey: Optional["_ApiKeyCredentials"]
    Custom: Optional["_CustomAuthCredentials"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomConnectorProfileCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomConnectorProfileCredentials"]:
        if not json_data:
            return None
        return cls(
            AuthenticationType=json_data.get("AuthenticationType"),
            Basic=BasicAuthCredentials._deserialize(json_data.get("Basic")),
            Oauth2=OAuth2Credentials._deserialize(json_data.get("Oauth2")),
            ApiKey=ApiKeyCredentials._deserialize(json_data.get("ApiKey")),
            Custom=CustomAuthCredentials._deserialize(json_data.get("Custom")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomConnectorProfileCredentials = CustomConnectorProfileCredentials


@dataclass
class OAuth2Credentials(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    AccessToken: Optional[str]
    RefreshToken: Optional[str]
    OAuthRequest: Optional["_ConnectorOAuthRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_OAuth2Credentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OAuth2Credentials"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            AccessToken=json_data.get("AccessToken"),
            RefreshToken=json_data.get("RefreshToken"),
            OAuthRequest=ConnectorOAuthRequest._deserialize(json_data.get("OAuthRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OAuth2Credentials = OAuth2Credentials


@dataclass
class ApiKeyCredentials(BaseModel):
    ApiKey: Optional[str]
    ApiSecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiKeyCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiKeyCredentials"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            ApiSecretKey=json_data.get("ApiSecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiKeyCredentials = ApiKeyCredentials


@dataclass
class CustomAuthCredentials(BaseModel):
    CustomAuthenticationType: Optional[str]
    CredentialsMap: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAuthCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAuthCredentials"]:
        if not json_data:
            return None
        return cls(
            CustomAuthenticationType=json_data.get("CustomAuthenticationType"),
            CredentialsMap=json_data.get("CredentialsMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAuthCredentials = CustomAuthCredentials


