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
class AwsElasticbeanstalkConfigurationtemplate(BaseModel):
    ApplicationName: Optional[str]
    Description: Optional[str]
    EnvironmentId: Optional[str]
    OptionSettings: Optional[Sequence["_ConfigurationOptionSetting"]]
    PlatformArn: Optional[str]
    SolutionStackName: Optional[str]
    SourceConfiguration: Optional["_SourceConfiguration"]
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticbeanstalkConfigurationtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticbeanstalkConfigurationtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationName=json_data.get("ApplicationName"),
            Description=json_data.get("Description"),
            EnvironmentId=json_data.get("EnvironmentId"),
            OptionSettings=deserialize_list(json_data.get("OptionSettings"), ConfigurationOptionSetting),
            PlatformArn=json_data.get("PlatformArn"),
            SolutionStackName=json_data.get("SolutionStackName"),
            SourceConfiguration=SourceConfiguration._deserialize(json_data.get("SourceConfiguration")),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticbeanstalkConfigurationtemplate = AwsElasticbeanstalkConfigurationtemplate


@dataclass
class ConfigurationOptionSetting(BaseModel):
    Namespace: Optional[str]
    OptionName: Optional[str]
    ResourceName: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationOptionSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationOptionSetting"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
            OptionName=json_data.get("OptionName"),
            ResourceName=json_data.get("ResourceName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationOptionSetting = ConfigurationOptionSetting


@dataclass
class SourceConfiguration(BaseModel):
    ApplicationName: Optional[str]
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationName=json_data.get("ApplicationName"),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConfiguration = SourceConfiguration


