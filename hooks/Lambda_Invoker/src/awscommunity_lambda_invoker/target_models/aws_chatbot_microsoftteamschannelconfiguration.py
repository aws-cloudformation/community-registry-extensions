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
class AwsChatbotMicrosoftteamschannelconfiguration(BaseModel):
    TeamId: Optional[str]
    TeamsChannelId: Optional[str]
    TeamsTenantId: Optional[str]
    ConfigurationName: Optional[str]
    IamRoleArn: Optional[str]
    SnsTopicArns: Optional[Sequence[str]]
    LoggingLevel: Optional[str]
    Arn: Optional[str]
    GuardrailPolicies: Optional[Sequence[str]]
    UserRoleRequired: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsChatbotMicrosoftteamschannelconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsChatbotMicrosoftteamschannelconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TeamId=json_data.get("TeamId"),
            TeamsChannelId=json_data.get("TeamsChannelId"),
            TeamsTenantId=json_data.get("TeamsTenantId"),
            ConfigurationName=json_data.get("ConfigurationName"),
            IamRoleArn=json_data.get("IamRoleArn"),
            SnsTopicArns=json_data.get("SnsTopicArns"),
            LoggingLevel=json_data.get("LoggingLevel"),
            Arn=json_data.get("Arn"),
            GuardrailPolicies=json_data.get("GuardrailPolicies"),
            UserRoleRequired=json_data.get("UserRoleRequired"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsChatbotMicrosoftteamschannelconfiguration = AwsChatbotMicrosoftteamschannelconfiguration


