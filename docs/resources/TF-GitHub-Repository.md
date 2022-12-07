
## TF::GitHub::Repository

## This resource allows you to create and manage repositories within your
GitHub organization or personal account.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::GitHub::Repository",
    "description": "This resource allows you to create and manage repositories within your\nGitHub organization or personal account.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/github/TF-GitHub-Repository/docs/README.md",
    "definitions": {
        "PagesDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Cname": {
                    "type": "string"
                },
                "Source": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/SourceDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                }
            },
            "required": []
        },
        "TemplateDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Owner": {
                    "type": "string"
                },
                "Repository": {
                    "type": "string"
                }
            },
            "required": [
                "Owner",
                "Repository"
            ]
        },
        "SourceDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Branch": {
                    "type": "string"
                },
                "Path": {
                    "type": "string"
                }
            },
            "required": [
                "Branch"
            ]
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "AllowMergeCommit": {
            "type": "boolean",
            "description": "Set to `false` to disable merge commits on the repository."
        },
        "AllowRebaseMerge": {
            "type": "boolean",
            "description": "Set to `false` to disable rebase merges on the repository."
        },
        "AllowSquashMerge": {
            "type": "boolean",
            "description": "Set to `false` to disable squash merges on the repository."
        },
        "ArchiveOnDestroy": {
            "type": "boolean",
            "description": "Set to `true` to archive the repository instead of deleting on destroy."
        },
        "Archived": {
            "type": "boolean",
            "description": "Specifies if the repository should be archived. Defaults to `false`. **NOTE** Currently, the API does not support unarchiving."
        },
        "AutoInit": {
            "type": "boolean",
            "description": "Set to `true` to produce an initial commit in the repository."
        },
        "DefaultBranch": {
            "type": "string",
            "description": "(Deprecated: Use `github_branch_default` resource instead) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created,\nand after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the\ninitial repository creation and create the target branch inside of the repository prior to setting this attribute."
        },
        "DeleteBranchOnMerge": {
            "type": "boolean",
            "description": "Automatically delete head branch after a pull request is merged. Defaults to `false`."
        },
        "Description": {
            "type": "string",
            "description": "A description of the repository."
        },
        "Etag": {
            "type": "string"
        },
        "FullName": {
            "type": "string"
        },
        "GitCloneUrl": {
            "type": "string"
        },
        "GitignoreTemplate": {
            "type": "string",
            "description": "Use the [name of the template](https://github.com/github/gitignore) without the extension. For example, \"Haskell\"."
        },
        "HasDownloads": {
            "type": "boolean",
            "description": "Set to `true` to enable the (deprecated) downloads features on the repository."
        },
        "HasIssues": {
            "type": "boolean",
            "description": "Set to `true` to enable the GitHub Issues features\non the repository."
        },
        "HasProjects": {
            "type": "boolean",
            "description": "Set to `true` to enable the GitHub Projects features on the repository. Per the GitHub [documentation](https://developer.github.com/v3/repos/#create) when in an organization that has disabled repository projects it will default to `false` and will otherwise default to `true`. If you specify `true` when it has been disabled it will return an error."
        },
        "HasWiki": {
            "type": "boolean",
            "description": "Set to `true` to enable the GitHub Wiki features on\nthe repository."
        },
        "HomepageUrl": {
            "type": "string",
            "description": "URL of a page describing the project."
        },
        "HtmlUrl": {
            "type": "string"
        },
        "HttpCloneUrl": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "IsTemplate": {
            "type": "boolean",
            "description": "Set to `true` to tell GitHub that this is a template repository."
        },
        "LicenseTemplate": {
            "type": "string",
            "description": "Use the [name of the template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension. For example, \"mit\" or \"mpl-2.0\"."
        },
        "Name": {
            "type": "string",
            "description": "The name of the repository."
        },
        "NodeId": {
            "type": "string"
        },
        "Private": {
            "type": "boolean",
            "description": "Set to `true` to create a private repository.\nRepositories are created as public (e.g. open source) by default."
        },
        "RepoId": {
            "type": "number"
        },
        "SshCloneUrl": {
            "type": "string"
        },
        "SvnUrl": {
            "type": "string"
        },
        "Topics": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            },
            "description": "The list of topics of the repository."
        },
        "Visibility": {
            "type": "string",
            "description": "Can be `public` or `private`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be `internal`. The `visibility` parameter overrides the `private` parameter."
        },
        "VulnerabilityAlerts": {
            "type": "boolean"
        },
        "Pages": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/PagesDefinition"
            },
            "maxItems": 1
        },
        "Template": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/TemplateDefinition"
            },
            "maxItems": 1
        }
    },
    "additionalProperties": false,
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Etag",
        "/properties/FullName",
        "/properties/GitCloneUrl",
        "/properties/HtmlUrl",
        "/properties/HttpCloneUrl",
        "/properties/Id",
        "/properties/NodeId",
        "/properties/RepoId",
        "/properties/SshCloneUrl",
        "/properties/SvnUrl"
    ],
    "primaryIdentifier": [
        "/properties/tfcfnid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "read": {
            "permissions": [
                "s3:GetObject"
            ]
        },
        "update": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "delete": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "list": {
            "permissions": [
                "s3:GetObject",
                "s3:ListBucket"
            ]
        }
    }
}
{% endhighlight %}
