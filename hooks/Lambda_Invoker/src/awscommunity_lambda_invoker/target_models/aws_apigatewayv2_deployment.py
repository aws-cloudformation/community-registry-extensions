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
class AwsApigatewayv2Deployment(BaseModel):
    DeploymentId: Optional[str]
    Description: Optional[str]
    StageName: Optional[str]
    ApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Deployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Deployment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            StageName=json_data.get("StageName"),
            ApiId=json_data.get("ApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Deployment = AwsApigatewayv2Deployment


