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
class AwsGrafanaWorkspace(BaseModel):
    AuthenticationProviders: Optional[AbstractSet[str]]
    SsoClientId: Optional[str]
    SamlConfiguration: Optional["_SamlConfiguration"]
    NetworkAccessControl: Optional["_NetworkAccessControl"]
    VpcConfiguration: Optional["_VpcConfiguration"]
    SamlConfigurationStatus: Optional[str]
    ClientToken: Optional[str]
    Status: Optional[str]
    CreationTimestamp: Optional[str]
    ModificationTimestamp: Optional[str]
    GrafanaVersion: Optional[str]
    Endpoint: Optional[str]
    AccountAccessType: Optional[str]
    OrganizationRoleName: Optional[str]
    PermissionType: Optional[str]
    StackSetName: Optional[str]
    DataSources: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NotificationDestinations: Optional[Sequence[str]]
    OrganizationalUnits: Optional[Sequence[str]]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGrafanaWorkspace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGrafanaWorkspace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AuthenticationProviders=set_or_none(json_data.get("AuthenticationProviders")),
            SsoClientId=json_data.get("SsoClientId"),
            SamlConfiguration=SamlConfiguration._deserialize(json_data.get("SamlConfiguration")),
            NetworkAccessControl=NetworkAccessControl._deserialize(json_data.get("NetworkAccessControl")),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            SamlConfigurationStatus=json_data.get("SamlConfigurationStatus"),
            ClientToken=json_data.get("ClientToken"),
            Status=json_data.get("Status"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            ModificationTimestamp=json_data.get("ModificationTimestamp"),
            GrafanaVersion=json_data.get("GrafanaVersion"),
            Endpoint=json_data.get("Endpoint"),
            AccountAccessType=json_data.get("AccountAccessType"),
            OrganizationRoleName=json_data.get("OrganizationRoleName"),
            PermissionType=json_data.get("PermissionType"),
            StackSetName=json_data.get("StackSetName"),
            DataSources=json_data.get("DataSources"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotificationDestinations=json_data.get("NotificationDestinations"),
            OrganizationalUnits=json_data.get("OrganizationalUnits"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGrafanaWorkspace = AwsGrafanaWorkspace


@dataclass
class SamlConfiguration(BaseModel):
    IdpMetadata: Optional["_IdpMetadata"]
    AssertionAttributes: Optional["_AssertionAttributes"]
    RoleValues: Optional["_RoleValues"]
    AllowedOrganizations: Optional[Sequence[str]]
    LoginValidityDuration: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SamlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamlConfiguration"]:
        if not json_data:
            return None
        return cls(
            IdpMetadata=IdpMetadata._deserialize(json_data.get("IdpMetadata")),
            AssertionAttributes=AssertionAttributes._deserialize(json_data.get("AssertionAttributes")),
            RoleValues=RoleValues._deserialize(json_data.get("RoleValues")),
            AllowedOrganizations=json_data.get("AllowedOrganizations"),
            LoginValidityDuration=json_data.get("LoginValidityDuration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamlConfiguration = SamlConfiguration


@dataclass
class IdpMetadata(BaseModel):
    Url: Optional[str]
    Xml: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdpMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpMetadata"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
            Xml=json_data.get("Xml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpMetadata = IdpMetadata


@dataclass
class AssertionAttributes(BaseModel):
    Name: Optional[str]
    Login: Optional[str]
    Email: Optional[str]
    Groups: Optional[str]
    Role: Optional[str]
    Org: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssertionAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssertionAttributes"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Login=json_data.get("Login"),
            Email=json_data.get("Email"),
            Groups=json_data.get("Groups"),
            Role=json_data.get("Role"),
            Org=json_data.get("Org"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssertionAttributes = AssertionAttributes


@dataclass
class RoleValues(BaseModel):
    Editor: Optional[Sequence[str]]
    Admin: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RoleValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleValues"]:
        if not json_data:
            return None
        return cls(
            Editor=json_data.get("Editor"),
            Admin=json_data.get("Admin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleValues = RoleValues


@dataclass
class NetworkAccessControl(BaseModel):
    PrefixListIds: Optional[AbstractSet[str]]
    VpceIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkAccessControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkAccessControl"]:
        if not json_data:
            return None
        return cls(
            PrefixListIds=set_or_none(json_data.get("PrefixListIds")),
            VpceIds=set_or_none(json_data.get("VpceIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkAccessControl = NetworkAccessControl


@dataclass
class VpcConfiguration(BaseModel):
    SecurityGroupIds: Optional[AbstractSet[str]]
    SubnetIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfiguration = VpcConfiguration


