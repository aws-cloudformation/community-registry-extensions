package com.awscommunity.kms.encryptionsettings.factory;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTarget;
/**
 * Interface to be used by implementation classes for a given AWS KMS-integrated
 * service resource type supported in this hook.
 */
public interface AwsKmsIntegratedService {

    /**
     * Consumes the hook context, and returns the resource properties for the
     * specific hook target.
     *
     * @return ResourceHookTarget Resource properties for the specified
     *         {@link ResourceHookTarget}.
     */
    ResourceHookTarget getResourcePropertiesFromHookContext();

    /**
     * Performs validation of AWS KMS-related, user-specified settings for a given,
     * supported resource type, and returns validation results.
     *
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    ProgressEvent<HookTargetModel, CallbackContext> validateAwsKmsSettings();
}
