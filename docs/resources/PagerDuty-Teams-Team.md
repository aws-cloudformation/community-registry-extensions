
## PagerDuty::Teams::Team

Manage a team in PagerDuty.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-pagerduty-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "PagerDuty::Teams::Team",
    "description": "Manage a team in PagerDuty.",
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
        "Name": {
            "description": "The name of the team.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "Description": {
            "description": "The description of the team.",
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
        },
        "Id": {
            "type": "string"
        },
        "Summary": {
            "description": "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
            "type": "string"
        },
        "HtmlUrl": {
            "description": "A URL at which the entity is uniquely displayed in the Web app.",
            "type": "string"
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
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "Description": {
            "$ref": "#/definitions/Description"
        },
        "Id": {
            "$ref": "#/definitions/Id"
        },
        "Summary": {
            "$ref": "#/definitions/Summary"
        },
        "Type": {
            "description": "The type of object being created.",
            "type": "string",
            "enum": [
                "team"
            ]
        },
        "HtmlUrl": {
            "$ref": "#/definitions/HtmlUrl"
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
        "/properties/Summary",
        "/properties/Type",
        "/properties/HtmlUrl"
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
