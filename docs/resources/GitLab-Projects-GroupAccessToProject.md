
## GitLab::Projects::GroupAccessToProject

## Adds a group as a member of a GitLab project

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Projects::GroupAccessToProject",
    "description": "Adds a group as a member of a GitLab project",
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
        "MembershipId": {
            "description": "Unique identifier for this membership resource, constructed by concatenating the other IDs",
            "type": "string"
        },
        "ProjectId": {
            "description": "ID of the project to which the group should be added",
            "type": "integer"
        },
        "GroupId": {
            "description": "ID of the group which should be added to the project",
            "type": "integer"
        },
        "AccessLevel": {
            "description": "The access level to grant to this group for the project, e.g. 'guest', 'developer', or 'maintainer'. Note the GitLab API may not allow all values.",
            "type": "string",
            "enum": [
                "None",
                "Minimal Access",
                "Guest",
                "Reporter",
                "Developer",
                "Maintainer",
                "Owner",
                "Admin"
            ]
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "ProjectId",
        "GroupId",
        "AccessLevel"
    ],
    "readOnlyProperties": [
        "/properties/MembershipId"
    ],
    "createOnlyProperties": [
        "/properties/ProjectId",
        "/properties/GroupId"
    ],
    "primaryIdentifier": [
        "/properties/ProjectId",
        "/properties/GroupId",
        "/properties/MembershipId"
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
