package com.awscommunity.kms.encryptionsettings;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Pre-create operations.
 */
public class PreCreateHookHandler extends BaseHookHandlerStd {

    /**
     * Run pre-create handler operations.
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
    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request, final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        return handlePreCreatePreUpdateRequests(proxy, request, callbackContext, logger, typeConfiguration);
    }
}
