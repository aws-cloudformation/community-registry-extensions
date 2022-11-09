"""
  Defines the errors that are returned from Guard
"""


class GuardError(Exception):
    """General exception to cover all Guard exceptions"""


class UnknownError(GuardError):
    """Raised when having an unknown error is encountered"""


class ParseError(GuardError, ValueError):
    """Raised when having an issue parsing rules"""


class MissingValueError(ParseError, NameError):
    """There was no variable or value object to resolve"""
