package com.awssamples.configproactiveeval.hook;

import software.amazon.awssdk.services.config.model.EvaluationMode;
import software.amazon.awssdk.services.config.model.GetResourceEvaluationSummaryRequest;
import software.amazon.awssdk.services.config.model.ResourceConfigurationSchemaType;
import software.amazon.awssdk.services.config.model.ResourceDetails;
import software.amazon.awssdk.services.config.model.StartResourceEvaluationRequest;

/**
 * Provides a centralized placeholder for request construction.
 */
public class RequestBuilders {
  
  /**
   * Build and return a StartResourceEvaluationRequest with a PROACTIVE evaluation
   * mode.
   *
   * @param resourceType          String
   * @param resourceId            String
   * @param resourceConfiguration String
   * @return StartResourceEvaluationRequest
   */
  public static StartResourceEvaluationRequest buildProactiveStartResourceEvaluationRequest(
      final String resourceType, final String resourceId, final String resourceConfiguration) {

    // Use a low value in seconds (e.g., 25) to avoid the 30-second hook timeout.
    final int resourceEvaluationRequestTimeout = 25;

    return StartResourceEvaluationRequest.builder()
        .evaluationMode(EvaluationMode.PROACTIVE)
        .evaluationTimeout(resourceEvaluationRequestTimeout)
        .resourceDetails(ResourceDetails.builder()
            .resourceConfigurationSchemaType(ResourceConfigurationSchemaType.CFN_RESOURCE_SCHEMA)
            .resourceType(resourceType)
            .resourceId(resourceId)
            .resourceConfiguration(resourceConfiguration)
            .build())
        .build();
  }

  /**
   * Build and return a GetResourceEvaluationSummaryRequest.
   *
   * @param resourceEvaluationId String
   * @return GetResourceEvaluationSummaryRequest
   */
  public static GetResourceEvaluationSummaryRequest buildGetResourceEvaluationSummaryRequest(
      final String resourceEvaluationId) {
    return GetResourceEvaluationSummaryRequest.builder()
        .resourceEvaluationId(resourceEvaluationId).build();
  }
}
