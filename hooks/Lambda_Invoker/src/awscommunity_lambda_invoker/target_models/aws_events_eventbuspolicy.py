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
class AwsEventsEventbuspolicy(BaseModel):
    EventBusName: Optional[str]
    Condition: Optional["_Condition"]
    Action: Optional[str]
    StatementId: Optional[str]
    Statement: Optional[MutableMapping[str, Any]]
    Id: Optional[str]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsEventbuspolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsEventbuspolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EventBusName=json_data.get("EventBusName"),
            Condition=Condition._deserialize(json_data.get("Condition")),
            Action=json_data.get("Action"),
            StatementId=json_data.get("StatementId"),
            Statement=json_data.get("Statement"),
            Id=json_data.get("Id"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsEventbuspolicy = AwsEventsEventbuspolicy


@dataclass
class Condition(BaseModel):
    Value: Optional[str]
    Type: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


