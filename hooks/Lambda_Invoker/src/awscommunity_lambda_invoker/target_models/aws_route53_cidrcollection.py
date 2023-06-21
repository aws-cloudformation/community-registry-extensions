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
class AwsRoute53Cidrcollection(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Arn: Optional[str]
    Locations: Optional[AbstractSet["_Location"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53Cidrcollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53Cidrcollection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            Locations=set_or_none(json_data.get("Locations")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53Cidrcollection = AwsRoute53Cidrcollection


@dataclass
class Location(BaseModel):
    LocationName: Optional[str]
    CidrList: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Location"]:
        if not json_data:
            return None
        return cls(
            LocationName=json_data.get("LocationName"),
            CidrList=set_or_none(json_data.get("CidrList")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Location = Location


