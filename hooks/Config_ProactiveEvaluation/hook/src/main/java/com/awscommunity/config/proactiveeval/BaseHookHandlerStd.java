package com.awscommunity.config.proactiveeval;

import org.apache.commons.lang3.exception.ExceptionUtils;

import software.amazon.awssdk.services.config.model.InvalidParameterValueException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Methods that are common to both pre-create and pre-update handlers for this
 * hook.
 */
public abstract class BaseHookHandlerStd
    extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

  private static final String insufficientDataOutcomeDefault = "PASS";

  /**
   * Run operations common to pre-create and pre-update phases for this hook.
   *
   * @param proxy             AmazonWebServicesClientProxy
   * @param request           HookHandlerRequest
   * @param callbackContext   CallbackContext
   * @param logger            Logger
   * @param typeConfiguration TypeConfigurationModel
   * @return ProgressEvent
   */
  protected ProgressEvent<HookTargetModel, CallbackContext> preCreatePreUpdateOperations(
      final AmazonWebServicesClientProxy proxy,
      final HookHandlerRequest request,
      final CallbackContext callbackContext,
      final Logger logger,
      final TypeConfigurationModel typeConfiguration) {

    final HookContext hookContext = request.getHookContext();
    final String resourceType = hookContext.getTargetName();
    final String resourceId = hookContext.getTargetLogicalId();
    final String resourceConfiguration = hookContext
        .getTargetModel()
        .getTargetModelAsJSONObject()
        .get("resourceProperties")
        .toString();

    try {

      ProactiveComplianceHandler proactiveComplianceHandler = ProactiveComplianceHandler.builder()
          .resourceType(resourceType)
          .resourceId(resourceId)
          .resourceConfiguration(resourceConfiguration)
          .awsClientProxy(proxy)
          .outcomeForComplianceTypeInsufficientData(getInsufficientDataOutcome(typeConfiguration))
          .configClient(ClientBuilder.getConfigClient())
          .build();

      String evaluationId = proactiveComplianceHandler.startResourceEvalution();
      return proactiveComplianceHandler.assessCompliance(evaluationId);

    } catch (final InvalidParameterValueException ipve) {
      final String messageForInvalidParameterValueException = ipve.getMessage()
          + "  Check that you have specified all the required parameters"
          + " for the resource type you are describing"
          + " in your CloudFormation template, and parameters' key(s)/value(s) are correct.";
      logger.log(messageForInvalidParameterValueException);

      return ProgressEvent.<HookTargetModel, CallbackContext>builder()
          .status(OperationStatus.FAILED)
          .message(messageForInvalidParameterValueException)
          .errorCode(HandlerErrorCode.InvalidRequest)
          .build();

    } catch (final Throwable throwable) {
      logger.log(ExceptionUtils.getStackTrace(throwable));

      String messageFromThrowable = "A handler internal failure error has occurred.";
      if (throwable.getMessage() != null) {
        messageFromThrowable += String.format(" %s", throwable.getMessage());
      }

      return ProgressEvent.<HookTargetModel, CallbackContext>builder()
          .status(OperationStatus.FAILED)
          .message(messageFromThrowable)
          .errorCode(HandlerErrorCode.HandlerInternalFailure)
          .build();
    }
  }

  /**
   * Return the default value for the InsufficientDataOutcome behavior if not set
   * in the type configuration; otherwise, return the value set in the type
   * configuration.
   *
   * @param typeConfiguration TypeConfigurationModel
   * @return String
   */
  private String getInsufficientDataOutcome(final TypeConfigurationModel typeConfiguration) {
    final String outcome = typeConfiguration.getOutcomeForComplianceTypeInsufficientData();

    return (outcome == null || outcome.isEmpty()) ? insufficientDataOutcomeDefault : outcome;
  }
}
