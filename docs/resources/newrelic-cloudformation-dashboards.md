
## newrelic::cloudformation::dashboards

CRUDL operations for New Relic Dashboards via the NerdGraph API

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by newrelic-experimental

## Schema
{% highlight json %}
{
    "typeName": "newrelic::cloudformation::dashboards",
    "description": "CRUDL operations for New Relic Dashboards via the NerdGraph API",
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "properties": {
        "AccountID": {
            "type": "string"
        },
        "Endpoint": {
            "type": "string"
        },
        "DashboardInput": {
            "type": "string"
        },
        "APIKey": {
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
    "required": [
        "APIKey",
        "DashboardInput"
    ],
    "readOnlyProperties": [
        "/properties/Guid"
    ],
    "primaryIdentifier": [
        "/properties/Guid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "initech:CreateReport"
            ]
        },
        "read": {
            "permissions": [
                "initech:DescribeReport"
            ]
        },
        "update": {
            "permissions": [
                "initech:UpdateReport"
            ]
        },
        "delete": {
            "permissions": [
                "initech:DeleteReport"
            ]
        },
        "list": {
            "permissions": [
                "initech:ListReports"
            ]
        }
    }
}
{% endhighlight %}
