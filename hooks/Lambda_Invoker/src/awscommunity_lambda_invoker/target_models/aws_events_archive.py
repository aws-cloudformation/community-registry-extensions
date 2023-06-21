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
class AwsEventsArchive(BaseModel):
    ArchiveName: Optional[str]
    SourceArn: Optional[str]
    Description: Optional[str]
    EventPattern: Optional[MutableMapping[str, Any]]
    Arn: Optional[str]
    RetentionDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsArchive"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsArchive"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ArchiveName=json_data.get("ArchiveName"),
            SourceArn=json_data.get("SourceArn"),
            Description=json_data.get("Description"),
            EventPattern=json_data.get("EventPattern"),
            Arn=json_data.get("Arn"),
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsArchive = AwsEventsArchive


