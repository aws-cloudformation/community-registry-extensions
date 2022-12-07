
## Datadog::Dashboards::Dashboard

## Datadog Dashboard 2.0.2

- [Source]() 
- [Documentation]()

Published by DataDog

## Schema
{% highlight json %}
{
    "typeName": "Datadog::Dashboards::Dashboard",
    "description": "Datadog Dashboard 2.0.2",
    "typeConfiguration": {
        "properties": {
            "DatadogCredentials": {
                "$ref": "#/definitions/DatadogCredentials"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "DatadogCredentials": {
            "description": "Credentials for the Datadog API",
            "properties": {
                "ApiKey": {
                    "description": "Datadog API key",
                    "type": "string"
                },
                "ApplicationKey": {
                    "description": "Datadog application key",
                    "type": "string"
                },
                "ApiURL": {
                    "description": "Datadog API URL (defaults to https://api.datadoghq.com) Use https://api.datadoghq.eu for EU accounts.",
                    "type": "string"
                }
            },
            "required": [
                "ApiKey",
                "ApplicationKey"
            ],
            "type": "object",
            "additionalProperties": false
        }
    },
    "properties": {
        "Id": {
            "description": "ID of the dashboard",
            "type": "string"
        },
        "Url": {
            "description": "Url of the dashboard",
            "type": "string"
        },
        "DashboardDefinition": {
            "description": "JSON string of the dashboard definition",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "DashboardDefinition"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Url"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": [
                ""
            ]
        },
        "read": {
            "permissions": [
                ""
            ]
        },
        "update": {
            "permissions": [
                ""
            ]
        },
        "delete": {
            "permissions": [
                ""
            ]
        }
    }
}
{% endhighlight %}
