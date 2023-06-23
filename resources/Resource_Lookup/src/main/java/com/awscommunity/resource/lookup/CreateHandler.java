package com.awscommunity.resource.lookup;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import io.burt.jmespath.Expression;
import io.burt.jmespath.JmesPath;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceResponse;
import software.amazon.awssdk.services.cloudcontrol.model.ListResourcesResponse;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.PutParameterResponse;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

/**
 * CreateHandler.
 */
public class CreateHandler extends BaseHandlerStd {

    /**
     * Defines a method to handle requests. As per one of the output requirements of
     * the Create handler contract
     * (https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract.html#resource-type-test-contract-create):
     * "A create handler MUST always return a ProgressEvent object within 60
     * seconds. [...] In every ProgressEvent object, the create handler MUST return
     * a model [...] Every model MUST include the primaryIdentifier [...]". Since
     * this resource type performs resource lookup operations that can take longer
     * than 60 seconds, this method will first generate the primary identifier (that
     * this resource type will use as the name of an AWS Systems Manager Parameter
     * Store parameter resource it creates in your account and current region to
     * persist the lookup result), and then will use a callback mechanism across
     * subsequent calls to this Create handler to perform resource lookup
     * operations.
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
        logger.log("*** CREATE handler ***");

        final ResourceModel requestModel = request.getDesiredResourceState();

        /*
         * Generates the primary identifier on the first invocation, sets it in the
         * resource model, and returns an in-progress event to continue with the search
         * on subsequent handler invocations. On subsequent invocations of the handler,
         * the primary identifier and other properties from the model are available in
         * request.getDesiredResourceState(), and there is no need to use the callback
         * context to store and reuse model-related properties. This implementation
         * stores the resourceLookupId, that is a property in the model, in the callback
         * context to help drive the boolean callback logic shown next with a reasonably
         * meaningful property and value, but the resourceLookupId and other model
         * properties can be consumed from the model directly (with values available
         * across invocations) without storing/consuming them from the callback context.
         */
        if (callbackContext.getResourceLookupId() == null) {
            final String resourceLookupId = LookupHelper.generateResourceLookupId();
            logger.log("First handler invocation; generating and setting ResourceLookupId: " + resourceLookupId);
            requestModel.setResourceLookupId(resourceLookupId);
            final CallbackContext currentContext = new CallbackContext();
            currentContext.setResourceLookupId(resourceLookupId);
            currentContext.setListResourcesNextToken(null);
            return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.IN_PROGRESS)
                    .resourceModel(requestModel).callbackContext(currentContext)
                    .callbackDelaySeconds(Constants.CALLBACK_DELAY_SECONDS).build();
        }
        logger.log("Callback handler invocation; resourceLookupId: " + callbackContext.getResourceLookupId());
        return lookupAndStoreResult(proxy, request, callbackContext, proxySsmClient, proxyCloudControlClient, logger);
    }

    /**
     * Defines a resource lookup method, and stores the lookup result.
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
    protected ProgressEvent<ResourceModel, CallbackContext> lookupAndStoreResult(
            final AmazonWebServicesClientProxy proxy, final ResourceHandlerRequest<ResourceModel> request,
            final CallbackContext callbackContext, final ProxyClient<SsmClient> proxySsmClient,
            final ProxyClient<CloudControlClient> proxyCloudControlClient, final Logger logger) {
        final ResourceModel requestModel = request.getDesiredResourceState();

        final CallbackContext currentContext = callbackContext;
        requestModel.setResourceLookupId(currentContext.getResourceLookupId());

        final String jmesPathQuery = requestModel.getJmesPathQuery();
        final String typeName = requestModel.getTypeName();
        final String resourceLookupRoleArn = requestModel.getResourceLookupRoleArn();
        final String resourceModel = requestModel.getResourceModel();

        final CloudControlClient cloudControlClient = proxyCloudControlClient.client();
        ListResourcesResponse listResourcesResponse = null;

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        // The maxResults field for AWS Cloud Control API's
        // ListResourcesRequest:
        // https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudcontrol/model/ListResourcesRequest.html#maxResults()
        // is marked as `Reserved`; hence, not using it here. The
        // implementation shown next uses a custom pagination across
        // handler invocations, that first fetches data from the
        // `ListResources` API, and fills up IdentifiersBuffer defined
        // in the callback context POJO. If a NextToken is found, it
        // is also stored in the POJO for later consumption, after the
        // custom pagination depletes the buffer.

        // If IdentifiersBuffer is null or empty: call ListResources,
        // and fill the buffer with resource identifiers.
        if (LookupHelper.isIdentifiersBufferNullOrEmpty(currentContext.getIdentifiersBuffer())) {
            logger.log("Identifiers buffer null or empty; fetching data via the ListResources API call.");
            listResourcesResponse = proxySsmClient.injectCredentialsAndInvokeV2(
                    Translator.translateToListResourcesRequest(typeName, resourceLookupRoleArn, resourceModel,
                            callbackContext.getListResourcesNextToken()),
                    cloudControlClient::listResources);

            if (listResourcesResponse.nextToken() != null && !listResourcesResponse.nextToken().isEmpty()) {
                logger.log("NextToken found in the ListResources API response; storing it for later consumption.");
                currentContext.setListResourcesNextToken(listResourcesResponse.nextToken());
            } else {
                logger.log("NextToken not found in the ListResources API response; setting it to `null`.");
                currentContext.setListResourcesNextToken(null);
            }

            logger.log("Filling identifiers buffer with data from the ListResources API call.");
            currentContext.setIdentifiersBuffer(listResourcesResponse.resourceDescriptions().stream()
                    .map(resourceDescription -> resourceDescription.identifier()).collect(Collectors.toList()));
        } else {
            logger.log("Identifiers buffer not empty; consuming it next.");
        }

        int identifierIteratorCounter = 0;
        final List<String> identifiers = currentContext.getIdentifiersBuffer();
        final Iterator<String> identifierIterator = identifiers.iterator();
        while (identifierIterator.hasNext()) {
            if (identifierIteratorCounter == Constants.IDENTIFIER_ITERATOR_COUNTER_MAX) {
                logger.log("Reached the max value of identifier iterations for buffer; stopping the iteration.");
                break;
            }

            final String identifier = identifierIterator.next();
            logger.log("Resource identifier: " + identifier);
            final GetResourceResponse getResourceResponse = proxyCloudControlClient.injectCredentialsAndInvokeV2(
                    Translator.translateToGetResourceRequest(typeName, resourceLookupRoleArn, identifier),
                    cloudControlClient::getResource);
            final String resourcePropertiesString = getResourceResponse.resourceDescription().properties();
            try {
                if (LookupHelper.jmesPathQueryMatches(resourcePropertiesString, expression)) {
                    logger.log("JMESPath match, resource identifier: " + identifier);
                    if (requestModel.getResourceIdentifier() == null) {
                        logger.log("Setting the resource identifier to: " + identifier + ".");
                        requestModel.setResourceIdentifier(identifier);
                    } else {
                        final String message = "The query returned more than one result; cannot provide a single resource identifier.";
                        logger.log(message);
                        return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.FAILED)
                                .errorCode(HandlerErrorCode.GeneralServiceException).message(message).build();
                    }
                }
            } catch (final JsonProcessingException jpe) {
                logger.log(jpe.getMessage());
                return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.FAILED)
                        .errorCode(HandlerErrorCode.GeneralServiceException).message(jpe.getMessage()).build();
            }
            identifierIterator.remove();
            identifierIteratorCounter++;
        }

        // If IdentifiersBuffer is not empty: call the handler again,
        // and consume from the buffer.
        if (LookupHelper.isIdentifiersBufferNotEmpty(currentContext.getIdentifiersBuffer())) {
            logger.log("The identifiers buffer is not empty; calling back the handler, and consuming from the buffer.");
            currentContext.setIdentifiersBuffer(identifiers);
            return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.IN_PROGRESS)
                    .resourceModel(requestModel).callbackContext(currentContext)
                    .callbackDelaySeconds(Constants.CALLBACK_DELAY_SECONDS).build();
        }

        // If NextToken is not empty, and IdentifiersBuffer is null or
        // empty: call the handler again, and make a new API call with
        // NextToken set.
        if (LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(currentContext.getListResourcesNextToken(),
                currentContext.getIdentifiersBuffer())) {
            logger.log(
                    "NextToken exists, and the identifiers buffer is null or empty; will make a new call with the NextToken set after calling back the handler.");
            return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.IN_PROGRESS)
                    .resourceModel(requestModel).callbackContext(currentContext)
                    .callbackDelaySeconds(Constants.CALLBACK_DELAY_SECONDS).build();
        }

        if (requestModel.getResourceIdentifier() == null) {
            final String message = "The provided search query did not return a matching result; cannot provide a single resource identifier.";
            logger.log(message);
            return ProgressEvent.<ResourceModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .errorCode(HandlerErrorCode.GeneralServiceException).message(message).build();
        }

        currentContext.setIdentifiersBuffer(null);
        requestModel.setJmesPathQuery(null);

        // Pass the lookup role ARN to the next step, for it to be
        // stored in Parameter Store.
        requestModel.setResourceLookupRoleArn(resourceLookupRoleArn);

        // If only one search result has been found, complete the
        // provisioning and store the result.
        return provisionLookupStorageAndSaveLookupResult(proxy, request, currentContext, proxySsmClient,
                proxyCloudControlClient, logger);
    }

    /**
     * Defines a method to provision storage (using AWS Systems Manager Parameter
     * Store) for the result from Cloud Control API, and then stores the result.
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
    protected ProgressEvent<ResourceModel, CallbackContext> provisionLookupStorageAndSaveLookupResult(
            final AmazonWebServicesClientProxy proxy, final ResourceHandlerRequest<ResourceModel> request,
            final CallbackContext callbackContext, final ProxyClient<SsmClient> proxySsmClient,
            final ProxyClient<CloudControlClient> proxyCloudControlClient, final Logger logger) {
        final ResourceModel requestModel = request.getDesiredResourceState();

        // Stack-level tags.
        final Map<String, String> requestTags = request.getDesiredResourceTags();
        // Resource-level tags.
        final Map<String, String> resourceTags = requestModel.getTags();
        // Combine tags.
        final Map<String, String> combinedTags = TagHelper.combineTags(requestTags, resourceTags);

        // Using a Progress Chain to perform operations shown next;
        // see:
        // https://github.com/aws-cloudformation/cloudformation-cli-java-plugin/blob/master/src/main/java/software/amazon/cloudformation/proxy/CallChain.java
        // for more information.
        return ProgressEvent.progress(requestModel, callbackContext)

                // Create/stabilize progress chain; required for
                // resource creation.
                .then(progress ->
                // Initialize the proxy context.
                proxy.initiate("AwsCommunity-Resource-Lookup::Create::PutParameter", proxySsmClient,
                        progress.getResourceModel(), progress.getCallbackContext())

                        // Construct the PutParameterRequest.
                        .translateToServiceRequest(
                                (model) -> Translator.translateToPutParameterRequest(model, combinedTags))

                        // Make the API call with the
                        // PutParameterRequest.
                        .makeServiceCall((putParameterRequest, client) -> {
                            final SsmClient ssmClient = client.client();
                            PutParameterResponse putParameterResponse = null;
                            try {
                                putParameterResponse = client.injectCredentialsAndInvokeV2(putParameterRequest,
                                        ssmClient::putParameter);
                            } catch (final AwsServiceException e) {
                                throw new CfnGeneralServiceException(ResourceModel.TYPE_NAME, e);
                            }

                            logger.log(String.format("%s has successfully been created.", ResourceModel.TYPE_NAME));
                            return putParameterResponse;
                        })

                        // Stabilize step; for more information, see
                        // https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract.html
                        .stabilize((putParameterRequest, putParameterResponse, client, model, context) -> {
                            return isStabilized(model, client, logger);
                        }).progress())

                // Use the Read handler to return the resource model.
                .then(progress -> new ReadHandler().handleRequest(proxy, request, callbackContext, proxySsmClient,
                        proxyCloudControlClient, logger));
    }

    /**
     * Stabilization logic for the resource being created; retrieve the Parameter
     * Store resource, and return a boolean value of `true` if no errors occur.
     *
     * @param model
     *            {@link ResourceModel}
     * @param proxySsmClient
     *            {@link ProxyClient} for {@link SsmClient}
     * @param logger
     *            {@link Logger}
     * @return boolean `true` if stabilized, `false` otherwise
     */
    protected boolean isStabilized(final ResourceModel model, final ProxyClient<SsmClient> proxySsmClient,
            final Logger logger) {

        final SsmClient ssmClient = proxySsmClient.client();

        final String expectedPrimaryIdentifier = model.getPrimaryIdentifier().getString("/properties/ResourceLookupId");

        GetParameterResponse getParameterResponse = null;
        try {
            getParameterResponse = proxySsmClient.injectCredentialsAndInvokeV2(
                    Translator.translateToGetParameterRequest(model), ssmClient::getParameter);
        } catch (final Exception e) {
            return false;
        }

        if (getParameterResponse == null) {
            return false;
        }

        if (getParameterResponse.parameter() == null) {
            return false;
        }

        if (getParameterResponse.parameter().name() == null) {
            return false;
        }

        if (getParameterResponse.parameter().name().equals(expectedPrimaryIdentifier)) {
            logger.log(String.format("%s [%s] has stabilized.", ResourceModel.TYPE_NAME, expectedPrimaryIdentifier));
            return true;
        }

        return false;
    }
}
