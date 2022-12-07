
## GitHub::Teams::Team

## Manage a team in Github

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Teams::Team",
    "description": "Manage a team in Github",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-github-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-github-resource-providers",
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
    "properties": {
        "Name": {
            "description": "Team name",
            "type": "string"
        },
        "Organization": {
            "description": "The Organization that the team will belong to",
            "type": "string"
        },
        "Description": {
            "description": "Describe the team",
            "type": "string"
        },
        "Privacy": {
            "description": "The privacy for the team - must be either secret or closed",
            "type": "string",
            "enum": [
                "secret",
                "closed"
            ]
        },
        "Slug": {
            "description": "The Organization unique identifier for the team",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "Organization"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/Organization"
    ],
    "readOnlyProperties": [
        "/properties/Slug"
    ],
    "primaryIdentifier": [
        "/properties/Organization",
        "/properties/Slug"
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
