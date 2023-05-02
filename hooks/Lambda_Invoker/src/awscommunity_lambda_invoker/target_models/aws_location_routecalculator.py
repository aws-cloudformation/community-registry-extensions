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
class AwsLocationRoutecalculator(BaseModel):
    CalculatorArn: Optional[str]
    Arn: Optional[str]
    CalculatorName: Optional[str]
    CreateTime: Optional[str]
    DataSource: Optional[str]
    Description: Optional[str]
    PricingPlan: Optional[str]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLocationRoutecalculator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLocationRoutecalculator"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CalculatorArn=json_data.get("CalculatorArn"),
            Arn=json_data.get("Arn"),
            CalculatorName=json_data.get("CalculatorName"),
            CreateTime=json_data.get("CreateTime"),
            DataSource=json_data.get("DataSource"),
            Description=json_data.get("Description"),
            PricingPlan=json_data.get("PricingPlan"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLocationRoutecalculator = AwsLocationRoutecalculator


