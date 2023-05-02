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
class AwsWafregionalRatebasedrule(BaseModel):
    Id: Optional[str]
    MetricName: Optional[str]
    RateLimit: Optional[int]
    MatchPredicates: Optional[Sequence["_Predicate"]]
    RateKey: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafregionalRatebasedrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafregionalRatebasedrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            RateLimit=json_data.get("RateLimit"),
            MatchPredicates=deserialize_list(json_data.get("MatchPredicates"), Predicate),
            RateKey=json_data.get("RateKey"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafregionalRatebasedrule = AwsWafregionalRatebasedrule


@dataclass
class Predicate(BaseModel):
    Type: Optional[str]
    DataId: Optional[str]
    Negated: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Predicate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicate"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            DataId=json_data.get("DataId"),
            Negated=json_data.get("Negated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicate = Predicate


