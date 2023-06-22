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
class AwsIotThing(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    AttributePayload: Optional["_AttributePayload"]
    ThingName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotThing"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotThing"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            AttributePayload=AttributePayload._deserialize(json_data.get("AttributePayload")),
            ThingName=json_data.get("ThingName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotThing = AwsIotThing


@dataclass
class AttributePayload(BaseModel):
    Attributes: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributePayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributePayload"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributePayload = AttributePayload


