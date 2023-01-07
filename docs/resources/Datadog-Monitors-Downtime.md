
## Datadog::Monitors::Downtime

Datadog Monitors Downtime 3.0.0

- [Source]() 
- [Documentation]()

Published by DataDog

## Schema
{% highlight json %}
{
    "typeName": "Datadog::Monitors::Downtime",
    "description": "Datadog Monitors Downtime 3.0.0",
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
        "Active": {
            "description": "Whether or not this downtime is currently active",
            "type": "boolean"
        },
        "Canceled": {
            "description": "POSIX Timestamp of cancellation of this downtime (null if not canceled)",
            "type": "integer"
        },
        "CreatorId": {
            "description": "Id of the user who created this downtime",
            "type": "integer"
        },
        "Disabled": {
            "description": "Whether or not this downtime is disabled",
            "type": "boolean"
        },
        "DowntimeType": {
            "description": "Type of this downtime",
            "type": "integer"
        },
        "End": {
            "description": "POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).",
            "type": "integer"
        },
        "Id": {
            "description": "Id of this downtime",
            "type": "integer"
        },
        "Message": {
            "description": "Message on the downtime",
            "type": "string"
        },
        "MonitorId": {
            "description": "A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.",
            "type": "integer"
        },
        "MonitorTags": {
            "description": "A comma-separated list of monitor tags, to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags.",
            "items": {
                "type": "string"
            },
            "type": "array"
        },
        "ParentId": {
            "description": "The ID of the parent downtime to this one",
            "type": "integer"
        },
        "Scope": {
            "description": "The scope(s) to which the downtime applies",
            "items": {
                "type": "string"
            },
            "type": "array"
        },
        "Start": {
            "description": "POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.",
            "type": "integer"
        },
        "Timezone": {
            "description": "The timezone for the downtime",
            "type": "string"
        },
        "UpdaterId": {
            "description": "Id of the user who updated this downtime",
            "type": "integer"
        }
    },
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "readOnlyProperties": [
        "/properties/Active",
        "/properties/Canceled",
        "/properties/CreatorId",
        "/properties/DowntimeType",
        "/properties/Id",
        "/properties/ParentId",
        "/properties/UpdaterId"
    ],
    "additionalProperties": false,
    "required": [
        "Scope"
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
