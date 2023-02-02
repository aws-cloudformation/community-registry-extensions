from typing import Callable, Any

class Converter():
    path: str
    converters: Callable[[str], Any]

    def __init__(self, path: str, converter: Callable[[str], Any]) -> None:
        self.path = path
        self.converter = converter


def to_int(v: str) -> int:
  return int(v)


def to_bool(v: str) -> bool:
  return bool(v)


def to_float(v: str) -> float:
  return float(v)
