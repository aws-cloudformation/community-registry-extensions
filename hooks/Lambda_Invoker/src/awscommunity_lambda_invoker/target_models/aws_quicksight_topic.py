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
class AwsQuicksightTopic(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    DataSets: Optional[Sequence["_DatasetMetadata"]]
    Description: Optional[str]
    Name: Optional[str]
    TopicId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightTopic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightTopic"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            DataSets=deserialize_list(json_data.get("DataSets"), DatasetMetadata),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            TopicId=json_data.get("TopicId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightTopic = AwsQuicksightTopic


@dataclass
class DatasetMetadata(BaseModel):
    DatasetArn: Optional[str]
    DatasetName: Optional[str]
    DatasetDescription: Optional[str]
    DataAggregation: Optional["_DataAggregation"]
    Filters: Optional[Sequence["_TopicFilter"]]
    Columns: Optional[Sequence["_TopicColumn"]]
    CalculatedFields: Optional[Sequence["_TopicCalculatedField"]]
    NamedEntities: Optional[Sequence["_TopicNamedEntity"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetMetadata"]:
        if not json_data:
            return None
        return cls(
            DatasetArn=json_data.get("DatasetArn"),
            DatasetName=json_data.get("DatasetName"),
            DatasetDescription=json_data.get("DatasetDescription"),
            DataAggregation=DataAggregation._deserialize(json_data.get("DataAggregation")),
            Filters=deserialize_list(json_data.get("Filters"), TopicFilter),
            Columns=deserialize_list(json_data.get("Columns"), TopicColumn),
            CalculatedFields=deserialize_list(json_data.get("CalculatedFields"), TopicCalculatedField),
            NamedEntities=deserialize_list(json_data.get("NamedEntities"), TopicNamedEntity),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetMetadata = DatasetMetadata


@dataclass
class DataAggregation(BaseModel):
    DatasetRowDateGranularity: Optional[str]
    DefaultDateColumnName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataAggregation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataAggregation"]:
        if not json_data:
            return None
        return cls(
            DatasetRowDateGranularity=json_data.get("DatasetRowDateGranularity"),
            DefaultDateColumnName=json_data.get("DefaultDateColumnName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataAggregation = DataAggregation


@dataclass
class TopicFilter(BaseModel):
    FilterDescription: Optional[str]
    FilterClass: Optional[str]
    FilterName: Optional[str]
    FilterSynonyms: Optional[Sequence[str]]
    OperandFieldName: Optional[str]
    FilterType: Optional[str]
    CategoryFilter: Optional["_TopicCategoryFilter"]
    NumericEqualityFilter: Optional["_TopicNumericEqualityFilter"]
    NumericRangeFilter: Optional["_TopicNumericRangeFilter"]
    DateRangeFilter: Optional["_TopicDateRangeFilter"]
    RelativeDateFilter: Optional["_TopicRelativeDateFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_TopicFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicFilter"]:
        if not json_data:
            return None
        return cls(
            FilterDescription=json_data.get("FilterDescription"),
            FilterClass=json_data.get("FilterClass"),
            FilterName=json_data.get("FilterName"),
            FilterSynonyms=json_data.get("FilterSynonyms"),
            OperandFieldName=json_data.get("OperandFieldName"),
            FilterType=json_data.get("FilterType"),
            CategoryFilter=TopicCategoryFilter._deserialize(json_data.get("CategoryFilter")),
            NumericEqualityFilter=TopicNumericEqualityFilter._deserialize(json_data.get("NumericEqualityFilter")),
            NumericRangeFilter=TopicNumericRangeFilter._deserialize(json_data.get("NumericRangeFilter")),
            DateRangeFilter=TopicDateRangeFilter._deserialize(json_data.get("DateRangeFilter")),
            RelativeDateFilter=TopicRelativeDateFilter._deserialize(json_data.get("RelativeDateFilter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicFilter = TopicFilter


@dataclass
class TopicCategoryFilter(BaseModel):
    CategoryFilterFunction: Optional[str]
    CategoryFilterType: Optional[str]
    Constant: Optional["_TopicCategoryFilterConstant"]
    Inverse: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TopicCategoryFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicCategoryFilter"]:
        if not json_data:
            return None
        return cls(
            CategoryFilterFunction=json_data.get("CategoryFilterFunction"),
            CategoryFilterType=json_data.get("CategoryFilterType"),
            Constant=TopicCategoryFilterConstant._deserialize(json_data.get("Constant")),
            Inverse=json_data.get("Inverse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicCategoryFilter = TopicCategoryFilter


@dataclass
class TopicCategoryFilterConstant(BaseModel):
    ConstantType: Optional[str]
    SingularConstant: Optional[str]
    CollectiveConstant: Optional["_CollectiveConstant"]

    @classmethod
    def _deserialize(
        cls: Type["_TopicCategoryFilterConstant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicCategoryFilterConstant"]:
        if not json_data:
            return None
        return cls(
            ConstantType=json_data.get("ConstantType"),
            SingularConstant=json_data.get("SingularConstant"),
            CollectiveConstant=CollectiveConstant._deserialize(json_data.get("CollectiveConstant")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicCategoryFilterConstant = TopicCategoryFilterConstant


@dataclass
class CollectiveConstant(BaseModel):
    ValueList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CollectiveConstant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CollectiveConstant"]:
        if not json_data:
            return None
        return cls(
            ValueList=json_data.get("ValueList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CollectiveConstant = CollectiveConstant


@dataclass
class TopicNumericEqualityFilter(BaseModel):
    Constant: Optional["_TopicSingularFilterConstant"]
    Aggregation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicNumericEqualityFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicNumericEqualityFilter"]:
        if not json_data:
            return None
        return cls(
            Constant=TopicSingularFilterConstant._deserialize(json_data.get("Constant")),
            Aggregation=json_data.get("Aggregation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicNumericEqualityFilter = TopicNumericEqualityFilter


@dataclass
class TopicSingularFilterConstant(BaseModel):
    ConstantType: Optional[str]
    SingularConstant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicSingularFilterConstant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicSingularFilterConstant"]:
        if not json_data:
            return None
        return cls(
            ConstantType=json_data.get("ConstantType"),
            SingularConstant=json_data.get("SingularConstant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicSingularFilterConstant = TopicSingularFilterConstant


@dataclass
class TopicNumericRangeFilter(BaseModel):
    Inclusive: Optional[bool]
    Constant: Optional["_TopicRangeFilterConstant"]
    Aggregation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicNumericRangeFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicNumericRangeFilter"]:
        if not json_data:
            return None
        return cls(
            Inclusive=json_data.get("Inclusive"),
            Constant=TopicRangeFilterConstant._deserialize(json_data.get("Constant")),
            Aggregation=json_data.get("Aggregation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicNumericRangeFilter = TopicNumericRangeFilter


@dataclass
class TopicRangeFilterConstant(BaseModel):
    ConstantType: Optional[str]
    RangeConstant: Optional["_RangeConstant"]

    @classmethod
    def _deserialize(
        cls: Type["_TopicRangeFilterConstant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicRangeFilterConstant"]:
        if not json_data:
            return None
        return cls(
            ConstantType=json_data.get("ConstantType"),
            RangeConstant=RangeConstant._deserialize(json_data.get("RangeConstant")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicRangeFilterConstant = TopicRangeFilterConstant


@dataclass
class RangeConstant(BaseModel):
    Minimum: Optional[str]
    Maximum: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeConstant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeConstant"]:
        if not json_data:
            return None
        return cls(
            Minimum=json_data.get("Minimum"),
            Maximum=json_data.get("Maximum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeConstant = RangeConstant


@dataclass
class TopicDateRangeFilter(BaseModel):
    Inclusive: Optional[bool]
    Constant: Optional["_TopicRangeFilterConstant"]

    @classmethod
    def _deserialize(
        cls: Type["_TopicDateRangeFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicDateRangeFilter"]:
        if not json_data:
            return None
        return cls(
            Inclusive=json_data.get("Inclusive"),
            Constant=TopicRangeFilterConstant._deserialize(json_data.get("Constant")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicDateRangeFilter = TopicDateRangeFilter


@dataclass
class TopicRelativeDateFilter(BaseModel):
    TimeGranularity: Optional[str]
    RelativeDateFilterFunction: Optional[str]
    Constant: Optional["_TopicSingularFilterConstant"]

    @classmethod
    def _deserialize(
        cls: Type["_TopicRelativeDateFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicRelativeDateFilter"]:
        if not json_data:
            return None
        return cls(
            TimeGranularity=json_data.get("TimeGranularity"),
            RelativeDateFilterFunction=json_data.get("RelativeDateFilterFunction"),
            Constant=TopicSingularFilterConstant._deserialize(json_data.get("Constant")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicRelativeDateFilter = TopicRelativeDateFilter


@dataclass
class TopicColumn(BaseModel):
    ColumnName: Optional[str]
    ColumnFriendlyName: Optional[str]
    ColumnDescription: Optional[str]
    ColumnSynonyms: Optional[Sequence[str]]
    ColumnDataRole: Optional[str]
    Aggregation: Optional[str]
    IsIncludedInTopic: Optional[bool]
    ComparativeOrder: Optional["_ComparativeOrder"]
    SemanticType: Optional["_SemanticType"]
    TimeGranularity: Optional[str]
    AllowedAggregations: Optional[Sequence[str]]
    NotAllowedAggregations: Optional[Sequence[str]]
    DefaultFormatting: Optional["_DefaultFormatting"]
    NeverAggregateInFilter: Optional[bool]
    CellValueSynonyms: Optional[Sequence["_CellValueSynonym"]]

    @classmethod
    def _deserialize(
        cls: Type["_TopicColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicColumn"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            ColumnFriendlyName=json_data.get("ColumnFriendlyName"),
            ColumnDescription=json_data.get("ColumnDescription"),
            ColumnSynonyms=json_data.get("ColumnSynonyms"),
            ColumnDataRole=json_data.get("ColumnDataRole"),
            Aggregation=json_data.get("Aggregation"),
            IsIncludedInTopic=json_data.get("IsIncludedInTopic"),
            ComparativeOrder=ComparativeOrder._deserialize(json_data.get("ComparativeOrder")),
            SemanticType=SemanticType._deserialize(json_data.get("SemanticType")),
            TimeGranularity=json_data.get("TimeGranularity"),
            AllowedAggregations=json_data.get("AllowedAggregations"),
            NotAllowedAggregations=json_data.get("NotAllowedAggregations"),
            DefaultFormatting=DefaultFormatting._deserialize(json_data.get("DefaultFormatting")),
            NeverAggregateInFilter=json_data.get("NeverAggregateInFilter"),
            CellValueSynonyms=deserialize_list(json_data.get("CellValueSynonyms"), CellValueSynonym),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicColumn = TopicColumn


@dataclass
class ComparativeOrder(BaseModel):
    UseOrdering: Optional[str]
    SpecifedOrder: Optional[Sequence[str]]
    TreatUndefinedSpecifiedValues: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComparativeOrder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComparativeOrder"]:
        if not json_data:
            return None
        return cls(
            UseOrdering=json_data.get("UseOrdering"),
            SpecifedOrder=json_data.get("SpecifedOrder"),
            TreatUndefinedSpecifiedValues=json_data.get("TreatUndefinedSpecifiedValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComparativeOrder = ComparativeOrder


@dataclass
class SemanticType(BaseModel):
    TypeName: Optional[str]
    SubTypeName: Optional[str]
    TypeParameters: Optional[MutableMapping[str, str]]
    TruthyCellValue: Optional[str]
    TruthyCellValueSynonyms: Optional[Sequence[str]]
    FalseyCellValue: Optional[str]
    FalseyCellValueSynonyms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SemanticType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SemanticType"]:
        if not json_data:
            return None
        return cls(
            TypeName=json_data.get("TypeName"),
            SubTypeName=json_data.get("SubTypeName"),
            TypeParameters=json_data.get("TypeParameters"),
            TruthyCellValue=json_data.get("TruthyCellValue"),
            TruthyCellValueSynonyms=json_data.get("TruthyCellValueSynonyms"),
            FalseyCellValue=json_data.get("FalseyCellValue"),
            FalseyCellValueSynonyms=json_data.get("FalseyCellValueSynonyms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SemanticType = SemanticType


@dataclass
class DefaultFormatting(BaseModel):
    DisplayFormat: Optional[str]
    DisplayFormatOptions: Optional["_DisplayFormatOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultFormatting"]:
        if not json_data:
            return None
        return cls(
            DisplayFormat=json_data.get("DisplayFormat"),
            DisplayFormatOptions=DisplayFormatOptions._deserialize(json_data.get("DisplayFormatOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultFormatting = DefaultFormatting


@dataclass
class DisplayFormatOptions(BaseModel):
    UseBlankCellFormat: Optional[bool]
    BlankCellFormat: Optional[str]
    DateFormat: Optional[str]
    DecimalSeparator: Optional[str]
    GroupingSeparator: Optional[str]
    UseGrouping: Optional[bool]
    FractionDigits: Optional[float]
    Prefix: Optional[str]
    Suffix: Optional[str]
    UnitScaler: Optional[str]
    NegativeFormat: Optional["_NegativeFormat"]
    CurrencySymbol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DisplayFormatOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisplayFormatOptions"]:
        if not json_data:
            return None
        return cls(
            UseBlankCellFormat=json_data.get("UseBlankCellFormat"),
            BlankCellFormat=json_data.get("BlankCellFormat"),
            DateFormat=json_data.get("DateFormat"),
            DecimalSeparator=json_data.get("DecimalSeparator"),
            GroupingSeparator=json_data.get("GroupingSeparator"),
            UseGrouping=json_data.get("UseGrouping"),
            FractionDigits=json_data.get("FractionDigits"),
            Prefix=json_data.get("Prefix"),
            Suffix=json_data.get("Suffix"),
            UnitScaler=json_data.get("UnitScaler"),
            NegativeFormat=NegativeFormat._deserialize(json_data.get("NegativeFormat")),
            CurrencySymbol=json_data.get("CurrencySymbol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisplayFormatOptions = DisplayFormatOptions


@dataclass
class NegativeFormat(BaseModel):
    Prefix: Optional[str]
    Suffix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NegativeFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NegativeFormat"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Suffix=json_data.get("Suffix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NegativeFormat = NegativeFormat


@dataclass
class CellValueSynonym(BaseModel):
    CellValue: Optional[str]
    Synonyms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CellValueSynonym"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CellValueSynonym"]:
        if not json_data:
            return None
        return cls(
            CellValue=json_data.get("CellValue"),
            Synonyms=json_data.get("Synonyms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CellValueSynonym = CellValueSynonym


@dataclass
class TopicCalculatedField(BaseModel):
    CalculatedFieldName: Optional[str]
    CalculatedFieldDescription: Optional[str]
    Expression: Optional[str]
    CalculatedFieldSynonyms: Optional[Sequence[str]]
    IsIncludedInTopic: Optional[bool]
    ColumnDataRole: Optional[str]
    TimeGranularity: Optional[str]
    DefaultFormatting: Optional["_DefaultFormatting"]
    Aggregation: Optional[str]
    ComparativeOrder: Optional["_ComparativeOrder"]
    SemanticType: Optional["_SemanticType"]
    AllowedAggregations: Optional[Sequence[str]]
    NotAllowedAggregations: Optional[Sequence[str]]
    NeverAggregateInFilter: Optional[bool]
    CellValueSynonyms: Optional[Sequence["_CellValueSynonym"]]

    @classmethod
    def _deserialize(
        cls: Type["_TopicCalculatedField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicCalculatedField"]:
        if not json_data:
            return None
        return cls(
            CalculatedFieldName=json_data.get("CalculatedFieldName"),
            CalculatedFieldDescription=json_data.get("CalculatedFieldDescription"),
            Expression=json_data.get("Expression"),
            CalculatedFieldSynonyms=json_data.get("CalculatedFieldSynonyms"),
            IsIncludedInTopic=json_data.get("IsIncludedInTopic"),
            ColumnDataRole=json_data.get("ColumnDataRole"),
            TimeGranularity=json_data.get("TimeGranularity"),
            DefaultFormatting=DefaultFormatting._deserialize(json_data.get("DefaultFormatting")),
            Aggregation=json_data.get("Aggregation"),
            ComparativeOrder=ComparativeOrder._deserialize(json_data.get("ComparativeOrder")),
            SemanticType=SemanticType._deserialize(json_data.get("SemanticType")),
            AllowedAggregations=json_data.get("AllowedAggregations"),
            NotAllowedAggregations=json_data.get("NotAllowedAggregations"),
            NeverAggregateInFilter=json_data.get("NeverAggregateInFilter"),
            CellValueSynonyms=deserialize_list(json_data.get("CellValueSynonyms"), CellValueSynonym),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicCalculatedField = TopicCalculatedField


@dataclass
class TopicNamedEntity(BaseModel):
    EntityName: Optional[str]
    EntityDescription: Optional[str]
    EntitySynonyms: Optional[Sequence[str]]
    SemanticEntityType: Optional["_SemanticEntityType"]
    Definition: Optional[Sequence["_NamedEntityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TopicNamedEntity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicNamedEntity"]:
        if not json_data:
            return None
        return cls(
            EntityName=json_data.get("EntityName"),
            EntityDescription=json_data.get("EntityDescription"),
            EntitySynonyms=json_data.get("EntitySynonyms"),
            SemanticEntityType=SemanticEntityType._deserialize(json_data.get("SemanticEntityType")),
            Definition=deserialize_list(json_data.get("Definition"), NamedEntityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicNamedEntity = TopicNamedEntity


@dataclass
class SemanticEntityType(BaseModel):
    TypeName: Optional[str]
    SubTypeName: Optional[str]
    TypeParameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_SemanticEntityType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SemanticEntityType"]:
        if not json_data:
            return None
        return cls(
            TypeName=json_data.get("TypeName"),
            SubTypeName=json_data.get("SubTypeName"),
            TypeParameters=json_data.get("TypeParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SemanticEntityType = SemanticEntityType


@dataclass
class NamedEntityDefinition(BaseModel):
    FieldName: Optional[str]
    PropertyName: Optional[str]
    PropertyRole: Optional[str]
    PropertyUsage: Optional[str]
    Metric: Optional["_NamedEntityDefinitionMetric"]

    @classmethod
    def _deserialize(
        cls: Type["_NamedEntityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedEntityDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldName=json_data.get("FieldName"),
            PropertyName=json_data.get("PropertyName"),
            PropertyRole=json_data.get("PropertyRole"),
            PropertyUsage=json_data.get("PropertyUsage"),
            Metric=NamedEntityDefinitionMetric._deserialize(json_data.get("Metric")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedEntityDefinition = NamedEntityDefinition


@dataclass
class NamedEntityDefinitionMetric(BaseModel):
    Aggregation: Optional[str]
    AggregationFunctionParameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_NamedEntityDefinitionMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedEntityDefinitionMetric"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            AggregationFunctionParameters=json_data.get("AggregationFunctionParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedEntityDefinitionMetric = NamedEntityDefinitionMetric


