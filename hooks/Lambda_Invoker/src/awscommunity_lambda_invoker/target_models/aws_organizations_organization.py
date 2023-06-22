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
class AwsOrganizationsOrganization(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    FeatureSet: Optional[str]
    ManagementAccountArn: Optional[str]
    ManagementAccountId: Optional[str]
    ManagementAccountEmail: Optional[str]
    RootId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOrganizationsOrganization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOrganizationsOrganization"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            FeatureSet=json_data.get("FeatureSet"),
            ManagementAccountArn=json_data.get("ManagementAccountArn"),
            ManagementAccountId=json_data.get("ManagementAccountId"),
            ManagementAccountEmail=json_data.get("ManagementAccountEmail"),
            RootId=json_data.get("RootId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOrganizationsOrganization = AwsOrganizationsOrganization


