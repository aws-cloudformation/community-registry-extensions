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
class AwsAthenaNamedquery(BaseModel):
    Name: Optional[str]
    Database: Optional[str]
    Description: Optional[str]
    QueryString: Optional[str]
    WorkGroup: Optional[str]
    NamedQueryId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAthenaNamedquery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAthenaNamedquery"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Database=json_data.get("Database"),
            Description=json_data.get("Description"),
            QueryString=json_data.get("QueryString"),
            WorkGroup=json_data.get("WorkGroup"),
            NamedQueryId=json_data.get("NamedQueryId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAthenaNamedquery = AwsAthenaNamedquery


