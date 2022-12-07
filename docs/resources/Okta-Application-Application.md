
## Okta::Application::Application

Manage an Application in Okta.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-okta-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Okta::Application::Application",
    "description": "Manage an Application in Okta.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers",
    "typeConfiguration": {
        "properties": {
            "OktaAccess": {
                "$ref": "#/definitions/OktaAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "OktaAccess"
        ]
    },
    "definitions": {
        "OktaAccess": {
            "type": "object",
            "properties": {
                "Url": {
                    "type": "string",
                    "description": "Okta URL, including organization identifier"
                },
                "ApiKey": {
                    "type": "string",
                    "description": "Okta API tokens are used to authenticate requests to Okta APIs."
                }
            },
            "additionalProperties": false
        },
        "Accessibility": {
            "type": "object",
            "description": "Specifies access settings for the application",
            "properties": {
                "ErrorRedirectUrl": {
                    "type": "string",
                    "description": "Custom error page for this application"
                },
                "LoginRedirectUrl": {
                    "type": "string",
                    "description": "Custom login page for this application"
                },
                "SelfService": {
                    "type": "boolean",
                    "description": "Enable self-service application assignment",
                    "default": false
                }
            },
            "additionalProperties": false
        },
        "ApplicationCredentials": {
            "type": "object",
            "description": "Specifies credentials and scheme for the application's signOnMode",
            "properties": {
                "OauthClient": {
                    "$ref": "#/definitions/OauthCredential"
                },
                "Password": {
                    "$ref": "#/definitions/Password"
                },
                "Scheme": {
                    "$ref": "#/definitions/AuthenticationScheme"
                },
                "Signing": {
                    "$ref": "#/definitions/SigningCredential"
                },
                "UserName": {
                    "type": "string",
                    "description": "Shared username for app"
                },
                "RevealPassword": {
                    "type": "boolean",
                    "description": "Whether to reveal the credential password"
                },
                "UserNameTemplate": {
                    "$ref": "#/definitions/UserNameTemplate"
                }
            },
            "additionalProperties": false
        },
        "OauthCredential": {
            "description": "Determines how to authenticate the OAuth 2.0 client",
            "type": "object",
            "properties": {
                "AutoKeyRotation": {
                    "type": "boolean",
                    "description": "Requested key rotation mode"
                },
                "ClientId": {
                    "type": "string",
                    "description": "Unique identifier for the OAuth 2.0 client application"
                },
                "ClientSecret": {
                    "type": "string",
                    "description": "OAuth 2.0 client secret string"
                },
                "TokenEndpointAuthMethod": {
                    "type": "string",
                    "description": "Requested authentication method for the token endpoint"
                }
            },
            "additionalProperties": false,
            "required": [
                "TokenEndpointAuthMethod"
            ]
        },
        "Password": {
            "description": "Specifies a password for a user",
            "type": "string"
        },
        "AuthenticationScheme": {
            "type": "string",
            "description": "Authentication Scheme",
            "enum": [
                "ADMIN_SETS_CREDENTIALS",
                "EDIT_PASSWORD_ONLY",
                "EDIT_USERNAME_AND_PASSWORD",
                "EXTERNAL_PASSWORD_SYNC",
                "SHARED_USERNAME_AND_PASSWORD"
            ]
        },
        "SigningCredential": {
            "type": "object",
            "description": "Determines the key used for signing assertions for the signOnMode",
            "properties": {
                "Kid": {
                    "type": "string",
                    "description": "Reference for key credential for the app"
                }
            },
            "additionalProperties": false
        },
        "UserNameTemplate": {
            "type": "object",
            "description": "Specifies the template used to generate a user's username when the application is assigned via a group or directly to a user",
            "properties": {
                "Template": {
                    "description": "mapping expression for username",
                    "type": "string",
                    "default": "${source.login}"
                },
                "Type": {
                    "description": "type of mapping expression",
                    "type": "string",
                    "enum": [
                        "NONE",
                        "BUILT_IN",
                        "CUSTOM"
                    ],
                    "default": "BUILT_IN"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type"
            ]
        },
        "SignOnMode": {
            "type": "string",
            "enum": [
                "AUTO_LOGIN",
                "BASIC_AUTH",
                "BOOKMARK",
                "BROWSER_PLUGIN",
                "Custom",
                "OPENID_CONNECT",
                "SAML_1_1",
                "SAML_2_0",
                "SECURE_PASSWORD_STORE",
                "WS_FEDERATION"
            ]
        },
        "Visibility": {
            "description": "Specifies visibility settings for the application",
            "type": "object",
            "properties": {
                "AutoLaunch": {
                    "description": "Automatically signs in to the app when user signs into Okta.",
                    "type": "boolean",
                    "default": false
                },
                "AutoSubmitToolbar": {
                    "description": "Automatically sign in when user lands on the sign-in page",
                    "type": "boolean",
                    "default": false
                },
                "Hide": {
                    "description": "Hides this app for specific end-user apps",
                    "$ref": "#/definitions/Hide"
                }
            },
            "additionalProperties": false,
            "required": [
                "AutoLaunch",
                "AutoSubmitToolbar",
                "Hide"
            ]
        },
        "Hide": {
            "description": "Hides this app for specific end-user apps",
            "type": "object",
            "properties": {
                "Ios": {
                    "type": "boolean",
                    "description": "Okta Mobile for iOS or Android (pre-dates Android)",
                    "default": false
                },
                "Web": {
                    "type": "boolean",
                    "description": "Okta Web Browser Home Page",
                    "default": false
                }
            },
            "additionalProperties": false,
            "required": [
                "Ios",
                "Web"
            ]
        }
    },
    "properties": {
        "Accessibility": {
            "$ref": "#/definitions/Accessibility"
        },
        "Credentials": {
            "$ref": "#/definitions/ApplicationCredentials"
        },
        "Id": {
            "description": "Unique key for app",
            "type": "string"
        },
        "Label": {
            "description": "User-defined display name for app",
            "type": "string"
        },
        "Name": {
            "description": "Unique key for app definition",
            "type": "string"
        },
        "RequestObjectSigningAlg": {
            "description": "The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request object",
            "type": "string",
            "enum": [
                "HS256",
                "HS384",
                "HS512",
                "RS256",
                "RS384",
                "RS512",
                "ES256",
                "ES384",
                "ES512"
            ]
        },
        "Settings": {
            "type": "object"
        },
        "SignOnMode": {
            "$ref": "#/definitions/SignOnMode"
        },
        "Visibility": {
            "$ref": "#/definitions/Visibility"
        }
    },
    "additionalProperties": false,
    "required": [
        "Label",
        "SignOnMode"
    ],
    "readOnlyProperties": [
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "writeOnlyProperties": [
        "/properties/Credentials",
        "/properties/RequestObjectSigningAlg"
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
