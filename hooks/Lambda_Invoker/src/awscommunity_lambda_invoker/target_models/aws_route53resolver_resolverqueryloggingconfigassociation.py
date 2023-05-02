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
class AwsRoute53resolverResolverqueryloggingconfigassociation(BaseModel):
    Id: Optional[str]
    ResolverQueryLogConfigId: Optional[str]
    ResourceId: Optional[str]
    Status: Optional[str]
    Error: Optional[str]
    ErrorMessage: Optional[str]
    CreationTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverResolverqueryloggingconfigassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverResolverqueryloggingconfigassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ResolverQueryLogConfigId=json_data.get("ResolverQueryLogConfigId"),
            ResourceId=json_data.get("ResourceId"),
            Status=json_data.get("Status"),
            Error=json_data.get("Error"),
            ErrorMessage=json_data.get("ErrorMessage"),
            CreationTime=json_data.get("CreationTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverResolverqueryloggingconfigassociation = AwsRoute53resolverResolverqueryloggingconfigassociation


