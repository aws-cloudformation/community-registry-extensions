
## Fastly::Dictionary::Dictionary

## Manage a Fastly service dictionary.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Dictionary::Dictionary",
    "description": "Manage a Fastly service dictionary.",
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
            "description": "Name for the Dictionary",
            "type": "string"
        },
        "WriteOnly": {
            "description": "Determines if items in the dictionary are readable or not.",
            "type": "boolean",
            "default": false
        },
        "CreatedAt": {
            "description": "Date and time in ISO 8601 format.",
            "type": "string",
            "format": "date-time"
        },
        "DeletedAt": {
            "description": "Date and time in ISO 8601 format.",
            "type": "string",
            "format": "date-time"
        },
        "Id": {
            "description": "Alphanumeric string identifying a Dictionary",
            "type": "string"
        },
        "ServiceId": {
            "description": "Alphanumeric string identifying the service. Read-only.",
            "type": "string"
        },
        "UpdatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "VersionId": {
            "description": "Alphanumeric string identifying the service version.",
            "type": "string"
        },
        "Version": {
            "description": "Integer identifying a domain version. Read-only.",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "ServiceId",
        "VersionId"
    ],
    "readOnlyProperties": [
        "/properties/WriteOnly",
        "/properties/CreatedAt",
        "/properties/Id",
        "/properties/UpdatedAt",
        "/properties/Version"
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
