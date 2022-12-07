
## NewRelic::CloudFormation::Workloads

## CRUD operations for New Relic Workloads via the NerdGraph API

- [Source](https:&#x2F;&#x2F;github.com&#x2F;newrelic-experimental&#x2F;newrelic-cloudformation-resource-providers-workloads.git) 
- [Documentation]()

Published by newrelic-experimental

## Schema
{% highlight json %}
{
    "typeName": "NewRelic::CloudFormation::Workloads",
    "description": "CRUD operations for New Relic Workloads via the NerdGraph API",
    "sourceUrl": "https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-workloads.git",
    "properties": {
        "Guid": {
            "type": "string"
        },
        "SourceGuid": {
            "type": "string"
        },
        "DuplicateName": {
            "type": "string"
        },
        "Workload": {
            "type": "string"
        },
        "ListQueryFilter": {
            "type": "string"
        },
        "Variables": {
            "type": "object",
            "patternProperties": {
                "^[A-Za-z0-9]{1,64}$": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "additionalProperties": false,
    "primaryIdentifier": [
        "/properties/Guid"
    ],
    "readOnlyProperties": [
        "/properties/Guid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "cloudformation:BatchDescribeTypeConfigurations"
            ]
        },
        "read": {
            "permissions": [
                "cloudformation:BatchDescribeTypeConfigurations"
            ]
        },
        "update": {
            "permissions": [
                "cloudformation:BatchDescribeTypeConfigurations"
            ]
        },
        "delete": {
            "permissions": [
                "cloudformation:BatchDescribeTypeConfigurations"
            ]
        },
        "list": {
            "permissions": [
                "cloudformation:BatchDescribeTypeConfigurations"
            ]
        }
    },
    "definitions": {
        "TagObject": {
            "type": "object",
            "required": [
                "Key",
                "Values"
            ],
            "properties": {
                "Key": {
                    "type": "string"
                },
                "Values": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                }
            },
            "additionalProperties": false
        }
    },
    "typeConfiguration": {
        "properties": {
            "Endpoint": {
                "type": "string",
                "default": "https://api.newrelic.com/graphql"
            },
            "APIKey": {
                "type": "string"
            },
            "AccountID": {
                "type": "string"
            }
        },
        "additionalProperties": false,
        "required": [
            "APIKey",
            "AccountID"
        ]
    }
}
{% endhighlight %}
