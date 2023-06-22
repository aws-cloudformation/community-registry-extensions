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
class AwsInspectorv2Filter(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    FilterCriteria: Optional["_FilterCriteria"]
    FilterAction: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsInspectorv2Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsInspectorv2Filter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            FilterCriteria=FilterCriteria._deserialize(json_data.get("FilterCriteria")),
            FilterAction=json_data.get("FilterAction"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsInspectorv2Filter = AwsInspectorv2Filter


@dataclass
class FilterCriteria(BaseModel):
    AwsAccountId: Optional[Sequence["_StringFilter"]]
    ComponentId: Optional[Sequence["_StringFilter"]]
    ComponentType: Optional[Sequence["_StringFilter"]]
    Ec2InstanceImageId: Optional[Sequence["_StringFilter"]]
    Ec2InstanceSubnetId: Optional[Sequence["_StringFilter"]]
    Ec2InstanceVpcId: Optional[Sequence["_StringFilter"]]
    EcrImageArchitecture: Optional[Sequence["_StringFilter"]]
    EcrImageHash: Optional[Sequence["_StringFilter"]]
    EcrImageTags: Optional[Sequence["_StringFilter"]]
    EcrImagePushedAt: Optional[Sequence["_DateFilter"]]
    EcrImageRegistry: Optional[Sequence["_StringFilter"]]
    EcrImageRepositoryName: Optional[Sequence["_StringFilter"]]
    FindingArn: Optional[Sequence["_StringFilter"]]
    FindingStatus: Optional[Sequence["_StringFilter"]]
    FindingType: Optional[Sequence["_StringFilter"]]
    FirstObservedAt: Optional[Sequence["_DateFilter"]]
    InspectorScore: Optional[Sequence["_NumberFilter"]]
    LastObservedAt: Optional[Sequence["_DateFilter"]]
    NetworkProtocol: Optional[Sequence["_StringFilter"]]
    PortRange: Optional[Sequence["_PortRangeFilter"]]
    RelatedVulnerabilities: Optional[Sequence["_StringFilter"]]
    ResourceId: Optional[Sequence["_StringFilter"]]
    ResourceTags: Optional[Sequence["_MapFilter"]]
    ResourceType: Optional[Sequence["_StringFilter"]]
    Severity: Optional[Sequence["_StringFilter"]]
    Title: Optional[Sequence["_StringFilter"]]
    UpdatedAt: Optional[Sequence["_DateFilter"]]
    VendorSeverity: Optional[Sequence["_StringFilter"]]
    VulnerabilityId: Optional[Sequence["_StringFilter"]]
    VulnerabilitySource: Optional[Sequence["_StringFilter"]]
    VulnerablePackages: Optional[Sequence["_PackageFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterCriteria"]:
        if not json_data:
            return None
        return cls(
            AwsAccountId=deserialize_list(json_data.get("AwsAccountId"), StringFilter),
            ComponentId=deserialize_list(json_data.get("ComponentId"), StringFilter),
            ComponentType=deserialize_list(json_data.get("ComponentType"), StringFilter),
            Ec2InstanceImageId=deserialize_list(json_data.get("Ec2InstanceImageId"), StringFilter),
            Ec2InstanceSubnetId=deserialize_list(json_data.get("Ec2InstanceSubnetId"), StringFilter),
            Ec2InstanceVpcId=deserialize_list(json_data.get("Ec2InstanceVpcId"), StringFilter),
            EcrImageArchitecture=deserialize_list(json_data.get("EcrImageArchitecture"), StringFilter),
            EcrImageHash=deserialize_list(json_data.get("EcrImageHash"), StringFilter),
            EcrImageTags=deserialize_list(json_data.get("EcrImageTags"), StringFilter),
            EcrImagePushedAt=deserialize_list(json_data.get("EcrImagePushedAt"), DateFilter),
            EcrImageRegistry=deserialize_list(json_data.get("EcrImageRegistry"), StringFilter),
            EcrImageRepositoryName=deserialize_list(json_data.get("EcrImageRepositoryName"), StringFilter),
            FindingArn=deserialize_list(json_data.get("FindingArn"), StringFilter),
            FindingStatus=deserialize_list(json_data.get("FindingStatus"), StringFilter),
            FindingType=deserialize_list(json_data.get("FindingType"), StringFilter),
            FirstObservedAt=deserialize_list(json_data.get("FirstObservedAt"), DateFilter),
            InspectorScore=deserialize_list(json_data.get("InspectorScore"), NumberFilter),
            LastObservedAt=deserialize_list(json_data.get("LastObservedAt"), DateFilter),
            NetworkProtocol=deserialize_list(json_data.get("NetworkProtocol"), StringFilter),
            PortRange=deserialize_list(json_data.get("PortRange"), PortRangeFilter),
            RelatedVulnerabilities=deserialize_list(json_data.get("RelatedVulnerabilities"), StringFilter),
            ResourceId=deserialize_list(json_data.get("ResourceId"), StringFilter),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), MapFilter),
            ResourceType=deserialize_list(json_data.get("ResourceType"), StringFilter),
            Severity=deserialize_list(json_data.get("Severity"), StringFilter),
            Title=deserialize_list(json_data.get("Title"), StringFilter),
            UpdatedAt=deserialize_list(json_data.get("UpdatedAt"), DateFilter),
            VendorSeverity=deserialize_list(json_data.get("VendorSeverity"), StringFilter),
            VulnerabilityId=deserialize_list(json_data.get("VulnerabilityId"), StringFilter),
            VulnerabilitySource=deserialize_list(json_data.get("VulnerabilitySource"), StringFilter),
            VulnerablePackages=deserialize_list(json_data.get("VulnerablePackages"), PackageFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterCriteria = FilterCriteria


@dataclass
class StringFilter(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringFilter"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringFilter = StringFilter


@dataclass
class DateFilter(BaseModel):
    EndInclusive: Optional[int]
    StartInclusive: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DateFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateFilter"]:
        if not json_data:
            return None
        return cls(
            EndInclusive=json_data.get("EndInclusive"),
            StartInclusive=json_data.get("StartInclusive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateFilter = DateFilter


@dataclass
class NumberFilter(BaseModel):
    LowerInclusive: Optional[float]
    UpperInclusive: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberFilter"]:
        if not json_data:
            return None
        return cls(
            LowerInclusive=json_data.get("LowerInclusive"),
            UpperInclusive=json_data.get("UpperInclusive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberFilter = NumberFilter


@dataclass
class PortRangeFilter(BaseModel):
    BeginInclusive: Optional[int]
    EndInclusive: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRangeFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRangeFilter"]:
        if not json_data:
            return None
        return cls(
            BeginInclusive=json_data.get("BeginInclusive"),
            EndInclusive=json_data.get("EndInclusive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRangeFilter = PortRangeFilter


@dataclass
class MapFilter(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapFilter"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapFilter = MapFilter


@dataclass
class PackageFilter(BaseModel):
    Architecture: Optional["_StringFilter"]
    Epoch: Optional["_NumberFilter"]
    Name: Optional["_StringFilter"]
    Release: Optional["_StringFilter"]
    SourceLayerHash: Optional["_StringFilter"]
    Version: Optional["_StringFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_PackageFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageFilter"]:
        if not json_data:
            return None
        return cls(
            Architecture=StringFilter._deserialize(json_data.get("Architecture")),
            Epoch=NumberFilter._deserialize(json_data.get("Epoch")),
            Name=StringFilter._deserialize(json_data.get("Name")),
            Release=StringFilter._deserialize(json_data.get("Release")),
            SourceLayerHash=StringFilter._deserialize(json_data.get("SourceLayerHash")),
            Version=StringFilter._deserialize(json_data.get("Version")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageFilter = PackageFilter


