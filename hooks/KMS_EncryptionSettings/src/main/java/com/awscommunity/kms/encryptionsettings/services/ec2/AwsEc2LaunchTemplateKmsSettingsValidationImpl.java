package com.awscommunity.kms.encryptionsettings.services.ec2;

import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches;
import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.isNullOrEmpty;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.ClientBuilder;
import com.awscommunity.kms.encryptionsettings.TypeConfigurationModel;
import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedService;
import com.awscommunity.kms.encryptionsettings.model.aws.ec2.launchtemplate.AwsEc2Launchtemplate;
import com.awscommunity.kms.encryptionsettings.model.aws.ec2.launchtemplate.AwsEc2LaunchtemplateTargetModel;
import com.awscommunity.kms.encryptionsettings.model.aws.ec2.launchtemplate.BlockDeviceMapping;
import com.awscommunity.kms.encryptionsettings.model.aws.ec2.launchtemplate.Ebs;
import com.awscommunity.kms.encryptionsettings.model.aws.ec2.launchtemplate.LaunchTemplateData;
import com.awscommunity.kms.encryptionsettings.services.ebs.AwsEbsHelpers;
import java.util.List;
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
public final class AwsEc2LaunchTemplateKmsSettingsValidationImpl implements AwsKmsIntegratedService {

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
    public AwsEc2Launchtemplate getResourcePropertiesFromHookContext() {
        final HookContext hookContext = request.getHookContext();
        final AwsEc2LaunchtemplateTargetModel awsEc2LaunchtemplateTargetModel = hookContext
                .getTargetModel(AwsEc2LaunchtemplateTargetModel.class);
        final AwsEc2Launchtemplate awsEc2Launchtemplate = awsEc2LaunchtemplateTargetModel.getResourceProperties();
        return awsEc2Launchtemplate;
    }

    /**
     * Performs validation of AWS KMS-related, user-specified settings for a given,
     * supported resource type, and returns validation results.
     *
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> validateAwsKmsSettings() {
        final AwsEc2Launchtemplate awsEc2Launchtemplate = getResourcePropertiesFromHookContext();

        final LaunchTemplateData launchTemplateData = awsEc2Launchtemplate.getLaunchTemplateData();
        if (isNullOrEmpty(launchTemplateData)) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .errorCode(HandlerErrorCode.InvalidRequest).message("The `LaunchTemplateData` property is missing.")
                    .build();
        }

        final List<BlockDeviceMapping> blockDeviceMappings = launchTemplateData.getBlockDeviceMappings();

        final String blockDeviceMappingsErrorMessagePrefix = "`Ebs` properties in `BlockDeviceMappings`:";
        Ebs ebs = null;

        if (!isNullOrEmpty(blockDeviceMappings)) {
            String kmsKeyId = null;
            for (final BlockDeviceMapping blockDeviceMapping : blockDeviceMappings) {
                ebs = blockDeviceMapping.getEbs();
                if (!isNullOrEmpty(ebs)) {
                    kmsKeyId = ebs.getKmsKeyId();
                    if (kmsKeyId != null) {
                        final Boolean ignoreKeyIdPattern = false;
                        final Boolean ignoreKeyAliasPattern = false;
                        final Boolean ignoreKeyArnPattern = false;
                        final Boolean ignoreAliasArnPattern = false;
                        if (!awsKmsKeyIdRegexMatches(kmsKeyId, ignoreKeyIdPattern, ignoreKeyAliasPattern,
                                ignoreKeyArnPattern, ignoreAliasArnPattern)) {
                            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                    .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.InvalidRequest)
                                    .message(blockDeviceMappingsErrorMessagePrefix
                                            + " a `KmsKeyId` property value contains an invalid pattern.")
                                    .build();
                        }
                    }
                }
            }
        }

        if (typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback().equals("yes")) {
            final Ec2Client ec2Client = ClientBuilder.getEc2Client();
            if (AwsEbsHelpers.isEbsEncryptionByDefaultEnabled(proxy, ec2Client)) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                        .message("The resource is compliant: EBS encryption by default is enabled.").build();
            }
        }

        if (!isNullOrEmpty(blockDeviceMappings)) {
            Boolean encrypted = null;
            for (final BlockDeviceMapping blockDeviceMapping : blockDeviceMappings) {
                ebs = blockDeviceMapping.getEbs();
                if (!isNullOrEmpty(ebs)) {
                    encrypted = ebs.getEncrypted();
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
            final String imageId = launchTemplateData.getImageId();
            if (!isNullOrEmpty(imageId)) {
                final Ec2Client ec2Client = ClientBuilder.getEc2Client();
                final ProgressEvent<HookTargetModel, CallbackContext> amiBlockDeviceMappingsValidationResult = AwsEc2Helpers
                        .runAmiBlockDeviceMappingsValidation(proxy, ec2Client, imageId);
                if (amiBlockDeviceMappingsValidationResult.getErrorCode() != null) {
                    return amiBlockDeviceMappingsValidationResult;
                }
            }
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("The resource is compliant.").build();
    }
}
