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
class AwsAcmpcaCertificate(BaseModel):
    ApiPassthrough: Optional["_ApiPassthrough"]
    CertificateAuthorityArn: Optional[str]
    CertificateSigningRequest: Optional[str]
    SigningAlgorithm: Optional[str]
    TemplateArn: Optional[str]
    Validity: Optional["_Validity"]
    ValidityNotBefore: Optional["_Validity"]
    Certificate: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAcmpcaCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAcmpcaCertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApiPassthrough=ApiPassthrough._deserialize(json_data.get("ApiPassthrough")),
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            TemplateArn=json_data.get("TemplateArn"),
            Validity=Validity._deserialize(json_data.get("Validity")),
            ValidityNotBefore=Validity._deserialize(json_data.get("ValidityNotBefore")),
            Certificate=json_data.get("Certificate"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAcmpcaCertificate = AwsAcmpcaCertificate


@dataclass
class ApiPassthrough(BaseModel):
    Extensions: Optional["_Extensions"]
    Subject: Optional["_Subject"]

    @classmethod
    def _deserialize(
        cls: Type["_ApiPassthrough"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiPassthrough"]:
        if not json_data:
            return None
        return cls(
            Extensions=Extensions._deserialize(json_data.get("Extensions")),
            Subject=Subject._deserialize(json_data.get("Subject")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiPassthrough = ApiPassthrough


@dataclass
class Extensions(BaseModel):
    CertificatePolicies: Optional[Sequence["_PolicyInformation"]]
    ExtendedKeyUsage: Optional[Sequence["_ExtendedKeyUsage"]]
    KeyUsage: Optional["_KeyUsage"]
    SubjectAlternativeNames: Optional[Sequence["_GeneralName"]]
    CustomExtensions: Optional[Sequence["_CustomExtension"]]

    @classmethod
    def _deserialize(
        cls: Type["_Extensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Extensions"]:
        if not json_data:
            return None
        return cls(
            CertificatePolicies=deserialize_list(json_data.get("CertificatePolicies"), PolicyInformation),
            ExtendedKeyUsage=deserialize_list(json_data.get("ExtendedKeyUsage"), ExtendedKeyUsage),
            KeyUsage=KeyUsage._deserialize(json_data.get("KeyUsage")),
            SubjectAlternativeNames=deserialize_list(json_data.get("SubjectAlternativeNames"), GeneralName),
            CustomExtensions=deserialize_list(json_data.get("CustomExtensions"), CustomExtension),
        )


# work around possible type aliasing issues when variable has same name as a model
_Extensions = Extensions


@dataclass
class PolicyInformation(BaseModel):
    CertPolicyId: Optional[str]
    PolicyQualifiers: Optional[Sequence["_PolicyQualifierInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyInformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyInformation"]:
        if not json_data:
            return None
        return cls(
            CertPolicyId=json_data.get("CertPolicyId"),
            PolicyQualifiers=deserialize_list(json_data.get("PolicyQualifiers"), PolicyQualifierInfo),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyInformation = PolicyInformation


@dataclass
class PolicyQualifierInfo(BaseModel):
    PolicyQualifierId: Optional[str]
    Qualifier: Optional["_Qualifier"]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyQualifierInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyQualifierInfo"]:
        if not json_data:
            return None
        return cls(
            PolicyQualifierId=json_data.get("PolicyQualifierId"),
            Qualifier=Qualifier._deserialize(json_data.get("Qualifier")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyQualifierInfo = PolicyQualifierInfo


@dataclass
class Qualifier(BaseModel):
    CpsUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Qualifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Qualifier"]:
        if not json_data:
            return None
        return cls(
            CpsUri=json_data.get("CpsUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Qualifier = Qualifier


@dataclass
class ExtendedKeyUsage(BaseModel):
    ExtendedKeyUsageType: Optional[str]
    ExtendedKeyUsageObjectIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedKeyUsage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedKeyUsage"]:
        if not json_data:
            return None
        return cls(
            ExtendedKeyUsageType=json_data.get("ExtendedKeyUsageType"),
            ExtendedKeyUsageObjectIdentifier=json_data.get("ExtendedKeyUsageObjectIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedKeyUsage = ExtendedKeyUsage


@dataclass
class KeyUsage(BaseModel):
    DigitalSignature: Optional[bool]
    NonRepudiation: Optional[bool]
    KeyEncipherment: Optional[bool]
    DataEncipherment: Optional[bool]
    KeyAgreement: Optional[bool]
    KeyCertSign: Optional[bool]
    CRLSign: Optional[bool]
    EncipherOnly: Optional[bool]
    DecipherOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsage"]:
        if not json_data:
            return None
        return cls(
            DigitalSignature=json_data.get("DigitalSignature"),
            NonRepudiation=json_data.get("NonRepudiation"),
            KeyEncipherment=json_data.get("KeyEncipherment"),
            DataEncipherment=json_data.get("DataEncipherment"),
            KeyAgreement=json_data.get("KeyAgreement"),
            KeyCertSign=json_data.get("KeyCertSign"),
            CRLSign=json_data.get("CRLSign"),
            EncipherOnly=json_data.get("EncipherOnly"),
            DecipherOnly=json_data.get("DecipherOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsage = KeyUsage


@dataclass
class GeneralName(BaseModel):
    OtherName: Optional["_OtherName"]
    Rfc822Name: Optional[str]
    DnsName: Optional[str]
    DirectoryName: Optional["_Subject"]
    EdiPartyName: Optional["_EdiPartyName"]
    UniformResourceIdentifier: Optional[str]
    IpAddress: Optional[str]
    RegisteredId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeneralName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneralName"]:
        if not json_data:
            return None
        return cls(
            OtherName=OtherName._deserialize(json_data.get("OtherName")),
            Rfc822Name=json_data.get("Rfc822Name"),
            DnsName=json_data.get("DnsName"),
            DirectoryName=Subject._deserialize(json_data.get("DirectoryName")),
            EdiPartyName=EdiPartyName._deserialize(json_data.get("EdiPartyName")),
            UniformResourceIdentifier=json_data.get("UniformResourceIdentifier"),
            IpAddress=json_data.get("IpAddress"),
            RegisteredId=json_data.get("RegisteredId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneralName = GeneralName


@dataclass
class OtherName(BaseModel):
    TypeId: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OtherName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OtherName"]:
        if not json_data:
            return None
        return cls(
            TypeId=json_data.get("TypeId"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OtherName = OtherName


@dataclass
class Subject(BaseModel):
    Country: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    DistinguishedNameQualifier: Optional[str]
    State: Optional[str]
    CommonName: Optional[str]
    SerialNumber: Optional[str]
    Locality: Optional[str]
    Title: Optional[str]
    Surname: Optional[str]
    GivenName: Optional[str]
    Initials: Optional[str]
    Pseudonym: Optional[str]
    GenerationQualifier: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subject"]:
        if not json_data:
            return None
        return cls(
            Country=json_data.get("Country"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            DistinguishedNameQualifier=json_data.get("DistinguishedNameQualifier"),
            State=json_data.get("State"),
            CommonName=json_data.get("CommonName"),
            SerialNumber=json_data.get("SerialNumber"),
            Locality=json_data.get("Locality"),
            Title=json_data.get("Title"),
            Surname=json_data.get("Surname"),
            GivenName=json_data.get("GivenName"),
            Initials=json_data.get("Initials"),
            Pseudonym=json_data.get("Pseudonym"),
            GenerationQualifier=json_data.get("GenerationQualifier"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subject = Subject


@dataclass
class CustomAttribute(BaseModel):
    ObjectIdentifier: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttribute"]:
        if not json_data:
            return None
        return cls(
            ObjectIdentifier=json_data.get("ObjectIdentifier"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttribute = CustomAttribute


@dataclass
class EdiPartyName(BaseModel):
    PartyName: Optional[str]
    NameAssigner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdiPartyName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdiPartyName"]:
        if not json_data:
            return None
        return cls(
            PartyName=json_data.get("PartyName"),
            NameAssigner=json_data.get("NameAssigner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdiPartyName = EdiPartyName


@dataclass
class CustomExtension(BaseModel):
    Critical: Optional[bool]
    ObjectIdentifier: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomExtension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomExtension"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            ObjectIdentifier=json_data.get("ObjectIdentifier"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomExtension = CustomExtension


@dataclass
class Validity(BaseModel):
    Value: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Validity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Validity"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Validity = Validity


