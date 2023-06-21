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
class AwsWafXssmatchset(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    XssMatchTuples: Optional[Sequence["_XssMatchTuple"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafXssmatchset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafXssmatchset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            XssMatchTuples=deserialize_list(json_data.get("XssMatchTuples"), XssMatchTuple),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafXssmatchset = AwsWafXssmatchset


@dataclass
class XssMatchTuple(BaseModel):
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XssMatchTuple"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XssMatchTuple"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformation=json_data.get("TextTransformation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XssMatchTuple = XssMatchTuple


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


