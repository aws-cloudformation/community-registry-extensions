
## PagerDuty::EscalationPolicies::EscalationPolicy

Manage an escalation policy in PagerDuty.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::EscalationPolicies::EscalationPolicy",
    "description": "Manage an escalation policy in PagerDuty.",
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
        "EscalationRule": {
            "type": "object",
            "properties": {
                "EscalationDelayInMinutes": {
                    "description": "The number of minutes before an unacknowledged incident escalates away from this rule.",
                    "type": "integer"
                },
                "Targets": {
                    "description": "The targets an incident should be assigned to upon reaching this rule.",
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/Target"
                    },
                    "minItems": 1,
                    "maxItems": 10
                }
            },
            "required": [
                "EscalationDelayInMinutes",
                "Targets"
            ],
            "additionalProperties": false
        },
        "Target": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.",
                    "type": "string",
                    "enum": [
                        "user",
                        "schedule",
                        "user_reference",
                        "schedule_reference"
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
        "Team": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference./, =, +, and -.",
                    "type": "string",
                    "enum": [
                        "team_reference"
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
        "HtmlUrl": {
            "description": "A URL at which the entity is uniquely displayed in the Web app.",
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Summary": {
            "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
            "type": "string"
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
        "Name": {
            "description": "The name of the escalation policy.",
            "type": "string",
            "minLength": 1
        },
        "Description": {
            "description": "Escalation policy description.",
            "type": "string"
        },
        "NumLoops": {
            "description": "The number of times the escalation policy will repeat after reaching the end of its escalation.",
            "type": "integer",
            "default": 0,
            "minimum": 0
        },
        "OnCallHandoffNotifications": {
            "description": "Determines how on call handoff notifications will be sent for users on the escalation policy. Defaults to \"if_has_services\".",
            "type": "string",
            "enum": [
                "if_has_services",
                "always"
            ]
        },
        "EscalationRules": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/EscalationRule"
            },
            "minItems": 1
        },
        "Teams": {
            "description": "Teams associated with the policy. Account must have the teams ability to use this parameter.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/Team"
            },
            "minItems": 1
        },
        "Id": {
            "$ref": "#/definitions/Id"
        },
        "Type": {
            "description": "The type of object being created.",
            "type": "string",
            "default": "escalation_policy",
            "enum": [
                "escalation_policy"
            ]
        },
        "Summary": {
            "$ref": "#/definitions/Summary"
        },
        "HtmlUrl": {
            "$ref": "#/definitions/HtmlUrl"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "EscalationRules"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Type",
        "/properties/Summary",
        "/properties/HtmlUrl"
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
