package com.awscommunity.config.proactiveeval;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;
import software.amazon.awssdk.services.config.ConfigClient;
import software.amazon.awssdk.services.config.model.ComplianceType;
import software.amazon.awssdk.services.config.model.GetResourceEvaluationSummaryRequest;
import software.amazon.awssdk.services.config.model.GetResourceEvaluationSummaryResponse;
import software.amazon.awssdk.services.config.model.ResourceEvaluationStatus;
import software.amazon.awssdk.services.config.model.StartResourceEvaluationRequest;
import software.amazon.awssdk.services.config.model.StartResourceEvaluationResponse;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Used to start a proactive AWS Config check
 * and retrieve the results of the check.
 */
@Builder
@ToString
@EqualsAndHashCode
@AllArgsConstructor
public class ProactiveComplianceHandler {

  @NonNull
  public ConfigClient configClient;

  @NonNull
  public AmazonWebServicesClientProxy awsClientProxy;

  @NonNull
  public String resourceType;

  @NonNull
  public String resourceId;

  @NonNull
  public String resourceConfiguration;

  @NonNull
  public String outcomeForComplianceTypeInsufficientData;

  private final int millisecondIntervalForGetEvaluationSummary = 2000;
  private final String failOutcome = "FAIL";

  /**
   * Start an AWS Config proactive resource evaluation, and return
   * the evaluation id.
   *
   * @return String
   */
  public String startResourceEvalution() {
    StartResourceEvaluationRequest startResourceEvaluationRequest = RequestBuilders
        .buildProactiveStartResourceEvaluationRequest(
            resourceType, resourceId, resourceConfiguration);

    final StartResourceEvaluationResponse startResourceEvaluationResponse = awsClientProxy
        .injectCredentialsAndInvokeV2(
            startResourceEvaluationRequest,
            configClient::startResourceEvaluation);

    return startResourceEvaluationResponse.resourceEvaluationId();
  }

  /**
   * Assess the compliance of a resource based on an AWS Config
   * resourceEvaluationId.
   *
   * @param resourceEvaluationId the resourceEvaluationId for an AWS Config check
   * @return ProgressEvent
   * @throws InterruptedException getResourceEvaluationResult threw exception
   */
  public ProgressEvent<HookTargetModel, CallbackContext> assessCompliance(
      String resourceEvaluationId) throws InterruptedException {

    GetResourceEvaluationSummaryResponse getResourceEvaluationSummaryResponse = getResourceEvaluationResult(
        resourceEvaluationId);
    ComplianceType complianceType = getResourceEvaluationSummaryResponse.compliance();

    if (complianceType == ComplianceType.NON_COMPLIANT) {
      final String failureMessage = String.format(
          "Resource [%s] is not compliant with Config proactive compliance rules.",
          resourceType);
      return ProgressEvent.<HookTargetModel, CallbackContext>builder()
          .status(OperationStatus.FAILED)
          .errorCode(HandlerErrorCode.NonCompliant)
          .message(failureMessage)
          .build();

    } else if (complianceType == ComplianceType.INSUFFICIENT_DATA) {
      String insufficientDataMessage = String.format(
          "Insufficient data to evaluate compliance.");
      if (getResourceEvaluationSummaryResponse.evaluationStatus().failureReason() != null) {
        insufficientDataMessage = insufficientDataMessage
            + " "
            + getResourceEvaluationSummaryResponse.evaluationStatus().failureReason();
      }
      
      if (outcomeForComplianceTypeInsufficientData.equals(failOutcome)) {
        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
            .status(OperationStatus.FAILED)
            .errorCode(HandlerErrorCode.NonCompliant)
            .message(insufficientDataMessage)
            .build();
      } else {
        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
            .status(OperationStatus.SUCCESS)
            .message(insufficientDataMessage)
            .build();
      }

    } else { // COMPLIANT
      final String compliantMessage = String.format(
          "Resource [%s] is compliant with Config proactive compliance rules.",
          resourceType);
      return ProgressEvent.<HookTargetModel, CallbackContext>builder()
          .status(OperationStatus.SUCCESS)
          .message(compliantMessage)
          .build();
    }
  }

  /**
   * Retrieve the evaluation summary for a given resource based on the evaluation
   * summary id.
   *
   * @param resourceEvaluationId the resourceEvaluationId for an AWS Config check
   * @return GetResourceEvaluationSummaryResponse
   * @throws InterruptedException Thread.sleep was interupted
   */
  private GetResourceEvaluationSummaryResponse getResourceEvaluationResult(
      String resourceEvaluationId) throws InterruptedException {

    GetResourceEvaluationSummaryRequest getResourceEvaluationSummaryRequest = RequestBuilders
        .buildGetResourceEvaluationSummaryRequest(resourceEvaluationId);

    GetResourceEvaluationSummaryResponse getResourceEvaluationSummaryResponse = null;
    ResourceEvaluationStatus resourceEvaluationStatus = null;

    do {
      getResourceEvaluationSummaryResponse = awsClientProxy.injectCredentialsAndInvokeV2(
          getResourceEvaluationSummaryRequest,
          configClient::getResourceEvaluationSummary);

      resourceEvaluationStatus = getResourceEvaluationSummaryResponse.evaluationStatus().status();

      Thread.sleep(millisecondIntervalForGetEvaluationSummary);
    } while (resourceEvaluationStatus.equals(ResourceEvaluationStatus.IN_PROGRESS));

    return getResourceEvaluationSummaryResponse;
  }
}
