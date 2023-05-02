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
class AwsLicensemanagerLicense(BaseModel):
    ProductSKU: Optional[str]
    Issuer: Optional["_IssuerData"]
    LicenseName: Optional[str]
    ProductName: Optional[str]
    HomeRegion: Optional[str]
    Validity: Optional["_ValidityDateFormat"]
    Entitlements: Optional[Sequence["_Entitlement"]]
    Beneficiary: Optional[str]
    ConsumptionConfiguration: Optional["_ConsumptionConfiguration"]
    LicenseMetadata: Optional[Sequence["_Metadata"]]
    LicenseArn: Optional[str]
    Status: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLicensemanagerLicense"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLicensemanagerLicense"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ProductSKU=json_data.get("ProductSKU"),
            Issuer=IssuerData._deserialize(json_data.get("Issuer")),
            LicenseName=json_data.get("LicenseName"),
            ProductName=json_data.get("ProductName"),
            HomeRegion=json_data.get("HomeRegion"),
            Validity=ValidityDateFormat._deserialize(json_data.get("Validity")),
            Entitlements=deserialize_list(json_data.get("Entitlements"), Entitlement),
            Beneficiary=json_data.get("Beneficiary"),
            ConsumptionConfiguration=ConsumptionConfiguration._deserialize(json_data.get("ConsumptionConfiguration")),
            LicenseMetadata=deserialize_list(json_data.get("LicenseMetadata"), Metadata),
            LicenseArn=json_data.get("LicenseArn"),
            Status=json_data.get("Status"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLicensemanagerLicense = AwsLicensemanagerLicense


@dataclass
class IssuerData(BaseModel):
    Name: Optional[str]
    SignKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerData"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SignKey=json_data.get("SignKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuerData = IssuerData


@dataclass
class ValidityDateFormat(BaseModel):
    Begin: Optional[str]
    End: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidityDateFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidityDateFormat"]:
        if not json_data:
            return None
        return cls(
            Begin=json_data.get("Begin"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidityDateFormat = ValidityDateFormat


@dataclass
class Entitlement(BaseModel):
    Name: Optional[str]
    Value: Optional[str]
    MaxCount: Optional[int]
    Overage: Optional[bool]
    Unit: Optional[str]
    AllowCheckIn: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Entitlement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entitlement"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
            MaxCount=json_data.get("MaxCount"),
            Overage=json_data.get("Overage"),
            Unit=json_data.get("Unit"),
            AllowCheckIn=json_data.get("AllowCheckIn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entitlement = Entitlement


@dataclass
class ConsumptionConfiguration(BaseModel):
    RenewType: Optional[str]
    ProvisionalConfiguration: Optional["_ProvisionalConfiguration"]
    BorrowConfiguration: Optional["_BorrowConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ConsumptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsumptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            RenewType=json_data.get("RenewType"),
            ProvisionalConfiguration=ProvisionalConfiguration._deserialize(json_data.get("ProvisionalConfiguration")),
            BorrowConfiguration=BorrowConfiguration._deserialize(json_data.get("BorrowConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsumptionConfiguration = ConsumptionConfiguration


@dataclass
class ProvisionalConfiguration(BaseModel):
    MaxTimeToLiveInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionalConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionalConfiguration"]:
        if not json_data:
            return None
        return cls(
            MaxTimeToLiveInMinutes=json_data.get("MaxTimeToLiveInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionalConfiguration = ProvisionalConfiguration


@dataclass
class BorrowConfiguration(BaseModel):
    MaxTimeToLiveInMinutes: Optional[int]
    AllowEarlyCheckIn: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BorrowConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BorrowConfiguration"]:
        if not json_data:
            return None
        return cls(
            MaxTimeToLiveInMinutes=json_data.get("MaxTimeToLiveInMinutes"),
            AllowEarlyCheckIn=json_data.get("AllowEarlyCheckIn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BorrowConfiguration = BorrowConfiguration


@dataclass
class Metadata(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


