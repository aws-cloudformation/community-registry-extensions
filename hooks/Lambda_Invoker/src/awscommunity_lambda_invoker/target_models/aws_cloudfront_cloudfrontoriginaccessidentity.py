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
class AwsCloudfrontCloudfrontoriginaccessidentity(BaseModel):
    CloudFrontOriginAccessIdentityConfig: Optional["_CloudFrontOriginAccessIdentityConfig"]
    Id: Optional[str]
    S3CanonicalUserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontCloudfrontoriginaccessidentity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontCloudfrontoriginaccessidentity"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig._deserialize(json_data.get("CloudFrontOriginAccessIdentityConfig")),
            Id=json_data.get("Id"),
            S3CanonicalUserId=json_data.get("S3CanonicalUserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontCloudfrontoriginaccessidentity = AwsCloudfrontCloudfrontoriginaccessidentity


@dataclass
class CloudFrontOriginAccessIdentityConfig(BaseModel):
    Comment: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudFrontOriginAccessIdentityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudFrontOriginAccessIdentityConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudFrontOriginAccessIdentityConfig = CloudFrontOriginAccessIdentityConfig


