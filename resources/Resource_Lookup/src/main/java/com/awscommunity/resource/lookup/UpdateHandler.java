package com.awscommunity.resource.lookup;

import java.util.Map;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.exceptions.CfnNotFoundException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

/**
 * UpdateHandler.
 */
public class UpdateHandler extends BaseHandlerStd {

    /**
     * Defines a method to handle requests.
     *
     * @param proxy
     *            {@link AmazonWebServicesClientProxy}
     * @param request
     *            {@link ResourceHandlerRequest}
     * @param callbackContext
     *            {@link CallbackContext}
     * @param proxySsmClient
     *            {@link ProxyClient} for {@link SsmClient}
     * @param proxyCloudControlClient
     *            {@link ProxyClient} for {@link CloudControlClient}
     * @param logger
     *            {@link Logger}
     * @return progress {@link ProgressEvent}
     */
    @Override
    protected ProgressEvent<ResourceModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final ResourceHandlerRequest<ResourceModel> request, final CallbackContext callbackContext,
            final ProxyClient<SsmClient> proxySsmClient, final ProxyClient<CloudControlClient> proxyCloudControlClient,
            final Logger logger) {
        logger.log("*** UPDATE handler ***");

        final ResourceModel requestModel = request.getDesiredResourceState();

        // Stack-level tags.
        final Map<String, String> requestTags = request.getDesiredResourceTags();
        // Resource-level tags.
        final Map<String, String> resourceTags = requestModel.getTags();
        // Combine tags.
        final Map<String, String> combinedTags = TagHelper.combineTags(requestTags, resourceTags);

        final ResourceModel previousRequestModel = request.getPreviousResourceState();

        // Previous stack-level tags.
        final Map<String, String> previousRequestTags = request.getPreviousResourceTags();
        // Previous resource-level tags.
        final Map<String, String> previousResourceTags = previousRequestModel.getTags();
        // Combine previous tags.
        final Map<String, String> previousCombinedTags = TagHelper.combineTags(previousRequestTags,
                previousResourceTags);

        // Determine which tags to add, or to remove, based on
        // combined tags above.
        final Map<String, String> combinedTagsToAdd = TagHelper.generateTagsToAdd(previousCombinedTags, combinedTags);
        final Map<String, String> combinedTagsToRemove = TagHelper.generateTagsToRemove(previousCombinedTags,
                combinedTags);

        // Using a Progress Chain to perform operations shown next;
        // see:
        // https://github.com/aws-cloudformation/cloudformation-cli-java-plugin/blob/master/src/main/java/software/amazon/cloudformation/proxy/CallChain.java
        // for more information.
        return ProgressEvent.progress(requestModel, callbackContext)

                .then(progress ->
                // Check if the resource exists.
                proxy.initiate("AwsCommunity-Resource-Lookup::Update::PreUpdateCheck", proxySsmClient,
                        progress.getResourceModel(), progress.getCallbackContext())

                        // Construct the GetParameterRequest.
                        .translateToServiceRequest(Translator::translateToGetParameterRequest)

                        // Make the API call with the
                        // GetParameterRequest.
                        .makeServiceCall((awsRequest, client) -> {
                            final SsmClient ssmClient = client.client();
                            GetParameterResponse getParameterResponse = null;
                            try {
                                getParameterResponse = client.injectCredentialsAndInvokeV2(
                                        Translator.translateToGetParameterRequest(requestModel),
                                        ssmClient::getParameter);
                            } catch (final ParameterNotFoundException pnfe) {
                                throw new CfnNotFoundException(ResourceModel.TYPE_NAME,
                                        requestModel.getResourceLookupId());
                            } catch (final AwsServiceException e) {
                                throw new CfnGeneralServiceException(ResourceModel.TYPE_NAME, e);
                            }

                            logger.log(String.format("%s has successfully been read.", ResourceModel.TYPE_NAME));
                            return getParameterResponse;
                        }).progress())

                .then((progress) -> {
                    final SsmClient ssmClient = proxySsmClient.client();

                    // Remove combined tags determined to be removed.
                    if (!combinedTagsToRemove.isEmpty()) {
                        proxySsmClient
                                .injectCredentialsAndInvokeV2(
                                        Translator.translateToRemoveTagsFromResourceRequest(
                                                requestModel.getResourceLookupId(), combinedTagsToRemove),
                                        ssmClient::removeTagsFromResource);
                    }

                    // Add combined tags determined to be added.
                    if (!combinedTagsToAdd.isEmpty()) {
                        proxySsmClient.injectCredentialsAndInvokeV2(Translator.translateToAddTagsToResourceRequest(
                                requestModel.getResourceLookupId(), combinedTagsToAdd), ssmClient::addTagsToResource);
                    }

                    return progress;
                })

                // Use the Read handler to return the resource model.
                .then(progress -> new ReadHandler().handleRequest(proxy, request, callbackContext, proxySsmClient,
                        proxyCloudControlClient, logger));
    }
}
