
## GitLab::Groups::Group

## Creates a group in GitLab

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Groups::Group",
    "description": "Creates a group in GitLab",
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
        "Id": {
            "description": "The ID of the group",
            "type": "integer"
        },
        "Name": {
            "description": "Name of the group to create",
            "type": "string"
        },
        "Path": {
            "description": "Path of the group to create",
            "type": "string"
        },
        "ParentId": {
            "description": "ID of the group's parent",
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
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/Path",
        "/properties/ParentId"
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
