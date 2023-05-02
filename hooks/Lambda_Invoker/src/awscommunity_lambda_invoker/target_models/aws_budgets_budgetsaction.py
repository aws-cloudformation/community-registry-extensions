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
class AwsBudgetsBudgetsaction(BaseModel):
    ActionId: Optional[str]
    BudgetName: Optional[str]
    NotificationType: Optional[str]
    ActionType: Optional[str]
    ActionThreshold: Optional["_ActionThreshold"]
    ExecutionRoleArn: Optional[str]
    ApprovalModel: Optional[str]
    Subscribers: Optional[Sequence["_Subscriber"]]
    Definition: Optional["_Definition"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBudgetsBudgetsaction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBudgetsBudgetsaction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ActionId=json_data.get("ActionId"),
            BudgetName=json_data.get("BudgetName"),
            NotificationType=json_data.get("NotificationType"),
            ActionType=json_data.get("ActionType"),
            ActionThreshold=ActionThreshold._deserialize(json_data.get("ActionThreshold")),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            ApprovalModel=json_data.get("ApprovalModel"),
            Subscribers=deserialize_list(json_data.get("Subscribers"), Subscriber),
            Definition=Definition._deserialize(json_data.get("Definition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBudgetsBudgetsaction = AwsBudgetsBudgetsaction


@dataclass
class ActionThreshold(BaseModel):
    Value: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionThreshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionThreshold"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionThreshold = ActionThreshold


@dataclass
class Subscriber(BaseModel):
    Type: Optional[str]
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subscriber"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subscriber"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subscriber = Subscriber


@dataclass
class Definition(BaseModel):
    IamActionDefinition: Optional["_IamActionDefinition"]
    ScpActionDefinition: Optional["_ScpActionDefinition"]
    SsmActionDefinition: Optional["_SsmActionDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Definition"]:
        if not json_data:
            return None
        return cls(
            IamActionDefinition=IamActionDefinition._deserialize(json_data.get("IamActionDefinition")),
            ScpActionDefinition=ScpActionDefinition._deserialize(json_data.get("ScpActionDefinition")),
            SsmActionDefinition=SsmActionDefinition._deserialize(json_data.get("SsmActionDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Definition = Definition


@dataclass
class IamActionDefinition(BaseModel):
    PolicyArn: Optional[str]
    Roles: Optional[Sequence[str]]
    Groups: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IamActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamActionDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyArn=json_data.get("PolicyArn"),
            Roles=json_data.get("Roles"),
            Groups=json_data.get("Groups"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamActionDefinition = IamActionDefinition


@dataclass
class ScpActionDefinition(BaseModel):
    PolicyId: Optional[str]
    TargetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ScpActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScpActionDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyId=json_data.get("PolicyId"),
            TargetIds=json_data.get("TargetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScpActionDefinition = ScpActionDefinition


@dataclass
class SsmActionDefinition(BaseModel):
    Subtype: Optional[str]
    Region: Optional[str]
    InstanceIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SsmActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Subtype=json_data.get("Subtype"),
            Region=json_data.get("Region"),
            InstanceIds=json_data.get("InstanceIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmActionDefinition = SsmActionDefinition


