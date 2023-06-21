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
class AwsIotAccountauditconfiguration(BaseModel):
    AccountId: Optional[str]
    AuditCheckConfigurations: Optional["_AuditCheckConfigurations"]
    AuditNotificationTargetConfigurations: Optional["_AuditNotificationTargetConfigurations"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotAccountauditconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotAccountauditconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccountId=json_data.get("AccountId"),
            AuditCheckConfigurations=AuditCheckConfigurations._deserialize(json_data.get("AuditCheckConfigurations")),
            AuditNotificationTargetConfigurations=AuditNotificationTargetConfigurations._deserialize(json_data.get("AuditNotificationTargetConfigurations")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotAccountauditconfiguration = AwsIotAccountauditconfiguration


@dataclass
class AuditCheckConfigurations(BaseModel):
    AuthenticatedCognitoRoleOverlyPermissiveCheck: Optional["_AuditCheckConfiguration"]
    CaCertificateExpiringCheck: Optional["_AuditCheckConfiguration"]
    CaCertificateKeyQualityCheck: Optional["_AuditCheckConfiguration"]
    ConflictingClientIdsCheck: Optional["_AuditCheckConfiguration"]
    DeviceCertificateExpiringCheck: Optional["_AuditCheckConfiguration"]
    DeviceCertificateKeyQualityCheck: Optional["_AuditCheckConfiguration"]
    DeviceCertificateSharedCheck: Optional["_AuditCheckConfiguration"]
    IotPolicyOverlyPermissiveCheck: Optional["_AuditCheckConfiguration"]
    IotRoleAliasAllowsAccessToUnusedServicesCheck: Optional["_AuditCheckConfiguration"]
    IotRoleAliasOverlyPermissiveCheck: Optional["_AuditCheckConfiguration"]
    LoggingDisabledCheck: Optional["_AuditCheckConfiguration"]
    RevokedCaCertificateStillActiveCheck: Optional["_AuditCheckConfiguration"]
    RevokedDeviceCertificateStillActiveCheck: Optional["_AuditCheckConfiguration"]
    UnauthenticatedCognitoRoleOverlyPermissiveCheck: Optional["_AuditCheckConfiguration"]
    IntermediateCaRevokedForActiveDeviceCertificatesCheck: Optional["_AuditCheckConfiguration"]
    IoTPolicyPotentialMisConfigurationCheck: Optional["_AuditCheckConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AuditCheckConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditCheckConfigurations"]:
        if not json_data:
            return None
        return cls(
            AuthenticatedCognitoRoleOverlyPermissiveCheck=AuditCheckConfiguration._deserialize(json_data.get("AuthenticatedCognitoRoleOverlyPermissiveCheck")),
            CaCertificateExpiringCheck=AuditCheckConfiguration._deserialize(json_data.get("CaCertificateExpiringCheck")),
            CaCertificateKeyQualityCheck=AuditCheckConfiguration._deserialize(json_data.get("CaCertificateKeyQualityCheck")),
            ConflictingClientIdsCheck=AuditCheckConfiguration._deserialize(json_data.get("ConflictingClientIdsCheck")),
            DeviceCertificateExpiringCheck=AuditCheckConfiguration._deserialize(json_data.get("DeviceCertificateExpiringCheck")),
            DeviceCertificateKeyQualityCheck=AuditCheckConfiguration._deserialize(json_data.get("DeviceCertificateKeyQualityCheck")),
            DeviceCertificateSharedCheck=AuditCheckConfiguration._deserialize(json_data.get("DeviceCertificateSharedCheck")),
            IotPolicyOverlyPermissiveCheck=AuditCheckConfiguration._deserialize(json_data.get("IotPolicyOverlyPermissiveCheck")),
            IotRoleAliasAllowsAccessToUnusedServicesCheck=AuditCheckConfiguration._deserialize(json_data.get("IotRoleAliasAllowsAccessToUnusedServicesCheck")),
            IotRoleAliasOverlyPermissiveCheck=AuditCheckConfiguration._deserialize(json_data.get("IotRoleAliasOverlyPermissiveCheck")),
            LoggingDisabledCheck=AuditCheckConfiguration._deserialize(json_data.get("LoggingDisabledCheck")),
            RevokedCaCertificateStillActiveCheck=AuditCheckConfiguration._deserialize(json_data.get("RevokedCaCertificateStillActiveCheck")),
            RevokedDeviceCertificateStillActiveCheck=AuditCheckConfiguration._deserialize(json_data.get("RevokedDeviceCertificateStillActiveCheck")),
            UnauthenticatedCognitoRoleOverlyPermissiveCheck=AuditCheckConfiguration._deserialize(json_data.get("UnauthenticatedCognitoRoleOverlyPermissiveCheck")),
            IntermediateCaRevokedForActiveDeviceCertificatesCheck=AuditCheckConfiguration._deserialize(json_data.get("IntermediateCaRevokedForActiveDeviceCertificatesCheck")),
            IoTPolicyPotentialMisConfigurationCheck=AuditCheckConfiguration._deserialize(json_data.get("IoTPolicyPotentialMisConfigurationCheck")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditCheckConfigurations = AuditCheckConfigurations


@dataclass
class AuditCheckConfiguration(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AuditCheckConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditCheckConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditCheckConfiguration = AuditCheckConfiguration


@dataclass
class AuditNotificationTargetConfigurations(BaseModel):
    Sns: Optional["_AuditNotificationTarget"]

    @classmethod
    def _deserialize(
        cls: Type["_AuditNotificationTargetConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditNotificationTargetConfigurations"]:
        if not json_data:
            return None
        return cls(
            Sns=AuditNotificationTarget._deserialize(json_data.get("Sns")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditNotificationTargetConfigurations = AuditNotificationTargetConfigurations


@dataclass
class AuditNotificationTarget(BaseModel):
    TargetArn: Optional[str]
    RoleArn: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AuditNotificationTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditNotificationTarget"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
            RoleArn=json_data.get("RoleArn"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditNotificationTarget = AuditNotificationTarget


