
## PagerDuty::Teams::Membership

## Manage a membership of a user into a team in PagerDuty.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::Teams::Membership",
    "description": "Manage a membership of a user into a team in PagerDuty.",
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
        "TeamId": {
            "description": "The ID of the resource.",
            "type": "string"
        },
        "UserId": {
            "description": "The user ID on the team.",
            "type": "string"
        },
        "Role": {
            "description": "The role of the user on the team.",
            "type": "string",
            "enum": [
                "observer",
                "responder",
                "manager"
            ]
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
        "TeamId": {
            "$ref": "#/definitions/TeamId"
        },
        "UserId": {
            "$ref": "#/definitions/UserId"
        },
        "Role": {
            "$ref": "#/definitions/Role"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "TeamId",
        "UserId"
    ],
    "createOnlyProperties": [
        "/properties/TeamId",
        "/properties/UserId"
    ],
    "primaryIdentifier": [
        "/properties/TeamId",
        "/properties/UserId"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
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
