package com.awscommunity.kms.encryptionsettings;

import static org.mockito.Mockito.spy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

/**
 * Test calls made on pre-update hook handler calls.
 */
@ExtendWith(MockitoExtension.class)
public class PreUpdateHookHandlerTest extends PreCreatePreUpdateHookHandlerCommonTests {

    private PreUpdateHookHandler handler;

    protected PreUpdateHookHandlerTest() {
        super();
    }

    /**
     * Set up tests.
     */
    @BeforeEach
    public void setup() {
        handler = spy(new PreUpdateHookHandler());
    }

    @Test
    public void testIsNullOrEmptyStringIsEmpty() {
        isNullOrEmptyStringIsEmpty();
    }

    @Test
    public void testIsNullOrEmptyStringIsNotEmpty() {
        isNullOrEmptyStringIsNotEmpty();
    }

    @Test
    public void testIsNullOrEmptyListIsEmpty() {
        isNullOrEmptyListIsEmpty();
    }

    @Test
    public void testIsNullOrEmptyListIsNotEmpty() {
        isNullOrEmptyListIsNotEmpty();
    }

    @Test
    public void testIsNullOrEmptySetIsEmpty() {
        isNullOrEmptySetIsEmpty();
    }

    @Test
    public void testIsNullOrEmptySetIsNotEmpty() {
        isNullOrEmptySetIsNotEmpty();
    }

    @Test
    public void testAwsKmsKeyIdRegexMatchesIgnoreKeyIdPattern() {
        awsKmsKeyIdRegexMatchesIgnoreKeyIdPattern();
    }

    @Test
    public void testAwsKmsKeyIdRegexMatchesIgnoreKeyAliasPattern() {
        awsKmsKeyIdRegexMatchesIgnoreKeyAliasPattern();
    }

    @Test
    public void testAwsKmsKeyIdRegexMatchesIgnoreKeyArnPattern() {
        awsKmsKeyIdRegexMatchesIgnoreKeyArnPattern();
    }

    @Test
    public void testAwsKmsKeyIdRegexMatchesIgnoreAliasArnPattern() {
        awsKmsKeyIdRegexMatchesIgnoreAliasArnPattern();
    }

    @Test
    public void testCallbackContextClassExistsAndInheritsFromStdCallbackContext() {
        callbackContextClassExistsAndInheritsFromStdCallbackContext();
    }

    @Test
    public void testNullPointerExceptionCaught() {
        nullPointerExceptionCaught(getProxy(), getLogger(), handler);
    }

    @Test
    public void testErrorCaughtWithMessage() {
        errorCaughtWithMessage(getProxy(), getLogger(), handler);
    }

    @Test
    public void testUnsupportedTargetException() {
        unsupportedTargetException(getProxy(), getLogger(), handler);
    }

    @Test
    public void testWhenTypeConfigurationModelIsNullAllDefaultValuesAreSet() {
        whenTypeConfigurationModelIsNullAllDefaultValuesAreSet(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationImageIdAndInstanceIdMissing() {
        awsAutoScalingLaunchConfigurationImageIdAndInstanceIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackFailure() {
        awsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackFailure(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackSuccess() {
        awsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackSuccess(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationBlockDeviceMappingsMissing() {
        awsAutoScalingLaunchConfigurationBlockDeviceMappingsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsMissing() {
        awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedMissing() {
        awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedFailure() {
        awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedSuccess() {
        awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsFailure() {
        awsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsFailure(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsSuccess() {
        awsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsSuccess(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure() {
        awsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess() {
        awsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure() {
        awsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure(
                getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess() {
        awsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess(
                getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsCloudTrailTrailKmsKeyIdMissing() {
        awsCloudTrailTrailKmsKeyIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsCloudTrailTrailKmsKeyIdPatternFailure() {
        awsCloudTrailTrailKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsCloudTrailTrailKmsKeyIdPatternSuccess() {
        awsCloudTrailTrailKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationMissing() {
        awsDynamoDbGlobalTableSseSpecificationMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseEnabledMissing() {
        awsDynamoDbGlobalTableSseSpecificationSseEnabledMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseEnabledFailure() {
        awsDynamoDbGlobalTableSseSpecificationSseEnabledFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseEnabledSuccess() {
        awsDynamoDbGlobalTableSseSpecificationSseEnabledSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseTypeMissing() {
        awsDynamoDbGlobalTableSseSpecificationSseTypeMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseTypeFailure() {
        awsDynamoDbGlobalTableSseSpecificationSseTypeFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableSseSpecificationSseTypeSuccess() {
        awsDynamoDbGlobalTableSseSpecificationSseTypeSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasMissing() {
        awsDynamoDbGlobalTableReplicasMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasReplicaSpecificationMissing() {
        awsDynamoDbGlobalTableReplicasReplicaSpecificationMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationMissing() {
        awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdMissing() {
        awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdMissing(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdFailure() {
        awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdFailure(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdSuccess() {
        awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdSuccess(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationMissing() {
        awsDynamoDbTableSseSpecificationMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseEnabledMissing() {
        awsDynamoDbTableSseSpecificationSseEnabledMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseEnabledFailure() {
        awsDynamoDbTableSseSpecificationSseEnabledFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseEnabledSuccess() {
        awsDynamoDbTableSseSpecificationSseEnabledSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseTypeMissing() {
        awsDynamoDbTableSseSpecificationSseTypeMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseTypeFailure() {
        awsDynamoDbTableSseSpecificationSseTypeFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationSseTypeSuccess() {
        awsDynamoDbTableSseSpecificationSseTypeSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationKmsKeyIdFailure() {
        awsDynamoDbTableSseSpecificationKmsKeyIdFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsDynamoDbTableSseSpecificationKmsKeyIdSuccess() {
        awsDynamoDbTableSseSpecificationKmsKeyIdSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternFailure() {
        awsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternSuccess() {
        awsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceImageIdAndBlockDeviceMappingsMissing() {
        awsEc2InstanceImageIdAndBlockDeviceMappingsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsMissing() {
        awsEc2InstanceBlockDeviceMappingsEbsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsEncryptedMissing() {
        awsEc2InstanceBlockDeviceMappingsEbsEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsEncryptedFailure() {
        awsEc2InstanceBlockDeviceMappingsEbsEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceBlockDeviceMappingsEbsEncryptedSuccess() {
        awsEc2InstanceBlockDeviceMappingsEbsEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackFailure() {
        awsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackSuccess() {
        awsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsFailure() {
        awsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsSuccess() {
        awsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2InstanceAmiImageIdMissing() {
        awsEc2InstanceAmiImageIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataMissing() {
        awsEc2LaunchTemplateLaunchTemplateDataMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternFailure() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternFailure(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternSuccess() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternSuccess(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackFailure() {
        awsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackSuccess() {
        awsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataImageIdAndBlockDeviceMappingsMissing() {
        awsEc2LaunchTemplateLaunchTemplateDataImageIdAndBlockDeviceMappingsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsMissing() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedMissing() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedFailure() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedSuccess() {
        awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsFailure() {
        awsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsSuccess() {
        awsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2LaunchTemplateAmiImageIdMissing() {
        awsEc2LaunchTemplateAmiImageIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeKmsKeyIdPatternFailure() {
        awsEc2VolumeKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeKmsKeyIdPatternSuccess() {
        awsEc2VolumeKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackFailure() {
        awsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackSuccess() {
        awsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeEncryptedMissing() {
        awsEc2VolumeEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeEncryptedFailure() {
        awsEc2VolumeEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEc2VolumeEncryptedSuccess() {
        awsEc2VolumeEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEfsFileSystemKmsKeyIdPatternFailure() {
        awsEfsFileSystemKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEfsFileSystemKmsKeyIdPatternSuccess() {
        awsEfsFileSystemKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEfsFileSystemEncryptedMissing() {
        awsEfsFileSystemEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEfsFileSystemEncryptedFailure() {
        awsEfsFileSystemEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsEfsFileSystemEncryptedSuccess() {
        awsEfsFileSystemEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionMissing() {
        awsKinesisStreamStreamEncryptionMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionEncryptionTypeMissing() {
        awsKinesisStreamStreamEncryptionEncryptionTypeMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionEncryptionTypeFailure() {
        awsKinesisStreamStreamEncryptionEncryptionTypeFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionKmsKeyIdMissing() {
        awsKinesisStreamStreamEncryptionKmsKeyIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionKmsKeyIdPatternFailure() {
        awsKinesisStreamStreamEncryptionKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsKinesisStreamStreamEncryptionKmsKeyIdPatternSuccess() {
        awsKinesisStreamStreamEncryptionKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsLogsLogGroupKmsKeyIdMissing() {
        awsLogsLogGroupKmsKeyIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsLogsLogGroupKmsKeyIdPatternFailure() {
        awsLogsLogGroupKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsLogsLogGroupKmsKeyIdPatternSuccess() {
        awsLogsLogGroupKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterKmsKeyIdPatternFailure() {
        awsRdsDbClusterKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterKmsKeyIdPatternSuccess() {
        awsRdsDbClusterKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterStorageEncryptedMissing() {
        awsRdsDbClusterStorageEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterStorageEncryptedFailure() {
        awsRdsDbClusterStorageEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterStorageEncryptedSuccess() {
        awsRdsDbClusterStorageEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterSourceDbClusterIdentifierSpecified() {
        awsRdsDbClusterSourceDbClusterIdentifierSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbClusterSnapshotIdentifierSpecified() {
        awsRdsDbClusterSnapshotIdentifierSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceKmsKeyIdPatternFailure() {
        awsRdsDbInstanceKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceKmsKeyIdPatternSuccess() {
        awsRdsDbInstanceKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceStorageEncryptedMissing() {
        awsRdsDbInstanceStorageEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceStorageEncryptedFailure() {
        awsRdsDbInstanceStorageEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceStorageEncryptedSuccess() {
        awsRdsDbInstanceStorageEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceRdsHelpersIsAuroraEngineNullValueSpecified() {
        awsRdsDbInstanceRdsHelpersIsAuroraEngineNullValueSpecified();
    }

    @Test
    public void testAwsRdsDbInstanceRdsHelpersIsAuroraEngineNonAuroraValueSpecified() {
        awsRdsDbInstanceRdsHelpersIsAuroraEngineNonAuroraValueSpecified();
    }

    @Test
    public void testAwsRdsDbInstanceRdsHelpersIsAuroraEngineAuroraValueSpecified() {
        awsRdsDbInstanceRdsHelpersIsAuroraEngineAuroraValueSpecified();
    }

    @Test
    public void testAwsRdsDbInstanceDbEngineAuroraSpecified() {
        awsRdsDbInstanceDbEngineAuroraSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceSourceDbInstanceIdentifierSpecified() {
        awsRdsDbInstanceSourceDbInstanceIdentifierSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceDbSnapshotIdentifierSpecified() {
        awsRdsDbInstanceDbSnapshotIdentifierSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsDbInstanceDbClusterSnapshotIdentifierSpecified() {
        awsRdsDbInstanceDbClusterSnapshotIdentifierSpecified(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsGlobalClusterStorageEncryptedMissing() {
        awsRdsGlobalClusterStorageEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsGlobalClusterStorageEncryptedFailure() {
        awsRdsGlobalClusterStorageEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRdsGlobalClusterStorageEncryptedSuccess() {
        awsRdsGlobalClusterStorageEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRedshiftClusterKmsKeyIdPatternFailure() {
        awsRedshiftClusterKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRedshiftClusterKmsKeyIdPatternSuccess() {
        awsRedshiftClusterKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRedshiftClusterEncryptedMissing() {
        awsRedshiftClusterEncryptedMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRedshiftClusterEncryptedFailure() {
        awsRedshiftClusterEncryptedFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsRedshiftClusterEncryptedSuccess() {
        awsRedshiftClusterEncryptedSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionMissing() {
        awsS3BucketBucketEncryptionMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionConfigurationMissing() {
        awsS3BucketBucketEncryptionServerSideEncryptionConfigurationMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleMissing() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultMissing() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultMissing(getProxy(), getLogger(),
                handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmMissing() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmMissing(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmFailure() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmFailure(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmSuccess() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmSuccess(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdFailure() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdFailure(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdSuccess() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdSuccess(getProxy(),
                getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledMissing() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledFailure() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledSuccess() {
        awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSnsTopicKmsKeyIdMissing() {
        awsSnsTopicKmsKeyIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSnsTopicKmsKeyIdPatternFailure() {
        awsSnsTopicKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSnsTopicKmsKeyIdPatternSuccess() {
        awsSnsTopicKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueKmsKeyIdMissing() {
        awsSqsQueueKmsKeyIdMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueKmsKeyIdPatternFailure() {
        awsSqsQueueKmsKeyIdPatternFailure(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueKmsKeyIdPatternSuccess() {
        awsSqsQueueKmsKeyIdPatternSuccess(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueSqsManagedSseEnabled() {
        awsSqsQueueSqsManagedSseEnabled(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueSqsManagedSseMissing() {
        awsSqsQueueSqsManagedSseMissing(getProxy(), getLogger(), handler);
    }

    @Test
    public void testAwsSqsQueueSqsManagedSseNotEnabled() {
        awsSqsQueueSqsManagedSseNotEnabled(getProxy(), getLogger(), handler);
    }
}
