
## MongoDB::Atlas::Cluster

## The cluster resource provides access to your cluster configurations. The resource lets you create, edit and delete clusters. The resource requires your Project ID.

- [Source]() 
- [Documentation]()

Published by MongoDB

## Schema
{% highlight json %}
{
    "typeName": "MongoDB::Atlas::Cluster",
    "description": "The cluster resource provides access to your cluster configurations. The resource lets you create, edit and delete clusters. The resource requires your Project ID.",
    "definitions": {
        "advancedAutoScaling": {
            "type": "object",
            "description": "AWS Automatic Cluster Scaling",
            "properties": {
                "DiskGB": {
                    "$ref": "#/definitions/diskGB"
                },
                "Compute": {
                    "$ref": "#/definitions/compute"
                }
            },
            "additionalProperties": false
        },
        "compute": {
            "type": "object",
            "description": "Automatic Compute Scaling",
            "properties": {
                "Enabled": {
                    "type": "boolean",
                    "description": "Flag that indicates whether someone enabled instance size auto-scaling.\n\nSet to true to enable instance size auto-scaling. If enabled, you must specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize.\nSet to false to disable instance size automatic scaling."
                },
                "ScaleDownEnabled": {
                    "type": "boolean",
                    "description": "Flag that indicates whether the instance size may scale down. MongoDB Cloud requires this parameter if \"replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled\" : true. If you enable this option, specify a value for replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize."
                },
                "MinInstanceSize": {
                    "type": "string",
                    "description": "Minimum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if \"replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled\" : true."
                },
                "MaxInstanceSize": {
                    "type": "string",
                    "description": "Maximum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if \"replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled\" : true."
                }
            },
            "additionalProperties": false
        },
        "advancedRegionConfig": {
            "type": "object",
            "description": "Hardware specifications for nodes set for a given region. Each regionConfigs object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each regionConfigs object must have either an analyticsSpecs object, electableSpecs object, or readOnlySpecs object. Tenant clusters only require electableSpecs. Dedicated clusters can specify any of these specifications, but must have at least one electableSpecs object within a replicationSpec. Every hardware specification must use the same instanceSize.\n\nExample:\n\nIf you set \"replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize\" : \"M30\", set \"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\" : \"M30\"if you have electable nodes and\"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize\" : \"M30\" if you have read-only nodes.\",",
            "properties": {
                "AnalyticsAutoScaling": {
                    "$ref": "#/definitions/advancedAutoScaling"
                },
                "AutoScaling": {
                    "$ref": "#/definitions/advancedAutoScaling"
                },
                "RegionName": {
                    "type": "string"
                },
                "AnalyticsSpecs": {
                    "$ref": "#/definitions/specs"
                },
                "ElectableSpecs": {
                    "$ref": "#/definitions/specs"
                },
                "Priority": {
                    "type": "integer"
                },
                "ReadOnlySpecs": {
                    "$ref": "#/definitions/specs"
                }
            },
            "additionalProperties": false
        },
        "specs": {
            "type": "object",
            "properties": {
                "DiskIOPS": {
                    "type": "string",
                    "description": "Target throughput desired for storage attached to your AWS-provisioned cluster. Only change this parameter if you:\n\nset \"replicationSpecs[n].regionConfigs[m].providerName\" : \"AWS\".\nset \"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\" : \"M30\" or greater not including Mxx_NVME tiers.\nThe maximum input/output operations per second (IOPS) depend on the selected .instanceSize and .diskSizeGB. This parameter defaults to the cluster tier's standard IOPS value. Changing this value impacts cluster cost. MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.\n\nInstance sizes M10 to M40 have a ratio of disk capacity to system memory of 60:1.\nInstance sizes greater than M40 have a ratio of 120:1."
                },
                "EbsVolumeType": {
                    "type": "string",
                    "description": "Type of storage you want to attach to your AWS-provisioned cluster.\n\nSTANDARD volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size.\n\nPROVISIONED volume types must fall within the allowable IOPS range for the selected volume size.\""
                },
                "InstanceSize": {
                    "type": "string",
                    "description": "Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size. If you deploy a Global Cluster, you must choose a instance size of M30 or greater."
                },
                "NodeCount": {
                    "type": "integer",
                    "description": "Number of read-only nodes for MongoDB Cloud deploys to the region. Read-only nodes can never become the primary, but can enable local reads."
                }
            },
            "additionalProperties": false
        },
        "diskGB": {
            "type": "object",
            "description": "Automatic cluster storage settings that apply to this cluster.",
            "properties": {
                "Enabled": {
                    "type": "boolean",
                    "description": "Flag that indicates whether this cluster enables disk auto-scaling. The maximum memory allowed for the selected cluster tier and the oplog size can limit storage auto-scaling."
                }
            },
            "additionalProperties": false
        },
        "advancedReplicationSpec": {
            "type": "object",
            "description": "List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.",
            "properties": {
                "ID": {
                    "type": "string",
                    "description": "Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Multi-Cloud Cluster. If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Multi-Cloud Cluster, you may specify this parameter. The request deletes any existing zones in the Multi-Cloud Cluster that you exclude from the request."
                },
                "NumShards": {
                    "type": "integer",
                    "description": "Positive integer that specifies the number of shards to deploy in each specified zone. If you set this value to 1 and \"clusterType\" : \"SHARDED\", MongoDB Cloud deploys a single-shard sharded cluster. Don't create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don't provide the same benefits as multi-shard configurations."
                },
                "AdvancedRegionConfigs": {
                    "type": "array",
                    "description": "Hardware specifications for nodes set for a given region. Each regionConfigs object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each regionConfigs object must have either an analyticsSpecs object, electableSpecs object, or readOnlySpecs object. Tenant clusters only require electableSpecs. Dedicated clusters can specify any of these specifications, but must have at least one electableSpecs object within a replicationSpec. Every hardware specification must use the same instanceSize.\n\nExample:\n\nIf you set \"replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize\" : \"M30\", set \"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\" : \"M30\"if you have electable nodes and\"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize\" : \"M30\" if you have read-only nodes.\",",
                    "items": {
                        "$ref": "#/definitions/advancedRegionConfig"
                    }
                },
                "ZoneName": {
                    "type": "string",
                    "description": "Human-readable label that identifies the zone in a Global Cluster. Provide this value only if \"clusterType\" : \"GEOSHARDED\"."
                }
            },
            "additionalProperties": false
        },
        "apiKeyDefinition": {
            "type": "object",
            "properties": {
                "PublicKey": {
                    "type": "string"
                },
                "PrivateKey": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "connectionStrings": {
            "type": "object",
            "description": "Collection of Uniform Resource Locators that point to the MongoDB database.",
            "properties": {
                "Standard": {
                    "type": "string",
                    "description": "Public connection string that you can use to connect to this cluster. This connection string uses the mongodb:// protocol."
                },
                "StandardSrv": {
                    "type": "string",
                    "description": "Public connection string that you can use to connect to this cluster. This connection string uses the mongodb+srv:// protocol."
                },
                "Private": {
                    "type": "string",
                    "description": "Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the mongodb+srv:// protocol. The resource returns this parameter once someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this resource returns this parameter only if you enable custom DNS."
                },
                "PrivateSrv": {
                    "type": "string",
                    "description": "Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the mongodb+srv:// protocol. The resource returns this parameter when someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this parameter returns only if you enable custom DNS."
                },
                "PrivateEndpoint": {
                    "type": "array",
                    "description": "List of private endpoint connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.",
                    "items": {
                        "$ref": "#/definitions/privateEndpoint"
                    }
                },
                "AwsPrivateLinkSrv": {
                    "type": "string",
                    "description": "Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to Atlas through the interface endpoint that the key names."
                },
                "AwsPrivateLink": {
                    "type": "string",
                    "description": "Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related mongodb:// connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names."
                }
            },
            "additionalProperties": false
        },
        "privateEndpoint": {
            "type": "object",
            "description": "List of private endpoint connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.",
            "properties": {
                "ConnectionString": {
                    "type": "string",
                    "description": "Private endpoint-aware connection string that uses the mongodb:// protocol to connect to MongoDB Cloud through a private endpoint."
                },
                "Endpoints": {
                    "type": "array",
                    "description": "List that contains the private endpoints through which you connect to MongoDB Cloud when you use connectionStrings.privateEndpoint[n].connectionString or connectionStrings.privateEndpoint[n].srvConnectionString.",
                    "items": {
                        "$ref": "#/definitions/endpoint"
                    }
                },
                "SRVConnectionString": {
                    "type": "string",
                    "description": "Private endpoint-aware connection string that uses the mongodb+srv:// protocol to connect to MongoDB Cloud through a private endpoint. The mongodb+srv protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application supports it. If it doesn't, use connectionStrings.privateEndpoint[n].connectionString."
                },
                "Type": {
                    "type": "string",
                    "description": "Enum: \"MONGOD\" \"MONGOS\"\nMongoDB process type to which your application connects. Use MONGOD for replica sets and MONGOS for sharded clusters."
                }
            },
            "additionalProperties": false
        },
        "endpoint": {
            "type": "object",
            "properties": {
                "EndpointID": {
                    "type": "string",
                    "description": "Unique string that the cloud provider uses to identify the private endpoint."
                },
                "ProviderName": {
                    "type": "string",
                    "description": "Cloud provider in which MongoDB Cloud deploys the private endpoint."
                },
                "Region": {
                    "type": "string",
                    "description": "Region in which MongoDB Cloud deploys the private endpoint."
                }
            },
            "additionalProperties": false
        },
        "processArgs": {
            "type": "object",
            "description": "Advanced configuration details to add for one cluster in the specified project.",
            "properties": {
                "DefaultReadConcern": {
                    "type": "string",
                    "description": "Default level of acknowledgment requested from MongoDB for read operations set for this cluster."
                },
                "DefaultWriteConcern": {
                    "type": "string",
                    "description": "Default level of acknowledgment requested from MongoDB for write operations set for this cluster."
                },
                "FailIndexKeyTooLong": {
                    "type": "boolean",
                    "description": "Flag that indicates whether you can insert or update documents where all indexed entries don't exceed 1024 bytes. If you set this to false, mongod writes documents that exceed this limit but doesn't index them."
                },
                "JavascriptEnabled": {
                    "type": "boolean",
                    "description": "Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript."
                },
                "MinimumEnabledTLSProtocol": {
                    "type": "string",
                    "description": "Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version."
                },
                "NoTableScan": {
                    "type": "boolean",
                    "description": "Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results."
                },
                "OplogSizeMB": {
                    "type": "integer",
                    "description": "Storage limit of cluster's oplog expressed in megabytes. A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates."
                },
                "SampleSizeBIConnector": {
                    "type": "integer",
                    "description": "Interval in seconds at which the mongosqld process re-samples data to create its relational schema."
                },
                "SampleRefreshIntervalBIConnector": {
                    "type": "integer",
                    "description": "Number of documents per database to sample when gathering schema information."
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "AdvancedSettings": {
            "$ref": "#/definitions/processArgs"
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        },
        "BackupEnabled": {
            "description": "Flag that indicates whether the cluster can perform backups. If set to true, the cluster can perform backups. You must set this value to true for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to false, the cluster doesn't use backups.",
            "type": "boolean"
        },
        "BiConnector": {
            "type": "object",
            "properties": {
                "ReadPreference": {
                    "type": "string",
                    "description": "Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud. The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to ANALYTICS node, or SECONDARY if there are no ANALYTICS nodes."
                },
                "Enabled": {
                    "type": "boolean",
                    "description": "Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster."
                }
            },
            "description": "Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.",
            "additionalProperties": false
        },
        "ClusterType": {
            "description": "Configuration of nodes that comprise the cluster.",
            "type": "string"
        },
        "CreatedDate": {
            "description": "Date and time when MongoDB Cloud created this cluster. This parameter expresses its value in ISO 8601 format in UTC.",
            "type": "string"
        },
        "ConnectionStrings": {
            "description": "Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) reference for further details.",
            "$ref": "#/definitions/connectionStrings"
        },
        "DiskSizeGB": {
            "description": "Storage capacity that the host's root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set replicationSpecs. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value. The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.",
            "type": "number"
        },
        "EncryptionAtRestProvider": {
            "description": "Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize setting must be M10 or higher and \"backupEnabled\" : false or omitted entirely.",
            "type": "string",
            "enum": [
                "AWS",
                "GCP",
                "AZURE",
                "NONE"
            ]
        },
        "ProjectId": {
            "description": "Unique identifier of the project the cluster belongs to.",
            "type": "string"
        },
        "Id": {
            "description": "Unique identifier of the cluster.",
            "type": "string"
        },
        "Labels": {
            "description": "Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Key": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255
                    },
                    "Value": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255
                    }
                },
                "additionalProperties": false
            }
        },
        "MongoDBMajorVersion": {
            "description": "Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version.",
            "type": "string"
        },
        "MongoDBVersion": {
            "description": "Version of MongoDB that the cluster runs.",
            "type": "string"
        },
        "Name": {
            "description": "Human-readable label that identifies the advanced cluster.",
            "type": "string"
        },
        "Paused": {
            "description": "Flag that indicates whether the cluster is paused or not.",
            "type": "boolean"
        },
        "PitEnabled": {
            "description": "Flag that indicates whether the cluster uses continuous cloud backups.",
            "type": "boolean"
        },
        "ReplicationSpecs": {
            "description": "List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global replica sets and sharded clusters, this array has one object representing where your clusters nodes deploy.",
            "type": "array",
            "items": {
                "$ref": "#/definitions/advancedReplicationSpec"
            }
        },
        "RootCertType": {
            "description": "Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group.",
            "type": "string"
        },
        "StateName": {
            "description": "Current state of the cluster.",
            "type": "string"
        },
        "VersionReleaseSystem": {
            "description": "Method by which the cluster maintains the MongoDB versions. If value is CONTINUOUS, you must not specify mongoDBMajorVersion",
            "type": "string"
        },
        "TerminationProtectionEnabled": {
            "description": "Flag that indicates whether termination protection is enabled on the cluster. If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.",
            "type": "boolean"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "ProjectId"
    ],
    "readOnlyProperties": [
        "/properties/ConnectionStrings",
        "/properties/ConnectionStrings.Standard",
        "/properties/ConnectionStrings.StandardSrv",
        "/properties/ConnectionStrings.Private",
        "/properties/ConnectionStrings.PrivateSrv",
        "/properties/StateName",
        "/properties/MongoDBVersion",
        "/properties/CreatedDate",
        "/properties/Id"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue",
                "secretsmanager:UpdateSecretVersionStage",
                "secretsmanager:CreateSecret",
                "secretsmanager:CreateSecretInput"
            ]
        },
        "read": {
            "permissions": [
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue",
                "secretsmanager:UpdateSecretVersionStage",
                "secretsmanager:CreateSecret",
                "secretsmanager:CreateSecretInput"
            ]
        },
        "update": {
            "permissions": [
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue",
                "secretsmanager:UpdateSecretVersionStage",
                "secretsmanager:CreateSecret",
                "secretsmanager:CreateSecretInput"
            ]
        },
        "delete": {
            "permissions": [
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue",
                "secretsmanager:UpdateSecretVersionStage",
                "secretsmanager:CreateSecret",
                "secretsmanager:CreateSecretInput"
            ]
        }
    }
}
{% endhighlight %}
