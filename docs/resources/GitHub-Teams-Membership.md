
## GitHub::Teams::Membership

Manages people&#39;s membership to GitHub teams

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Teams::Membership",
    "description": "Manages people's membership to GitHub teams",
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
            "description": "The organization name. The name is not case sensitive. If not specified, then the managed repository will be within the currently logged-in user account.",
            "type": "string"
        },
        "TeamSlug": {
            "description": "TThe slug of the team name.",
            "type": "string"
        },
        "Username": {
            "description": "The handle for the GitHub user account.",
            "type": "string",
            "pattern": "^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
        },
        "Role": {
            "description": "The handle for the GitHub user account.",
            "type": "string",
            "default": "member",
            "enum": [
                "member",
                "maintainer"
            ]
        },
        "State": {
            "description": "Membership state",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Org",
        "TeamSlug"
    ],
    "primaryIdentifier": [
        "/properties/Org",
        "/properties/TeamSlug",
        "/properties/Username"
    ],
    "createOnlyProperties": [
        "/properties/Org",
        "/properties/TeamSlug",
        "/properties/Username"
    ],
    "readOnlyProperties": [
        "/properties/State"
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
