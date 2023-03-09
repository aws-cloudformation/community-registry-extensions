package com.awscommunity.kms.encryptionsettings.services.autoscaling;

import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.isNullOrEmpty;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.ClientBuilder;
import com.awscommunity.kms.encryptionsettings.TypeConfigurationModel;
import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedService;
import com.awscommunity.kms.encryptionsettings.model.aws.autoscaling.launchconfiguration.AwsAutoscalingLaunchconfiguration;
import com.awscommunity.kms.encryptionsettings.model.aws.autoscaling.launchconfiguration.AwsAutoscalingLaunchconfigurationTargetModel;
import com.awscommunity.kms.encryptionsettings.model.aws.autoscaling.launchconfiguration.BlockDevice;
import com.awscommunity.kms.encryptionsettings.model.aws.autoscaling.launchconfiguration.BlockDeviceMapping;
import com.awscommunity.kms.encryptionsettings.services.ebs.AwsEbsHelpers;
import com.awscommunity.kms.encryptionsettings.services.ec2.AwsEc2Helpers;
import java.util.Set;
import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Service-specific AwsKmsIntegratedService implementation class.
 */
@Builder
@EqualsAndHashCode
@ToString
public final class AwsAutoScalingLaunchConfigurationKmsSettingsValidationImpl implements AwsKmsIntegratedService {

    /**
     * An {@link AmazonWebServicesClientProxy} object.
     */
    @NonNull
    private final AmazonWebServicesClientProxy proxy;

    /**
     * A {@link HookHandlerRequest} object.
     */
    @NonNull
    private final HookHandlerRequest request;

    /**
     * A {@link CallbackContext} object.
     */
    private final CallbackContext callbackContext;

    /**
     * A {@link Logger} object.
     */
    @NonNull
    private final Logger logger;

    /**
     * A {@link TypeConfigurationModel} object.
     */
    @NonNull
    private final TypeConfigurationModel typeConfiguration;

    /**
     * Consumes the hook context, and returns the resource properties for the
     * specific hook target.
     *
     * @return ResourceHookTarget Resource properties for the specified
     *         {@link software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTarget}.
     */
    @Override
    public AwsAutoscalingLaunchconfiguration getResourcePropertiesFromHookContext() {
        final HookContext hookContext = request.getHookContext();
        final AwsAutoscalingLaunchconfigurationTargetModel awsAutoscalingLaunchconfigurationTargetModel = hookContext
                .getTargetModel(AwsAutoscalingLaunchconfigurationTargetModel.class);
        final AwsAutoscalingLaunchconfiguration awsAutoscalingLaunchconfiguration = awsAutoscalingLaunchconfigurationTargetModel
                .getResourceProperties();
        return awsAutoscalingLaunchconfiguration;
    }

    /**
     * Performs validation of AWS KMS-related, user-specified settings for a given,
     * supported resource type, and returns validation results.
     *
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> validateAwsKmsSettings() {
        final AwsAutoscalingLaunchconfiguration awsAutoscalingLaunchconfiguration = getResourcePropertiesFromHookContext();

        final Set<BlockDeviceMapping> blockDeviceMappings = awsAutoscalingLaunchconfiguration.getBlockDeviceMappings();

        final String imageId = awsAutoscalingLaunchconfiguration.getImageId();
        final String instanceId = awsAutoscalingLaunchconfiguration.getInstanceId();
        // For more information on the `ImageId` and `InstanceId` properties, see:
        // https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instanceid
        if (isNullOrEmpty(imageId) && isNullOrEmpty(instanceId)) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .message("Both the `ImageId` property and the `InstanceId` property are missing.").build();
        }

        if (typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback().equals("yes")) {
            final Ec2Client ec2Client = ClientBuilder.getEc2Client();
            if (AwsEbsHelpers.isEbsEncryptionByDefaultEnabled(proxy, ec2Client)) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                        .message("The resource is compliant: EBS encryption by default is enabled.").build();
            }
        }

        if (!isNullOrEmpty(blockDeviceMappings)) {
            final String blockDeviceMappingsErrorMessagePrefix = "`Ebs` properties in `BlockDeviceMappings`:";

            BlockDevice blockDevice = null;
            Boolean encrypted = null;
            for (final BlockDeviceMapping blockDeviceMapping : blockDeviceMappings) {
                blockDevice = blockDeviceMapping.getEbs();
                if (!isNullOrEmpty(blockDevice)) {
                    encrypted = blockDevice.getEncrypted();
                    if (isNullOrEmpty(encrypted)) {
                        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                                .errorCode(HandlerErrorCode.NonCompliant)
                                .message(blockDeviceMappingsErrorMessagePrefix + " an `Encrypted` property is missing.")
                                .build();
                    } else if (!encrypted) {
                        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                                .errorCode(HandlerErrorCode.NonCompliant)
                                .message(blockDeviceMappingsErrorMessagePrefix
                                        + " an `Encrypted` property value is not set to a boolean value of `true`.")
                                .build();
                    }
                }
            }
        }

        if (typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings().equals("yes")) {
            if (!isNullOrEmpty(imageId)) {
                final Ec2Client ec2Client = ClientBuilder.getEc2Client();
                // Validate the AMI ID override specified in the ImageId property.
                final ProgressEvent<HookTargetModel, CallbackContext> amiBlockDeviceMappingsValidationResult = AwsEc2Helpers
                        .runAmiBlockDeviceMappingsValidation(proxy, ec2Client, imageId);
                if (amiBlockDeviceMappingsValidationResult.getErrorCode() != null) {
                    return amiBlockDeviceMappingsValidationResult;
                }
            }
            if (!isNullOrEmpty(instanceId) && isNullOrEmpty(imageId)) {
                final Ec2Client ec2Client = ClientBuilder.getEc2Client();
                // Validate the AMI ID inherited from the instance.
                final String imageIdFromInstanceId = AwsEc2Helpers.getImageIdFromInstanceId(proxy, ec2Client,
                        instanceId);
                final ProgressEvent<HookTargetModel, CallbackContext> amiBlockDeviceMappingsValidationResult = AwsEc2Helpers
                        .runAmiBlockDeviceMappingsValidation(proxy, ec2Client, imageIdFromInstanceId);
                if (amiBlockDeviceMappingsValidationResult.getErrorCode() != null) {
                    return amiBlockDeviceMappingsValidationResult;
                }
            }
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("The resource is compliant.").build();
    }
}
