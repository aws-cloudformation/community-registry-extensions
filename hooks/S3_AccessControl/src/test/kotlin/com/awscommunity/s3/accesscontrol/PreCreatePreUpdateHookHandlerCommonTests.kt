package com.awscommunity.s3.accesscontrol

import io.mockk.mockk
import org.assertj.core.api.Assertions.assertThat
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy
import software.amazon.cloudformation.proxy.Logger
import software.amazon.cloudformation.proxy.ProgressEvent
import software.amazon.cloudformation.proxy.StdCallbackContext
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel

open class PreCreatePreUpdateHookHandlerCommonTests : AbstractTestBase() {

    protected fun callbackContextIsInstanceOfStdCallbackContext() {
        val callbackContext = CallbackContext()
        assertThat(callbackContext).isInstanceOf(CallbackContext::class.java)
        assertThat(callbackContext).isInstanceOf(StdCallbackContext::class.java)
    }

    protected fun anS3BucketWithoutTheAccessControlPropertyShouldSucceed(
        proxy: AmazonWebServicesClientProxy,
        logger: Logger,
        handler: BaseHookHandlerStd
    ) {
        val typeConfiguration: TypeConfigurationModel = mockk()
        val targetModel: MutableMap<String, Any> = getMockTargetModelWithoutAccessControl()
        val request: HookHandlerRequest = getMockHookHandlerRequest("AWS::S3::Bucket", "Example", targetModel)
        val response: ProgressEvent<HookTargetModel, CallbackContext?> = handler.handleRequest(
            proxy,
            request,
            null,
            logger,
            typeConfiguration
        )
        testCompliant(
            response,
            "The legacy AccessControl property is either not present in the resource's configuration, or it is set to Private."
        )
    }

    protected fun anS3BucketWithTheAccessControlPropertySetToPrivateShouldSucceed(
        proxy: AmazonWebServicesClientProxy,
        logger: Logger,
        handler: BaseHookHandlerStd
    ) {
        val typeConfiguration: TypeConfigurationModel = mockk()
        val targetModel: MutableMap<String, Any> = getMockTargetModelWithAccessControlSetToPrivate()
        val request: HookHandlerRequest = getMockHookHandlerRequest("AWS::S3::Bucket", "Example", targetModel)
        val response: ProgressEvent<HookTargetModel, CallbackContext?> = handler.handleRequest(
            proxy,
            request,
            null,
            logger,
            typeConfiguration
        )
        testCompliant(
            response,
            "The legacy AccessControl property is either not present in the resource's configuration, or it is set to Private."
        )
    }

    protected fun anS3BucketWithTheAccessControlPropertySetToAValueDifferentThanPrivateShouldFail(
        proxy: AmazonWebServicesClientProxy,
        logger: Logger,
        handler: BaseHookHandlerStd
    ) {
        val typeConfiguration: TypeConfigurationModel = mockk()
        val targetModel: MutableMap<String, Any> = getMockTargetModelWithAccessControlSetToPublicRead()
        val request: HookHandlerRequest = getMockHookHandlerRequest("AWS::S3::Bucket", "Example", targetModel)
        val response: ProgressEvent<HookTargetModel, CallbackContext?> = handler.handleRequest(
            proxy,
            request,
            null,
            logger,
            typeConfiguration
        )
        testNonCompliant(
            response,
            "The legacy AccessControl property is present in the resource's configuration, and it is not set to Private.  Remove the legacy AccessControl property, or set it to Private."
        )
    }
}
