
## GitHub::Git::Tag

## Manage a git tag on GitHub

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Git::Tag",
    "description": "Manage a git tag on GitHub",
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
        "Owner": {
            "description": "The account owner of the repository. The name is not case sensitive.",
            "type": "string"
        },
        "Repository": {
            "description": "The name of the repository. The name is not case sensitive.",
            "type": "string"
        },
        "Tag": {
            "description": "The name of git tag.",
            "type": "string"
        },
        "Sha": {
            "description": "The SHA1 value for this reference.",
            "type": "string"
        },
        "Force": {
            "description": "Indicates whether to force the update or to make sure the update is a fast-forward update. Leaving this out or setting it to false will make sure you're not overwriting work. This is used only during updates",
            "type": "boolean",
            "default": false
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Owner",
        "Repository",
        "Tag",
        "Sha"
    ],
    "createOnlyProperties": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Tag"
    ],
    "primaryIdentifier": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Tag"
    ],
    "writeOnlyProperties": [
        "/properties/Force"
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
