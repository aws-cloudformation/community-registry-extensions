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
class AwsAppsyncApicache(BaseModel):
    Type: Optional[str]
    TransitEncryptionEnabled: Optional[bool]
    AtRestEncryptionEnabled: Optional[bool]
    Id: Optional[str]
    ApiId: Optional[str]
    ApiCachingBehavior: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncApicache"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncApicache"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
            AtRestEncryptionEnabled=json_data.get("AtRestEncryptionEnabled"),
            Id=json_data.get("Id"),
            ApiId=json_data.get("ApiId"),
            ApiCachingBehavior=json_data.get("ApiCachingBehavior"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncApicache = AwsAppsyncApicache


