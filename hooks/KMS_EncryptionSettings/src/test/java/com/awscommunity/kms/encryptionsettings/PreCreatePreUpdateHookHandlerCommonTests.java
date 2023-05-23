package com.awscommunity.kms.encryptionsettings;

import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK;
import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS;
import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.VALIDATE_BUCKET_KEY_ENABLED;
import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers;
import com.awscommunity.kms.encryptionsettings.services.rds.AwsRdsHelpers;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import software.amazon.awssdk.services.ec2.model.DescribeImagesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultRequest;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.StdCallbackContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Defines tests that are common to pre-create and pre-update hook handler
 * calls.
 */
public class PreCreatePreUpdateHookHandlerCommonTests extends AbstractTestBase {

    protected final void isNullOrEmptyStringIsEmpty() {
        final String inputString = "";
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isTrue();
    }

    protected final void isNullOrEmptyStringIsNotEmpty() {
        final String inputString = "test";
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isFalse();
    }

    protected final void isNullOrEmptyListIsEmpty() {
        final List<String> inputString = new ArrayList<String>();
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isTrue();
    }

    protected final void isNullOrEmptyListIsNotEmpty() {
        final List<String> inputString = new ArrayList<String>();
        inputString.add("test");
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isFalse();
    }

    protected final void isNullOrEmptySetIsEmpty() {
        final Set<String> inputString = new HashSet<String>();
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isTrue();
    }

    protected final void isNullOrEmptySetIsNotEmpty() {
        final Set<String> inputString = new HashSet<String>();
        inputString.add("test");
        final Boolean response = ResourcePropertyValuesValidationHelpers.isNullOrEmpty(inputString);
        assertThat(response).isFalse();
    }

    protected final void awsKmsKeyIdRegexMatchesIgnoreKeyIdPattern() {
        final String inputString = Mocks.MOCK_KMS_KEY_ID;
        final Boolean ignoreKeyIdPattern = true;
        final Boolean ignoreKeyAliasPattern = false;
        final Boolean ignoreKeyArnPattern = false;
        final Boolean ignoreAliasArnPattern = false;
        final Boolean response = ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches(inputString,
                ignoreKeyIdPattern, ignoreKeyAliasPattern, ignoreKeyArnPattern, ignoreAliasArnPattern);
        assertThat(response).isFalse();
    }

    protected final void awsKmsKeyIdRegexMatchesIgnoreKeyAliasPattern() {
        final String inputString = Mocks.MOCK_KMS_KEY_ALIAS;
        final Boolean ignoreKeyIdPattern = false;
        final Boolean ignoreKeyAliasPattern = true;
        final Boolean ignoreKeyArnPattern = false;
        final Boolean ignoreAliasArnPattern = false;
        final Boolean response = ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches(inputString,
                ignoreKeyIdPattern, ignoreKeyAliasPattern, ignoreKeyArnPattern, ignoreAliasArnPattern);
        assertThat(response).isFalse();
    }

    protected final void awsKmsKeyIdRegexMatchesIgnoreKeyArnPattern() {
        final String inputString = Mocks.MOCK_KMS_KEY_ARN;
        final Boolean ignoreKeyIdPattern = false;
        final Boolean ignoreKeyAliasPattern = false;
        final Boolean ignoreKeyArnPattern = true;
        final Boolean ignoreAliasArnPattern = false;
        final Boolean response = ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches(inputString,
                ignoreKeyIdPattern, ignoreKeyAliasPattern, ignoreKeyArnPattern, ignoreAliasArnPattern);
        assertThat(response).isFalse();
    }

    protected final void awsKmsKeyIdRegexMatchesIgnoreAliasArnPattern() {
        final String inputString = Mocks.MOCK_KMS_ALIAS_ARN;
        final Boolean ignoreKeyIdPattern = false;
        final Boolean ignoreKeyAliasPattern = false;
        final Boolean ignoreKeyArnPattern = false;
        final Boolean ignoreAliasArnPattern = true;
        final Boolean response = ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches(inputString,
                ignoreKeyIdPattern, ignoreKeyAliasPattern, ignoreKeyArnPattern, ignoreAliasArnPattern);
        assertThat(response).isFalse();
    }

    protected final void callbackContextClassExistsAndInheritsFromStdCallbackContext() {
        final CallbackContext callbackContext = new CallbackContext();
        assertThat(callbackContext).isInstanceOf(CallbackContext.class);
        assertThat(callbackContext).isInstanceOf(StdCallbackContext.class);
    }

    protected final void nullPointerExceptionCaught(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        when(handler.getAwsKmsIntegratedServiceFromFactory(proxy, request, null, logger, typeConfiguration))
                .thenThrow(new NullPointerException());

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testHandlerInternalFailure(response, "Handler internal failure.");
    }

    protected final void errorCaughtWithMessage(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        when(handler.getAwsKmsIntegratedServiceFromFactory(proxy, request, null, logger, typeConfiguration))
                .thenThrow(new Error("Test."));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testHandlerInternalFailure(response, "Handler internal failure.  Test.");
    }

    protected final void unsupportedTargetException(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest(Mocks.MOCK_INVALID_TARGET_NAME,
                Mocks.MOCK_LOGICAL_ID, targetModel);

        assertThatExceptionOfType(UnsupportedTargetException.class).isThrownBy(() -> {
            handler.handleRequest(proxy, request, null, logger, typeConfiguration);
        });
    }

    protected final void whenTypeConfigurationModelIsNullAllDefaultValuesAreSet(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = handler.setTypeConfigurationDefaultValues(null);
        assertThat(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback())
                .isEqualTo(USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK);
        assertThat(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings())
                .isEqualTo(VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS);
        assertThat(typeConfiguration.getValidateBucketKeyEnabled()).isEqualTo(VALIDATE_BUCKET_KEY_ENABLED);
    }

    protected final void awsAutoScalingLaunchConfigurationImageIdAndInstanceIdMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = null;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "Both the `ImageId` property and the `InstanceId` property are missing.");
    }

    protected final void awsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final Boolean setEbsEncryptionByDefaultEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsAutoScalingLaunchConfigurationUseGetEbsEncryptionByDefaultAsFallbackSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setEbsEncryptionByDefaultEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant: EBS encryption by default is enabled.");
    }

    protected final void awsAutoScalingLaunchConfigurationBlockDeviceMappingsMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property is missing.");
    }

    protected final void awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = false;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsEncryptedSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiBlockDeviceMappingEncryptionSettingsSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = null;
        final String setInstanceId = Mocks.MOCK_INSTANCE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        when(proxy.injectCredentialsAndInvokeV2(any(DescribeInstancesRequest.class), any()))
                .thenReturn(Mocks.getDescribeInstancesMockResponse());

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = null;
        final String setInstanceId = Mocks.MOCK_INSTANCE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        when(proxy.injectCredentialsAndInvokeV2(any(DescribeInstancesRequest.class), any()))
                .thenReturn(Mocks.getDescribeInstancesMockResponse());

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = Mocks.MOCK_INSTANCE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsAutoScalingLaunchConfigurationAmiImageIdAndFromInstanceIdBlockDeviceMappingEncryptionSettingsSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final String setInstanceId = Mocks.MOCK_INSTANCE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsAutoScalingLaunchConfigurationMockTargetModel(setImageId,
                setInstanceId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::AutoScaling::LaunchConfiguration",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsCloudTrailTrailKmsKeyIdMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKMSKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsCloudTrailTrailMockTargetModel(setKMSKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::CloudTrail::Trail",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `KMSKeyId` property is missing.");
    }

    protected final void awsCloudTrailTrailKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKMSKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsCloudTrailTrailMockTargetModel(setKMSKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::CloudTrail::Trail",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KMSKeyId` property value contains an invalid pattern.");
    }

    protected final void awsCloudTrailTrailKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKMSKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsCloudTrailTrailMockTargetModel(setKMSKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::CloudTrail::Trail",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = null;
        final Boolean setSSEEnabled = null;
        final String setSSEType = null;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSESpecification` property is missing.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseEnabledMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = null;
        final String setSSEType = null;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEEnabled` property is missing.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseEnabledFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = false;
        final String setSSEType = null;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEEnabled` property value is not set to a boolean value of `true`.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseEnabledSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseTypeMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = null;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEType` property is missing.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseTypeFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_INVALID_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEType` property value is not set to `KMS`.");
    }

    protected final void awsDynamoDbGlobalTableSseSpecificationSseTypeSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbGlobalTableReplicasMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = null;
        final Boolean setReplicaSpecification = null;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `Replicas` property is missing.");
    }

    protected final void awsDynamoDbGlobalTableReplicasReplicaSpecificationMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = null;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `Replicas` property is missing.");
    }

    protected final void awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = null;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = true;
        final String setKMSMasterKeyIdForReplica = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = true;
        final String setKMSMasterKeyIdForReplica = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KMSMasterKeyId` property value for a replica contains an invalid pattern.");
    }

    protected final void awsDynamoDbGlobalTableReplicasReplicaSpecificationSseSpecificationKmsKeyIdSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final Boolean setReplicas = true;
        final Boolean setReplicaSpecification = true;
        final Boolean setSSESpecificationForReplica = true;
        final String setKMSMasterKeyIdForReplica = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbGlobalTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setReplicas, setReplicaSpecification, setSSESpecificationForReplica,
                setKMSMasterKeyIdForReplica);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::GlobalTable",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbTableSseSpecificationMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = null;
        final Boolean setSSEEnabled = null;
        final String setSSEType = null;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSESpecification` property is missing.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseEnabledMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = null;
        final String setSSEType = null;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEEnabled` property is missing.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseEnabledFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = false;
        final String setSSEType = null;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEEnabled` property value is not set to a boolean value of `true`.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseEnabledSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseTypeMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = null;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEType` property is missing.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseTypeFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_INVALID_SSE_TYPE;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEType` property value is not set to `KMS`.");
    }

    protected final void awsDynamoDbTableSseSpecificationSseTypeSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final String setKMSMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsDynamoDbTableSseSpecificationKmsKeyIdFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final String setKMSMasterKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KMSMasterKeyId` property value contains an invalid pattern.");
    }

    protected final void awsDynamoDbTableSseSpecificationKmsKeyIdSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setSSESpecification = true;
        final Boolean setSSEEnabled = true;
        final String setSSEType = Mocks.MOCK_DESIRED_SSE_TYPE;
        final String setKMSMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsDynamoDbTableMockTargetModel(setSSESpecification,
                setSSEEnabled, setSSEType, setKMSMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::DynamoDB::Table",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final String setEbsKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response,
                "`Ebs` properties in `BlockDeviceMappings`: a `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsKmsKeyIdPatternSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final String setEbsKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final Boolean setEbsEncryptionByDefaultEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2InstanceUseGetEbsEncryptionByDefaultAsFallbackSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setEbsEncryptionByDefaultEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant: EBS encryption by default is enabled.");
    }

    protected final void awsEc2InstanceImageIdAndBlockDeviceMappingsMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsEncryptedMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property is missing.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsEncryptedFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = false;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2InstanceBlockDeviceMappingsEbsEncryptedSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2InstanceAmiBlockDeviceMappingEncryptionSettingsSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2InstanceAmiImageIdMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final String setImageId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2InstanceMockTargetModel(setImageId,
                setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Instance", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = null;
        final String setImageId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `LaunchTemplateData` property is missing.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final String setEbsKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response,
                "`Ebs` properties in `BlockDeviceMappings`: a `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsKmsKeyIdPatternSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = true;
        final String setEbsKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final Boolean setEbsEncryptionByDefaultEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2LaunchTemplateUseGetEbsEncryptionByDefaultAsFallbackSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setEbsEncryptionByDefaultEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant: EBS encryption by default is enabled.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataImageIdAndBlockDeviceMappingsMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property is missing.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = true;
        final Boolean setBlockDeviceMapping = true;
        final Boolean setEbs = true;
        final Boolean setEbsEncrypted = false;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings`: an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2LaunchTemplateLaunchTemplateDataBlockDeviceMappingsEbsEncryptedSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("no");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "`Ebs` properties in `BlockDeviceMappings` for the specified Amazon Machine Image (AMI): an `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2LaunchTemplateAmiBlockDeviceMappingEncryptionSettingsSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = Mocks.MOCK_IMAGE_ID;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final Boolean setAmiEbsBlockDeviceEncryptedEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(DescribeImagesRequest.class), any()))
                .thenReturn(Mocks.getDescribeImagesMockResponse(setAmiEbsBlockDeviceEncryptedEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2LaunchTemplateAmiImageIdMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");
        when(typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings()).thenReturn("yes");

        final Boolean setLaunchTemplateData = true;
        final String setImageId = null;
        final Boolean setBlockDeviceMappings = null;
        final Boolean setBlockDeviceMapping = null;
        final Boolean setEbs = null;
        final Boolean setEbsEncrypted = null;
        final String setEbsKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2LaunchTemplateMockTargetModel(setLaunchTemplateData,
                setImageId, setBlockDeviceMappings, setBlockDeviceMapping, setEbs, setEbsEncrypted, setEbsKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::LaunchTemplate",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2VolumeKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setEncrypted = false;
        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsEc2VolumeKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setEncrypted = true;
        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setEncrypted = false;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setEbsEncryptionByDefaultEnabled = false;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2VolumeWithUseGetEbsEncryptionByDefaultAsFallbackSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("yes");

        final Boolean setEncrypted = false;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final Boolean setEbsEncryptionByDefaultEnabled = true;
        when(proxy.injectCredentialsAndInvokeV2(any(GetEbsEncryptionByDefaultRequest.class), any()))
                .thenReturn(Mocks.getEbsEncryptionByDefaultMockResponse(setEbsEncryptionByDefaultEnabled));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant: EBS encryption by default is enabled.");
    }

    protected final void awsEc2VolumeEncryptedMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setEncrypted = null;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property is missing.");
    }

    protected final void awsEc2VolumeEncryptedFailure(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setEncrypted = false;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEc2VolumeEncryptedSuccess(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback()).thenReturn("no");

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEc2VolumeMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EC2::Volume", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEfsFileSystemKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = false;
        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEfsFileSystemMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EFS::FileSystem",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsEfsFileSystemKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsEfsFileSystemMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EFS::FileSystem",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsEfsFileSystemEncryptedMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = null;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEfsFileSystemMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EFS::FileSystem",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property is missing.");
    }

    protected final void awsEfsFileSystemEncryptedFailure(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = false;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEfsFileSystemMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EFS::FileSystem",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsEfsFileSystemEncryptedSuccess(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsEfsFileSystemMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::EFS::FileSystem",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsKinesisStreamStreamEncryptionMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = null;
        final String setEncryptionType = null;
        final String setKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StreamEncryption` property is missing.");
    }

    protected final void awsKinesisStreamStreamEncryptionEncryptionTypeMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = true;
        final String setEncryptionType = null;
        final String setKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `EncryptionType` property is missing.");
    }

    protected final void awsKinesisStreamStreamEncryptionEncryptionTypeFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = true;
        final String setEncryptionType = Mocks.MOCK_INVALID_ENCRYPTION_TYPE;
        final String setKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `EncryptionType` property value is not set to `KMS`.");
    }

    protected final void awsKinesisStreamStreamEncryptionKmsKeyIdMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = true;
        final String setEncryptionType = "KMS";
        final String setKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KeyId` property is missing.");
    }

    protected final void awsKinesisStreamStreamEncryptionKmsKeyIdPatternFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = true;
        final String setEncryptionType = "KMS";
        final String setKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KeyId` property value contains an invalid pattern.");
    }

    protected final void awsKinesisStreamStreamEncryptionKmsKeyIdPatternSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStreamEncryption = true;
        final String setEncryptionType = "KMS";
        final String setKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsKinesisStreamMockTargetModel(setStreamEncryption,
                setEncryptionType, setKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Kinesis::Stream",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsLogsLogGroupKmsKeyIdMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsLogsLogGroupMockTargetModel(setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Logs::LogGroup", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `KmsKeyId` property is missing.");
    }

    protected final void awsLogsLogGroupKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsLogsLogGroupMockTargetModel(setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Logs::LogGroup", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid ARN or alias ARN pattern.");
    }

    protected final void awsLogsLogGroupKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ARN;
        final Map<String, Object> targetModel = Mocks.getAwsLogsLogGroupMockTargetModel(setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Logs::LogGroup", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbClusterKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = false;
        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsRdsDbClusterKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = true;
        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbClusterStorageEncryptedMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property is missing.");
    }

    protected final void awsRdsDbClusterStorageEncryptedFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = false;
        final String setKmsKeyId = null;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsRdsDbClusterStorageEncryptedSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = true;
        final String setKmsKeyId = null;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbClusterSourceDbClusterIdentifierSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setSourceDBClusterIdentifier = Mocks.MOCK_SOURCE_DB_INSTANCE_IDENTIFIER;
        final String setSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbClusterSnapshotIdentifierSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setSourceDBClusterIdentifier = null;
        final String setSnapshotIdentifier = Mocks.MOCK_DB_SNAPSHOT_IDENTIFIER;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbClusterMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setSourceDBClusterIdentifier, setSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBCluster", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = false;
        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsRdsDbInstanceKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = true;
        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceStorageEncryptedMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property is missing.");
    }

    protected final void awsRdsDbInstanceStorageEncryptedFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = false;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsRdsDbInstanceStorageEncryptedSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = true;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceRdsHelpersIsAuroraEngineNullValueSpecified() {
        assertThat(AwsRdsHelpers.isAuroraEngine(null)).isFalse();
    }

    protected final void awsRdsDbInstanceRdsHelpersIsAuroraEngineNonAuroraValueSpecified() {
        assertThat(AwsRdsHelpers.isAuroraEngine(Mocks.MOCK_DB_ENGINE_MYSQL)).isFalse();
    }

    protected final void awsRdsDbInstanceRdsHelpersIsAuroraEngineAuroraValueSpecified() {
        assertThat(AwsRdsHelpers.isAuroraEngine(Mocks.MOCK_DB_ENGINE_AURORA)).isTrue();
    }

    protected final void awsRdsDbInstanceDbEngineAuroraSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_AURORA;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceSourceDbInstanceIdentifierSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = Mocks.MOCK_SOURCE_DB_INSTANCE_IDENTIFIER;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceDbSnapshotIdentifierSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = Mocks.MOCK_DB_SNAPSHOT_IDENTIFIER;
        final String setDBClusterSnapshotIdentifier = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsDbInstanceDbClusterSnapshotIdentifierSpecified(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final String setKmsKeyId = null;
        final String setEngine = Mocks.MOCK_DB_ENGINE_MYSQL;
        final String setSourceDBInstanceIdentifier = null;
        final String setDBSnapshotIdentifier = null;
        final String setDBClusterSnapshotIdentifier = Mocks.MOCK_DB_CLUSTER_SNAPSHOT_IDENTIFIER;
        final Map<String, Object> targetModel = Mocks.getAwsRdsDbInstanceMockTargetModel(setStorageEncrypted,
                setKmsKeyId, setEngine, setSourceDBInstanceIdentifier, setDBSnapshotIdentifier,
                setDBClusterSnapshotIdentifier);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::DBInstance",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRdsGlobalClusterStorageEncryptedMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = null;
        final Map<String, Object> targetModel = Mocks.getAwsRdsGlobalClusterMockTargetModel(setStorageEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::GlobalCluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property is missing.");
    }

    protected final void awsRdsGlobalClusterStorageEncryptedFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = false;
        final Map<String, Object> targetModel = Mocks.getAwsRdsGlobalClusterMockTargetModel(setStorageEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::GlobalCluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `StorageEncrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsRdsGlobalClusterStorageEncryptedSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setStorageEncrypted = true;
        final Map<String, Object> targetModel = Mocks.getAwsRdsGlobalClusterMockTargetModel(setStorageEncrypted);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::RDS::GlobalCluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRedshiftClusterKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = false;
        final String setKmsKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsRedshiftClusterMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Redshift::Cluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsKeyId` property value contains an invalid pattern.");
    }

    protected final void awsRedshiftClusterKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsRedshiftClusterMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Redshift::Cluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsRedshiftClusterEncryptedMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = null;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsRedshiftClusterMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Redshift::Cluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property is missing.");
    }

    protected final void awsRedshiftClusterEncryptedFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = false;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsRedshiftClusterMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Redshift::Cluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `Encrypted` property value is not set to a boolean value of `true`.");
    }

    protected final void awsRedshiftClusterEncryptedSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final Boolean setEncrypted = true;
        final String setKmsKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsRedshiftClusterMockTargetModel(setEncrypted, setKmsKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::Redshift::Cluster",
                Mocks.MOCK_LOGICAL_ID, targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsS3BucketBucketEncryptionMissing(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = null;
        final Boolean setServerSideEncryptionConfiguration = null;
        final Boolean setServerSideEncryptionRule = null;
        final Boolean setServerSideEncryptionByDefault = null;
        final String setSSEAlgorithm = null;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `BucketEncryption` property is missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionConfigurationMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = null;
        final Boolean setServerSideEncryptionRule = null;
        final Boolean setServerSideEncryptionByDefault = null;
        final String setSSEAlgorithm = null;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "`ServerSideEncryptionConfiguration`/`ServerSideEncryptionRule` property missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = null;
        final Boolean setServerSideEncryptionByDefault = null;
        final String setSSEAlgorithm = null;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "`ServerSideEncryptionConfiguration`/`ServerSideEncryptionRule` property missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = null;
        final String setSSEAlgorithm = null;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `ServerSideEncryptionByDefault` property is missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = null;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `SSEAlgorithm` property is missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_INVALID_SSE_ALGORITHM;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "An `SSEAlgorithm` property value is not set to `aws:kms`.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultSseAlgorithmSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "A `KMSMasterKeyID` property value contains an invalid pattern.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleServerSideEncryptionByDefaultKmsKeyIdSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("no");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = Mocks.MOCK_KMS_KEY_ID;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledMissing(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("yes");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `BucketKeyEnabled` property is missing.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledFailure(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("yes");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = false;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `BucketKeyEnabled` property value is not set to a boolean value of `true`.");
    }

    protected final void awsS3BucketBucketEncryptionServerSideEncryptionRuleBucketKeyEnabledSuccess(
            final AmazonWebServicesClientProxy proxy, final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getValidateBucketKeyEnabled()).thenReturn("yes");

        final Boolean setBucketEncryption = true;
        final Boolean setServerSideEncryptionConfiguration = true;
        final Boolean setServerSideEncryptionRule = true;
        final Boolean setServerSideEncryptionByDefault = true;
        final String setSSEAlgorithm = Mocks.MOCK_DESIRED_SSE_ALGORITHM;
        final String setKMSMasterKeyID = null;
        final Boolean setBucketKeyEnabled = true;
        final Map<String, Object> targetModel = Mocks.getAwsS3BucketMockTargetModel(setBucketEncryption,
                setServerSideEncryptionConfiguration, setServerSideEncryptionRule, setServerSideEncryptionByDefault,
                setSSEAlgorithm, setKMSMasterKeyID, setBucketKeyEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::S3::Bucket", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsSnsTopicKmsKeyIdMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = null;
        final Map<String, Object> targetModel = Mocks.getAwsSnsTopicMockTargetModel(setKmsMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SNS::Topic", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `KmsMasterKeyId` property is missing.");
    }

    protected final void awsSnsTopicKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsSnsTopicMockTargetModel(setKmsMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SNS::Topic", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsMasterKeyId` property value contains an invalid pattern.");
    }

    protected final void awsSnsTopicKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Map<String, Object> targetModel = Mocks.getAwsSnsTopicMockTargetModel(setKmsMasterKeyId);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SNS::Topic", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsSqsQueueKmsKeyIdMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = null;
        final Boolean setSqsManagedSseEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response, "The `KmsMasterKeyId` property is missing.");
    }

    protected final void awsSqsQueueKmsKeyIdPatternFailure(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_INVALID_KMS_KEY_ID;
        final Boolean setSqsManagedSseEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testInvalidRequest(response, "The `KmsMasterKeyId` property value contains an invalid pattern.");
    }

    protected final void awsSqsQueueKmsKeyIdPatternSuccess(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Boolean setSqsManagedSseEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsSqsQueueSqsManagedSseEnabled(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Boolean setSqsManagedSseEnabled = true;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testNonCompliant(response,
                "The `SqsManagedSseEnabled` property for the `SSE-SQS` encryption cannot be enabled when the intent is to use the `SSE-KMS` encryption instead.");
    }

    protected final void awsSqsQueueSqsManagedSseMissing(final AmazonWebServicesClientProxy proxy, final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Boolean setSqsManagedSseEnabled = null;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }

    protected final void awsSqsQueueSqsManagedSseNotEnabled(final AmazonWebServicesClientProxy proxy,
            final Logger logger, final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);

        final String setKmsMasterKeyId = Mocks.MOCK_KMS_KEY_ID;
        final Boolean setSqsManagedSseEnabled = false;
        final Map<String, Object> targetModel = Mocks.getAwsSqsQueueMockTargetModel(setKmsMasterKeyId,
                setSqsManagedSseEnabled);

        final HookHandlerRequest request = Mocks.getHookHandlerMockRequest("AWS::SQS::Queue", Mocks.MOCK_LOGICAL_ID,
                targetModel);

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, typeConfiguration);

        testCompliant(response, "The resource is compliant.");
    }
}
