import boto3
import json
import sys
from botocore.config import Config

def get_resource_types(prefix):
    """Return a list of resource types."""

    client = boto3.client("cloudformation")

    list_types_args = {
        "DeprecatedStatus": "LIVE",
        "Type": "RESOURCE",
        "Filters": {
            "Category": "AWS_TYPES",
            "TypeNamePrefix": prefix
        },
        "Visibility": "PUBLIC"
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

    # TODO - For each type, describe-type to get the schema.
    # Parse the schema to emit required properties

    for name in resource_types:
        args = {
            "Type": "RESOURCE", 
            "TypeName": name
        }
        res = client.describe_type(**args)
        schema = json.loads(res["Schema"])
        if "required" in schema:
            req = schema["required"]
            for r in req:
                prop = schema["properties"][r]
            resource_types[name]["resourceProperties"][r] = "TODO"

    return resource_types

if __name__ == "__main__":
    print(json.dumps(get_resource_types(sys.argv[1]), indent=4))

