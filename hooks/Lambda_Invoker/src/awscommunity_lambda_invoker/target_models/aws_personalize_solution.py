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
class AwsPersonalizeSolution(BaseModel):
    Name: Optional[str]
    SolutionArn: Optional[str]
    EventType: Optional[str]
    DatasetGroupArn: Optional[str]
    PerformAutoML: Optional[bool]
    PerformHPO: Optional[bool]
    RecipeArn: Optional[str]
    SolutionConfig: Optional["_SolutionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPersonalizeSolution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPersonalizeSolution"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            SolutionArn=json_data.get("SolutionArn"),
            EventType=json_data.get("EventType"),
            DatasetGroupArn=json_data.get("DatasetGroupArn"),
            PerformAutoML=json_data.get("PerformAutoML"),
            PerformHPO=json_data.get("PerformHPO"),
            RecipeArn=json_data.get("RecipeArn"),
            SolutionConfig=SolutionConfig._deserialize(json_data.get("SolutionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPersonalizeSolution = AwsPersonalizeSolution


@dataclass
class SolutionConfig(BaseModel):
    AlgorithmHyperParameters: Optional[MutableMapping[str, str]]
    AutoMLConfig: Optional["_AutoMLConfig"]
    EventValueThreshold: Optional[str]
    FeatureTransformationParameters: Optional[MutableMapping[str, str]]
    HpoConfig: Optional["_HpoConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_SolutionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SolutionConfig"]:
        if not json_data:
            return None
        return cls(
            AlgorithmHyperParameters=json_data.get("AlgorithmHyperParameters"),
            AutoMLConfig=AutoMLConfig._deserialize(json_data.get("AutoMLConfig")),
            EventValueThreshold=json_data.get("EventValueThreshold"),
            FeatureTransformationParameters=json_data.get("FeatureTransformationParameters"),
            HpoConfig=HpoConfig._deserialize(json_data.get("HpoConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SolutionConfig = SolutionConfig


@dataclass
class AutoMLConfig(BaseModel):
    MetricName: Optional[str]
    RecipeList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoMLConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoMLConfig"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            RecipeList=json_data.get("RecipeList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoMLConfig = AutoMLConfig


@dataclass
class HpoConfig(BaseModel):
    AlgorithmHyperParameterRanges: Optional["_AlgorithmHyperParameterRanges"]
    HpoObjective: Optional["_HpoObjective"]
    HpoResourceConfig: Optional["_HpoResourceConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_HpoConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HpoConfig"]:
        if not json_data:
            return None
        return cls(
            AlgorithmHyperParameterRanges=AlgorithmHyperParameterRanges._deserialize(json_data.get("AlgorithmHyperParameterRanges")),
            HpoObjective=HpoObjective._deserialize(json_data.get("HpoObjective")),
            HpoResourceConfig=HpoResourceConfig._deserialize(json_data.get("HpoResourceConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HpoConfig = HpoConfig


@dataclass
class AlgorithmHyperParameterRanges(BaseModel):
    CategoricalHyperParameterRanges: Optional[Sequence["_CategoricalHyperParameterRange"]]
    ContinuousHyperParameterRanges: Optional[Sequence["_ContinuousHyperParameterRange"]]
    IntegerHyperParameterRanges: Optional[Sequence["_IntegerHyperParameterRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlgorithmHyperParameterRanges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlgorithmHyperParameterRanges"]:
        if not json_data:
            return None
        return cls(
            CategoricalHyperParameterRanges=deserialize_list(json_data.get("CategoricalHyperParameterRanges"), CategoricalHyperParameterRange),
            ContinuousHyperParameterRanges=deserialize_list(json_data.get("ContinuousHyperParameterRanges"), ContinuousHyperParameterRange),
            IntegerHyperParameterRanges=deserialize_list(json_data.get("IntegerHyperParameterRanges"), IntegerHyperParameterRange),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlgorithmHyperParameterRanges = AlgorithmHyperParameterRanges


@dataclass
class CategoricalHyperParameterRange(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoricalHyperParameterRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoricalHyperParameterRange"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoricalHyperParameterRange = CategoricalHyperParameterRange


@dataclass
class ContinuousHyperParameterRange(BaseModel):
    Name: Optional[str]
    MinValue: Optional[float]
    MaxValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ContinuousHyperParameterRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContinuousHyperParameterRange"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContinuousHyperParameterRange = ContinuousHyperParameterRange


@dataclass
class IntegerHyperParameterRange(BaseModel):
    Name: Optional[str]
    MinValue: Optional[int]
    MaxValue: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerHyperParameterRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerHyperParameterRange"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerHyperParameterRange = IntegerHyperParameterRange


@dataclass
class HpoObjective(BaseModel):
    MetricName: Optional[str]
    Type: Optional[str]
    MetricRegex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HpoObjective"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HpoObjective"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Type=json_data.get("Type"),
            MetricRegex=json_data.get("MetricRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HpoObjective = HpoObjective


@dataclass
class HpoResourceConfig(BaseModel):
    MaxNumberOfTrainingJobs: Optional[str]
    MaxParallelTrainingJobs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HpoResourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HpoResourceConfig"]:
        if not json_data:
            return None
        return cls(
            MaxNumberOfTrainingJobs=json_data.get("MaxNumberOfTrainingJobs"),
            MaxParallelTrainingJobs=json_data.get("MaxParallelTrainingJobs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HpoResourceConfig = HpoResourceConfig


