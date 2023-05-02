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
class AwsDevopsguruResourcecollection(BaseModel):
    ResourceCollectionFilter: Optional["_ResourceCollectionFilter"]
    ResourceCollectionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDevopsguruResourcecollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDevopsguruResourcecollection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResourceCollectionFilter=ResourceCollectionFilter._deserialize(json_data.get("ResourceCollectionFilter")),
            ResourceCollectionType=json_data.get("ResourceCollectionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDevopsguruResourcecollection = AwsDevopsguruResourcecollection


@dataclass
class ResourceCollectionFilter(BaseModel):
    CloudFormation: Optional["_CloudFormationCollectionFilter"]
    Tags: Optional[Sequence["_TagCollection"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceCollectionFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceCollectionFilter"]:
        if not json_data:
            return None
        return cls(
            CloudFormation=CloudFormationCollectionFilter._deserialize(json_data.get("CloudFormation")),
            Tags=deserialize_list(json_data.get("Tags"), TagCollection),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceCollectionFilter = ResourceCollectionFilter


@dataclass
class CloudFormationCollectionFilter(BaseModel):
    StackNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudFormationCollectionFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudFormationCollectionFilter"]:
        if not json_data:
            return None
        return cls(
            StackNames=json_data.get("StackNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudFormationCollectionFilter = CloudFormationCollectionFilter


@dataclass
class TagCollection(BaseModel):
    AppBoundaryKey: Optional[str]
    TagValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TagCollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagCollection"]:
        if not json_data:
            return None
        return cls(
            AppBoundaryKey=json_data.get("AppBoundaryKey"),
            TagValues=json_data.get("TagValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagCollection = TagCollection


