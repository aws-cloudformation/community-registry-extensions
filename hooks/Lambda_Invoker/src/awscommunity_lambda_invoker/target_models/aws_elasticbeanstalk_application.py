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
class AwsElasticbeanstalkApplication(BaseModel):
    ApplicationName: Optional[str]
    Description: Optional[str]
    ResourceLifecycleConfig: Optional["_ApplicationResourceLifecycleConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticbeanstalkApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticbeanstalkApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationName=json_data.get("ApplicationName"),
            Description=json_data.get("Description"),
            ResourceLifecycleConfig=ApplicationResourceLifecycleConfig._deserialize(json_data.get("ResourceLifecycleConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticbeanstalkApplication = AwsElasticbeanstalkApplication


@dataclass
class ApplicationResourceLifecycleConfig(BaseModel):
    ServiceRole: Optional[str]
    VersionLifecycleConfig: Optional["_ApplicationVersionLifecycleConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationResourceLifecycleConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationResourceLifecycleConfig"]:
        if not json_data:
            return None
        return cls(
            ServiceRole=json_data.get("ServiceRole"),
            VersionLifecycleConfig=ApplicationVersionLifecycleConfig._deserialize(json_data.get("VersionLifecycleConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationResourceLifecycleConfig = ApplicationResourceLifecycleConfig


@dataclass
class ApplicationVersionLifecycleConfig(BaseModel):
    MaxAgeRule: Optional["_MaxAgeRule"]
    MaxCountRule: Optional["_MaxCountRule"]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationVersionLifecycleConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationVersionLifecycleConfig"]:
        if not json_data:
            return None
        return cls(
            MaxAgeRule=MaxAgeRule._deserialize(json_data.get("MaxAgeRule")),
            MaxCountRule=MaxCountRule._deserialize(json_data.get("MaxCountRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationVersionLifecycleConfig = ApplicationVersionLifecycleConfig


@dataclass
class MaxAgeRule(BaseModel):
    DeleteSourceFromS3: Optional[bool]
    Enabled: Optional[bool]
    MaxAgeInDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MaxAgeRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxAgeRule"]:
        if not json_data:
            return None
        return cls(
            DeleteSourceFromS3=json_data.get("DeleteSourceFromS3"),
            Enabled=json_data.get("Enabled"),
            MaxAgeInDays=json_data.get("MaxAgeInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxAgeRule = MaxAgeRule


@dataclass
class MaxCountRule(BaseModel):
    DeleteSourceFromS3: Optional[bool]
    Enabled: Optional[bool]
    MaxCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MaxCountRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxCountRule"]:
        if not json_data:
            return None
        return cls(
            DeleteSourceFromS3=json_data.get("DeleteSourceFromS3"),
            Enabled=json_data.get("Enabled"),
            MaxCount=json_data.get("MaxCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxCountRule = MaxCountRule


