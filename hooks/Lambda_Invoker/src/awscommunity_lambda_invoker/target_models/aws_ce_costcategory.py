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
class AwsCeCostcategory(BaseModel):
    Arn: Optional[str]
    EffectiveStart: Optional[str]
    Name: Optional[str]
    RuleVersion: Optional[str]
    Rules: Optional[str]
    SplitChargeRules: Optional[str]
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCeCostcategory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCeCostcategory"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            EffectiveStart=json_data.get("EffectiveStart"),
            Name=json_data.get("Name"),
            RuleVersion=json_data.get("RuleVersion"),
            Rules=json_data.get("Rules"),
            SplitChargeRules=json_data.get("SplitChargeRules"),
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCeCostcategory = AwsCeCostcategory


