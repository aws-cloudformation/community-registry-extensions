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
class AwsSsmcontactsContactchannel(BaseModel):
    ContactId: Optional[str]
    ChannelName: Optional[str]
    ChannelType: Optional[str]
    DeferActivation: Optional[bool]
    ChannelAddress: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmcontactsContactchannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmcontactsContactchannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ContactId=json_data.get("ContactId"),
            ChannelName=json_data.get("ChannelName"),
            ChannelType=json_data.get("ChannelType"),
            DeferActivation=json_data.get("DeferActivation"),
            ChannelAddress=json_data.get("ChannelAddress"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmcontactsContactchannel = AwsSsmcontactsContactchannel


