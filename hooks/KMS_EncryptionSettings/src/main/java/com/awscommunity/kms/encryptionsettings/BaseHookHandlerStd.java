package com.awscommunity.kms.encryptionsettings;

import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK;
import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS;
import static com.awscommunity.kms.encryptionsettings.HookDefaultConfigurationValues.VALIDATE_BUCKET_KEY_ENABLED;

import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedService;
import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedServiceFactoryImpl;
import org.apache.commons.lang3.exception.ExceptionUtils;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
public abstract class BaseHookHandlerStd extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    /**
     * Defines a common method for pre-create and pre-update handler operations,
     * which are the same for this hook.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param request
     *            A {@link HookHandlerRequest} object.
     * @param callbackContext
     *            A {@link CallbackContext} object.
     * @param logger
     *            A {@link Logger} object.
     * @param typeConfiguration
     *            A {@link TypeConfigurationModel} object.
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    public ProgressEvent<HookTargetModel, CallbackContext> handlePreCreatePreUpdateRequests(
            final AmazonWebServicesClientProxy proxy, final HookHandlerRequest request,
            final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        try {
            // Set default values for TypeConfigurationModel options.
            final TypeConfigurationModel typeConfigurationWithDefaultValues = setTypeConfigurationDefaultValues(
                    typeConfiguration);

            // Get the factory for the specified target.
            final AwsKmsIntegratedService awsKmsIntegratedService = getAwsKmsIntegratedServiceFromFactory(proxy,
                    request, callbackContext, logger, typeConfigurationWithDefaultValues);

            // Validate the settings for the specified target.
            final ProgressEvent<HookTargetModel, CallbackContext> validationResults = awsKmsIntegratedService
                    .validateAwsKmsSettings();

            // Return validation results.
            return validationResults;
        } catch (final UnsupportedTargetException ute) {
            throw ute;
        } catch (final Throwable throwable) {
            logger.log(ExceptionUtils.getStackTrace(throwable));
            String message = "Handler internal failure.";
            if (throwable.getMessage() != null) {
                message += String.format("  %s", throwable.getMessage());
            }
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .message(message).errorCode(HandlerErrorCode.HandlerInternalFailure).build();
        }
    }

    /**
     * Returns an {@link AwsKmsIntegratedService} object from the factory.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param request
     *            A {@link HookHandlerRequest} object.
     * @param callbackContext
     *            A {@link CallbackContext} object.
     * @param logger
     *            A {@link Logger} object.
     * @param typeConfiguration
     *            A {@link TypeConfigurationModel} object.
     * @return AwsKmsIntegratedService An {@link AwsKmsIntegratedService} object.
     */
    protected AwsKmsIntegratedService getAwsKmsIntegratedServiceFromFactory(final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request, final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        // Set up the AwsKmsIntegratedServiceFactory.
        final AwsKmsIntegratedServiceFactoryImpl awsKmsIntegratedServiceFactoryImpl = AwsKmsIntegratedServiceFactoryImpl
                .builder().proxy(proxy).request(request).callbackContext(callbackContext).logger(logger)
                .typeConfiguration(typeConfiguration).build();
        // Get the factory for the specific AwsKmsIntegratedService.
        return awsKmsIntegratedServiceFactoryImpl.getFactory();
    }

    /**
     * Sets default values for the input `TypeConfigurationModel` object if relevant
     * configuration values in the object are set to null, or if
     * `TypeConfigurationModel` itself is null.
     *
     * @param typeConfiguration
     *            A {@link TypeConfigurationModel} object.
     * @return typeConfiguration A {@link TypeConfigurationModel} object.
     */
    protected TypeConfigurationModel setTypeConfigurationDefaultValues(final TypeConfigurationModel typeConfiguration) {
        if (typeConfiguration == null) {
            final TypeConfigurationModel typeConfigurationModel = new TypeConfigurationModel();

            typeConfigurationModel
                    .setUseGetEbsEncryptionByDefaultAsFallback(USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK);

            typeConfigurationModel.setValidateAmiBlockDeviceMappingEncryptionSettings(
                    VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS);

            typeConfigurationModel.setValidateBucketKeyEnabled(VALIDATE_BUCKET_KEY_ENABLED);

            return typeConfigurationModel;
        }

        if (typeConfiguration.getUseGetEbsEncryptionByDefaultAsFallback() == null) {
            typeConfiguration.setUseGetEbsEncryptionByDefaultAsFallback(USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK);
        }

        if (typeConfiguration.getValidateAmiBlockDeviceMappingEncryptionSettings() == null) {
            typeConfiguration.setValidateAmiBlockDeviceMappingEncryptionSettings(
                    VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS);
        }

        if (typeConfiguration.getValidateBucketKeyEnabled() == null) {
            typeConfiguration.setValidateBucketKeyEnabled(VALIDATE_BUCKET_KEY_ENABLED);
        }

        return typeConfiguration;
    }
}
