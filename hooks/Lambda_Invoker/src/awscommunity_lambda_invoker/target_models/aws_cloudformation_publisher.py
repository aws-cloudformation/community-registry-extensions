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
class AwsCloudformationPublisher(BaseModel):
    AcceptTermsAndConditions: Optional[bool]
    PublisherId: Optional[str]
    ConnectionArn: Optional[str]
    PublisherStatus: Optional[str]
    PublisherProfile: Optional[str]
    IdentityProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationPublisher"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationPublisher"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AcceptTermsAndConditions=json_data.get("AcceptTermsAndConditions"),
            PublisherId=json_data.get("PublisherId"),
            ConnectionArn=json_data.get("ConnectionArn"),
            PublisherStatus=json_data.get("PublisherStatus"),
            PublisherProfile=json_data.get("PublisherProfile"),
            IdentityProvider=json_data.get("IdentityProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationPublisher = AwsCloudformationPublisher


