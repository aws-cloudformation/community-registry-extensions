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
class AwsWafSizeconstraintset(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    SizeConstraints: Optional[Sequence["_SizeConstraint"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafSizeconstraintset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafSizeconstraintset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SizeConstraints=deserialize_list(json_data.get("SizeConstraints"), SizeConstraint),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafSizeconstraintset = AwsWafSizeconstraintset


@dataclass
class SizeConstraint(BaseModel):
    ComparisonOperator: Optional[str]
    FieldToMatch: Optional["_FieldToMatch"]
    Size: Optional[int]
    TextTransformation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SizeConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SizeConstraint"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            Size=json_data.get("Size"),
            TextTransformation=json_data.get("TextTransformation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SizeConstraint = SizeConstraint


@dataclass
class FieldToMatch(BaseModel):
    Data: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatch"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatch = FieldToMatch


