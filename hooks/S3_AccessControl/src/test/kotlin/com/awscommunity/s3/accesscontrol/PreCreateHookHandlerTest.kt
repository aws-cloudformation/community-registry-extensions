package com.awscommunity.s3.accesscontrol

import io.mockk.impl.annotations.MockK
import io.mockk.junit5.MockKExtension
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.ExtendWith
import software.amazon.cloudformation.proxy.Logger

@ExtendWith(MockKExtension::class)
class PreCreateHookHandlerTest : PreCreatePreUpdateHookHandlerCommonTests() {

    private var handler: BaseHookHandlerStd = PreCreateHookHandler()

    @MockK
    lateinit var logger: Logger

    @BeforeEach
    fun setup() {
        handler = PreCreateHookHandler()
    }

    @Test
    fun testCallbackContextIsInstanceOfStdCallbackContext() {
        callbackContextIsInstanceOfStdCallbackContext()
    }

    @Test
    fun testAnS3BucketWithoutTheAccessControlPropertyShouldSucceed() {
        anS3BucketWithoutTheAccessControlPropertyShouldSucceed(proxy, logger, handler)
    }

    @Test
    fun testAnS3BucketWithTheAccessControlPropertySetToPrivateShouldSucceed() {
        anS3BucketWithTheAccessControlPropertySetToPrivateShouldSucceed(proxy, logger, handler)
    }

    @Test
    fun testAnS3BucketWithTheAccessControlPropertySetToAValueDifferentThanPrivateShouldFail() {
        anS3BucketWithTheAccessControlPropertySetToAValueDifferentThanPrivateShouldFail(proxy, logger, handler)
    }
}
