
## GitHub::Repositories::Collaborator

The Collaborators resource allows you to add, invite, and remove collaborators from a repository.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Repositories::Collaborator",
    "description": "The Collaborators resource allows you to add, invite, and remove collaborators from a repository.",
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
        "Username": {
            "description": "The login name for the GitHub user account.",
            "type": "string"
        },
        "Permission": {
            "description": "The permission to grant the collaborator. Only valid on organization-owned repositories. In addition to the enumerated values, you can also specify a custom repository role name, if the owning organization has defined any..",
            "type": "string",
            "default": "push",
            "enum": [
                "pull",
                "push",
                "admin",
                "maintain",
                "triage"
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Owner",
        "Repository",
        "Username"
    ],
    "primaryIdentifier": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Username"
    ],
    "createOnlyProperties": [
        "/properties/Owner",
        "/properties/Repository",
        "/properties/Username"
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
