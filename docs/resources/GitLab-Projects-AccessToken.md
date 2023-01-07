
## GitLab::Projects::AccessToken

Creates a Project Access Token in GitLab

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Projects::AccessToken",
    "description": "Creates a Project Access Token in GitLab",
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
            "description": "The name of the Project Access Token to create.",
            "type": "string",
            "maxLength": 64
        },
        "ProjectId": {
            "description": "The ID (numeric) of the project for which this Access Token is created. The project should exist and the user creating the Access Token should have rights to do this on this project.",
            "type": "integer"
        },
        "AccessLevel": {
            "description": "A valid access level. Default value is 40 (Maintainer). Other allowed values are 10 (Guest), 20 (Reporter), and 30 (Developer).",
            "type": "integer"
        },
        "Scopes": {
            "description": "The scopes this Project Access Token will be used for. The list of supported scopes is in the official GitLab documentation here: https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html#scopes-for-a-project-access-token .",
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            }
        },
        "Id": {
            "description": "The ID of the Project Access Token",
            "type": "integer"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "ProjectId",
        "Scopes"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/ProjectId"
    ],
    "readOnlyProperties": [
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/ProjectId",
        "/properties/Name",
        "/properties/Scopes"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
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
