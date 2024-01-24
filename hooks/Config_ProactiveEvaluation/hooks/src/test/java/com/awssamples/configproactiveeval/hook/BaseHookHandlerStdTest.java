package com.awssamples.configproactiveeval.hook;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;

import software.amazon.awssdk.services.config.model.ComplianceType;
import software.amazon.awssdk.services.config.model.EvaluationStatus;
import software.amazon.awssdk.services.config.model.GetResourceEvaluationSummaryRequest;
import software.amazon.awssdk.services.config.model.GetResourceEvaluationSummaryResponse;
import software.amazon.awssdk.services.config.model.InvalidParameterValueException;
import software.amazon.awssdk.services.config.model.ResourceEvaluationStatus;
import software.amazon.awssdk.services.config.model.StartResourceEvaluationRequest;
import software.amazon.awssdk.services.config.model.StartResourceEvaluationResponse;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Tests for hook common operations.
 */
@ExtendWith(MockitoExtension.class)
public class BaseHookHandlerStdTest {

  private HookHandlerRequest request;

  @Mock
  private AmazonWebServicesClientProxy awsProxy;

  @Mock
  private Logger logger;

  @Mock
  private TypeConfigurationModel typeConfiguration;

  protected void setup() {

    // Default "Compliant" resource
    final Map<String, Object> targetModel = new HashMap<String, Object>();
    final Map<String, Object> resourceProperties = new HashMap<String, Object>();
    resourceProperties.put("InstanceId", "i-1234abcd");
    targetModel.put("resourceProperties", resourceProperties);

    // Default "User configured" OutcomeForComplianceTypeInsufficientData property
    when(typeConfiguration.getOutcomeForComplianceTypeInsufficientData()).thenReturn("PASS");

    final String resourceEvaluationId = "123";
    when(awsProxy.injectCredentialsAndInvokeV2(any(StartResourceEvaluationRequest.class), any()))
        .thenReturn(StartResourceEvaluationResponse.builder()
            .resourceEvaluationId(resourceEvaluationId)
            .build());

    request = HookHandlerRequest.builder()
        .hookContext(HookContext.builder()
            .targetName("AWS::EC2::EIP")
            .targetLogicalId("sample")
            .targetModel(HookTargetModel.of(targetModel))
            .build())
        .build();
  }

  /**
   * Test exception handling in preCreatePreUpdateOperations.
   *
   * @param handler The hook handler
   */
  protected void test_exceptionCaughtInPreCreatePreUpdateOperations(
      final BaseHookHandlerStd handler) {

    Mockito.reset(awsProxy);
    // When an exception is thrown in preCreatePreUpdateOperations
    final String exceptionMessage = "Test exception.";
    when(awsProxy.injectCredentialsAndInvokeV2(any(), any()))
        .thenThrow(new Error(exceptionMessage));

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the exception is caught and the handler
    // returns a FAILED status with the exception message
    assertNotNull(response);
    assertNull(response.getCallbackContext());
    assertThat(response.getMessage())
        .isEqualTo("A handler internal failure error has occurred. " + exceptionMessage);
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.HandlerInternalFailure);
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test null pointer exception handling in preCreatePreUpdateOperations.
   *
   * @param handler The hook handler
   */
  protected void test_nullPointerExceptionCaughtInPreCreatePreUpdateOperations(
      final BaseHookHandlerStd handler) {

    Mockito.reset(awsProxy);
    // When a null pointer exception is thrown in preCreatePreUpdateOperations
    when(awsProxy.injectCredentialsAndInvokeV2(any(), any()))
        .thenThrow(new NullPointerException());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);
  
    // The exception is caught and the handler returns a FAILED status without the exception message
    assertNotNull(response);
    assertNull(response.getCallbackContext());
    assertThat(response.getMessage())
        .isEqualTo("A handler internal failure error has occurred.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.HandlerInternalFailure);
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test invalidParameterValueException handling in preCreatePreUpdateOperations.
   *
   * @param handler The hook handler
   */
  protected void test_invalidParameterValueExceptionCaughtInPreCreatePreUpdateOperations(
      final BaseHookHandlerStd handler) {

    Mockito.reset(awsProxy);
    // When an invalidParameterValue Exception is thrown in
    // preCreatePreUpdateOperations
    final String exceptionMessage = "Test exception.";
    when(awsProxy.injectCredentialsAndInvokeV2(any(), any()))
        .thenThrow(InvalidParameterValueException.builder().message(exceptionMessage).build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // The exception is caught and the handler returns a FAILED status with the
    // exception message
    assertNotNull(response);
    assertNull(response.getCallbackContext());
    assertThat(response.getMessage())
        .isEqualTo(exceptionMessage
            + "  Check that you have specified all the required parameters"
            + " for the resource type you are describing"
            + " in your CloudFormation template, and parameters' key(s)/value(s) are correct.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that non-compliant resource properties for a given resource returns a
   * FAILED status and NonCompliant error code.
   *
   * @param handler The hook handler
   */
  protected void test_nonCompliantResource(final BaseHookHandlerStd handler) {

    // Given resource properties are non-compliant with an enabled AWS Config rule
    final Map<String, Object> targetModel = new HashMap<String, Object>();
    final Map<String, Object> resourceProperties = new HashMap<String, Object>();
    resourceProperties.put("Domain", "vpc");
    targetModel.put("resourceProperties", resourceProperties);
    targetModel.put("ResourceProperties", resourceProperties);

    final String targetName = "AWS::EC2::EIP";
    final String targetLogicalId = "sample";
    request = HookHandlerRequest.builder()
        .hookContext(HookContext.builder()
            .targetName(targetName)
            .targetLogicalId(targetLogicalId)
            .targetModel(HookTargetModel.of(targetModel))
            .build())
        .build();

    // When the resource is evaluated and the returned compliance type is
    // NON_COMPLIANT
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.SUCCEEDED)
                .build())
            .compliance(ComplianceType.NON_COMPLIANT)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a FAILED status with the NonCompliant error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Resource [AWS::EC2::EIP] is not compliant with Config proactive compliance rules.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that compliant resource properties for a given resource returns a
   * SUCCESS status and no error code.
   *
   * @param handler The hook handler
   */
  protected void test_compliantResource(final BaseHookHandlerStd handler) {

    // Given resource properties are compliant with an enabled AWS Config rule
    // When the resource is evaluated and the returned compliance type is COMPLIANT
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.SUCCEEDED)
                .build())
            .compliance(ComplianceType.COMPLIANT)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a SUCCESS status with no error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Resource [AWS::EC2::EIP] is compliant with Config proactive compliance rules.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
    assertNull(response.getErrorCode());
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that when the compliance type is INSUFFICIENT_DATA and 
   * the hook is configured for OutcomeForComplianceTypeInsufficientData equals PASS
   * that a SUCCESS status and no error code are returned.
   *
   * @param handler The hook handler
   */
  protected void test_insufficientDataConfiguredToPass(final BaseHookHandlerStd handler) {

    // Given the hook configuration for OutcomeForComplianceTypeInsufficientData equals PASS
    // When the resource is evaluated and the returned compliance type is INSUFFICIENT_DATA
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.FAILED)
                .build())
            .compliance(ComplianceType.INSUFFICIENT_DATA)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a SUCCESS status with no error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Insufficient data to evaluate compliance.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
    assertNull(response.getErrorCode());
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that when the compliance type is INSUFFICIENT_DATA and 
   * the hook is configured for OutcomeForComplianceTypeInsufficientData equals FAIL
   * that a FAILED status and NonCompliant error code are returned.
   *
   * @param handler The hook handler
   */
  protected void test_insufficientDataConfiguredToFail(final BaseHookHandlerStd handler) {

    // Given the hook configuration for OutcomeForComplianceTypeInsufficientData equals FAIL
    Mockito.reset(typeConfiguration);
    when(typeConfiguration.getOutcomeForComplianceTypeInsufficientData()).thenReturn("FAIL");

    // When the resource is evaluated and the returned compliance type is INSUFFICIENT_DATA
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.FAILED)
                .build())
            .compliance(ComplianceType.INSUFFICIENT_DATA)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a FAILED status with no error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Insufficient data to evaluate compliance.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that when the compliance type is INSUFFICIENT_DATA, and there is a failureReason, 
   * and the hook is configured for OutcomeForComplianceTypeInsufficientData equals FAIL
   * that a FAILED status and NonCompliant error code are returned and the failureReason is
   * in the response message.
   */
  protected void test_insufficientDataConfiguredToFailWithFailureReason(
      final BaseHookHandlerStd handler) {

    // Given the hook configuration for OutcomeForComplianceTypeInsufficientData equals FAIL
    Mockito.reset(typeConfiguration);
    when(typeConfiguration.getOutcomeForComplianceTypeInsufficientData()).thenReturn("FAIL");
    
    // When the resource is evaluated and the returned compliance type is INSUFFICIENT_DATA
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.FAILED)
                .failureReason("Resource evaluation timed out.")
                .build())
            .compliance(ComplianceType.INSUFFICIENT_DATA)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a FAILED status with no error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Insufficient data to evaluate compliance. Resource evaluation timed out.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
    assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }

  /**
   * Test that when the compliance type is INSUFFICIENT_DATA 
   * and the hook is configured for the OutcomeForComplianceTypeInsufficientData default value
   * that a SUCCESS status and no error code are returned.
   */
  protected void test_insufficientDataConfiguredToDefault(
      final BaseHookHandlerStd handler) {

    // Given the hook configuration for OutcomeForComplianceTypeInsufficientData equals FAIL
    Mockito.reset(typeConfiguration);
    
    // When the resource is evaluated and the returned compliance type is INSUFFICIENT_DATA
    when(awsProxy.injectCredentialsAndInvokeV2(
        any(GetResourceEvaluationSummaryRequest.class), any()))
        .thenReturn(GetResourceEvaluationSummaryResponse.builder()
            .evaluationStatus(EvaluationStatus.builder()
                .status(ResourceEvaluationStatus.FAILED)
                .failureReason("Resource evaluation timed out.")
                .build())
            .compliance(ComplianceType.INSUFFICIENT_DATA)
            .build());

    final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
        awsProxy,
        request,
        new CallbackContext(),
        logger,
        typeConfiguration);

    // Then the handler returns a FAILED status with no error code
    assertNotNull(response);
    assertThat(response.getMessage())
        .isEqualTo(
            "Insufficient data to evaluate compliance. Resource evaluation timed out.");
    assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
    assertNull(response.getErrorCode());
    assertNull(response.getCallbackContext());
    assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
  }
}
