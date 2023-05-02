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
class AwsPanoramaPackageversion(BaseModel):
    OwnerAccount: Optional[str]
    PackageId: Optional[str]
    PackageArn: Optional[str]
    PackageVersion: Optional[str]
    PatchVersion: Optional[str]
    MarkLatest: Optional[bool]
    IsLatestPatch: Optional[bool]
    PackageName: Optional[str]
    Status: Optional[str]
    StatusDescription: Optional[str]
    RegisteredTime: Optional[int]
    UpdatedLatestPatchVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPanoramaPackageversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPanoramaPackageversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OwnerAccount=json_data.get("OwnerAccount"),
            PackageId=json_data.get("PackageId"),
            PackageArn=json_data.get("PackageArn"),
            PackageVersion=json_data.get("PackageVersion"),
            PatchVersion=json_data.get("PatchVersion"),
            MarkLatest=json_data.get("MarkLatest"),
            IsLatestPatch=json_data.get("IsLatestPatch"),
            PackageName=json_data.get("PackageName"),
            Status=json_data.get("Status"),
            StatusDescription=json_data.get("StatusDescription"),
            RegisteredTime=json_data.get("RegisteredTime"),
            UpdatedLatestPatchVersion=json_data.get("UpdatedLatestPatchVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPanoramaPackageversion = AwsPanoramaPackageversion


