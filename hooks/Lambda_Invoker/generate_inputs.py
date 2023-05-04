import boto3
import json
from botocore.config import Config

def get_resource_types(category: str = "AWS_TYPES"):
    """Return a list of resource types."""

    client = boto3.client("cloudformation")

    list_types_args = {
        "DeprecatedStatus": "LIVE",
        "Type": "RESOURCE",
        "Filters": {
            "Category": category,
        },
    }

    if category == "THIRD_PARTY":
        visibility = None
    elif category in ["AWS_TYPES","ACTIVATED"]:
        visibility = "PUBLIC"
    else:
        visibility = "PRIVATE"

    if visibility:
        list_types_args["Visibility"] = visibility

    paginator = client.get_paginator("list_types")
    page_iterator = paginator.paginate(**list_types_args)

    resource_types = []
    for page in page_iterator:
        type_summaries = page["TypeSummaries"]
        resource_types += [
            {
                "type_name": type_summary["TypeName"],
            }
            for type_summary in type_summaries
        ]

    # TODO - For each type, describe-type to get the schema.
    # Parse the schema to emit required properties

    return resource_types

if __name__ == "__main__":
    print(json.dumps(get_resource_types()))

