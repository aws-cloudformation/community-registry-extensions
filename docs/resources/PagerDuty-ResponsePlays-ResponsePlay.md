
## PagerDuty::ResponsePlays::ResponsePlay

## Manage a response play in PagerDuty

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::ResponsePlays::ResponsePlay",
    "description": "Manage a response play in PagerDuty",
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
            "type": "string"
        },
        "Summary": {
            "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
            "type": "string"
        },
        "HtmlUrl": {
            "description": "A URL at which the entity is uniquely displayed in the Web app.",
            "type": "string"
        },
        "Team": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.",
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
        "Subscriber": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.",
                    "type": "string",
                    "enum": [
                        "user_reference",
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
        "Responder": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.",
                    "type": "string",
                    "enum": [
                        "user_reference",
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
        "FromEmail": {
            "description": "The email address of a valid user associated with the account making the request.",
            "type": "string",
            "format": "email"
        },
        "Name": {
            "description": "The name of the response play.",
            "type": "string",
            "minLength": 1
        },
        "Description": {
            "description": "The description of the response play.",
            "type": "string",
            "minLength": 1,
            "maxLength": 349
        },
        "Team": {
            "anyOf": [
                {
                    "$ref": "#/definitions/Team"
                },
                {
                    "type": "object"
                }
            ]
        },
        "Subscribers": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/Subscriber"
            }
        },
        "SubscribersMessage": {
            "description": "The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.",
            "type": "string",
            "minLength": 1
        },
        "Responders": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/Responder"
            }
        },
        "RespondersMessage": {
            "description": "The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.",
            "type": "string",
            "minLength": 1
        },
        "Runnability": {
            "description": "String representing how this response play is allowed to be run. Valid options are:\n\n    services: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play.\n    teams: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the team property for this response play is not empty.\n    responders: This response play can be run manually on an incident by any responders in this account.",
            "type": "string",
            "enum": [
                "services",
                "teams",
                "responders"
            ],
            "default": "services"
        },
        "ConferenceNumber": {
            "description": "The telephone number that will be set as the conference number for any incident on which this response play is run.",
            "type": "string",
            "minLength": 1
        },
        "ConferenceUrl": {
            "description": "The URL that will be set as the conference URL for any incident on which this response play is run.",
            "type": "string",
            "minLength": 1
        },
        "ConferenceType": {
            "description": "This field has three possible values and indicates how the response play was created.\n\n    none : The response play had no conference_number or conference_url set at time of creation.\n    manual : The response play had one or both of conference_number and conference_url set at time of creation.\n    zoom : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom",
            "type": "string",
            "enum": [
                "none",
                "manual",
                "zoom"
            ],
            "default": "none"
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
                "response_play"
            ],
            "default": "response_play"
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
        "FromEmail"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Summary",
        "/properties/Type",
        "/properties/HtmlUrl"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/FromEmail"
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
