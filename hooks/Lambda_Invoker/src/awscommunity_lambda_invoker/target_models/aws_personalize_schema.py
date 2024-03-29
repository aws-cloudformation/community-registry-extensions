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
class AwsPersonalizeSchema(BaseModel):
    Name: Optional[str]
    SchemaArn: Optional[str]
    Schema: Optional[str]
    Domain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPersonalizeSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPersonalizeSchema"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            SchemaArn=json_data.get("SchemaArn"),
            Schema=json_data.get("Schema"),
            Domain=json_data.get("Domain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPersonalizeSchema = AwsPersonalizeSchema


