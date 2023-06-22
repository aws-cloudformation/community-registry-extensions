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
class AwsRoute53recoverycontrolRoutingcontrol(BaseModel):
    RoutingControlArn: Optional[str]
    ControlPanelArn: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    ClusterArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53recoverycontrolRoutingcontrol"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53recoverycontrolRoutingcontrol"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RoutingControlArn=json_data.get("RoutingControlArn"),
            ControlPanelArn=json_data.get("ControlPanelArn"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            ClusterArn=json_data.get("ClusterArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53recoverycontrolRoutingcontrol = AwsRoute53recoverycontrolRoutingcontrol


