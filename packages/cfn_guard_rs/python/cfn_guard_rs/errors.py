"""
  Defines the errors that are returned from Guard
"""


# pylint: disable=no-name-in-module,unused-import
from .cfn_guard_rs import (
    JsonError,
    YamlError,
    FormatError,
    IoError,
    ParseError,
    RegexError,
    MissingProperty,
    MissingVariable,
    MultipleValues,
    IncompatibleRetrievalError,
    IncompatibleError,
    NotComparable,
    ConversionError,
    Errors,
    RetrievalError,
    MissingValue,
    FileNotFoundError as GuardFileNotFoundError,  # rename for redefined-builtin
)
