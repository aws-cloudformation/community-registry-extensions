
## PagerDuty::Schedules::Schedule

## Manage a on-call schedule in PagerDuty

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::Schedules::Schedule",
    "description": "Manage a on-call schedule in PagerDuty",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-pagerduty-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-pagerduty-resource-providers",
    "definitions": {
        "PagerDutyAccess": {
            "type": "object",
            "properties": {
                "Token": {
                    "description": "Personal Access Token",
                    "type": "string"
                }
            },
            "required": [
                "Token"
            ],
            "additionalProperties": false
        },
        "Id": {
            "type": "string",
            "minLength": 1
        },
        "Summary": {
            "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
            "type": "string"
        },
        "Self": {
            "description": "The API show URL at which the object is accessible",
            "type": "string"
        },
        "HtmlUrl": {
            "description": "A URL at which the entity is uniquely displayed in the Web app.",
            "type": "string"
        },
        "RenderedCoveragePercentage": {
            "description": "The percentage of the time range covered by this layer. Returns null unless since or until are set.",
            "type": "number"
        },
        "ScheduleLayer": {
            "type": "object",
            "properties": {
                "Id": {
                    "$ref": "#/definitions/Id"
                },
                "Start": {
                    "description": "The start time of this layer.",
                    "type": "string",
                    "format": "date-time"
                },
                "End": {
                    "description": "The end time of this layer. If null, the layer does not end.",
                    "type": "string",
                    "format": "date-time"
                },
                "Users": {
                    "description": "The ordered list of users on this layer. The position of the user on the list determines their order in the layer.",
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/UserWrapper"
                    }
                },
                "Restrictions": {
                    "description": "An array of restrictions for the layer. A restriction is a limit on which period of the day or week the schedule layer can accept assignments.",
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/Restriction"
                    }
                },
                "RotationVirtualStart": {
                    "description": "The effective start time of the layer. This can be before the start time of the schedule.",
                    "type": "string",
                    "format": "date-time"
                },
                "RotationTurnLengthSeconds": {
                    "description": "The duration of each on-call shift in seconds.",
                    "type": "integer",
                    "minimum": 0
                },
                "Name": {
                    "description": "The name of the schedule layer.",
                    "type": "string"
                }
            },
            "required": [
                "Start",
                "Users",
                "RotationVirtualStart",
                "RotationTurnLengthSeconds"
            ],
            "additionalProperties": false
        },
        "Restriction": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Specify the types of restriction.",
                    "type": "string",
                    "enum": [
                        "daily_restriction",
                        "weekly_restriction"
                    ]
                },
                "DurationSeconds": {
                    "description": "The duration of the restriction in seconds.",
                    "type": "integer",
                    "minimum": 0
                },
                "StartTimeOfDay": {
                    "description": "The start time in HH:mm:ss format.",
                    "type": "string",
                    "pattern": "([0-1][0-9]|2[0-3])(:[0-5][0-9]){2}"
                },
                "StartDayOfWeek": {
                    "description": "Only required for use with a weekly_restriction restriction type. The first day of the weekly rotation schedule as ISO 8601 day (1 is Monday, etc.)",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 7
                }
            },
            "required": [
                "Type",
                "DurationSeconds",
                "StartTimeOfDay"
            ],
            "additionalProperties": false
        },
        "SubSchedule": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The name of the subschedule",
                    "type": "string",
                    "enum": [
                        "Final Scheduled",
                        "Overrides"
                    ]
                },
                "RenderedScheduleEntries": {
                    "description": "This is a list of entries on the computed layer for the current time range. Since or until must be set in order for this field to be populated.",
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/RenderedScheduleEntries"
                    }
                },
                "RenderedCoveragePercentage": {
                    "type": "number"
                }
            },
            "required": [
                "Name"
            ],
            "additionalProperties": false
        },
        "RenderedScheduleEntries": {
            "type": "object",
            "properties": {
                "User": {
                    "$ref": "#/definitions/User"
                },
                "Start": {
                    "description": "The start time of this entry.",
                    "type": "string",
                    "format": "date-time"
                },
                "End": {
                    "description": "The end time of this entry. If null, the entry does not end.",
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "Start",
                "End"
            ],
            "additionalProperties": false
        },
        "EscalationPolicy": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.",
                    "type": "string",
                    "enum": [
                        "escalation_policy_reference"
                    ]
                },
                "Id": {
                    "$ref": "#/definitions/Id"
                }
            },
            "required": [
                "Type",
                "Id"
            ],
            "additionalProperties": false
        },
        "UserWrapper": {
            "type": "object",
            "properties": {
                "User": {
                    "$ref": "#/definitions/User"
                }
            },
            "required": [
                "User"
            ],
            "additionalProperties": false
        },
        "User": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.",
                    "type": "string",
                    "enum": [
                        "user_reference"
                    ]
                },
                "Id": {
                    "$ref": "#/definitions/Id"
                },
                "Summary": {
                    "$ref": "#/definitions/Summary"
                },
                "HtmlUrl": {
                    "$ref": "#/definitions/HtmlUrl"
                },
                "Self": {
                    "$ref": "#/definitions/HtmlUrl"
                }
            },
            "required": [
                "Type",
                "Id"
            ],
            "additionalProperties": false
        },
        "Team": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.",
                    "type": "string",
                    "enum": [
                        "team_reference",
                        "team"
                    ]
                },
                "Id": {
                    "$ref": "#/definitions/Id"
                },
                "Summary": {
                    "$ref": "#/definitions/Summary"
                },
                "HtmlUrl": {
                    "$ref": "#/definitions/HtmlUrl"
                },
                "Self": {
                    "$ref": "#/definitions/Self"
                }
            },
            "required": [
                "Type",
                "Id"
            ],
            "additionalProperties": false
        }
    },
    "typeConfiguration": {
        "properties": {
            "PagerDutyAccess": {
                "$ref": "#/definitions/PagerDutyAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "PagerDutyAccess"
        ]
    },
    "properties": {
        "ScheduleLayers": {
            "description": "A list of schedule layers.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ScheduleLayer"
            },
            "minItems": 1
        },
        "TimeZone": {
            "description": "The time zone of the schedule.",
            "type": "string"
        },
        "Name": {
            "description": "The name of the schedule.",
            "type": "string"
        },
        "Description": {
            "description": "The description of the schedule",
            "type": "string"
        },
        "FinalSchedule": {
            "$ref": "#/definitions/SubSchedule"
        },
        "OverridesSubschedule": {
            "$ref": "#/definitions/SubSchedule"
        },
        "Id": {
            "$ref": "#/definitions/Id"
        },
        "Summary": {
            "$ref": "#/definitions/Summary"
        },
        "Type": {
            "description": "The type of object being created.",
            "type": "string",
            "enum": [
                "schedule"
            ]
        },
        "Self": {
            "$ref": "#/definitions/Self"
        },
        "HtmlUrl": {
            "$ref": "#/definitions/HtmlUrl"
        },
        "Users": {
            "description": "An array of all of the users on the schedule.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/User"
            },
            "minItems": 1
        },
        "Teams": {
            "description": "An array of all of the teams on the schedule.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/Team"
            }
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "TimeZone"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Summary",
        "/properties/Type",
        "/properties/HtmlUrl",
        "/properties/Users/*/Id"
    ],
    "writeOnlyProperties": [
        "/properties/FinalSchedule",
        "/properties/OverridesSubschedule",
        "/properties/ScheduleLayers/*/Restrictions/*/StartDayOfWeek"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "update": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
