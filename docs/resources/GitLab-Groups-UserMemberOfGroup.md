
## GitLab::Groups::UserMemberOfGroup

## Adds a user as a member of a GitLab group

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Groups::UserMemberOfGroup",
    "description": "Adds a user as a member of a GitLab group",
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
        "GroupId": {
            "description": "ID of the group to which the user should be added",
            "type": "integer"
        },
        "UserId": {
            "description": "ID (numeric) of the user to add to the group. Either this or Username but not both should be supplied.",
            "type": "integer"
        },
        "Username": {
            "description": "Username (handle, e.g. often written starting with '@') of the user to add to the group. Either this or the UserId but not both should be supplied.",
            "type": "string"
        },
        "AccessLevel": {
            "description": "The access level to grant to this user in the group, e.g. 'Guest', 'Developer', or 'Maintainer'. Note the GitLab API may not allow all values.",
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
    "required": [
        "GroupId",
        "AccessLevel"
    ],
    "readOnlyProperties": [
        "/properties/MembershipId"
    ],
    "createOnlyProperties": [
        "/properties/GroupId",
        "/properties/UserId",
        "/properties/Username"
    ],
    "primaryIdentifier": [
        "/properties/MembershipId",
        "/properties/GroupId",
        "/properties/UserId",
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
