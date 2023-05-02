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
class AwsWafv2Loggingconfiguration(BaseModel):
    ResourceArn: Optional[str]
    LogDestinationConfigs: Optional[Sequence[str]]
    RedactedFields: Optional[Sequence["_FieldToMatch"]]
    ManagedByFirewallManager: Optional[bool]
    LoggingFilter: Optional["_LoggingFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafv2Loggingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafv2Loggingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            LogDestinationConfigs=json_data.get("LogDestinationConfigs"),
            RedactedFields=deserialize_list(json_data.get("RedactedFields"), FieldToMatch),
            ManagedByFirewallManager=json_data.get("ManagedByFirewallManager"),
            LoggingFilter=LoggingFilter._deserialize(json_data.get("LoggingFilter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafv2Loggingconfiguration = AwsWafv2Loggingconfiguration


@dataclass
class FieldToMatch(BaseModel):
    JsonBody: Optional["_JsonBody"]
    Method: Optional[MutableMapping[str, Any]]
    QueryString: Optional[MutableMapping[str, Any]]
    SingleHeader: Optional["_SingleHeader"]
    UriPath: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatch"]:
        if not json_data:
            return None
        return cls(
            JsonBody=JsonBody._deserialize(json_data.get("JsonBody")),
            Method=json_data.get("Method"),
            QueryString=json_data.get("QueryString"),
            SingleHeader=SingleHeader._deserialize(json_data.get("SingleHeader")),
            UriPath=json_data.get("UriPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatch = FieldToMatch


@dataclass
class JsonBody(BaseModel):
    InvalidFallbackBehavior: Optional[str]
    MatchPattern: Optional["_MatchPattern"]
    MatchScope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonBody"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonBody"]:
        if not json_data:
            return None
        return cls(
            InvalidFallbackBehavior=json_data.get("InvalidFallbackBehavior"),
            MatchPattern=MatchPattern._deserialize(json_data.get("MatchPattern")),
            MatchScope=json_data.get("MatchScope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonBody = JsonBody


@dataclass
class MatchPattern(BaseModel):
    All: Optional[MutableMapping[str, Any]]
    IncludedPaths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchPattern"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            IncludedPaths=json_data.get("IncludedPaths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchPattern = MatchPattern


@dataclass
class SingleHeader(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleHeader = SingleHeader


@dataclass
class LoggingFilter(BaseModel):
    DefaultBehavior: Optional[str]
    Filters: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingFilter"]:
        if not json_data:
            return None
        return cls(
            DefaultBehavior=json_data.get("DefaultBehavior"),
            Filters=deserialize_list(json_data.get("Filters"), Filter),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingFilter = LoggingFilter


@dataclass
class Filter(BaseModel):
    Behavior: Optional[str]
    Conditions: Optional[Sequence["_Condition"]]
    Requirement: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Behavior=json_data.get("Behavior"),
            Conditions=deserialize_list(json_data.get("Conditions"), Condition),
            Requirement=json_data.get("Requirement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class Condition(BaseModel):
    ActionCondition: Optional["_ActionCondition"]
    LabelNameCondition: Optional["_LabelNameCondition"]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            ActionCondition=ActionCondition._deserialize(json_data.get("ActionCondition")),
            LabelNameCondition=LabelNameCondition._deserialize(json_data.get("LabelNameCondition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class ActionCondition(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionCondition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionCondition = ActionCondition


@dataclass
class LabelNameCondition(BaseModel):
    LabelName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelNameCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelNameCondition"]:
        if not json_data:
            return None
        return cls(
            LabelName=json_data.get("LabelName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelNameCondition = LabelNameCondition


