
## GitLab::Groups::GroupAccessToGroup

## Adds a group as a member of another GitLab group

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Groups::GroupAccessToGroup",
    "description": "Adds a group as a member of another GitLab group",
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
        "SharedGroupId": {
            "description": "ID of the group which should be shared, i.e. the group to which access is being granted",
            "type": "integer"
        },
        "SharedWithGroupId": {
            "description": "ID of the group to share with, i.e. the group being given access to another group",
            "type": "integer"
        },
        "AccessLevel": {
            "description": "The access level to grant to the shared-with group for acessing the shared group, e.g. 'Guest', 'Developer', or 'Maintainer'. Note the GitLab API may not allow all values.",
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
        "SharedGroupId",
        "SharedWithGroupId",
        "AccessLevel"
    ],
    "readOnlyProperties": [
        "/properties/MembershipId"
    ],
    "createOnlyProperties": [
        "/properties/SharedGroupId",
        "/properties/SharedWithGroupId"
    ],
    "primaryIdentifier": [
        "/properties/SharedGroupId",
        "/properties/SharedWithGroupId",
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
