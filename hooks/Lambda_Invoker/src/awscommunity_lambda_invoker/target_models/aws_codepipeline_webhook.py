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
class AwsCodepipelineWebhook(BaseModel):
    AuthenticationConfiguration: Optional["_WebhookAuthConfiguration"]
    Filters: Optional[Sequence["_WebhookFilterRule"]]
    Authentication: Optional[str]
    TargetPipeline: Optional[str]
    TargetAction: Optional[str]
    Id: Optional[str]
    Url: Optional[str]
    Name: Optional[str]
    TargetPipelineVersion: Optional[int]
    RegisterWithThirdParty: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodepipelineWebhook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodepipelineWebhook"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AuthenticationConfiguration=WebhookAuthConfiguration._deserialize(json_data.get("AuthenticationConfiguration")),
            Filters=deserialize_list(json_data.get("Filters"), WebhookFilterRule),
            Authentication=json_data.get("Authentication"),
            TargetPipeline=json_data.get("TargetPipeline"),
            TargetAction=json_data.get("TargetAction"),
            Id=json_data.get("Id"),
            Url=json_data.get("Url"),
            Name=json_data.get("Name"),
            TargetPipelineVersion=json_data.get("TargetPipelineVersion"),
            RegisterWithThirdParty=json_data.get("RegisterWithThirdParty"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodepipelineWebhook = AwsCodepipelineWebhook


@dataclass
class WebhookAuthConfiguration(BaseModel):
    AllowedIPRange: Optional[str]
    SecretToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookAuthConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookAuthConfiguration"]:
        if not json_data:
            return None
        return cls(
            AllowedIPRange=json_data.get("AllowedIPRange"),
            SecretToken=json_data.get("SecretToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookAuthConfiguration = WebhookAuthConfiguration


@dataclass
class WebhookFilterRule(BaseModel):
    JsonPath: Optional[str]
    MatchEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookFilterRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookFilterRule"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
            MatchEquals=json_data.get("MatchEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookFilterRule = WebhookFilterRule


