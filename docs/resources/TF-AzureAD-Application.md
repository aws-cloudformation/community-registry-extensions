
## TF::AzureAD::Application

## Manages an Application within Azure Active Directory.

-&gt; **NOTE:** If you&#39;re authenticating using a Service Principal then it must have permissions to both &#x60;Read and write owned by applications&#x60; and &#x60;Sign in and read user profile&#x60; within the &#x60;Windows Azure Active Directory&#x60; API.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AzureAD::Application",
    "description": "Manages an Application within Azure Active Directory.\n\n-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/azuread/TF-AzureAD-Application/docs/README.md",
    "definitions": {
        "AppRoleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AllowedMemberTypes": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "type": "string"
                    }
                },
                "Description": {
                    "type": "string"
                },
                "DisplayName": {
                    "type": "string"
                },
                "Enabled": {
                    "type": "boolean"
                },
                "Id": {
                    "type": "string"
                },
                "IsEnabled": {
                    "type": "boolean"
                },
                "Value": {
                    "type": "string"
                }
            }
        },
        "Oauth2PermissionsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AdminConsentDescription": {
                    "type": "string"
                },
                "AdminConsentDisplayName": {
                    "type": "string"
                },
                "Id": {
                    "type": "string"
                },
                "IsEnabled": {
                    "type": "boolean"
                },
                "Type": {
                    "type": "string"
                },
                "UserConsentDescription": {
                    "type": "string"
                },
                "UserConsentDisplayName": {
                    "type": "string"
                },
                "Value": {
                    "type": "string"
                }
            }
        },
        "ApiDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Oauth2PermissionScope": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/Oauth2PermissionScopeDefinition"
                    }
                }
            },
            "required": []
        },
        "OptionalClaimsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AccessToken": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/AccessTokenDefinition"
                    }
                },
                "IdToken": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/IdTokenDefinition"
                    }
                }
            },
            "required": []
        },
        "RequiredResourceAccessDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "ResourceAppId": {
                    "type": "string",
                    "description": "The unique identifier for the resource that the application requires access to. This should be the Application ID of the target application."
                },
                "ResourceAccess": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/ResourceAccessDefinition"
                    },
                    "minItems": 1
                }
            },
            "required": [
                "ResourceAppId"
            ]
        },
        "TimeoutsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Create": {
                    "type": "string"
                },
                "Delete": {
                    "type": "string"
                },
                "Read": {
                    "type": "string"
                },
                "Update": {
                    "type": "string"
                }
            },
            "required": []
        },
        "WebDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "HomepageUrl": {
                    "type": "string",
                    "description": "Home page or landing page of the application."
                },
                "LogoutUrl": {
                    "type": "string",
                    "description": "The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols."
                },
                "RedirectUris": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "type": "string"
                    },
                    "description": "A list of URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent."
                },
                "ImplicitGrant": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/ImplicitGrantDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": []
        },
        "Oauth2PermissionScopeDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AdminConsentDescription": {
                    "type": "string",
                    "description": "Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users."
                },
                "AdminConsentDisplayName": {
                    "type": "string",
                    "description": "Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users."
                },
                "Enabled": {
                    "type": "boolean",
                    "description": "Determines if the permission scope is enabled. Defaults to `true`."
                },
                "Id": {
                    "type": "string",
                    "description": "The unique identifier of the delegated permission. Must be a valid UUID."
                },
                "Type": {
                    "type": "string",
                    "description": "Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions. Defaults to `User`. Possible values are `User` or `Admin`."
                },
                "UserConsentDescription": {
                    "type": "string",
                    "description": "Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf."
                },
                "UserConsentDisplayName": {
                    "type": "string",
                    "description": "Display name for the delegated permission that appears in the end user consent experience."
                },
                "Value": {
                    "type": "string",
                    "description": "The value that is used for the `scp` claim in OAuth 2.0 access tokens."
                }
            },
            "required": [
                "Id"
            ]
        },
        "AccessTokenDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AdditionalProperties": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "Essential": {
                    "type": "boolean"
                },
                "Name": {
                    "type": "string"
                },
                "Source": {
                    "type": "string"
                }
            },
            "required": [
                "Name"
            ]
        },
        "IdTokenDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AdditionalProperties": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "Essential": {
                    "type": "boolean"
                },
                "Name": {
                    "type": "string"
                },
                "Source": {
                    "type": "string"
                }
            },
            "required": [
                "Name"
            ]
        },
        "ResourceAccessDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Id": {
                    "type": "string",
                    "description": "The unique identifier for one of the `OAuth2Permission` or `AppRole` instances that the resource application exposes."
                },
                "Type": {
                    "type": "string",
                    "description": "Specifies whether the `id` property references an `OAuth2Permission` or an `AppRole`. Possible values are `Scope` or `Role`."
                }
            },
            "required": [
                "Id",
                "Type"
            ]
        },
        "ImplicitGrantDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AccessTokenIssuanceEnabled": {
                    "type": "boolean"
                }
            },
            "required": []
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "AppRole": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/AppRoleDefinition"
            },
            "description": "A collection of `app_role` blocks as documented below. For more information see [official documentation on Application Roles](https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles)."
        },
        "ApplicationId": {
            "type": "string"
        },
        "AvailableToOtherTenants": {
            "type": "boolean",
            "description": "Is this Azure AD Application available to other tenants? Defaults to `false`. This property is deprecated and has been replaced by the `sign_in_audience` property."
        },
        "DisplayName": {
            "type": "string",
            "description": "The display name for the application."
        },
        "FallbackPublicClientEnabled": {
            "type": "boolean",
            "description": "The fallback application type as public client, such as an installed application running on a mobile device. Defaults to `false`."
        },
        "GroupMembershipClaims": {
            "type": "string",
            "description": "Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`."
        },
        "Homepage": {
            "type": "string",
            "description": "The URL to the application's home page. This property is deprecated and has been replaced by the `homepage_url` property in the `web` block."
        },
        "Id": {
            "type": "string"
        },
        "IdentifierUris": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string"
            },
            "description": "The user-defined URI(s) that uniquely identify an application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant."
        },
        "LogoutUrl": {
            "type": "string",
            "description": "The URL of the logout page. This property is deprecated and has been replaced by the `logout_url` property in the `web` block."
        },
        "Name": {
            "type": "string",
            "description": "The name of the optional claim."
        },
        "Oauth2AllowImplicitFlow": {
            "type": "boolean",
            "description": "Does this Azure AD Application allow OAuth 2.0 implicit flow tokens? Defaults to `false`. This property is deprecated and has been replaced by the `access_token_issuance_enabled` property in the `implicit_grant` block."
        },
        "Oauth2Permissions": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/Oauth2PermissionsDefinition"
            },
            "description": "A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below. This block is deprecated and has been replaced by the `oauth2_permission_scope` block in the `api` block."
        },
        "ObjectId": {
            "type": "string"
        },
        "Owners": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            },
            "description": "A list of object IDs of principals that will be granted ownership of the application. It's recommended to specify the object ID of the authenticated principal running Terraform, to ensure sufficient permissions that the application can be subsequently updated."
        },
        "PreventDuplicateNames": {
            "type": "boolean",
            "description": "If `true`, will return an error when an existing Application is found with the same name. Defaults to `false`."
        },
        "PublicClient": {
            "type": "boolean",
            "description": "Is this Azure AD Application a public client? Defaults to `false`. This property is deprecated and has been replaced by the `fallback_public_client_enabled` property."
        },
        "ReplyUrls": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            },
            "description": "A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to. This property is deprecated and has been replaced by the `redirect_uris` property in the `web` block."
        },
        "SignInAudience": {
            "type": "string",
            "description": "The Microsoft account types that are supported for the current application. Must be one of `AzureADMyOrg` or `AzureADMultipleOrgs`. Defaults to `AzureADMyOrg`."
        },
        "Type": {
            "type": "string",
            "description": "The type of the application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**."
        },
        "Api": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ApiDefinition"
            },
            "maxItems": 1
        },
        "OptionalClaims": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/OptionalClaimsDefinition"
            },
            "maxItems": 1
        },
        "RequiredResourceAccess": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/RequiredResourceAccessDefinition"
            }
        },
        "Timeouts": {
            "$ref": "#/definitions/TimeoutsDefinition"
        },
        "Web": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/WebDefinition"
            },
            "maxItems": 1
        }
    },
    "additionalProperties": false,
    "required": [],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/ApplicationId",
        "/properties/Id",
        "/properties/ObjectId"
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
