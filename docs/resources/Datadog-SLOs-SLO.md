
## Datadog::SLOs::SLO

## Datadog SLO 1.0.1

- [Source]() 
- [Documentation]()

Published by DataDog

## Schema
{% highlight json %}
{
    "typeName": "Datadog::SLOs::SLO",
    "description": "Datadog SLO 1.0.1",
    "typeConfiguration": {
        "properties": {
            "DatadogCredentials": {
                "$ref": "#/definitions/DatadogCredentials"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "Creator": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Name": {
                    "description": "Name of the creator of the slo",
                    "type": "string"
                },
                "Handle": {
                    "description": "Handle of the creator of the slo",
                    "type": "string"
                },
                "Email": {
                    "description": "Email of the creator of the slo",
                    "type": "string"
                }
            }
        },
        "Threshold": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Target": {
                    "description": "The target value for the service level indicator within the corresponding timeframe.",
                    "type": "number"
                },
                "TargetDisplay": {
                    "description": "A string representation of the target that indicates its precision.(e.g. 98.00)",
                    "type": "string"
                },
                "Timeframe": {
                    "description": "The SLO time window options. Allowed enum values: 7d,30d,90d",
                    "type": "string",
                    "enum": [
                        "7d",
                        "30d",
                        "90d"
                    ]
                },
                "Warning": {
                    "description": "The warning value for the service level objective.",
                    "type": "number"
                },
                "WarningDisplay": {
                    "description": "A string representation of the warning target.(e.g. 98.00)",
                    "type": "string"
                }
            }
        },
        "Query": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Numerator": {
                    "description": "A Datadog metric query for total (valid) events.",
                    "type": "string"
                },
                "Denominator": {
                    "description": "A Datadog metric query for good events.",
                    "type": "string"
                }
            }
        },
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
        "Creator": {
            "$ref": "#/definitions/Creator"
        },
        "Description": {
            "description": "Description of the slo",
            "type": "string"
        },
        "Groups": {
            "description": "A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "Id": {
            "description": "ID of the slo",
            "type": "string"
        },
        "MonitorIds": {
            "description": "A list of monitor ids that defines the scope of a monitor service level objective. Required if type is monitor.",
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "Name": {
            "description": "Name of the slo",
            "type": "string"
        },
        "Query": {
            "$ref": "#/definitions/Query"
        },
        "Tags": {
            "description": "Tags associated with the slo",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "Thresholds": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Threshold"
            }
        },
        "Type": {
            "type": "string",
            "description": "The type of the slo",
            "enum": [
                "monitor",
                "metric"
            ]
        },
        "Created": {
            "description": "Date of creation of the slo",
            "type": "string",
            "format": "date-time"
        },
        "Deleted": {
            "description": "Date of deletion of the slo",
            "type": "string",
            "format": "date-time"
        },
        "Modified": {
            "description": "Date of modification of the slo",
            "type": "string",
            "format": "date-time"
        }
    },
    "required": [
        "Name",
        "Thresholds",
        "Type"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "readOnlyProperties": [
        "/properties/Modified",
        "/properties/Id",
        "/properties/Deleted",
        "/properties/State",
        "/properties/OverallState",
        "/properties/Creator",
        "/properties/Created"
    ],
    "additionalProperties": false,
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
