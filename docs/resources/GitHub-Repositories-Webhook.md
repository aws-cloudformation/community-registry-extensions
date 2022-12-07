
## GitHub::Repositories::Webhook

## Repositories can have multiple webhooks installed. Each webhook should have a unique config. Multiple webhooks can share the same config as long as those webhooks do not have any events that overlap.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Repositories::Webhook",
    "description": "Repositories can have multiple webhooks installed. Each webhook should have a unique config. Multiple webhooks can share the same config as long as those webhooks do not have any events that overlap.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-github-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-github-resource-providers",
    "typeConfiguration": {
        "properties": {
            "GitHubAccess": {
                "$ref": "#/definitions/GitHubAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "GitHubAccess"
        ]
    },
    "definitions": {
        "GitHubAccess": {
            "type": "object",
            "properties": {
                "AccessToken": {
                    "description": "Personal Access Token",
                    "type": "string"
                }
            },
            "required": [
                "AccessToken"
            ],
            "additionalProperties": false
        }
    },
    "properties": {
        "Owner": {
            "description": "The organisation owner",
            "type": "string"
        },
        "Name": {
            "description": "Use web to create a webhook. Default: web. This parameter only accepts the value web.",
            "type": "string",
            "default": "web",
            "enum": [
                "web"
            ]
        },
        "Active": {
            "description": "Determines if notifications are sent when the webhook is triggered. Set to true to send notifications.",
            "type": "boolean"
        },
        "Id": {
            "description": "ID of the webhook",
            "type": "number"
        },
        "Events": {
            "description": "Determines what events the hook is triggered for.",
            "type": "array",
            "insertionOrder": false,
            "uniqueItems": true,
            "items": {
                "type": "string"
            }
        },
        "Repository": {
            "description": "The name of the repository. The name is not case sensitive.",
            "type": "string"
        },
        "ContentType": {
            "description": "The media type used to serialize the payloads. Supported values include json and form. The default is form.",
            "type": "string",
            "enum": [
                "form",
                "json"
            ],
            "default": "form"
        },
        "Url": {
            "description": "The URL to which the payloads will be delivered.",
            "type": "string"
        },
        "Secret": {
            "description": "If provided, the secret will be used as the key to generate the HMAC hex digest value for delivery signature headers.",
            "type": "string"
        },
        "InsecureSsl": {
            "description": "Determines whether the SSL certificate of the host for url will be verified when delivering payloads. Supported values include 0 (verification is performed) and 1 (verification is not performed). The default is 0. We strongly recommend not setting this to 1 as you are subject to man-in-the-middle and other attacks.",
            "type": "number",
            "default": 0,
            "enum": [
                0,
                1
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Owner"
    ],
    "readOnlyProperties": [
        "/properties/Id"
    ],
    "primaryIdentifier": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Name"
    ],
    "writeOnlyProperties": [
        "/properties/Secret"
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
