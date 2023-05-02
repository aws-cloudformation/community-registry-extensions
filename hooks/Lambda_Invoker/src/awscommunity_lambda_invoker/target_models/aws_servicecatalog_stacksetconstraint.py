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
class AwsServicecatalogStacksetconstraint(BaseModel):
    Id: Optional[str]
    Description: Optional[str]
    StackInstanceControl: Optional[str]
    AcceptLanguage: Optional[str]
    PortfolioId: Optional[str]
    ProductId: Optional[str]
    RegionList: Optional[Sequence[str]]
    AdminRole: Optional[str]
    AccountList: Optional[Sequence[str]]
    ExecutionRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicecatalogStacksetconstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicecatalogStacksetconstraint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Description=json_data.get("Description"),
            StackInstanceControl=json_data.get("StackInstanceControl"),
            AcceptLanguage=json_data.get("AcceptLanguage"),
            PortfolioId=json_data.get("PortfolioId"),
            ProductId=json_data.get("ProductId"),
            RegionList=json_data.get("RegionList"),
            AdminRole=json_data.get("AdminRole"),
            AccountList=json_data.get("AccountList"),
            ExecutionRole=json_data.get("ExecutionRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicecatalogStacksetconstraint = AwsServicecatalogStacksetconstraint


