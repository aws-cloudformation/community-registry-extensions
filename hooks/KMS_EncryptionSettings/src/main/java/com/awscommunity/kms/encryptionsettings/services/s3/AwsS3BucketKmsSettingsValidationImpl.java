package com.awscommunity.kms.encryptionsettings.services.s3;

import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.awsKmsKeyIdRegexMatches;
import static com.awscommunity.kms.encryptionsettings.helpers.ResourcePropertyValuesValidationHelpers.isNullOrEmpty;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.TypeConfigurationModel;
import com.awscommunity.kms.encryptionsettings.factory.AwsKmsIntegratedService;
import com.awscommunity.kms.encryptionsettings.model.aws.s3.bucket.AwsS3Bucket;
import com.awscommunity.kms.encryptionsettings.model.aws.s3.bucket.AwsS3BucketTargetModel;
import com.awscommunity.kms.encryptionsettings.model.aws.s3.bucket.BucketEncryption;
import com.awscommunity.kms.encryptionsettings.model.aws.s3.bucket.ServerSideEncryptionByDefault;
import com.awscommunity.kms.encryptionsettings.model.aws.s3.bucket.ServerSideEncryptionRule;
import java.util.List;
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
public final class AwsS3BucketKmsSettingsValidationImpl implements AwsKmsIntegratedService {

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
    public AwsS3Bucket getResourcePropertiesFromHookContext() {
        final HookContext hookContext = request.getHookContext();
        final AwsS3BucketTargetModel awsS3BucketTargetModel = hookContext.getTargetModel(AwsS3BucketTargetModel.class);
        final AwsS3Bucket awsS3Bucket = awsS3BucketTargetModel.getResourceProperties();
        return awsS3Bucket;
    }

    /**
     * Performs validation of AWS KMS-related, user-specified settings for a given,
     * supported resource type, and returns validation results.
     *
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> validateAwsKmsSettings() {
        final AwsS3Bucket awsS3Bucket = getResourcePropertiesFromHookContext();

        final BucketEncryption bucketEncryption = awsS3Bucket.getBucketEncryption();
        if (!isNullOrEmpty(bucketEncryption)) {
            final List<ServerSideEncryptionRule> serverSideEncryptionRuleList = bucketEncryption
                    .getServerSideEncryptionConfiguration();
            if (!isNullOrEmpty(serverSideEncryptionRuleList)) {
                String kmsKeyId = null;
                for (final ServerSideEncryptionRule serverSideEncryptionRule : serverSideEncryptionRuleList) {
                    final ServerSideEncryptionByDefault serverSideEncryptionByDefault = serverSideEncryptionRule
                            .getServerSideEncryptionByDefault();
                    if (!isNullOrEmpty(serverSideEncryptionByDefault)) {
                        kmsKeyId = serverSideEncryptionByDefault.getKMSMasterKeyID();
                        if (kmsKeyId != null) {
                            final Boolean ignoreKeyIdPattern = false;
                            final Boolean ignoreKeyAliasPattern = false;
                            final Boolean ignoreKeyArnPattern = false;
                            final Boolean ignoreAliasArnPattern = false;
                            if (!awsKmsKeyIdRegexMatches(kmsKeyId, ignoreKeyIdPattern, ignoreKeyAliasPattern,
                                    ignoreKeyArnPattern, ignoreAliasArnPattern)) {
                                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                        .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.InvalidRequest)
                                        .message("A `KMSMasterKeyID` property value contains an invalid pattern.")
                                        .build();
                            }
                        }

                        final String sseAlgorithm = serverSideEncryptionByDefault.getSSEAlgorithm();
                        if (sseAlgorithm != null) {
                            final String desiredSSEAlgorithm = "aws:kms";
                            if (!sseAlgorithm.equals(desiredSSEAlgorithm)) {
                                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                        .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.NonCompliant)
                                        .message("An `SSEAlgorithm` property value is not set to `"
                                                + desiredSSEAlgorithm + "`.")
                                        .build();
                            }
                        } else {
                            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                    .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.NonCompliant)
                                    .message("The `SSEAlgorithm` property is missing.").build();
                        }
                    } else {
                        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                                .errorCode(HandlerErrorCode.NonCompliant)
                                .message("The `ServerSideEncryptionByDefault` property is missing.").build();
                    }

                    if (typeConfiguration.getValidateBucketKeyEnabled().equals("yes")) {
                        final Boolean bucketKeyEnabled = serverSideEncryptionRule.getBucketKeyEnabled();
                        if (!isNullOrEmpty(bucketKeyEnabled)) {
                            if (!bucketKeyEnabled) {
                                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                        .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.NonCompliant)
                                        .message(
                                                "The `BucketKeyEnabled` property value is not set to a boolean value of `true`.")
                                        .build();
                            }
                        } else {
                            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                    .status(OperationStatus.FAILED).errorCode(HandlerErrorCode.NonCompliant)
                                    .message("The `BucketKeyEnabled` property is missing.").build();
                        }
                    }
                }
            } else {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .message("`ServerSideEncryptionConfiguration`/`ServerSideEncryptionRule` property missing.")
                        .build();
            }
        } else {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .errorCode(HandlerErrorCode.NonCompliant).message("The `BucketEncryption` property is missing.")
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("The resource is compliant.").build();
    }
}
