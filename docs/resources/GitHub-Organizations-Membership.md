
## GitHub::Organizations::Membership

## Add people to an organization. Will create an invite and user will only become a member once they accept this invite.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Organizations::Membership",
    "description": "Add people to an organization. Will create an invite and user will only become a member once they accept this invite.",
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
        "Organization": {
            "description": "The Organization the user is being added to",
            "type": "string"
        },
        "Username": {
            "description": "The handle for the GitHub user account",
            "type": "string"
        },
        "Role": {
            "description": "The role for the new member.",
            "type": "string",
            "enum": [
                "admin",
                "member"
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Organization",
        "Username"
    ],
    "primaryIdentifier": [
        "/properties/Username",
        "/properties/Organization"
    ],
    "createOnlyProperties": [
        "/properties/Organization",
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
