
## newrelic::cloudformation::tagging

CRUD operations for New Relic Tags via the NerdGraph API

- [Source](https:&#x2F;&#x2F;github.com&#x2F;newrelic-experimental&#x2F;newrelic-cloudformation-resource-providers-tagging.git) 
- [Documentation]()

Published by newrelic-experimental

## Schema
{% highlight json %}
{
    "typeName": "newrelic::cloudformation::tagging",
    "description": "CRUD operations for New Relic Tags via the NerdGraph API",
    "sourceUrl": "https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-tagging.git",
    "properties": {
        "Endpoint": {
            "type": "string",
            "default": "https://api.newrelic.com/graphql"
        },
        "APIKey": {
            "type": "string"
        },
        "Guid": {
            "type": "string"
        },
        "EntityGuid": {
            "type": "string"
        },
        "ListQueryFilter": {
            "type": "string"
        },
        "Variables": {
            "type": "object",
            "patternProperties": {
                "^[A-Za-z0-9]{1,64}$": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "Tags": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/TagObject"
            }
        },
        "Semantics": {
            "type": "string",
            "default": "Map"
        }
    },
    "additionalProperties": false,
    "required": [
        "APIKey",
        "EntityGuid",
        "Tags"
    ],
    "primaryIdentifier": [
        "/properties/Guid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "newrelic:NerdGraphCreate"
            ]
        },
        "read": {
            "permissions": [
                "newrelic:NerdGraphDescribe"
            ]
        },
        "update": {
            "permissions": [
                "newrelic:NerdGraphUpdate"
            ]
        },
        "delete": {
            "permissions": [
                "newrelic:NerdGraphDelete"
            ]
        }
    },
    "definitions": {
        "TagObject": {
            "type": "object",
            "required": [
                "Key",
                "Values"
            ],
            "properties": {
                "Key": {
                    "type": "string"
                },
                "Values": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                }
            },
            "additionalProperties": false
        }
    }
}
{% endhighlight %}
