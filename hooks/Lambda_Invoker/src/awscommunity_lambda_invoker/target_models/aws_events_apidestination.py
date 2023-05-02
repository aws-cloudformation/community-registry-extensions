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
class AwsEventsApidestination(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ConnectionArn: Optional[str]
    Arn: Optional[str]
    InvocationRateLimitPerSecond: Optional[int]
    InvocationEndpoint: Optional[str]
    HttpMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsApidestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsApidestination"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ConnectionArn=json_data.get("ConnectionArn"),
            Arn=json_data.get("Arn"),
            InvocationRateLimitPerSecond=json_data.get("InvocationRateLimitPerSecond"),
            InvocationEndpoint=json_data.get("InvocationEndpoint"),
            HttpMethod=json_data.get("HttpMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsApidestination = AwsEventsApidestination


