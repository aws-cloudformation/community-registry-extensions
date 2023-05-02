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
class AwsCodestarGithubrepository(BaseModel):
    EnableIssues: Optional[bool]
    ConnectionArn: Optional[str]
    RepositoryName: Optional[str]
    RepositoryAccessToken: Optional[str]
    Id: Optional[str]
    RepositoryOwner: Optional[str]
    IsPrivate: Optional[bool]
    Code: Optional["_Code"]
    RepositoryDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodestarGithubrepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodestarGithubrepository"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EnableIssues=json_data.get("EnableIssues"),
            ConnectionArn=json_data.get("ConnectionArn"),
            RepositoryName=json_data.get("RepositoryName"),
            RepositoryAccessToken=json_data.get("RepositoryAccessToken"),
            Id=json_data.get("Id"),
            RepositoryOwner=json_data.get("RepositoryOwner"),
            IsPrivate=json_data.get("IsPrivate"),
            Code=Code._deserialize(json_data.get("Code")),
            RepositoryDescription=json_data.get("RepositoryDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodestarGithubrepository = AwsCodestarGithubrepository


@dataclass
class Code(BaseModel):
    S3: Optional["_S3"]

    @classmethod
    def _deserialize(
        cls: Type["_Code"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Code"]:
        if not json_data:
            return None
        return cls(
            S3=S3._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Code = Code


@dataclass
class S3(BaseModel):
    ObjectVersion: Optional[str]
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            ObjectVersion=json_data.get("ObjectVersion"),
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


