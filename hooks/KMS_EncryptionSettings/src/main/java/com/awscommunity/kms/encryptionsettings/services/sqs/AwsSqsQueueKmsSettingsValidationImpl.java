package com.awscommunity.kms.encryptionsettings.services.sqs;

import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches;
import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.isNullOrEmpty;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.TypeConfigurationModel;
import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedService;
import com.awscommunity.kms.encryptionsettings.model.aws.sqs.queue.AwsSqsQueue;
import com.awscommunity.kms.encryptionsettings.model.aws.sqs.queue.AwsSqsQueueTargetModel;
import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;
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
public final class AwsSqsQueueKmsSettingsValidationImpl implements AwsKmsIntegratedService {

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
    public AwsSqsQueue getResourcePropertiesFromHookContext() {
        final HookContext hookContext = request.getHookContext();
        final AwsSqsQueueTargetModel awsSqsQueueTargetModel = hookContext.getTargetModel(AwsSqsQueueTargetModel.class);
        final AwsSqsQueue awsSqsQueue = awsSqsQueueTargetModel.getResourceProperties();
        return awsSqsQueue;
    }

    /**
     * Performs validation of AWS KMS-related, user-specified settings for a given,
     * supported resource type, and returns validation results.
     *
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> validateAwsKmsSettings() {
        final AwsSqsQueue awsSqsQueue = getResourcePropertiesFromHookContext();

        final String kmsKeyId = awsSqsQueue.getKmsMasterKeyId();
        if (!isNullOrEmpty(kmsKeyId)) {
            final Boolean ignoreKeyIdPattern = false;
            final Boolean ignoreKeyAliasPattern = false;
            final Boolean ignoreKeyArnPattern = false;
            final Boolean ignoreAliasArnPattern = false;
            if (!awsKmsKeyIdRegexMatches(kmsKeyId, ignoreKeyIdPattern, ignoreKeyAliasPattern, ignoreKeyArnPattern,
                    ignoreAliasArnPattern)) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                        .errorCode(HandlerErrorCode.InvalidRequest)
                        .message("The `KmsMasterKeyId` property value contains an invalid pattern.").build();
            }
        } else {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .errorCode(HandlerErrorCode.NonCompliant).message("The `KmsMasterKeyId` property is missing.")
                    .build();
        }

        final Boolean sqsManagedSseEnabled = awsSqsQueue.getSqsManagedSseEnabled();
        if (!isNullOrEmpty(sqsManagedSseEnabled)) {
            if (sqsManagedSseEnabled) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .message(
                                "The `SqsManagedSseEnabled` property for the `SSE-SQS` encryption cannot be enabled when the intent is to use the `SSE-KMS` encryption instead.")
                        .build();
            }
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("The resource is compliant.").build();
    }
}
