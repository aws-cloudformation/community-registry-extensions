package com.awscommunity.s3.accesscontrol

import io.mockk.impl.annotations.MockK
import org.assertj.core.api.Assertions.assertThat
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy
import software.amazon.cloudformation.proxy.HandlerErrorCode
import software.amazon.cloudformation.proxy.OperationStatus
import software.amazon.cloudformation.proxy.ProgressEvent
import software.amazon.cloudformation.proxy.hook.HookContext
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel

abstract class AbstractTestBase {

    @MockK
    protected lateinit var proxy: AmazonWebServicesClientProxy

    protected fun getMockTargetModelWithoutAccessControl(): MutableMap<String, Any> {
        val targetModel: MutableMap<String, Any> = HashMap()
        val resourceProperties: MutableMap<String, Any> = HashMap()
        targetModel["resourceProperties"] = resourceProperties
        return targetModel
    }

    protected fun getMockTargetModelWithAccessControlSetToPrivate(): MutableMap<String, Any> {
        val targetModel: MutableMap<String, Any> = HashMap()
        val resourceProperties: MutableMap<String, Any> = HashMap()
        resourceProperties["AccessControl"] = "Private"
        targetModel["resourceProperties"] = resourceProperties
        return targetModel
    }

    protected fun getMockTargetModelWithAccessControlSetToPublicRead(): MutableMap<String, Any> {
        val targetModel: MutableMap<String, Any> = HashMap()
        val resourceProperties: MutableMap<String, Any> = HashMap()
        resourceProperties["AccessControl"] = "PublicRead"
        targetModel["resourceProperties"] = resourceProperties
        return targetModel
    }

    protected fun getMockHookHandlerRequest(targetName: String, targetLogicalId: String, targetModel: MutableMap<String, Any>): HookHandlerRequest {
        return HookHandlerRequest.builder().hookContext(
            HookContext.builder().targetName(targetName)
                .targetLogicalId(targetLogicalId).targetModel(HookTargetModel.of(targetModel)).build()
        )
            .build()
    }

    protected fun testNonCompliant(
        response: ProgressEvent<HookTargetModel, CallbackContext?>,
        message: String
    ) {
        assertThat(response).isNotNull()
        assertThat(response.message).isEqualTo(message)
        assertThat(response.status).isEqualTo(OperationStatus.FAILED)
        assertThat(response.errorCode).isEqualTo(HandlerErrorCode.NonCompliant)
        assertThat(response.callbackContext).isNull()
        assertThat(response.callbackDelaySeconds).isEqualTo(0)
    }

    protected fun testCompliant(
        response: ProgressEvent<HookTargetModel, CallbackContext?>,
        message: String
    ) {
        assertThat(response).isNotNull()
        assertThat(response.message).isEqualTo(message)
        assertThat(response.status).isEqualTo(OperationStatus.SUCCESS)
        assertThat(response.errorCode).isNull()
        assertThat(response.callbackContext).isNull()
        assertThat(response.callbackDelaySeconds).isEqualTo(0)
    }
}
