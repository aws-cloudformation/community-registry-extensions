
## Fastly::Services::Domain

Manage a Fastly service domain.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Services::Domain",
    "description": "Manage a Fastly service domain.",
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
        "Name": {
            "description": "The name of the domain or domains associated with this service.",
            "type": "string",
            "minLength": 1
        },
        "Comment": {
            "description": "A freeform descriptive note.",
            "type": "string"
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
            "description": "Integer identifying a domain version. Read-only.",
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
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "Comment": {
            "$ref": "#/definitions/Comment"
        },
        "ServiceId": {
            "$ref": "#/definitions/ServiceId"
        },
        "VersionId": {
            "$ref": "#/definitions/VersionId"
        },
        "Version": {
            "$ref": "#/definitions/Version"
        },
        "DomainName": {
            "$ref": "#/definitions/Name"
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
        "/properties/DomainName",
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
