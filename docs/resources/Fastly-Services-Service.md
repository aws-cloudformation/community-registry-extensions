
## Fastly::Services::Service

Manage a Fastly service.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Services::Service",
    "description": "Manage a Fastly service.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-fastly-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-fastly-resource-providers",
    "definitions": {
        "FastlyAccess": {
            "description": "Properties needed to access Fastly.",
            "type": "object",
            "properties": {
                "Token": {
                    "type": "string",
                    "description": "API token used to access Fastly"
                }
            },
            "required": [
                "Token"
            ],
            "additionalProperties": false
        },
        "Comment": {
            "description": "A freeform descriptive note.",
            "type": "string",
            "pattern": "^[a-zA-Z0-9_';:, \\!\\-\\.\\*\\\"\\?]*$"
        },
        "CreatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "CustomerId": {
            "description": "Alphanumeric string identifying the customer. Read-only.",
            "type": "string"
        },
        "DeletedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "Id": {
            "description": "Alphanumeric string identifying the service. Read-only.",
            "type": "string"
        },
        "Name": {
            "description": "The name of the service.",
            "type": "string",
            "minLength": 1
        },
        "PublishKey": {
            "description": "Unused at this time.",
            "type": "string"
        },
        "Paused": {
            "description": "Whether the service is paused. Services are paused due to a lack of traffic for an extended period of time. Services are resumed either when a draft version is activated or a locked version is cloned and reactivated.",
            "type": "boolean"
        },
        "Type": {
            "description": "The type of this service.",
            "type": "string",
            "enum": [
                "vcl",
                "wasm"
            ]
        },
        "UpdatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        }
    },
    "typeConfiguration": {
        "properties": {
            "FastlyAccess": {
                "$ref": "#/definitions/FastlyAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "FastlyAccess"
        ]
    },
    "properties": {
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "Comment": {
            "$ref": "#/definitions/Comment"
        },
        "Paused": {
            "$ref": "#/definitions/Paused"
        },
        "Id": {
            "$ref": "#/definitions/Id"
        },
        "ActiveVersionId": {
            "description": "The number of the active version.",
            "type": "string"
        },
        "LatestVersionId": {
            "description": "The number of the latest version.",
            "type": "string"
        },
        "Type": {
            "$ref": "#/definitions/Type"
        },
        "CustomerId": {
            "$ref": "#/definitions/CustomerId"
        },
        "CreatedAt": {
            "$ref": "#/definitions/CreatedAt"
        },
        "UpdatedAt": {
            "$ref": "#/definitions/UpdatedAt"
        },
        "DeletedAt": {
            "$ref": "#/definitions/DeletedAt"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/ActiveVersionId",
        "/properties/LatestVersionId",
        "/properties/Type",
        "/properties/Paused",
        "/properties/CustomerId",
        "/properties/CreatedAt",
        "/properties/UpdatedAt",
        "/properties/DeletedAt"
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
