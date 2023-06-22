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
class AwsAppsyncSourceapiassociation(BaseModel):
    SourceApiIdentifier: Optional[str]
    MergedApiIdentifier: Optional[str]
    Description: Optional[str]
    SourceApiAssociationConfig: Optional["_SourceApiAssociationConfig"]
    AssociationId: Optional[str]
    AssociationArn: Optional[str]
    SourceApiId: Optional[str]
    SourceApiArn: Optional[str]
    MergedApiId: Optional[str]
    MergedApiArn: Optional[str]
    SourceApiAssociationStatus: Optional[str]
    SourceApiAssociationStatusDetail: Optional[str]
    LastSuccessfulMergeDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncSourceapiassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncSourceapiassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SourceApiIdentifier=json_data.get("SourceApiIdentifier"),
            MergedApiIdentifier=json_data.get("MergedApiIdentifier"),
            Description=json_data.get("Description"),
            SourceApiAssociationConfig=SourceApiAssociationConfig._deserialize(json_data.get("SourceApiAssociationConfig")),
            AssociationId=json_data.get("AssociationId"),
            AssociationArn=json_data.get("AssociationArn"),
            SourceApiId=json_data.get("SourceApiId"),
            SourceApiArn=json_data.get("SourceApiArn"),
            MergedApiId=json_data.get("MergedApiId"),
            MergedApiArn=json_data.get("MergedApiArn"),
            SourceApiAssociationStatus=json_data.get("SourceApiAssociationStatus"),
            SourceApiAssociationStatusDetail=json_data.get("SourceApiAssociationStatusDetail"),
            LastSuccessfulMergeDate=json_data.get("LastSuccessfulMergeDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncSourceapiassociation = AwsAppsyncSourceapiassociation


@dataclass
class SourceApiAssociationConfig(BaseModel):
    MergeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceApiAssociationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceApiAssociationConfig"]:
        if not json_data:
            return None
        return cls(
            MergeType=json_data.get("MergeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceApiAssociationConfig = SourceApiAssociationConfig


