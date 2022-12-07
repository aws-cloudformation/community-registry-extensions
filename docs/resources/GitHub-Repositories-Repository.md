
## GitHub::Repositories::Repository

Manage a repository in GitHub.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-github-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "GitHub::Repositories::Repository",
    "description": "Manage a repository in GitHub.",
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
        },
        "SecurityAndAnalysis": {
            "description": "Specify which security and analysis features to enable or disable. For example, to enable GitHub Advanced Security, use this data in the body of the PATCH request: {\"security_and_analysis\": {\"advanced_security\": {\"status\": \"enabled\"}}}. If you have admin permissions for a private repository covered by an Advanced Security license, you can check which security and analysis features are currently enabled by using a GET /repos/{owner}/{repo} request.",
            "type": "object",
            "properties": {
                "AdvanceSecurity": {
                    "$ref": "#/definitions/AdvanceSecurity"
                },
                "SecretScanning": {
                    "$ref": "#/definitions/SecretScanning"
                },
                "SecretScanningPushProtection": {
                    "$ref": "#/definitions/SecretScanningPushProtection"
                }
            },
            "additionalProperties": false
        },
        "AdvanceSecurity": {
            "description": "Use the status property to enable or disable GitHub Advanced Security for this repository. For more information, see \"About GitHub Advanced Security.\" (https://docs.github.com/github/getting-started-with-github/learning-about-github/about-github-advanced-security)",
            "type": "object",
            "properties": {
                "Status": {
                    "description": "Can be enabled or disabled.",
                    "type": "string",
                    "enum": [
                        "enabled",
                        "disabled"
                    ]
                }
            },
            "required": [
                "Status"
            ],
            "additionalProperties": false
        },
        "SecretScanning": {
            "description": "Use the status property to enable or disable secret scanning for this repository. For more information, see \"About secret scanning.\" (https://docs.github.com/code-security/secret-security/about-secret-scanning)",
            "type": "object",
            "properties": {
                "Status": {
                    "description": "Can be enabled or disabled.",
                    "type": "string",
                    "enum": [
                        "enabled",
                        "disabled"
                    ]
                }
            },
            "required": [
                "Status"
            ],
            "additionalProperties": false
        },
        "SecretScanningPushProtection": {
            "description": "Use the status property to enable or disable secret scanning push protection for this repository. For more information, see \"Protecting pushes with secret scanning.\" (https://docs.github.com/code-security/secret-scanning/protecting-pushes-with-secret-scanning)",
            "type": "object",
            "properties": {
                "Status": {
                    "description": "Can be enabled or disabled.",
                    "type": "string",
                    "enum": [
                        "enabled",
                        "disabled"
                    ]
                }
            },
            "required": [
                "Status"
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
            "description": "The organization name. The name is not case sensitive. If not specified, then the managed repository will be within the currently logged-in user account.",
            "type": "string"
        },
        "Name": {
            "description": "The name of the repository.",
            "type": "string"
        },
        "Description": {
            "description": "A short description of the repository.",
            "type": "string"
        },
        "Homepage": {
            "description": "A URL with more information about the repository.",
            "type": "string",
            "pattern": "^https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&//=]*)$"
        },
        "Private": {
            "description": "Whether the repository is private.",
            "type": "boolean"
        },
        "Visibility": {
            "description": "Can be public or private. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be internal. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise. For more information, see \"Creating an internal repository\" (https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-internal-repositories) in the GitHub Help documentation.",
            "type": "string",
            "enum": [
                "public",
                "private",
                "internal"
            ]
        },
        "HasIssues": {
            "description": "Either true to enable issues for this repository or false to disable them.",
            "type": "boolean",
            "default": true
        },
        "HasProjects": {
            "description": "Either true to enable projects for this repository or false to disable them. Note: If you're creating a repository in an organization that has disabled repository projects, the default is false, and if you pass true, the API returns an error.",
            "type": "boolean",
            "default": true
        },
        "HasWiki": {
            "description": "Either true to enable the wiki for this repository or false to disable it.",
            "type": "boolean",
            "default": true
        },
        "IsTemplate": {
            "description": "Either true to make this repo available as a template repository or false to prevent it.",
            "type": "boolean"
        },
        "TeamId": {
            "description": "The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.",
            "type": "number"
        },
        "AutoInit": {
            "description": "Pass true to create an initial commit with empty README.",
            "type": "boolean"
        },
        "GitIgnoreTemplate": {
            "description": "Desired language or platform .gitignore template to apply. Use the name of the template without the extension (https://github.com/github/gitignore). For example, \"Haskell\".",
            "type": "string"
        },
        "LicenseTemplate": {
            "description": "Choose an open source license template (https://choosealicense.com/) that best suits your needs, and then use the license keyword (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#searching-github-by-license-type) as the license_template string. For example, \"mit\" or \"mpl-2.0\".",
            "type": "string"
        },
        "AllowSquashMerge": {
            "description": "Either true to allow squash-merging pull requests, or false to prevent squash-merging.",
            "type": "boolean",
            "default": true
        },
        "AllowMergeCommit": {
            "description": "Either true to allow merging pull requests with a merge commit, or false to prevent merging pull requests with merge commits.",
            "type": "boolean",
            "default": true
        },
        "AllowRebaseMerge": {
            "description": "Either true to allow rebase-merging pull requests, or false to prevent rebase-merging.",
            "type": "boolean",
            "default": true
        },
        "AllowAutoMerge": {
            "description": "Either true to allow auto-merge on pull requests, or false to disallow auto-merge.",
            "type": "boolean"
        },
        "DeleteBranchOnMerge": {
            "description": "Either true to allow automatically deleting head branches when pull requests are merged, or false to prevent automatic deletion.",
            "type": "boolean",
            "default": true
        },
        "AllowForking": {
            "description": "Either true to allow private forks, or false to prevent private forks.",
            "type": "boolean"
        },
        "Archived": {
            "description": "true to archive this repository. Note: You cannot unarchive repositories through the API.",
            "type": "boolean"
        },
        "SecurityAndAnalysis": {
            "$ref": "#/definitions/SecurityAndAnalysis"
        },
        "Owner": {
            "description": "ID of the repository owner.",
            "type": "string"
        },
        "HtmlUrl": {
            "description": "URL of the git repository on Github.",
            "type": "string"
        },
        "GitUrl": {
            "description": "Git URL of the repository on Github.",
            "type": "string"
        },
        "DefaultBranch": {
            "description": "Updates the default branch for this repository.",
            "type": "string"
        },
        "Language": {
            "description": "The main programming language used for this GitHub repository.",
            "type": "string"
        },
        "ForksCount": {
            "description": "Number of forks for this GitHub repository.",
            "type": "number"
        },
        "StarsCount": {
            "description": "Number of stars for this GitHub repository.",
            "type": "number"
        },
        "WatchersCount": {
            "description": "Number of stars for this GitHub repository.",
            "type": "number"
        },
        "IssuesCount": {
            "description": "Number of issues for this GitHub repository.",
            "type": "number"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/Owner",
        "/properties/HtmlUrl",
        "/properties/GitUrl",
        "/properties/DefaultBranch",
        "/properties/Language",
        "/properties/ForksCount",
        "/properties/StarsCount",
        "/properties/WatchersCount",
        "/properties/IssuesCount"
    ],
    "createOnlyProperties": [
        "/properties/Organization",
        "/properties/Name",
        "/properties/TeamId",
        "/properties/AutoInit",
        "/properties/GitIgnoreTemplate",
        "/properties/LicenseTemplate"
    ],
    "writeOnlyProperties": [
        "/properties/Organization",
        "/properties/TeamId",
        "/properties/AllowForking",
        "/properties/AllowAutoMerge",
        "/properties/AutoInit",
        "/properties/GitIgnoreTemplate",
        "/properties/SecurityAndAnalysis"
    ],
    "primaryIdentifier": [
        "/properties/Owner",
        "/properties/Name"
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
