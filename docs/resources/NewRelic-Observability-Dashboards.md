
## NewRelic::Observability::Dashboards

## CRUD operations for New Relic Dashboards via the NerdGraph API

- [Source](https:&#x2F;&#x2F;github.com&#x2F;newrelic-experimental&#x2F;newrelic-cloudformation-resource-providers-dashboards) 
- [Documentation]()

Published by newrelic-experimental

## Schema
{% highlight json %}
{
    "typeName": "NewRelic::Observability::Dashboards",
    "description": "CRUD operations for New Relic Dashboards via the NerdGraph API",
    "sourceUrl": "https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-dashboards",
    "properties": {
        "DashboardInput": {
            "type": "string"
        },
        "Guid": {
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
        },
        "Tags": {
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
