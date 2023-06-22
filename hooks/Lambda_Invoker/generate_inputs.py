"""
Auto generate the inputs for contract testing.

WARNING: Overwrites everything in inputs/

"""

import json
from time import sleep
import boto3

def get_resource_types():
    """Return a list of all public AWS resource types."""

    client = boto3.client("cloudformation")

    list_types_args = {
        "DeprecatedStatus": "LIVE",
        "Type": "RESOURCE",
        "Filters": {
            "Category": "AWS_TYPES",
        },
        "Visibility": "PUBLIC",
    }

    paginator = client.get_paginator("list_types")
    page_iterator = paginator.paginate(**list_types_args)

    resource_types = {}
    for page in page_iterator:
        type_summaries = page["TypeSummaries"]
        for type_summary in type_summaries:
            name = type_summary["TypeName"]
            resource_types[name] = {}
            resource_types[name]["resourceProperties"] = {}

    for name, resource_type in resource_types.items():
        print(name)
        args = {"Type": "RESOURCE", "TypeName": name}
        res = client.describe_type(**args)
        schema = json.loads(res["Schema"])
        if "required" in schema:
            req = schema["required"]
            for r in req:
                #prop = schema["properties"][r]
                # We might want to generate something valid based on regex
                resource_type["resourceProperties"][r] = "TODO"
        sleep(1) # API throttling

    return resource_types


def main():
    "Main"

    print("About to get resource types")
    resource_types = get_resource_types()

    valids = [
        "inputs/inputs_1_pre_create.json",
        "inputs/inputs_1_pre_delete.json",
        "inputs/inputs_1_pre_update.json",
    ]
    invalids = [
        "inputs/inputs_1_invalid_pre_create.json",
        "inputs/inputs_1_invalid_pre_delete.json",
        "inputs/inputs_1_invalid_pre_update.json",
    ]

    for valid in valids:
        print("Writing to ", valid)
        with open(valid, "w", encoding="utf8") as f:
            json.dump(resource_types, f)

    for _, resource_type in resource_types.items():
        resource_type["resourceProperties"]["FAIL"] = "FAIL"

    for invalid in invalids:
        print("Writing to ", invalid)
        with open(invalid, "w", encoding="utf8") as f:
            json.dump(resource_types, f)


if __name__ == "__main__":
    main()
