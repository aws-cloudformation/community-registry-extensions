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
class AwsAppsyncApikey(BaseModel):
    ApiKey: Optional[str]
    Description: Optional[str]
    ApiKeyId: Optional[str]
    Expires: Optional[float]
    Arn: Optional[str]
    ApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncApikey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncApikey"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApiKey=json_data.get("ApiKey"),
            Description=json_data.get("Description"),
            ApiKeyId=json_data.get("ApiKeyId"),
            Expires=json_data.get("Expires"),
            Arn=json_data.get("Arn"),
            ApiId=json_data.get("ApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncApikey = AwsAppsyncApikey


