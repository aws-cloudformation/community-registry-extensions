package com.awscommunity.s3.accesscontrol

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy
import software.amazon.cloudformation.proxy.Logger
import software.amazon.cloudformation.proxy.ProgressEvent
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel

/**
 * Class for validation operations on pre-create.
 */
open class PreCreateHookHandler : BaseHookHandlerStd() {

    /**
     * Function for pre-create validation operations.
     *
     * @param proxy AmazonWebServicesClientProxy
     * @param request HookHandlerRequest
     * @param callbackContext CallbackContext
     * @param logger Logger
     * @param typeConfiguration TypeConfigurationModel
     */
    override fun handleRequest(
        proxy: AmazonWebServicesClientProxy,
        request: HookHandlerRequest,
        callbackContext: CallbackContext?,
        logger: Logger,
        typeConfiguration: TypeConfigurationModel
    ): ProgressEvent<HookTargetModel, CallbackContext?> {
        return handlePreCreatePreUpdateRequests(proxy, request, callbackContext, logger, typeConfiguration)
    }
}
