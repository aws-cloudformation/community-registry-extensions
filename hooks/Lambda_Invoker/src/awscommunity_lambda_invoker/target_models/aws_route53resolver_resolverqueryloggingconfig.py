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
class AwsRoute53resolverResolverqueryloggingconfig(BaseModel):
    Id: Optional[str]
    OwnerId: Optional[str]
    Status: Optional[str]
    ShareStatus: Optional[str]
    AssociationCount: Optional[int]
    Arn: Optional[str]
    Name: Optional[str]
    CreatorRequestId: Optional[str]
    DestinationArn: Optional[str]
    CreationTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverResolverqueryloggingconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverResolverqueryloggingconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            Status=json_data.get("Status"),
            ShareStatus=json_data.get("ShareStatus"),
            AssociationCount=json_data.get("AssociationCount"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            CreatorRequestId=json_data.get("CreatorRequestId"),
            DestinationArn=json_data.get("DestinationArn"),
            CreationTime=json_data.get("CreationTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverResolverqueryloggingconfig = AwsRoute53resolverResolverqueryloggingconfig


