package com.awscommunity.kms.encryptionsettings;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

import org.mockito.Mock;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Common unit tests logic base class.
 */
public abstract class AbstractTestBase {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private Logger logger;

    protected final AmazonWebServicesClientProxy getProxy() {
        return proxy;
    }

    protected final Logger getLogger() {
        return logger;
    }

    protected AbstractTestBase() {
        proxy = mock(AmazonWebServicesClientProxy.class);
        logger = mock(Logger.class);
    }

    protected final void testHandlerInternalFailure(final ProgressEvent<HookTargetModel, CallbackContext> response,
            final String message) {
        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(message);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.HandlerInternalFailure);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
    }

    protected final void testInvalidRequest(final ProgressEvent<HookTargetModel, CallbackContext> response,
            final String message) {
        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(message);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
    }

    protected final void testNonCompliant(final ProgressEvent<HookTargetModel, CallbackContext> response,
            final String message) {
        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(message);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
    }

    protected final void testCompliant(final ProgressEvent<HookTargetModel, CallbackContext> response,
            final String message) {
        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(message);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
    }
}
