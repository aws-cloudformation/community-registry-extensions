package com.awscommunity.appsync.breakingchangedetection;

import com.awscommunity.appsync.breakingchangedetection.model.aws.appsync.graphqlschema.AwsAppsyncGraphqlschema;
import com.awscommunity.appsync.breakingchangedetection.model.aws.appsync.graphqlschema.AwsAppsyncGraphqlschemaTargetModel;
import com.awscommunity.appsync.breakingchangedetection.schema.AppSyncSchemaDiffReporter;
import com.awscommunity.appsync.breakingchangedetection.schema.AppSyncSchemaDiffUtil;
import com.google.common.collect.ImmutableSet;
import graphql.schema.idl.errors.SchemaProblem;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

import java.util.Collection;

public class PreUpdateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    private static final Collection<String> HOOK_TARGET_NAMES = ImmutableSet.of(
        "AWS::AppSync::GraphQLSchema"
    );

    private static final String BREAKING_ERROR_MESSAGE =
        "Breaking changes have been detected for this AWS::AppSync::GraphQLSchema:\n";

    private static final String SUCCESS_MESSAGE =
        "Successfully verified there are no breaking changes for AWS::AppSync::GraphQLSchema.\n";

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
        final AmazonWebServicesClientProxy proxy,
        final HookHandlerRequest request,
        final CallbackContext callbackContext,
        final Logger logger,
        final TypeConfigurationModel typeConfiguration) {

        final String targetName = request.getHookContext().getTargetName();

        if (!HOOK_TARGET_NAMES.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        logger.log(String.format("Successfully invoked PreUpdateHookHandler for target %s.", targetName));

        final ResourceHookTargetModel<AwsAppsyncGraphqlschema> targetModel = request.getHookContext()
                .getTargetModel(AwsAppsyncGraphqlschemaTargetModel.class);
        final AwsAppsyncGraphqlschema previousResourceProperties = targetModel.getPreviousResourceProperties();
        final AwsAppsyncGraphqlschema resourceProperties = targetModel.getResourceProperties();

        boolean considerDangerousChanges = false;
        if (typeConfiguration != null && typeConfiguration.getConsiderDangerousChangesBreaking() != null) {
            considerDangerousChanges = typeConfiguration.getConsiderDangerousChangesBreaking();
        }

        try {
            final AppSyncSchemaDiffReporter reporter = AppSyncSchemaDiffUtil.diffSchema(previousResourceProperties,
                    resourceProperties, proxy, logger);
            final String changeReport = reporter.getFormattedChangeReport();
            logger.log(changeReport);
            if (reporter.validateChanges(!considerDangerousChanges)) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.SUCCESS)
                        .message(SUCCESS_MESSAGE + changeReport)
                        .build();
            } else {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.FAILED)
                        .message(BREAKING_ERROR_MESSAGE + changeReport)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .build();
            }
        } catch (SchemaProblem ex) {
            logger.log(ex.toString());
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("Unable to parse the new schema with the following errors: " + ex.getErrors().toString())
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        } catch (Exception ex) {
            logger.log(ex.toString());
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("An unexpected error occurred validating the schema: " + ex.toString())
                    .errorCode(HandlerErrorCode.HandlerInternalFailure)
                    .build();
        }
    }
}
