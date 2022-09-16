import argparse
import json
import re
from functools import wraps
from typing import Sequence

from .logger import LOG, logdebug
from .common import (
    FILE_PATTERN,
    GUARD_FILE_PATTERN,
    GUARD_PATH_EXTRACT_PATTERN,
    JSON_PATH_EXTRACT_PATTERN,
    read_file,
    SCHEMA_FILE_PATTERN,
)


def apply_rule(execute_rule, msg, /):
    def validation_wrapper(func: object):
        @wraps(func)
        def wrapper(args):
            assert execute_rule(args), msg
            return func(args)

        return wrapper

    return validation_wrapper


@apply_rule(
    lambda args: len(args.schemas) == 2 if args.statefull else True,
    "If Statefull mode is executed, then two schemas MUST be provided (current/previous)",
)
def argument_validation(args: argparse.Namespace):  # pylint: disable=unused-argument
    pass


@logdebug
def setup_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("--version", action="version", version="v0.1alpha")

    parser.add_argument(
        "--schema",
        dest="schemas",
        action="extend",
        nargs="+",
        type=str,
        required=True,
        help="Should specify schema for CFN compliance evaluation (path or plain value)",
    )

    parser.add_argument(
        "--statefull",
        dest="statefull",
        action="store_true",
        default=False,
        help="If specified will execute statefull compliance evaluation",
    )

    parser.add_argument(
        "--format",
        dest="format",
        action="store_true",
        default=False,
        help="Should specify schema for CFN compliance evaluation (path or plain value)",
    )

    parser.add_argument(
        "--rules",
        dest="rules",
        action="extend",
        nargs="+",
        type=str,
        help="Should specify additional rules for compliance evaluation (path of `.guard` file)",
    )

    return parser


@logdebug
def input_path_validation(input_path: str):
    if not re.search(FILE_PATTERN, input_path):
        LOG.info("%s is not starting with `file://...`", input_path)
        raise ValueError("file path must be specified with `file://...`")


@logdebug
def collect_schemas(schemas: Sequence[str] = None):
    _schemas = []

    @logdebug
    def __to_json(schema_raw: str):
        try:
            return json.loads(schema_raw)
        except json.JSONDecodeError as ex:
            raise ValueError(f"Invalid Schema Body {ex}") from ex

    if schemas:
        for schema_item in schemas:

            input_path_validation(schema_item)

            if re.search(SCHEMA_FILE_PATTERN, schema_item):
                path = "/" + re.search(JSON_PATH_EXTRACT_PATTERN, schema_item).group(0)
                file_obj = read_file(path)
                _schemas.append(__to_json(file_obj))
            else:
                schema_deser = __to_json(schema_item)
                _schemas.append(schema_deser)
    return _schemas


@logdebug
def collect_rules(rules: Sequence[str] = None):
    _rules = []
    if rules:
        for rule in rules:
            input_path_validation(rule)

            if re.search(GUARD_FILE_PATTERN, rule):
                path = "/" + re.search(GUARD_PATH_EXTRACT_PATTERN, rule).group(0)
                file_obj = read_file(path)
                _rules.append(file_obj)

            else:
                raise ValueError("file extenstion is invalid - MUST be `.guard`")
    return _rules
