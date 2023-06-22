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
class AwsLocationMap(BaseModel):
    Configuration: Optional["_MapConfiguration"]
    CreateTime: Optional[str]
    DataSource: Optional[str]
    Description: Optional[str]
    MapArn: Optional[str]
    Arn: Optional[str]
    MapName: Optional[str]
    PricingPlan: Optional[str]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLocationMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLocationMap"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Configuration=MapConfiguration._deserialize(json_data.get("Configuration")),
            CreateTime=json_data.get("CreateTime"),
            DataSource=json_data.get("DataSource"),
            Description=json_data.get("Description"),
            MapArn=json_data.get("MapArn"),
            Arn=json_data.get("Arn"),
            MapName=json_data.get("MapName"),
            PricingPlan=json_data.get("PricingPlan"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLocationMap = AwsLocationMap


@dataclass
class MapConfiguration(BaseModel):
    Style: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapConfiguration"]:
        if not json_data:
            return None
        return cls(
            Style=json_data.get("Style"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapConfiguration = MapConfiguration


