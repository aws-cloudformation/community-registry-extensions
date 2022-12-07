
## Rollbar::Projects::AccessToken

## Manage an access token for a Rollbar project.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-rollbar-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Rollbar::Projects::AccessToken",
    "description": "Manage an access token for a Rollbar project.",
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
        "ProjectId": {
            "description": "The project ID",
            "type": "integer"
        },
        "Name": {
            "description": "Name to identify the access token",
            "type": "string"
        },
        "Scopes": {
            "description": "Scopes to assign to the create access token",
            "type": "array",
            "insertionOrder": false,
            "uniqueItems": true,
            "items": {
                "type": "string",
                "enum": [
                    "write",
                    "read",
                    "post_server_item",
                    "post_client_item"
                ]
            },
            "minItems": 1
        },
        "RateLimitWindowSize": {
            "description": "Period of time (in seconds) for the rate limit configuration",
            "type": "integer",
            "minimum": 0,
            "maximum": 4294967295
        },
        "RateLimitWindowCount": {
            "description": "Number of requests for the defined rate limiting period",
            "type": "integer",
            "minimum": 0,
            "maximum": 4294967295
        },
        "AccessToken": {
            "description": "The project access token",
            "type": "string"
        },
        "Status": {
            "description": "Whether or not this access token is enabled",
            "type": "string",
            "enum": [
                "enabled",
                "disabled"
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "ProjectId",
        "Name",
        "Scopes"
    ],
    "createOnlyProperties": [
        "/properties/ProjectId",
        "/properties/Name",
        "/properties/Scopes"
    ],
    "readOnlyProperties": [
        "/properties/AccessToken",
        "/properties/Status"
    ],
    "primaryIdentifier": [
        "/properties/ProjectId",
        "/properties/AccessToken"
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
