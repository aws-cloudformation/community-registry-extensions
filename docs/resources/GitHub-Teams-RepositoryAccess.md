
## GitHub::Teams::RepositoryAccess

## Manage a team access to a repository in GitHub.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Teams::RepositoryAccess",
    "description": "Manage a team access to a repository in GitHub.",
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
        "Org": {
            "description": "The organization name. The name is not case sensitive.",
            "type": "string"
        },
        "Team": {
            "description": "The slug of the team name.",
            "type": "string"
        },
        "Owner": {
            "description": "The account owner of the repository. The name is not case sensitive.",
            "type": "string"
        },
        "Repository": {
            "description": "The name of the repository. The name is not case sensitive.",
            "type": "string"
        },
        "Permission": {
            "description": "The permission to grant the team on this repository. In addition to the enumerated values, you can also specify a custom repository role name, if the owning organization has defined any. If no permission is specified, the team's permission attribute will be used to determine what permission to grant the team on this repository.",
            "type": "string",
            "enum": [
                "pull",
                "push",
                "admin",
                "maintain",
                "triage"
            ],
            "default": "push"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Org",
        "Team",
        "Owner",
        "Repository"
    ],
    "createOnlyProperties": [
        "/properties/Org",
        "/properties/Team",
        "/properties/Owner",
        "/properties/Repository"
    ],
    "primaryIdentifier": [
        "/properties/Org",
        "/properties/Team",
        "/properties/Owner",
        "/properties/Repository"
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
