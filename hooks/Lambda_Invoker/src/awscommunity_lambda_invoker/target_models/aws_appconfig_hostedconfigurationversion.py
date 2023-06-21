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
class AwsAppconfigHostedconfigurationversion(BaseModel):
    ConfigurationProfileId: Optional[str]
    Description: Optional[str]
    ContentType: Optional[str]
    LatestVersionNumber: Optional[float]
    Content: Optional[str]
    VersionLabel: Optional[str]
    Id: Optional[str]
    ApplicationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigHostedconfigurationversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigHostedconfigurationversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConfigurationProfileId=json_data.get("ConfigurationProfileId"),
            Description=json_data.get("Description"),
            ContentType=json_data.get("ContentType"),
            LatestVersionNumber=json_data.get("LatestVersionNumber"),
            Content=json_data.get("Content"),
            VersionLabel=json_data.get("VersionLabel"),
            Id=json_data.get("Id"),
            ApplicationId=json_data.get("ApplicationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigHostedconfigurationversion = AwsAppconfigHostedconfigurationversion


