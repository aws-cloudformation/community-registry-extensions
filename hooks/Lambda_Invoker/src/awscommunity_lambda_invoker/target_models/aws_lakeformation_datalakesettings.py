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
class AwsLakeformationDatalakesettings(BaseModel):
    AllowExternalDataFiltering: Optional[bool]
    ExternalDataFilteringAllowList: Optional[MutableMapping[str, Any]]
    CreateTableDefaultPermissions: Optional[MutableMapping[str, Any]]
    Parameters: Optional[MutableMapping[str, Any]]
    Admins: Optional[MutableMapping[str, Any]]
    CreateDatabaseDefaultPermissions: Optional[MutableMapping[str, Any]]
    Id: Optional[str]
    AuthorizedSessionTagValueList: Optional[Sequence[str]]
    TrustedResourceOwners: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLakeformationDatalakesettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLakeformationDatalakesettings"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AllowExternalDataFiltering=json_data.get("AllowExternalDataFiltering"),
            ExternalDataFilteringAllowList=json_data.get("ExternalDataFilteringAllowList"),
            CreateTableDefaultPermissions=json_data.get("CreateTableDefaultPermissions"),
            Parameters=json_data.get("Parameters"),
            Admins=json_data.get("Admins"),
            CreateDatabaseDefaultPermissions=json_data.get("CreateDatabaseDefaultPermissions"),
            Id=json_data.get("Id"),
            AuthorizedSessionTagValueList=json_data.get("AuthorizedSessionTagValueList"),
            TrustedResourceOwners=json_data.get("TrustedResourceOwners"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLakeformationDatalakesettings = AwsLakeformationDatalakesettings


