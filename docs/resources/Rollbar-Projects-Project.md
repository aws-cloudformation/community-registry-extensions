
## Rollbar::Projects::Project

Manage a project on Rollbar.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-rollbar-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Rollbar::Projects::Project",
    "description": "Manage a project on Rollbar.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers",
    "definitions": {
        "RollbarAccess": {
            "description": "Properties needed to access Rollbar.",
            "type": "object",
            "properties": {
                "Token": {
                    "type": "string",
                    "description": "API token used to access Rollbar."
                }
            },
            "required": [
                "Token"
            ],
            "additionalProperties": false
        },
        "Slack": {
            "description": "Configuring Slack notifications integration.",
            "type": "object",
            "properties": {
                "Enabled": {
                    "description": "Enable the Slack notifications globally",
                    "type": "boolean"
                },
                "ServiceAccountId": {
                    "description": "You can find your Service Account ID in https://rollbar.com/settings/integrations/#slack",
                    "type": "integer"
                },
                "Channel": {
                    "description": "The default Slack channel to send the messages",
                    "type": "string"
                },
                "ShowMessageButtons": {
                    "description": "Show the Slack actionable buttons",
                    "type": "boolean"
                }
            },
            "required": [
                "Enabled",
                "ServiceAccountId",
                "Channel"
            ],
            "additionalProperties": false
        },
        "Webhook": {
            "description": "Configuring Webhook notifications integration.",
            "type": "object",
            "properties": {
                "Enabled": {
                    "description": "Enable the webhook notifications globally",
                    "type": "boolean"
                },
                "Url": {
                    "description": "The webhook url",
                    "type": "string"
                }
            },
            "required": [
                "Enabled",
                "Url"
            ],
            "additionalProperties": false
        },
        "PagerDuty": {
            "description": "Configuring PagerDuty notifications integration.",
            "type": "object",
            "properties": {
                "Enabled": {
                    "description": "Enable the PagerDuty notifications globally",
                    "type": "boolean"
                },
                "ServiceKey": {
                    "description": "PagerDuty Service API Key",
                    "type": "string"
                }
            },
            "required": [
                "Enabled",
                "ServiceKey"
            ],
            "additionalProperties": false
        },
        "Email": {
            "description": "Configuring Email notifications integration.",
            "type": "object",
            "properties": {
                "Enabled": {
                    "description": "Enable the Email notifications globally",
                    "type": "boolean"
                },
                "IncludeRequestParams": {
                    "description": "Whether to include request parameters",
                    "type": "boolean"
                }
            },
            "required": [
                "Enabled"
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
            "description": "Name of the project. Must start with a letter; can contain letters, numbers, spaces, underscores, hyphens, periods, and commas. Max length 32 characters.",
            "type": "string",
            "pattern": "^[a-zA-Z][\\w\\_\\-\\.\\,]{0,31}$"
        },
        "Slack": {
            "$ref": "#/definitions/Slack"
        },
        "Webhook": {
            "$ref": "#/definitions/Webhook"
        },
        "PagerDuty": {
            "$ref": "#/definitions/PagerDuty"
        },
        "Email": {
            "$ref": "#/definitions/Email"
        },
        "Id": {
            "description": "The project ID.",
            "type": "integer"
        },
        "AccountId": {
            "description": "The account ID where the project belongs to.",
            "type": "integer"
        },
        "Status": {
            "description": "Whether or not this project is enabled.",
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
        "Name"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "writeOnlyProperties": [
        "/properties/Slack",
        "/properties/Webhook",
        "/properties/PagerDuty",
        "/properties/Email"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/AccountId",
        "/properties/Status"
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
