
## Fastly::Services::Backend

Manage a Fastly service backend.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-fastly-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Fastly::Services::Backend",
    "description": "Manage a Fastly service backend.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-fastly-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-fastly-resource-providers",
    "definitions": {
        "FastlyAccess": {
            "description": "Properties needed to access Fastly.",
            "type": "object",
            "properties": {
                "Token": {
                    "type": "string",
                    "description": "API token used to access Fastly"
                }
            },
            "required": [
                "Token"
            ],
            "additionalProperties": false
        },
        "Address": {
            "description": "A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend.",
            "type": "string"
        },
        "AutoLoadbalance": {
            "description": "Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a request_condition will be selected based on their weight.",
            "type": "boolean"
        },
        "BetweenBytesTimeout": {
            "description": "Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using bereq.between_bytes_timeout.",
            "type": "integer"
        },
        "ClientCert": {
            "description": "Unused",
            "type": "string"
        },
        "Comment": {
            "description": "A freeform descriptive note.",
            "type": "string"
        },
        "ConnectTimeout": {
            "description": "Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthethic 503 response will be presented instead. May be set at runtime using bereq.connect_timeout.",
            "type": "integer"
        },
        "FirstByteTimeout": {
            "description": "Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthethic 503 response will be presented instead. May be set at runtime using bereq.first_byte_timeout.",
            "type": "integer"
        },
        "Healthcheck": {
            "description": "The name of the healthcheck to use with this backend.",
            "type": "string"
        },
        "Ipv4": {
            "description": "IPv4 address of the backend. May be used as an alternative to address to set the backend location.",
            "type": "string"
        },
        "Ipv6": {
            "description": "IPv6 address of the backend. May be used as an alternative to address to set the backend location.",
            "type": "string"
        },
        "MaxConn": {
            "description": "Maximum number of concurrent connections this backend will accept.",
            "type": "integer"
        },
        "MaxTlsVersion": {
            "description": "Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic 503 error response will be generated.",
            "type": "string",
            "enum": [
                "1",
                "1.0",
                "1.1",
                "1.2",
                "1.3"
            ]
        },
        "MinTlsVersion": {
            "description": "Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic 503 error response will be generated.",
            "type": "string",
            "enum": [
                "1",
                "1.0",
                "1.1",
                "1.2",
                "1.3"
            ]
        },
        "Name": {
            "description": "The name of the backend.",
            "type": "string"
        },
        "BackendName": {
            "description": "The name of the backend. Read-only",
            "type": "string"
        },
        "OverrideHost": {
            "description": "If set, will replace the client-supplied HTTP Host header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing bereq.http.Host in VCL.",
            "type": "string"
        },
        "Port": {
            "description": "Port on which the backend server is listening for connections from Fastly. Setting port to 80 or 443 will also set use_ssl automatically (to false and true respectively), unless explicitly overridden by setting use_ssl in the same request.",
            "type": "integer",
            "default": 443
        },
        "RequestCondition": {
            "description": "Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any auto_loadbalance setting. By default, the first backend added to a service is selected for all requests.",
            "type": "string"
        },
        "Shield": {
            "description": "Identifier of the POP to use as a shield (https://docs.fastly.com/en/guides/shielding).",
            "type": "string"
        },
        "SslCaCert": {
            "description": "CA certificate attached to origin.",
            "type": "string"
        },
        "SslCertHostname": {
            "description": "Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.",
            "type": "string"
        },
        "SslCheckCert": {
            "description": "Be strict on checking SSL certs. [Default true]",
            "type": "boolean",
            "default": true
        },
        "SslCiphers": {
            "description": "List of OpenSSL ciphers (https://www.openssl.org/docs/manmaster/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic 503 error response will be generated.",
            "type": "string"
        },
        "SslClientCert": {
            "description": "Client certificate attached to origin.",
            "type": "string"
        },
        "SslClientKey": {
            "description": "Client key attached to origin.",
            "type": "string"
        },
        "SslHostname": {
            "description": "Deprecated. Use ssl_cert_hostname and ssl_sni_hostname to configure certificate validation.",
            "type": "string"
        },
        "SslSniHostname": {
            "description": "Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.",
            "type": "string"
        },
        "UseSsl": {
            "description": "Whether or not to require TLS for connections to this backend.",
            "type": "boolean",
            "default": true
        },
        "Weight": {
            "description": "Weight used to load balance this backend against others. May be any positive integer. If auto_loadbalance is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have auto_loadbalance set to true.",
            "type": "integer"
        },
        "CreatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "DeletedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "Locked": {
            "description": "Indicates whether the version of the service this backend is attached to accepts edits. Read-only.",
            "type": "boolean"
        },
        "ServiceId": {
            "description": "Alphanumeric string identifying the service. Read-only.",
            "type": "string"
        },
        "VersionId": {
            "description": "Alphanumeric string identifying the service version.",
            "type": "string"
        },
        "UpdatedAt": {
            "description": "Date and time in ISO 8601 format. Read-only.",
            "type": "string",
            "format": "date-time"
        },
        "Version": {
            "description": "Integer identifying a backend version. Read-only.",
            "type": "string"
        }
    },
    "typeConfiguration": {
        "properties": {
            "FastlyAccess": {
                "$ref": "#/definitions/FastlyAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "FastlyAccess"
        ]
    },
    "properties": {
        "Address": {
            "$ref": "#/definitions/Address"
        },
        "AutoLoadbalance": {
            "$ref": "#/definitions/AutoLoadbalance"
        },
        "BetweenBytesTimeout": {
            "$ref": "#/definitions/BetweenBytesTimeout"
        },
        "ClientCert": {
            "$ref": "#/definitions/ClientCert"
        },
        "Comment": {
            "$ref": "#/definitions/Comment"
        },
        "ConnectTimeout": {
            "$ref": "#/definitions/ConnectTimeout"
        },
        "FirstByteTimeout": {
            "$ref": "#/definitions/FirstByteTimeout"
        },
        "Healthcheck": {
            "$ref": "#/definitions/Healthcheck"
        },
        "Ipv4": {
            "$ref": "#/definitions/Ipv4"
        },
        "Ipv6": {
            "$ref": "#/definitions/Ipv6"
        },
        "MaxConn": {
            "$ref": "#/definitions/MaxConn"
        },
        "MaxTlsVersion": {
            "$ref": "#/definitions/MaxTlsVersion"
        },
        "MinTlsVersion": {
            "$ref": "#/definitions/MinTlsVersion"
        },
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "OverrideHost": {
            "$ref": "#/definitions/OverrideHost"
        },
        "Port": {
            "$ref": "#/definitions/Port"
        },
        "RequestCondition": {
            "$ref": "#/definitions/RequestCondition"
        },
        "Shield": {
            "$ref": "#/definitions/Shield"
        },
        "SslCaCert": {
            "$ref": "#/definitions/SslCaCert"
        },
        "SslCertHostname": {
            "$ref": "#/definitions/SslCertHostname"
        },
        "SslCheckCert": {
            "$ref": "#/definitions/SslCheckCert"
        },
        "SslCiphers": {
            "$ref": "#/definitions/SslCiphers"
        },
        "SslClientCert": {
            "$ref": "#/definitions/SslClientCert"
        },
        "SslClientKey": {
            "$ref": "#/definitions/SslClientKey"
        },
        "SslSniHostname": {
            "$ref": "#/definitions/SslSniHostname"
        },
        "UseSsl": {
            "$ref": "#/definitions/UseSsl"
        },
        "Weight": {
            "$ref": "#/definitions/Weight"
        },
        "ServiceId": {
            "$ref": "#/definitions/ServiceId"
        },
        "BackendName": {
            "$ref": "#/definitions/BackendName"
        },
        "VersionId": {
            "$ref": "#/definitions/VersionId"
        },
        "CreatedAt": {
            "$ref": "#/definitions/CreatedAt"
        },
        "UpdatedAt": {
            "$ref": "#/definitions/UpdatedAt"
        },
        "DeletedAt": {
            "$ref": "#/definitions/DeletedAt"
        },
        "Version": {
            "$ref": "#/definitions/Version"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "ServiceId",
        "VersionId"
    ],
    "readOnlyProperties": [
        "/properties/Version",
        "/properties/CreatedAt",
        "/properties/UpdatedAt",
        "/properties/DeletedAt"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/ServiceId",
        "/properties/VersionId"
    ],
    "primaryIdentifier": [
        "/properties/Name",
        "/properties/ServiceId",
        "/properties/VersionId"
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
