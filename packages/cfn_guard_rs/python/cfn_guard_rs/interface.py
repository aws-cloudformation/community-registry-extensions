"""
  Defines the non-verbose output format returned
  from run_checks
"""
from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Any, List, Dict, Sequence, Tuple

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name
class ValueComparisons(abc.ABC):
    @property
    @abc.abstractmethod
    def value_from(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def value_to(self) -> Any:
        pass


@dataclass(eq=True, frozen=True)
class Messages:
    """Messages Output"""

    custom_message: str | None = field(default=None)
    error_message: str | None = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "Messages" | None:
        if obj is None:
            return None

        return cls(
            custom_message=obj.get("custom_message"),
            error_message=obj.get("error_message"),
        )

    def __repr__(self) -> str:
        if self.custom_message:
            return self.custom_message
        if self.error_message:
            return self.error_message
        return ""


@dataclass(eq=True, frozen=True)
class RuleReport:
    """Messages Output"""

    name: str = field()
    metadata: Dict[str, Any] = field()
    messages: Messages = field()
    checks: Sequence[ClauseReport] = field()

    @classmethod
    def from_object(cls, obj) -> "RuleReport" | None:
        if obj is None:
            return None

        return cls(
            name=obj.get("name"),
            metadata=obj.get("metadata"),
            messages=Messages.from_object(obj.get("messages")),
            checks=ClauseReport.from_array(obj.get("checks")),
        )


@dataclass(eq=True, frozen=True)
class GuardBlockReport(ValueComparisons):
    """Guard Block Report"""

    context: str = field()
    messages: Messages = field()
    unresolved: Any = field()

    @classmethod
    def from_object(cls, obj) -> "GuardBlockReport" | None:
        if obj is None:
            return obj

        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            unresolved=obj.get("resolved"),
        )

    @property
    def value_from(self) -> Any:
        return None

    @property
    def value_to(self) -> Any:
        return None


@dataclass(eq=True, frozen=True)
class DisjunctionsReport:
    """Disjunctions"""

    checks: ClauseReport = field()

    @classmethod
    def from_object(cls, obj) -> "DisjunctionsReport" | None:
        if obj is None:
            return obj

        return cls(checks=ClauseReport.from_object(obj.get("checks")))


@dataclass(eq=True, frozen=True)
class UnaryComparison:
    """Unary Comparison"""

    value: Any = field()
    comparison: Tuple[str, bool] = field()

    @classmethod
    def from_object(cls, obj) -> "UnaryComparison" | None:
        if obj is None:
            return None

        return cls(
            value=obj.get("value"),
            comparison=tuple(obj.get("comparison")),
        )


@dataclass(eq=True, frozen=True)
class UnResolved:
    """Unresolved"""

    traversed_to: Any = field()
    remaining_query: Any = field()
    reason: Any = field()

    @classmethod
    def from_object(cls, obj) -> "UnResolved" | None:
        if obj is None:
            return None
        return cls(
            traversed_to=obj.get("traversed_to"),
            remaining_query=obj.get("remaining_query"),
            reason=obj.get("reason"),
        )


@dataclass(eq=True, frozen=True)
class ValueUnResolved:
    value: Any = field()
    comparison: Any = field()

    @classmethod
    def from_object(cls, obj) -> "ValueUnResolved" | None:
        if obj is None:
            return None

        return cls(
            value=obj.get("value"),
            comparison=obj.get("comparison"),
        )


@dataclass(eq=True, frozen=True)
class UnaryCheck(ValueComparisons):
    """Unary Check"""

    Resolved: UnaryComparison | None = field(default=None)
    UnResolved: UnResolved | None = field(default=None)
    UnresolvedContext: Any | None = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "UnaryCheck" | None:
        if obj is None:
            return obj

        return cls(
            Resolved=UnaryComparison.from_object(obj.get("Resolved")),
            UnResolved=UnResolved.from_object(obj.get("UnResolved")),
            UnresolvedContext=obj.get("UnresolvedContext"),
        )

    @property
    def value_from(self) -> Any:
        if self.Resolved is not None:
            return self.Resolved.value
        if self.UnResolved is not None:
            return self.UnResolved.traversed_to
        return None

    @property
    def value_to(self) -> Any:
        return None


@dataclass(eq=True, frozen=True)
class UnaryReport:
    """Unary Report"""

    context: str = field()
    messages: Messages = field()
    check: UnaryCheck = field()

    @classmethod
    def from_object(cls, obj) -> "UnaryReport" | None:
        if obj is None:
            return None

        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            check=UnaryCheck.from_object(obj.get("check")),
        )


@dataclass(eq=True, frozen=True)
class BinaryComparison:
    from_: Any = field()
    to_: Any = field()
    comparison: Any = field()

    @classmethod
    def from_object(cls, obj) -> "BinaryComparison" | None:
        if obj is None:
            return None
        return cls(
            from_=obj.get("from"), to_=obj.get("to"), comparison=obj.get("comparison")
        )


@dataclass(eq=True, frozen=True)
class InComparison:
    def __init__(self, **kwargs) -> None:
        self.from_ = kwargs["from"]
        self.to_ = kwargs["to"]
        self.comparison = kwargs["comparison"]

    @classmethod
    def from_object(cls, obj) -> "InComparison" | None:
        if obj is None:
            return None

        return cls(
            from_=obj.get("from"),
            to_=obj.get("to"),
            comparison=obj.get("comparison"),
        )


@dataclass(eq=True, frozen=True)
class BinaryCheck(ValueComparisons):
    Resolved: BinaryComparison | None = field(default=None)
    UnResolved: UnResolved | None = field(default=None)
    InResolved: Any = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "BinaryCheck" | None:
        if obj is None:
            return None

        return cls(
            Resolved=BinaryComparison.from_object(obj.get("Resolved")),
            UnResolved=UnResolved.from_object(obj.get("UnResolved")),
            InResolved=obj.get("InResolved"),
        )

    @property
    def value_from(self) -> Any:
        if self.Resolved is not None:
            return self.Resolved.from_
        if self.InResolved is not None:
            return self.InResolved.from_
        if self.UnResolved is not None:
            return self.UnResolved.traversed_to
        return None

    @property
    def value_to(self) -> Any:
        if self.Resolved is not None:
            return self.Resolved.to_
        return None


@dataclass(eq=True, frozen=True)
class BinaryReport:
    context: str = field()
    messages: Messages = field()
    check: BinaryCheck = field()

    @classmethod
    def from_object(cls, obj) -> "BinaryReport" | None:
        if obj is None:
            return obj
        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            check=BinaryCheck.from_object(obj.get("check")),
        )


@dataclass(eq=True, frozen=True)
class GuardClauseReport(ValueComparisons):
    """Guard Clause Report"""

    Unary: UnaryReport | None = field(default=None)
    Binary: BinaryReport | None = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "GuardClauseReport" | None:
        if obj is None:
            return obj

        return cls(
            Unary=UnaryReport.from_object(obj.get("Unary")),
            Binary=BinaryReport.from_object(obj.get("Binary")),
        )

    @property
    def context(self) -> str | None:
        if self.Unary is not None:
            return self.Unary.context
        if self.Binary is not None:
            return self.Binary.context
        return None

    @property
    def messages(self) -> Messages | None:
        if self.Unary is not None:
            return self.Unary.messages
        if self.Binary is not None:
            return self.Binary.messages
        return None

    @property
    def value_from(self):
        if self.Unary is not None:
            return self.Unary.check.value_from
        if self.Binary is not None:
            return self.Binary.check.value_from
        return None

    @property
    def value_to(self):
        if self.Unary is not None:
            return self.Unary.check.value_to
        if self.Binary is not None:
            return self.Binary.check.value_to
        return None


@dataclass(eq=True, frozen=True)
class ClauseReport(ValueComparisons):
    """Clause Report"""

    Rule: RuleReport | None = field(default=None)
    Disjunctions: DisjunctionsReport | None = field(default=None)
    GuardBlock: GuardBlockReport | None = field(default=None)
    Clause: GuardClauseReport | None = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "ClauseReport" | None:
        if obj is None:
            return None

        return cls(
            Rule=RuleReport.from_object(obj.get("Rule")),
            Disjunctions=DisjunctionsReport.from_object(obj.get("Disjunctions")),
            GuardBlock=GuardBlockReport.from_object(obj.get("GuardBlock")),
            Clause=GuardClauseReport.from_object(obj.get("Clause")),
        )

    @classmethod
    def from_array(cls, items):
        results = []
        for item in items:
            results.append(ClauseReport.from_object(item))

        return results

    @property
    def value_from(self) -> Any:
        if self.GuardBlock is not None:
            return self.GuardBlock.value_from
        if self.Clause is not None:
            return self.Clause.value_from
        return None

    @property
    def value_to(self) -> Any:
        if self.GuardBlock is not None:
            return self.GuardBlock.value_to
        if self.Clause is not None:
            return self.Clause.value_to
        return None


# pylint: disable=too-many-instance-attributes
@dataclass(eq=True, frozen=True)
class FileReport:
    name: str = field()
    metadata: Dict[str, Any] = field()
    status: str = field()
    not_compliant: List[ClauseReport] = field()
    not_applicable: List[str] = field()
    compliant: List[str] = field()
    data_from: str = field(default="cfn_guard_rs")
    rules_from: str = field(default="cfn_guard_rs")

    @classmethod
    def from_object(cls, obj) -> "FileReport":
        return cls(
            name=obj.get("name"),
            metadata=obj.get("metadata"),
            status=obj.get("status"),
            not_compliant=ClauseReport.from_array(obj.get("not_compliant")),
            not_applicable=obj.get("not_applicable"),
            compliant=obj.get("compliant"),
            data_from=obj.get("data_from", "cfn_guard_rs"),
            rules_from=obj.get("rules_from", "cfn_guard_rs"),
        )
