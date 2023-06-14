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
class AwsLambdaLayerversionpermission(BaseModel):
    Id: Optional[str]
    Action: Optional[str]
    LayerVersionArn: Optional[str]
    OrganizationId: Optional[str]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaLayerversionpermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaLayerversionpermission"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Action=json_data.get("Action"),
            LayerVersionArn=json_data.get("LayerVersionArn"),
            OrganizationId=json_data.get("OrganizationId"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaLayerversionpermission = AwsLambdaLayerversionpermission


