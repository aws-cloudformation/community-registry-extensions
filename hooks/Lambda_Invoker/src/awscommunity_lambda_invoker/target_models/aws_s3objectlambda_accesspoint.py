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
class AwsS3objectlambdaAccesspoint(BaseModel):
    Name: Optional[str]
    Alias: Optional["_Alias"]
    Arn: Optional[str]
    CreationDate: Optional[str]
    PublicAccessBlockConfiguration: Optional["_PublicAccessBlockConfiguration"]
    PolicyStatus: Optional["_PolicyStatus"]
    ObjectLambdaConfiguration: Optional["_ObjectLambdaConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3objectlambdaAccesspoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3objectlambdaAccesspoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Alias=Alias._deserialize(json_data.get("Alias")),
            Arn=json_data.get("Arn"),
            CreationDate=json_data.get("CreationDate"),
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration._deserialize(json_data.get("PublicAccessBlockConfiguration")),
            PolicyStatus=PolicyStatus._deserialize(json_data.get("PolicyStatus")),
            ObjectLambdaConfiguration=ObjectLambdaConfiguration._deserialize(json_data.get("ObjectLambdaConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3objectlambdaAccesspoint = AwsS3objectlambdaAccesspoint


@dataclass
class Alias(BaseModel):
    Status: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alias"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alias = Alias


@dataclass
class PublicAccessBlockConfiguration(BaseModel):
    BlockPublicAcls: Optional[bool]
    IgnorePublicAcls: Optional[bool]
    BlockPublicPolicy: Optional[bool]
    RestrictPublicBuckets: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessBlockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessBlockConfiguration"]:
        if not json_data:
            return None
        return cls(
            BlockPublicAcls=json_data.get("BlockPublicAcls"),
            IgnorePublicAcls=json_data.get("IgnorePublicAcls"),
            BlockPublicPolicy=json_data.get("BlockPublicPolicy"),
            RestrictPublicBuckets=json_data.get("RestrictPublicBuckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessBlockConfiguration = PublicAccessBlockConfiguration


@dataclass
class PolicyStatus(BaseModel):
    IsPublic: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyStatus"]:
        if not json_data:
            return None
        return cls(
            IsPublic=json_data.get("IsPublic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyStatus = PolicyStatus


@dataclass
class ObjectLambdaConfiguration(BaseModel):
    SupportingAccessPoint: Optional[str]
    AllowedFeatures: Optional[AbstractSet[str]]
    CloudWatchMetricsEnabled: Optional[bool]
    TransformationConfigurations: Optional[AbstractSet["_TransformationConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLambdaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLambdaConfiguration"]:
        if not json_data:
            return None
        return cls(
            SupportingAccessPoint=json_data.get("SupportingAccessPoint"),
            AllowedFeatures=set_or_none(json_data.get("AllowedFeatures")),
            CloudWatchMetricsEnabled=json_data.get("CloudWatchMetricsEnabled"),
            TransformationConfigurations=set_or_none(json_data.get("TransformationConfigurations")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLambdaConfiguration = ObjectLambdaConfiguration


@dataclass
class TransformationConfiguration(BaseModel):
    Actions: Optional[AbstractSet[str]]
    ContentTransformation: Optional["_ContentTransformation"]

    @classmethod
    def _deserialize(
        cls: Type["_TransformationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Actions=set_or_none(json_data.get("Actions")),
            ContentTransformation=ContentTransformation._deserialize(json_data.get("ContentTransformation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformationConfiguration = TransformationConfiguration


@dataclass
class ContentTransformation(BaseModel):
    AwsLambda: Optional["_AwsLambda"]

    @classmethod
    def _deserialize(
        cls: Type["_ContentTransformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentTransformation"]:
        if not json_data:
            return None
        return cls(
            AwsLambda=AwsLambda._deserialize(json_data.get("AwsLambda")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentTransformation = ContentTransformation


@dataclass
class AwsLambda(BaseModel):
    FunctionArn: Optional[str]
    FunctionPayload: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambda"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            FunctionPayload=json_data.get("FunctionPayload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambda = AwsLambda


