"""
    Primary Guard type conversion
"""
from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Converter():
    """
        Converts types using JSON Patch and a conversion function
    """
    path: str
    converter: Callable[[str], Any]


def to_int(value: str) -> int:
    """ Convert string to int"""
    return int(value)


def to_bool(value: str) -> bool:
    """ Convert string to bool"""
    return bool(value)


def to_float(value: str) -> float:
    """ Convert string to float"""
    return float(value)
