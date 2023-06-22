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
class AwsSupportappSlackchannelconfiguration(BaseModel):
    TeamId: Optional[str]
    ChannelId: Optional[str]
    ChannelName: Optional[str]
    NotifyOnCreateOrReopenCase: Optional[bool]
    NotifyOnAddCorrespondenceToCase: Optional[bool]
    NotifyOnResolveCase: Optional[bool]
    NotifyOnCaseSeverity: Optional[str]
    ChannelRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSupportappSlackchannelconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSupportappSlackchannelconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TeamId=json_data.get("TeamId"),
            ChannelId=json_data.get("ChannelId"),
            ChannelName=json_data.get("ChannelName"),
            NotifyOnCreateOrReopenCase=json_data.get("NotifyOnCreateOrReopenCase"),
            NotifyOnAddCorrespondenceToCase=json_data.get("NotifyOnAddCorrespondenceToCase"),
            NotifyOnResolveCase=json_data.get("NotifyOnResolveCase"),
            NotifyOnCaseSeverity=json_data.get("NotifyOnCaseSeverity"),
            ChannelRoleArn=json_data.get("ChannelRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSupportappSlackchannelconfiguration = AwsSupportappSlackchannelconfiguration


