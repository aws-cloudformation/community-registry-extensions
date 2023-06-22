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
class AwsWafRule(BaseModel):
    Id: Optional[str]
    MetricName: Optional[str]
    Name: Optional[str]
    Predicates: Optional[Sequence["_Predicate"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafRule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            Name=json_data.get("Name"),
            Predicates=deserialize_list(json_data.get("Predicates"), Predicate),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafRule = AwsWafRule


@dataclass
class Predicate(BaseModel):
    DataId: Optional[str]
    Negated: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Predicate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicate"]:
        if not json_data:
            return None
        return cls(
            DataId=json_data.get("DataId"),
            Negated=json_data.get("Negated"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicate = Predicate


