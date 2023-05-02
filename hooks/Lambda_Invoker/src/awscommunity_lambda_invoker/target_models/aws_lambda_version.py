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
class AwsLambdaVersion(BaseModel):
    FunctionName: Optional[str]
    ProvisionedConcurrencyConfig: Optional["_ProvisionedConcurrencyConfiguration"]
    Description: Optional[str]
    Id: Optional[str]
    CodeSha256: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaVersion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FunctionName=json_data.get("FunctionName"),
            ProvisionedConcurrencyConfig=ProvisionedConcurrencyConfiguration._deserialize(json_data.get("ProvisionedConcurrencyConfig")),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            CodeSha256=json_data.get("CodeSha256"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaVersion = AwsLambdaVersion


@dataclass
class ProvisionedConcurrencyConfiguration(BaseModel):
    ProvisionedConcurrentExecutions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedConcurrencyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedConcurrencyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ProvisionedConcurrentExecutions=json_data.get("ProvisionedConcurrentExecutions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedConcurrencyConfiguration = ProvisionedConcurrencyConfiguration


