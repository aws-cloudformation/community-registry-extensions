
## Rollbar::Teams::Team

Manage a team on Rollbar.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-rollbar-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Rollbar::Teams::Team",
    "description": "Manage a team on Rollbar.",
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
        "Name": {
            "description": "Name of the team. Max length 32 characters.",
            "type": "string",
            "pattern": "^[a-zA-Z0-9\\-\\_ ]{1,32}$"
        },
        "AccessLevel": {
            "description": "Can be standard, light, or view.",
            "type": "string",
            "enum": [
                "standard",
                "light",
                "view"
            ]
        },
        "Id": {
            "description": "The team ID.",
            "type": "integer"
        },
        "AccountId": {
            "description": "The account ID where the team belongs to.",
            "type": "integer"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "AccessLevel"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/AccountId"
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
        "delete": {
            "permissions": []
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
