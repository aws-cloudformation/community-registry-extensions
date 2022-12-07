
## GitLab::Projects::Project

## Creates a project in GitLab

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Projects::Project",
    "description": "Creates a project in GitLab",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-gitlab-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-gitlab-resource-providers",
    "definitions": {
        "GitLabAccess": {
            "type": "object",
            "properties": {
                "Url": {
                    "description": "URL of the GitLab Server",
                    "type": "string"
                },
                "AccessToken": {
                    "description": "Access Token",
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
        "Name": {
            "description": "The name of the project to create",
            "type": "string",
            "maxLength": 64
        },
        "Path": {
            "description": "The path of the project",
            "type": "string",
            "maxLength": 64,
            "pattern": "^[a-zA-Z0-9_';:, \\!\\-\\.\\*\\\"\\?]*$"
        },
        "Public": {
            "description": "Whether the project should be public (default false)",
            "type": "boolean"
        },
        "Id": {
            "description": "The ID of the project",
            "type": "integer"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/Path"
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
    },
    "typeConfiguration": {
        "properties": {
            "GitLabAccess": {
                "$ref": "#/definitions/GitLabAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "GitLabAccess"
        ]
    }
}
{% endhighlight %}
