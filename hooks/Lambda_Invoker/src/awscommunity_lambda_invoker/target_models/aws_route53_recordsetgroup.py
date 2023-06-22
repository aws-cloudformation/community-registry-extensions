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
class AwsRoute53Recordsetgroup(BaseModel):
    Comment: Optional[str]
    Id: Optional[str]
    HostedZoneName: Optional[str]
    RecordSets: Optional[Sequence["_RecordSet"]]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53Recordsetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53Recordsetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            HostedZoneName=json_data.get("HostedZoneName"),
            RecordSets=deserialize_list(json_data.get("RecordSets"), RecordSet),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53Recordsetgroup = AwsRoute53Recordsetgroup


@dataclass
class RecordSet(BaseModel):
    HealthCheckId: Optional[str]
    AliasTarget: Optional["_AliasTarget"]
    HostedZoneName: Optional[str]
    ResourceRecords: Optional[Sequence[str]]
    HostedZoneId: Optional[str]
    SetIdentifier: Optional[str]
    TTL: Optional[str]
    Weight: Optional[int]
    Name: Optional[str]
    Type: Optional[str]
    CidrRoutingConfig: Optional["_CidrRoutingConfig"]
    Failover: Optional[str]
    Region: Optional[str]
    GeoLocation: Optional["_GeoLocation"]
    MultiValueAnswer: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSet"]:
        if not json_data:
            return None
        return cls(
            HealthCheckId=json_data.get("HealthCheckId"),
            AliasTarget=AliasTarget._deserialize(json_data.get("AliasTarget")),
            HostedZoneName=json_data.get("HostedZoneName"),
            ResourceRecords=json_data.get("ResourceRecords"),
            HostedZoneId=json_data.get("HostedZoneId"),
            SetIdentifier=json_data.get("SetIdentifier"),
            TTL=json_data.get("TTL"),
            Weight=json_data.get("Weight"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            CidrRoutingConfig=CidrRoutingConfig._deserialize(json_data.get("CidrRoutingConfig")),
            Failover=json_data.get("Failover"),
            Region=json_data.get("Region"),
            GeoLocation=GeoLocation._deserialize(json_data.get("GeoLocation")),
            MultiValueAnswer=json_data.get("MultiValueAnswer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSet = RecordSet


@dataclass
class AliasTarget(BaseModel):
    DNSName: Optional[str]
    HostedZoneId: Optional[str]
    EvaluateTargetHealth: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AliasTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasTarget"]:
        if not json_data:
            return None
        return cls(
            DNSName=json_data.get("DNSName"),
            HostedZoneId=json_data.get("HostedZoneId"),
            EvaluateTargetHealth=json_data.get("EvaluateTargetHealth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasTarget = AliasTarget


@dataclass
class CidrRoutingConfig(BaseModel):
    CollectionId: Optional[str]
    LocationName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CidrRoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CidrRoutingConfig"]:
        if not json_data:
            return None
        return cls(
            CollectionId=json_data.get("CollectionId"),
            LocationName=json_data.get("LocationName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CidrRoutingConfig = CidrRoutingConfig


@dataclass
class GeoLocation(BaseModel):
    ContinentCode: Optional[str]
    CountryCode: Optional[str]
    SubdivisionCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocation"]:
        if not json_data:
            return None
        return cls(
            ContinentCode=json_data.get("ContinentCode"),
            CountryCode=json_data.get("CountryCode"),
            SubdivisionCode=json_data.get("SubdivisionCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocation = GeoLocation


