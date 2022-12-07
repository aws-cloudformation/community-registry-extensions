
## Rollbar::Teams::Membership

## Manage a team membership for a user or project on Rollbar.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-rollbar-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Rollbar::Teams::Membership",
    "description": "Manage a team membership for a user or project on Rollbar.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers",
    "definitions": {
        "RollbarAccess": {
            "description": "Properties needed to access Rollbar.",
            "type": "object",
            "properties": {
                "Token": {
                    "type": "string",
                    "description": "API token used to access Rollbar"
                }
            },
            "required": [
                "Token"
            ],
            "additionalProperties": false
        }
    },
    "typeConfiguration": {
        "properties": {
            "RollbarAccess": {
                "$ref": "#/definitions/RollbarAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "RollbarAccess"
        ]
    },
    "properties": {
        "TeamId": {
            "description": "The team ID for the membership.",
            "type": "integer"
        },
        "MemberId": {
            "description": "The ID of the user or project to associate to the team.",
            "type": "integer"
        },
        "MemberType": {
            "description": "The type of membership",
            "type": "string",
            "enum": [
                "user",
                "project"
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "TeamId",
        "MemberId",
        "MemberType"
    ],
    "createOnlyProperties": [
        "/properties/TeamId",
        "/properties/MemberId",
        "/properties/MemberType"
    ],
    "primaryIdentifier": [
        "/properties/TeamId",
        "/properties/MemberId",
        "/properties/MemberType"
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
