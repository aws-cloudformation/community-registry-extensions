package com.awscommunity.resource.lookup;

import java.util.List;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.DescribeParametersRequest;
import software.amazon.awssdk.services.ssm.model.DescribeParametersResponse;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

/**
 * ListHandler.
 */
public class ListHandler extends BaseHandlerStd {

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
    public ProgressEvent<ResourceModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final ResourceHandlerRequest<ResourceModel> request, final CallbackContext callbackContext,
            final ProxyClient<SsmClient> proxySsmClient, final ProxyClient<CloudControlClient> proxyCloudControlClient,
            final Logger logger) {
        logger.log("*** LIST handler ***");

        // Construct the DescribeParametersRequest.
        final DescribeParametersRequest describeParametersRequest = Translator
                .translateToDescribeParametersRequest(request.getNextToken());

        // Make the API call with the DescribeParametersRequest.
        final SsmClient ssmClient = proxySsmClient.client();
        final DescribeParametersResponse describeParametersResponse = proxy
                .injectCredentialsAndInvokeV2(describeParametersRequest, ssmClient::describeParameters);

        // Get a token for the next page.
        final String nextToken = describeParametersResponse.nextToken();

        // Construct resource models.
        final List<ResourceModel> models = Translator.translateFromListRequest(describeParametersResponse);

        return ProgressEvent.<ResourceModel, CallbackContext>builder().resourceModels(models).nextToken(nextToken)
                .status(OperationStatus.SUCCESS).build();
    }
}
