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
class AwsLicensemanagerGrant(BaseModel):
    GrantArn: Optional[str]
    GrantName: Optional[str]
    LicenseArn: Optional[str]
    HomeRegion: Optional[str]
    Version: Optional[str]
    AllowedOperations: Optional[Sequence[str]]
    Principals: Optional[Sequence[str]]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLicensemanagerGrant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLicensemanagerGrant"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GrantArn=json_data.get("GrantArn"),
            GrantName=json_data.get("GrantName"),
            LicenseArn=json_data.get("LicenseArn"),
            HomeRegion=json_data.get("HomeRegion"),
            Version=json_data.get("Version"),
            AllowedOperations=json_data.get("AllowedOperations"),
            Principals=json_data.get("Principals"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLicensemanagerGrant = AwsLicensemanagerGrant


