from functools import singledispatch
from typing import List

# pylint: disable=no-name-in-module
from rpdk.guard_rail.utils.arg_handler import (
    argument_validation,
    collect_rules,
    collect_schemas,
    setup_args,
)
from rpdk.guard_rail.core.data_types import GuardRuleSetResult, Statefull, Stateless
from rpdk.guard_rail.core.runner import exec_compliance

def main(args_in=None):
    parser = setup_args()
    args = parser.parse_args(args=args_in)

    argument_validation(args)
    collected_schemas = collect_schemas(schemas=args.schemas)
    collected_rules = collect_rules(rules=args.rules)

    compliance_result = None

    if not args.statefull:
        payload: Stateless = Stateless(schemas=collected_schemas, rules=collected_rules)
        compliance_result = invoke(payload)
    else:
        # should be index safe as argument validation should fail prematurely
        payload: Statefull = Statefull(
            previous_schema=collected_schemas[0],
            current_schema=collected_schemas[1],
            rules=collected_rules,
        )
        compliance_result = invoke(payload)

    if args.format:
        display(compliance_result)
    else:
        print(compliance_result)


def display(compliance_result: List[GuardRuleSetResult]):
    for item in compliance_result:
        print()
        print(item)
    print()


@singledispatch
def invoke(*args, **kwargs):
    raise NotImplementedError("not supported implementation")


@invoke.register(Stateless)
def _(payload):
    return exec_compliance(payload)


@invoke.register(Statefull)
def _(payload):
    return exec_compliance(payload)
