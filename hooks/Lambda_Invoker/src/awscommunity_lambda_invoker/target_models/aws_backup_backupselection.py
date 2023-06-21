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
class AwsBackupBackupselection(BaseModel):
    Id: Optional[str]
    BackupPlanId: Optional[str]
    BackupSelection: Optional["_BackupSelectionResourceType"]
    SelectionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupBackupselection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupBackupselection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            BackupPlanId=json_data.get("BackupPlanId"),
            BackupSelection=BackupSelectionResourceType._deserialize(json_data.get("BackupSelection")),
            SelectionId=json_data.get("SelectionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupBackupselection = AwsBackupBackupselection


@dataclass
class BackupSelectionResourceType(BaseModel):
    IamRoleArn: Optional[str]
    ListOfTags: Optional[Sequence["_ConditionResourceType"]]
    Resources: Optional[Sequence[str]]
    SelectionName: Optional[str]
    NotResources: Optional[Sequence[str]]
    Conditions: Optional["_Conditions"]

    @classmethod
    def _deserialize(
        cls: Type["_BackupSelectionResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupSelectionResourceType"]:
        if not json_data:
            return None
        return cls(
            IamRoleArn=json_data.get("IamRoleArn"),
            ListOfTags=deserialize_list(json_data.get("ListOfTags"), ConditionResourceType),
            Resources=json_data.get("Resources"),
            SelectionName=json_data.get("SelectionName"),
            NotResources=json_data.get("NotResources"),
            Conditions=Conditions._deserialize(json_data.get("Conditions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupSelectionResourceType = BackupSelectionResourceType


@dataclass
class ConditionResourceType(BaseModel):
    ConditionKey: Optional[str]
    ConditionValue: Optional[str]
    ConditionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionResourceType"]:
        if not json_data:
            return None
        return cls(
            ConditionKey=json_data.get("ConditionKey"),
            ConditionValue=json_data.get("ConditionValue"),
            ConditionType=json_data.get("ConditionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionResourceType = ConditionResourceType


@dataclass
class Conditions(BaseModel):
    StringEquals: Optional[Sequence["_ConditionParameter"]]
    StringNotEquals: Optional[Sequence["_ConditionParameter"]]
    StringLike: Optional[Sequence["_ConditionParameter"]]
    StringNotLike: Optional[Sequence["_ConditionParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            StringEquals=deserialize_list(json_data.get("StringEquals"), ConditionParameter),
            StringNotEquals=deserialize_list(json_data.get("StringNotEquals"), ConditionParameter),
            StringLike=deserialize_list(json_data.get("StringLike"), ConditionParameter),
            StringNotLike=deserialize_list(json_data.get("StringNotLike"), ConditionParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class ConditionParameter(BaseModel):
    ConditionKey: Optional[str]
    ConditionValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionParameter"]:
        if not json_data:
            return None
        return cls(
            ConditionKey=json_data.get("ConditionKey"),
            ConditionValue=json_data.get("ConditionValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionParameter = ConditionParameter


