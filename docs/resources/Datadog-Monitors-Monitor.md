
## Datadog::Monitors::Monitor

## Datadog Monitor 4.4.0

- [Source]() 
- [Documentation]()

Published by DataDog

## Schema
{% highlight json %}
{
    "typeName": "Datadog::Monitors::Monitor",
    "description": "Datadog Monitor 4.4.0",
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
                    "description": "Name of the creator of the monitor",
                    "type": "string"
                },
                "Handle": {
                    "description": "Handle of the creator of the monitor",
                    "type": "string"
                },
                "Email": {
                    "description": "Email of the creator of the monitor",
                    "type": "string"
                }
            }
        },
        "MonitorThresholds": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Critical": {
                    "description": "Threshold value for triggering an alert",
                    "type": "number"
                },
                "CriticalRecovery": {
                    "description": "Threshold value for recovering from an alert state",
                    "type": "number"
                },
                "OK": {
                    "description": "Threshold value for recovering from an alert state",
                    "type": "number"
                },
                "Warning": {
                    "description": "Threshold value for triggering a warning",
                    "type": "number"
                },
                "WarningRecovery": {
                    "description": "Threshold value for recovering from a warning state",
                    "type": "number"
                }
            }
        },
        "MonitorThresholdWindows": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "TriggerWindow": {
                    "description": "How long a metric must be anomalous before triggering an alert",
                    "type": "string"
                },
                "RecoveryWindow": {
                    "description": "How long an anomalous metric must be normal before recovering from an alert state",
                    "type": "string"
                }
            }
        },
        "MonitorOptions": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "EnableLogsSample": {
                    "description": "Whether or not to include a sample of the logs",
                    "type": "boolean"
                },
                "EscalationMessage": {
                    "description": "Message to include with a re-notification when renotify_interval is set",
                    "type": "string"
                },
                "EvaluationDelay": {
                    "description": "Time in seconds to delay evaluation",
                    "type": "integer"
                },
                "IncludeTags": {
                    "description": "Whether or not to include triggering tags into notification title",
                    "type": "boolean",
                    "insertionOrder": false,
                    "default": true
                },
                "Locked": {
                    "description": "Whether or not changes to this monitor should be restricted to the creator or admins",
                    "type": "boolean"
                },
                "MinLocationFailed": {
                    "description": "Number of locations allowed to fail before triggering alert",
                    "type": "integer"
                },
                "NewHostDelay": {
                    "description": "Time in seconds to allow a host to start reporting data before starting the evaluation of monitor results",
                    "type": "integer",
                    "default": 300
                },
                "NoDataTimeframe": {
                    "description": "Number of minutes data stopped reporting before notifying",
                    "type": "integer"
                },
                "NotifyAudit": {
                    "description": "Whether or not to notify tagged users when changes are made to the monitor",
                    "type": "boolean"
                },
                "NotifyNoData": {
                    "description": "Whether or not to notify when data stops reporting",
                    "type": "boolean"
                },
                "RenotifyInterval": {
                    "description": "Number of minutes after the last notification before the monitor re-notifies on the current status",
                    "type": "integer"
                },
                "RequireFullWindow": {
                    "description": "Whether or not the monitor requires a full window of data before it is evaluated",
                    "type": "boolean"
                },
                "SyntheticsCheckID": {
                    "description": "ID of the corresponding synthetics check",
                    "type": "integer"
                },
                "Thresholds": {
                    "description": "The threshold definitions",
                    "$ref": "#/definitions/MonitorThresholds"
                },
                "ThresholdWindows": {
                    "description": "The threshold window definitions",
                    "$ref": "#/definitions/MonitorThresholdWindows"
                },
                "TimeoutH": {
                    "description": "Number of hours of the monitor not reporting data before it automatically resolves",
                    "type": "integer"
                },
                "RenotifyOccurrences": {
                    "description": "The number of times re-notification messages should be sent on the current status at the provided re-notification interval.",
                    "type": "integer"
                },
                "RenotifyStatuses": {
                    "description": "The types of monitor statuses for which re-notification messages are sent.",
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string",
                        "enum": [
                            "alert",
                            "no data",
                            "warn"
                        ]
                    }
                },
                "MinFailureDuration": {
                    "description": "How long the test should be in failure before alerting (integer, number of seconds, max 7200).",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 7200
                },
                "NewGroupDelay": {
                    "description": "Time (in seconds) to skip evaluations for new groups. For example, this option can be used to skip evaluations for new hosts while they initialize. Must be a non negative integer.",
                    "type": "integer",
                    "minimum": 0
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
        "Id": {
            "description": "ID of the monitor",
            "type": "integer"
        },
        "Message": {
            "description": "A message to include with notifications for the monitor",
            "type": "string"
        },
        "Name": {
            "description": "Name of the monitor",
            "type": "string"
        },
        "Tags": {
            "description": "Tags associated with the monitor",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "Priority": {
            "description": "Integer from 1 (high) to 5 (low) indicating alert severity.",
            "type": "integer"
        },
        "Options": {
            "description": "The monitor options",
            "$ref": "#/definitions/MonitorOptions"
        },
        "Query": {
            "description": "The monitor query",
            "type": "string"
        },
        "Type": {
            "type": "string",
            "description": "The type of the monitor",
            "enum": [
                "audit alert",
                "composite",
                "event alert",
                "event-v2 alert",
                "log alert",
                "metric alert",
                "process alert",
                "query alert",
                "service check",
                "synthetics alert",
                "trace-analytics alert",
                "slo alert",
                "rum alert",
                "ci-pipelines alert",
                "error-tracking alert",
                "ci-tests alert"
            ]
        },
        "Multi": {
            "description": "Whether or not the monitor is multi alert",
            "type": "boolean"
        },
        "Created": {
            "description": "Date of creation of the monitor",
            "type": "string",
            "format": "date-time"
        },
        "Deleted": {
            "description": "Date of deletion of the monitor",
            "type": "string",
            "format": "date-time"
        },
        "Modified": {
            "description": "Date of modification of the monitor",
            "type": "string",
            "format": "date-time"
        },
        "RestrictedRoles": {
            "description": "A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. `restricted_roles` is the successor of `locked`. For more information about `locked` and `restricted_roles`, see the [monitor options docs](https://docs.datadoghq.com/monitors/guide/monitor_api_options/#permissions-options).",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "Query",
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
