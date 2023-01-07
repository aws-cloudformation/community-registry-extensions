
## Fastly::Dictionary::DictionaryItem

Manage a Fastly service dictionary item.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Dictionary::DictionaryItem",
    "description": "Manage a Fastly service dictionary item.",
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
        "ItemKey": {
            "description": "Item key",
            "type": "string"
        },
        "ItemValue": {
            "description": "Item key",
            "type": "string"
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
        "DictionaryId": {
            "description": "Alphanumeric string identifying a Dictionary.",
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
        }
    },
    "additionalProperties": false,
    "required": [
        "ItemKey",
        "ServiceId",
        "DictionaryId"
    ],
    "readOnlyProperties": [
        "/properties/CreatedAt",
        "/properties/DeletedAt",
        "/properties/UpdatedAt"
    ],
    "createOnlyProperties": [
        "/properties/ItemKey",
        "/properties/ServiceId",
        "/properties/DictionaryId"
    ],
    "primaryIdentifier": [
        "/properties/ItemKey",
        "/properties/ServiceId",
        "/properties/DictionaryId"
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
