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
class AwsLambdaPermission(BaseModel):
    FunctionName: Optional[str]
    Action: Optional[str]
    EventSourceToken: Optional[str]
    FunctionUrlAuthType: Optional[str]
    SourceArn: Optional[str]
    SourceAccount: Optional[str]
    PrincipalOrgID: Optional[str]
    Id: Optional[str]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaPermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaPermission"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FunctionName=json_data.get("FunctionName"),
            Action=json_data.get("Action"),
            EventSourceToken=json_data.get("EventSourceToken"),
            FunctionUrlAuthType=json_data.get("FunctionUrlAuthType"),
            SourceArn=json_data.get("SourceArn"),
            SourceAccount=json_data.get("SourceAccount"),
            PrincipalOrgID=json_data.get("PrincipalOrgID"),
            Id=json_data.get("Id"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaPermission = AwsLambdaPermission


