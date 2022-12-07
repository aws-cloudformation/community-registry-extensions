
## Fastly::Services::Healthcheck

Manage a Fastly service health check.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Services::Healthcheck",
    "description": "Manage a Fastly service health check.",
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
        "ServiceId": {
            "description": "Alphanumeric string identifying the service.",
            "type": "string"
        },
        "VersionId": {
            "description": "Alphanumeric string identifying the service version.",
            "type": "string"
        },
        "CheckInterval": {
            "description": "How often to run the healthcheck in milliseconds.",
            "type": "integer"
        },
        "Comment": {
            "description": "A freeform descriptive note.",
            "type": "string"
        },
        "ExpectedResponse": {
            "description": "The status code expected from the host.",
            "type": "integer",
            "minimum": 200,
            "maximum": 599
        },
        "Host": {
            "description": "Which host to check.",
            "type": "string"
        },
        "HttpVersion": {
            "description": "Whether to use version 1.0 or 1.1 HTTP.",
            "type": "string",
            "enum": [
                "1.0",
                "1.1"
            ]
        },
        "Initial": {
            "description": "When loading a config, the initial number of probes to be seen as OK.",
            "type": "integer"
        },
        "Method": {
            "description": "Which HTTP method to use.",
            "type": "string",
            "enum": [
                "HEAD",
                "GET",
                "POST"
            ]
        },
        "Name": {
            "description": "The name of the healthcheck.",
            "type": "string"
        },
        "Path": {
            "description": "The path to check.",
            "type": "string"
        },
        "Threshold": {
            "description": "How many healthchecks must succeed to be considered healthy.",
            "type": "integer"
        },
        "Timeout": {
            "description": "Timeout in milliseconds.",
            "type": "integer"
        },
        "Window": {
            "description": "The number of most recent healthcheck queries to keep for this healthcheck.",
            "type": "integer"
        },
        "CreatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "UpdatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "DeletedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "Version": {
            "description": "Integer identifying a healthcheck version. Read-only.",
            "type": "string"
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
        "CheckInterval": {
            "$ref": "#/definitions/CheckInterval"
        },
        "Comment": {
            "$ref": "#/definitions/Comment"
        },
        "ExpectedResponse": {
            "$ref": "#/definitions/ExpectedResponse"
        },
        "Host": {
            "$ref": "#/definitions/Host"
        },
        "HttpVersion": {
            "$ref": "#/definitions/HttpVersion"
        },
        "Initial": {
            "$ref": "#/definitions/Initial"
        },
        "Method": {
            "$ref": "#/definitions/Method"
        },
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "Path": {
            "$ref": "#/definitions/Path"
        },
        "Threshold": {
            "$ref": "#/definitions/Threshold"
        },
        "Timeout": {
            "$ref": "#/definitions/Timeout"
        },
        "Window": {
            "$ref": "#/definitions/Window"
        },
        "ServiceId": {
            "$ref": "#/definitions/ServiceId"
        },
        "VersionId": {
            "$ref": "#/definitions/VersionId"
        },
        "HealthcheckName": {
            "$ref": "#/definitions/Name"
        },
        "Version": {
            "$ref": "#/definitions/Version"
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
        "Name",
        "ServiceId",
        "VersionId"
    ],
    "readOnlyProperties": [
        "/properties/Version",
        "/properties/CreatedAt",
        "/properties/UpdatedAt",
        "/properties/DeletedAt"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/ServiceId",
        "/properties/VersionId"
    ],
    "primaryIdentifier": [
        "/properties/Name",
        "/properties/ServiceId",
        "/properties/VersionId"
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
