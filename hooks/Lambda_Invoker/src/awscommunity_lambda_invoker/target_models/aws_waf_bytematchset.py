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
class AwsWafBytematchset(BaseModel):
    Id: Optional[str]
    ByteMatchTuples: Optional[Sequence["_ByteMatchTuple"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafBytematchset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafBytematchset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ByteMatchTuples=deserialize_list(json_data.get("ByteMatchTuples"), ByteMatchTuple),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafBytematchset = AwsWafBytematchset


@dataclass
class ByteMatchTuple(BaseModel):
    FieldToMatch: Optional["_FieldToMatch"]
    PositionalConstraint: Optional[str]
    TargetString: Optional[str]
    TargetStringBase64: Optional[str]
    TextTransformation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ByteMatchTuple"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ByteMatchTuple"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            PositionalConstraint=json_data.get("PositionalConstraint"),
            TargetString=json_data.get("TargetString"),
            TargetStringBase64=json_data.get("TargetStringBase64"),
            TextTransformation=json_data.get("TextTransformation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ByteMatchTuple = ByteMatchTuple


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


