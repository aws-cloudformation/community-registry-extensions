package com.awscommunity.s3.accesscontrol

import com.awscommunity.s3.accesscontrol.model.aws.s3.bucket.AwsS3BucketTargetModel
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy
import software.amazon.cloudformation.proxy.HandlerErrorCode
import software.amazon.cloudformation.proxy.Logger
import software.amazon.cloudformation.proxy.OperationStatus
import software.amazon.cloudformation.proxy.ProgressEvent
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel

/**
 * This class is used by both pre-create and pre-update handlers for this hook,
 * and it contains common business logic for validation of target(s).
 */
abstract class BaseHookHandlerStd : BaseHookHandler<CallbackContext?, TypeConfigurationModel>() {

    /**
     * Common entry point for pre-create and pre-update validation operations.
     *
     * @param proxy AmazonWebServicesClientProxy
     * @param request HookHandlerRequest
     * @param callbackContext CallbackContext
     * @param logger Logger
     * @param typeConfiguration TypeConfigurationModel
     */
    fun handlePreCreatePreUpdateRequests(
        proxy: AmazonWebServicesClientProxy,
        request: HookHandlerRequest,
        callbackContext: CallbackContext?,
        logger: Logger,
        typeConfiguration: TypeConfigurationModel?
    ): ProgressEvent<HookTargetModel, CallbackContext?> {
        val targetModel = request.hookContext.getTargetModel(AwsS3BucketTargetModel::class.java)
        val resourceProperties = targetModel.resourceProperties
        val accessControl: String? = resourceProperties.accessControl
        if (accessControl != null && accessControl != "Private") {
            return ProgressEvent.builder<HookTargetModel, CallbackContext?>()
                .status(OperationStatus.FAILED)
                .errorCode(HandlerErrorCode.NonCompliant)
                .message("The legacy AccessControl property is present in the resource's configuration, and it is not set to Private.  Remove the legacy AccessControl property, or set it to Private.")
                .build()
        }

        return ProgressEvent.builder<HookTargetModel, CallbackContext?>()
            .status(OperationStatus.SUCCESS)
            .message("The legacy AccessControl property is either not present in the resource's configuration, or it is set to Private.")
            .build()
    }
}
