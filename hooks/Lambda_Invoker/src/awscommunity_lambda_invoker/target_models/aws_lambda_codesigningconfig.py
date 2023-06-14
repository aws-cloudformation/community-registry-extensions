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
class AwsLambdaCodesigningconfig(BaseModel):
    Description: Optional[str]
    AllowedPublishers: Optional["_AllowedPublishers"]
    CodeSigningPolicies: Optional["_CodeSigningPolicies"]
    CodeSigningConfigId: Optional[str]
    CodeSigningConfigArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaCodesigningconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaCodesigningconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            AllowedPublishers=AllowedPublishers._deserialize(json_data.get("AllowedPublishers")),
            CodeSigningPolicies=CodeSigningPolicies._deserialize(json_data.get("CodeSigningPolicies")),
            CodeSigningConfigId=json_data.get("CodeSigningConfigId"),
            CodeSigningConfigArn=json_data.get("CodeSigningConfigArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaCodesigningconfig = AwsLambdaCodesigningconfig


@dataclass
class AllowedPublishers(BaseModel):
    SigningProfileVersionArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedPublishers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedPublishers"]:
        if not json_data:
            return None
        return cls(
            SigningProfileVersionArns=json_data.get("SigningProfileVersionArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedPublishers = AllowedPublishers


@dataclass
class CodeSigningPolicies(BaseModel):
    UntrustedArtifactOnDeployment: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeSigningPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeSigningPolicies"]:
        if not json_data:
            return None
        return cls(
            UntrustedArtifactOnDeployment=json_data.get("UntrustedArtifactOnDeployment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeSigningPolicies = CodeSigningPolicies


