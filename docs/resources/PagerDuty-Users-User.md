
## PagerDuty::Users::User

Manage a user in PagerDuty.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::Users::User",
    "description": "Manage a user in PagerDuty.",
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
        "ContactMethod": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.",
                    "type": "string",
                    "enum": [
                        "email_contact_method_reference",
                        "phone_contact_method_reference",
                        "push_notification_contact_method_reference",
                        "sms_contact_method_reference"
                    ]
                },
                "Id": {
                    "type": "string"
                },
                "Summary": {
                    "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
                    "type": "string"
                },
                "HtmlUrl": {
                    "description": "A URL at which the entity is uniquely displayed in the Web app",
                    "type": "string"
                }
            },
            "required": [
                "Type",
                "Id"
            ],
            "additionalProperties": false
        },
        "NotificationRule": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "A string that determines the schema of the object. This must be the standard name for the entity, suffixed by _reference if the object is a reference.",
                    "type": "string",
                    "enum": [
                        "assignment_notification_rule_reference"
                    ]
                },
                "Id": {
                    "type": "string"
                },
                "Summary": {
                    "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
                    "type": "string"
                },
                "HtmlUrl": {
                    "description": "A URL at which the entity is uniquely displayed in the Web app",
                    "type": "string"
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
        "Name": {
            "description": "The name of the user.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "Email": {
            "description": "The user's email address.",
            "type": "string",
            "minLength": 6,
            "maxLength": 100
        },
        "TimeZone": {
            "description": "The preferred time zone name. If null, the account's time zone will be used.",
            "type": "string"
        },
        "Color": {
            "description": "The schedule color.",
            "type": "string"
        },
        "Role": {
            "description": "The user role. Account must have the read_only_users ability to set a user as a read_only_user or a read_only_limited_user, and must have advanced permissions abilities to set a user as observer or restricted_access.",
            "type": "string",
            "enum": [
                "admin",
                "limited_user",
                "observer",
                "owner",
                "read_only_user",
                "restricted_access",
                "read_only_limited_user",
                "user"
            ]
        },
        "Description": {
            "description": "The user's bio.",
            "type": "string"
        },
        "JobTitle": {
            "description": "The user's title.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "Id": {
            "description": "The ID of the user",
            "type": "string"
        },
        "Summary": {
            "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
            "type": "string"
        },
        "Type": {
            "description": "The type of object being created.",
            "type": "string",
            "enum": [
                "user"
            ]
        },
        "HtmlUrl": {
            "description": "A URL at which the entity is uniquely displayed in the Web app",
            "type": "string"
        },
        "AvatarUrl": {
            "description": "The URL of the user's avatar.",
            "type": "string"
        },
        "InvitationSent": {
            "description": "If true, the user has an outstanding invitation.",
            "type": "boolean"
        },
        "ContactMethods": {
            "description": "The list of contact methods for the user.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ContactMethod"
            }
        },
        "NotificationRules": {
            "description": "The list of notification rules for the user.",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/NotificationRule"
            }
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "Email"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Summary",
        "/properties/Type",
        "/properties/HtmlUrl",
        "/properties/AvatarUrl",
        "/properties/InvitationSent"
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
