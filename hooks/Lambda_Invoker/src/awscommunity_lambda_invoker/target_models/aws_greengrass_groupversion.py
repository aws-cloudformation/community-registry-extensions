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
class AwsGreengrassGroupversion(BaseModel):
    Id: Optional[str]
    LoggerDefinitionVersionArn: Optional[str]
    DeviceDefinitionVersionArn: Optional[str]
    FunctionDefinitionVersionArn: Optional[str]
    CoreDefinitionVersionArn: Optional[str]
    ResourceDefinitionVersionArn: Optional[str]
    ConnectorDefinitionVersionArn: Optional[str]
    SubscriptionDefinitionVersionArn: Optional[str]
    GroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassGroupversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassGroupversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            LoggerDefinitionVersionArn=json_data.get("LoggerDefinitionVersionArn"),
            DeviceDefinitionVersionArn=json_data.get("DeviceDefinitionVersionArn"),
            FunctionDefinitionVersionArn=json_data.get("FunctionDefinitionVersionArn"),
            CoreDefinitionVersionArn=json_data.get("CoreDefinitionVersionArn"),
            ResourceDefinitionVersionArn=json_data.get("ResourceDefinitionVersionArn"),
            ConnectorDefinitionVersionArn=json_data.get("ConnectorDefinitionVersionArn"),
            SubscriptionDefinitionVersionArn=json_data.get("SubscriptionDefinitionVersionArn"),
            GroupId=json_data.get("GroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassGroupversion = AwsGreengrassGroupversion


