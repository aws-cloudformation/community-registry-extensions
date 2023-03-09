package com.awscommunity.kms.encryptionsettings;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import software.amazon.awssdk.services.ec2.model.BlockDeviceMapping;
import software.amazon.awssdk.services.ec2.model.DescribeImagesResponse;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.EbsBlockDevice;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultResponse;
import software.amazon.awssdk.services.ec2.model.Image;
import software.amazon.awssdk.services.ec2.model.Instance;
import software.amazon.awssdk.services.ec2.model.Reservation;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

public final class Mocks {

    private Mocks() {
    }

    public static final String MOCK_DB_CLUSTER_SNAPSHOT_IDENTIFIER = "test";
    public static final String MOCK_DB_ENGINE_AURORA = "aurora";
    public static final String MOCK_DB_ENGINE_MYSQL = "MySQL";
    public static final String MOCK_DB_SNAPSHOT_IDENTIFIER = "test";
    public static final String MOCK_DESIRED_SSE_ALGORITHM = "aws:kms";
    public static final String MOCK_DESIRED_SSE_TYPE = "KMS";
    public static final String MOCK_IMAGE_ID = "ami-11223344";
    public static final String MOCK_INSTANCE_ID = "i-11223344";
    public static final String MOCK_INVALID_ENCRYPTION_TYPE = "invalid_encryption_type";
    public static final String MOCK_INVALID_KMS_KEY_ID = "invalid_kms_key_id";
    public static final String MOCK_INVALID_SSE_ALGORITHM = "invalid_sse_algorithm";
    public static final String MOCK_INVALID_SSE_TYPE = "invalid_sse_type";
    public static final String MOCK_INVALID_TARGET_NAME = "invalid_target_name";
    public static final String MOCK_KMS_ALIAS_ARN = "arn:aws:kms:us-west-2:111122223333:alias/Example";
    public static final String MOCK_KMS_KEY_ALIAS = "alias/Example";
    public static final String MOCK_KMS_KEY_ARN = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab";
    public static final String MOCK_KMS_KEY_ID = "1234abcd-12ab-34cd-56ef-1234567890ab";
    public static final String MOCK_LOGICAL_ID = "Sample";
    public static final String MOCK_SOURCE_DB_INSTANCE_IDENTIFIER = "test";

    public static HookHandlerRequest getHookHandlerMockRequest(final String setTargetName,
            final String setTargetLogicalId, final Map<String, Object> setHookTargetModel) {
        String targetLogicalId = setTargetLogicalId;
        if (setTargetLogicalId.isEmpty()) {
            targetLogicalId = "Sample";
        }
        return HookHandlerRequest.builder().hookContext(HookContext.builder().targetName(setTargetName)
                .targetLogicalId(targetLogicalId).targetModel(HookTargetModel.of(setHookTargetModel)).build()).build();
    }

    public static GetEbsEncryptionByDefaultResponse getEbsEncryptionByDefaultMockResponse(
            final Boolean setEbsEncryptionByDefaultEnabled) {
        return GetEbsEncryptionByDefaultResponse.builder().ebsEncryptionByDefault(setEbsEncryptionByDefaultEnabled)
                .build();
    }

    public static DescribeImagesResponse getDescribeImagesMockResponse(
            final Boolean setAmiEbsBlockDeviceEncryptedEnabled) {
        return DescribeImagesResponse.builder()
                .images(Image.builder().blockDeviceMappings(BlockDeviceMapping.builder()
                        .ebs(EbsBlockDevice.builder().encrypted(setAmiEbsBlockDeviceEncryptedEnabled).build()).build())
                        .build())
                .build();
    }

    public static DescribeInstancesResponse getDescribeInstancesMockResponse() {
        final Instance instance = Instance.builder().imageId("i-00112233").build();
        final Collection<Instance> instances = new ArrayList<Instance>();
        instances.add(instance);
        return DescribeInstancesResponse.builder().reservations(Reservation.builder().instances(instances).build())
                .build();
    }

    public static Map<String, Object> getAwsAutoScalingLaunchConfigurationMockTargetModel(final String setImageId,
            final String setInstanceId, final Boolean setBlockDeviceMappings, final Boolean setBlockDeviceMapping,
            final Boolean setEbs, final Boolean setEbsEncrypted) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        resourceProperties.put("InstanceType", "a1.large");

        if (setImageId != null) {
            resourceProperties.put("ImageId", setImageId);
        }

        if (setInstanceId != null) {
            resourceProperties.put("InstanceId", setInstanceId);
        }

        if (setBlockDeviceMappings != null && setBlockDeviceMappings) {
            final List<Map<String, Object>> blockDeviceMappings = new ArrayList<Map<String, Object>>();

            if (setBlockDeviceMapping != null && setBlockDeviceMapping) {
                final Map<String, Object> blockDeviceMapping = new HashMap<String, Object>();
                blockDeviceMapping.put("DeviceName", "/dev/sdm");

                if (setEbs != null && setEbs) {
                    final Map<String, Object> ebs = new HashMap<String, Object>();
                    ebs.put("VolumeSize", 1);
                    ebs.put("VolumeType", "gp3");

                    if (setEbsEncrypted != null) {
                        ebs.put("Encrypted", setEbsEncrypted);
                    }

                    blockDeviceMapping.put("Ebs", ebs);
                }
                blockDeviceMappings.add(blockDeviceMapping);
            }
            resourceProperties.put("BlockDeviceMappings", blockDeviceMappings);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsCloudTrailTrailMockTargetModel(final String setKMSKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setKMSKeyId != null) {
            resourceProperties.put("KMSKeyId", setKMSKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsDynamoDbGlobalTableMockTargetModel(final Boolean setSSESpecification,
            final Boolean setSSEEnabled, final String setSSEType, final Boolean setReplicas,
            final Boolean setReplicaSpecification, final Boolean setSSESpecificationForReplica,
            final String setKMSMasterKeyIdForReplica) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setSSESpecification != null && setSSESpecification) {
            final Map<String, Object> sseSpecification = new HashMap<String, Object>();

            if (setSSEEnabled != null) {
                sseSpecification.put("SSEEnabled", setSSEEnabled);
            }

            if (setSSEType != null) {
                sseSpecification.put("SSEType", setSSEType);
            }

            resourceProperties.put("SSESpecification", sseSpecification);
        }

        if (setReplicas != null && setReplicas) {
            final List<Map<String, Object>> replicas = new ArrayList<Map<String, Object>>();

            if (setReplicaSpecification != null && setReplicaSpecification) {
                final Map<String, Object> replica = new HashMap<String, Object>();
                replica.put("Region", "us-east-1");
                replica.put("TableClass", "STANDARD");

                if (setSSESpecificationForReplica != null && setSSESpecificationForReplica) {
                    final Map<String, Object> sseSpecification = new HashMap<String, Object>();

                    if (setKMSMasterKeyIdForReplica != null) {
                        sseSpecification.put("KMSMasterKeyId", setKMSMasterKeyIdForReplica);
                    }

                    replica.put("SSESpecification", sseSpecification);
                }

                replicas.add(replica);
            }

            resourceProperties.put("Replicas", replicas);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsDynamoDbTableMockTargetModel(final Boolean setSSESpecification,
            final Boolean setSSEEnabled, final String setSSEType, final String setKMSMasterKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setSSESpecification != null && setSSESpecification) {
            final Map<String, Object> sseSpecification = new HashMap<String, Object>();

            if (setSSEEnabled != null) {
                sseSpecification.put("SSEEnabled", setSSEEnabled);
            }

            if (setSSEType != null) {
                sseSpecification.put("SSEType", setSSEType);
            }

            if (setKMSMasterKeyId != null) {
                sseSpecification.put("KMSMasterKeyId", setKMSMasterKeyId);
            }

            resourceProperties.put("SSESpecification", sseSpecification);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsEc2InstanceMockTargetModel(final String setImageId,
            final Boolean setBlockDeviceMappings, final Boolean setBlockDeviceMapping, final Boolean setEbs,
            final Boolean setEbsEncrypted, final String setEbsKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setImageId != null) {
            resourceProperties.put("ImageId", setImageId);
        }

        if (setBlockDeviceMappings != null && setBlockDeviceMappings) {
            final List<Map<String, Object>> blockDeviceMappings = new ArrayList<Map<String, Object>>();

            if (setBlockDeviceMapping != null && setBlockDeviceMapping) {
                final Map<String, Object> blockDeviceMapping = new HashMap<String, Object>();
                blockDeviceMapping.put("DeviceName", "/dev/sdm");

                if (setEbs != null && setEbs) {
                    final Map<String, Object> ebs = new HashMap<String, Object>();
                    ebs.put("VolumeSize", 1);
                    ebs.put("VolumeType", "gp3");

                    if (setEbsEncrypted != null) {
                        ebs.put("Encrypted", setEbsEncrypted);
                    }

                    if (setEbsKmsKeyId != null) {
                        ebs.put("KmsKeyId", setEbsKmsKeyId);
                    }

                    blockDeviceMapping.put("Ebs", ebs);
                }
                blockDeviceMappings.add(blockDeviceMapping);
            }
            resourceProperties.put("BlockDeviceMappings", blockDeviceMappings);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsEc2LaunchTemplateMockTargetModel(final Boolean setLaunchTemplateData,
            final String setImageId, final Boolean setBlockDeviceMappings, final Boolean setBlockDeviceMapping,
            final Boolean setEbs, final Boolean setEbsEncrypted, final String setEbsKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setLaunchTemplateData != null && setLaunchTemplateData) {
            final Map<String, Object> launchTemplateData = new HashMap<String, Object>();

            if (setImageId != null) {
                launchTemplateData.put("ImageId", setImageId);
            }

            if (setBlockDeviceMappings != null && setBlockDeviceMappings) {
                final List<Map<String, Object>> blockDeviceMappings = new ArrayList<Map<String, Object>>();

                if (setBlockDeviceMapping != null && setBlockDeviceMapping) {
                    final Map<String, Object> blockDeviceMapping = new HashMap<String, Object>();
                    blockDeviceMapping.put("DeviceName", "/dev/sdm");

                    if (setEbs != null && setEbs) {
                        final Map<String, Object> ebs = new HashMap<String, Object>();
                        ebs.put("VolumeSize", 1);
                        ebs.put("VolumeType", "gp3");

                        if (setEbsEncrypted != null) {
                            ebs.put("Encrypted", setEbsEncrypted);
                        }

                        if (setEbsKmsKeyId != null) {
                            ebs.put("KmsKeyId", setEbsKmsKeyId);
                        }

                        blockDeviceMapping.put("Ebs", ebs);
                    }
                    blockDeviceMappings.add(blockDeviceMapping);
                }
                launchTemplateData.put("BlockDeviceMappings", blockDeviceMappings);
            }
            resourceProperties.put("LaunchTemplateData", launchTemplateData);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsEc2VolumeMockTargetModel(final Boolean setEncrypted,
            final String setKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setEncrypted != null) {
            resourceProperties.put("Encrypted", setEncrypted);
        }

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsEfsFileSystemMockTargetModel(final Boolean setEncrypted,
            final String setKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setEncrypted != null) {
            resourceProperties.put("Encrypted", setEncrypted);
        }

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsKinesisStreamMockTargetModel(final Boolean setStreamEncryption,
            final String setEncryptionType, final String setKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setStreamEncryption != null && setStreamEncryption) {
            final Map<String, Object> streamEncryption = new HashMap<String, Object>();

            if (setEncryptionType != null) {
                streamEncryption.put("EncryptionType", setEncryptionType);
            }

            if (setKeyId != null) {
                streamEncryption.put("KeyId", setKeyId);
            }

            resourceProperties.put("StreamEncryption", streamEncryption);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsLogsLogGroupMockTargetModel(final String setKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsRdsDbClusterMockTargetModel(final Boolean setStorageEncrypted,
            final String setKmsKeyId, final String setSourceDBClusterIdentifier, final String setSnapshotIdentifier) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setStorageEncrypted != null) {
            resourceProperties.put("StorageEncrypted", setStorageEncrypted);
        }

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        if (setSourceDBClusterIdentifier != null) {
            resourceProperties.put("SourceDBClusterIdentifier", setSourceDBClusterIdentifier);
        }

        if (setSnapshotIdentifier != null) {
            resourceProperties.put("SnapshotIdentifier", setSnapshotIdentifier);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsRdsDbInstanceMockTargetModel(final Boolean setStorageEncrypted,
            final String setKmsKeyId, final String setEngine, final String setSourceDBInstanceIdentifier,
            final String setDBSnapshotIdentifier, final String setDBClusterSnapshotIdentifier) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setStorageEncrypted != null) {
            resourceProperties.put("StorageEncrypted", setStorageEncrypted);
        }

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        if (setEngine != null) {
            resourceProperties.put("Engine", setEngine);
        }

        if (setSourceDBInstanceIdentifier != null) {
            resourceProperties.put("SourceDBInstanceIdentifier", setSourceDBInstanceIdentifier);
        }

        if (setDBSnapshotIdentifier != null) {
            resourceProperties.put("DBSnapshotIdentifier", setDBSnapshotIdentifier);
        }

        if (setDBClusterSnapshotIdentifier != null) {
            resourceProperties.put("DBClusterSnapshotIdentifier", setDBClusterSnapshotIdentifier);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsRdsGlobalClusterMockTargetModel(final Boolean setStorageEncrypted) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setStorageEncrypted != null) {
            resourceProperties.put("StorageEncrypted", setStorageEncrypted);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsRedshiftClusterMockTargetModel(final Boolean setEncrypted,
            final String setKmsKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setEncrypted != null) {
            resourceProperties.put("Encrypted", setEncrypted);
        }

        if (setKmsKeyId != null) {
            resourceProperties.put("KmsKeyId", setKmsKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsS3BucketMockTargetModel(final Boolean setBucketEncryption,
            final Boolean setServerSideEncryptionConfiguration, final Boolean setServerSideEncryptionRule,
            final Boolean setServerSideEncryptionByDefault, final String setSSEAlgorithm,
            final String setKMSMasterKeyID, final Boolean setBucketKeyEnabled) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setBucketEncryption != null && setBucketEncryption) {
            final Map<String, Object> bucketEncryption = new HashMap<String, Object>();

            if (setServerSideEncryptionConfiguration != null && setServerSideEncryptionConfiguration) {
                final List<Map<String, Object>> serverSideEncryptionConfiguration = new ArrayList<Map<String, Object>>();

                if (setServerSideEncryptionRule != null && setServerSideEncryptionRule) {
                    final Map<String, Object> serverSideEncryptionRule = new HashMap<String, Object>();

                    if (setServerSideEncryptionByDefault != null && setServerSideEncryptionByDefault) {
                        final Map<String, Object> serverSideEncryptionByDefault = new HashMap<String, Object>();

                        if (setSSEAlgorithm != null) {
                            serverSideEncryptionByDefault.put("SSEAlgorithm", setSSEAlgorithm);
                        }

                        if (setKMSMasterKeyID != null) {
                            serverSideEncryptionByDefault.put("KMSMasterKeyID", setKMSMasterKeyID);
                        }

                        serverSideEncryptionRule.put("ServerSideEncryptionByDefault", serverSideEncryptionByDefault);
                    }

                    if (setBucketKeyEnabled != null) {
                        serverSideEncryptionRule.put("BucketKeyEnabled", setBucketKeyEnabled);
                    }
                    serverSideEncryptionConfiguration.add(serverSideEncryptionRule);
                }
                bucketEncryption.put("ServerSideEncryptionConfiguration", serverSideEncryptionConfiguration);
            }
            resourceProperties.put("BucketEncryption", bucketEncryption);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsSnsTopicMockTargetModel(final String setKmsMasterKeyId) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setKmsMasterKeyId != null) {
            resourceProperties.put("KmsMasterKeyId", setKmsMasterKeyId);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }

    public static Map<String, Object> getAwsSqsQueueMockTargetModel(final String setKmsMasterKeyId,
            final Boolean setSqsManagedSseEnabled) {
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        if (setKmsMasterKeyId != null) {
            resourceProperties.put("KmsMasterKeyId", setKmsMasterKeyId);
        }

        if (setSqsManagedSseEnabled != null) {
            resourceProperties.put("SqsManagedSseEnabled", setSqsManagedSseEnabled);
        }

        targetModel.put("resourceProperties", resourceProperties);
        return targetModel;
    }
}
