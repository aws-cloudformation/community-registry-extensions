
## GitLab::Code::Tag

## Creates a tag against a code ref in GitLab

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-gitlab-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitLab::Code::Tag",
    "description": "Creates a tag against a code ref in GitLab",
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
            "description": "The name of the tag to create",
            "type": "string",
            "maxLength": 64
        },
        "ProjectId": {
            "description": "The ID of the project which will be tagged",
            "type": "integer"
        },
        "Ref": {
            "description": "The reference to the code commit to be tagged, either a commit SHA ID or a branch name (to use the commit which is head of that branch at time of tag creation)",
            "type": "string",
            "maxLength": 64
        },
        "CommitId": {
            "description": "The actual commit SHA ID referenced by this tag, set by the resource provider. This will be equal to Ref if Ref is a commit SHA ID, or set by the provider to point at the commit if Ref is a branch name.",
            "type": "string"
        },
        "Message": {
            "description": "A message to attach to the tag",
            "type": "string"
        },
        "TagId": {
            "description": "A CloudFormation ID to identify this tag",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "ProjectId",
        "Ref"
    ],
    "primaryIdentifier": [
        "/properties/Name",
        "/properties/ProjectId",
        "/properties/TagId"
    ],
    "readOnlyProperties": [
        "/properties/TagId",
        "/properties/CommitId"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/ProjectId",
        "/properties/Ref"
    ],
    "writeOnlyProperties": [
        "/properties/Ref"
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
