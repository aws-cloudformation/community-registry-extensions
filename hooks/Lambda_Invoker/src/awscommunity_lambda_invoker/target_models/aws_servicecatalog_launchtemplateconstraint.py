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
class AwsServicecatalogLaunchtemplateconstraint(BaseModel):
    Id: Optional[str]
    Description: Optional[str]
    AcceptLanguage: Optional[str]
    PortfolioId: Optional[str]
    ProductId: Optional[str]
    Rules: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicecatalogLaunchtemplateconstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicecatalogLaunchtemplateconstraint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Description=json_data.get("Description"),
            AcceptLanguage=json_data.get("AcceptLanguage"),
            PortfolioId=json_data.get("PortfolioId"),
            ProductId=json_data.get("ProductId"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicecatalogLaunchtemplateconstraint = AwsServicecatalogLaunchtemplateconstraint


