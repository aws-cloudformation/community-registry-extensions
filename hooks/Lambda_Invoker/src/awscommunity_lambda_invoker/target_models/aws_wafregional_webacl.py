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
class AwsWafregionalWebacl(BaseModel):
    Id: Optional[str]
    MetricName: Optional[str]
    DefaultAction: Optional["_Action"]
    Rules: Optional[Sequence["_Rule"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafregionalWebacl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafregionalWebacl"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            DefaultAction=Action._deserialize(json_data.get("DefaultAction")),
            Rules=deserialize_list(json_data.get("Rules"), Rule),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafregionalWebacl = AwsWafregionalWebacl


@dataclass
class Action(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Rule(BaseModel):
    Action: Optional["_Action"]
    Priority: Optional[int]
    RuleId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=Action._deserialize(json_data.get("Action")),
            Priority=json_data.get("Priority"),
            RuleId=json_data.get("RuleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


