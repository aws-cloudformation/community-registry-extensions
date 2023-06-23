package com.awscommunity.resource.lookup;

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
 * ReadHandler.
 */
public class ReadHandler extends BaseHandlerStd {

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
        logger.log("*** READ handler ***");

        final ResourceModel requestModel = request.getDesiredResourceState();

        // Using a Progress Chain to perform operations shown next;
        // see:
        // https://github.com/aws-cloudformation/cloudformation-cli-java-plugin/blob/master/src/main/java/software/amazon/cloudformation/proxy/CallChain.java
        // for more information.

        // Initialize the proxy context.
        return proxy.initiate("AwsCommunity-Resource-Lookup::Read", proxySsmClient, requestModel, callbackContext)

                // Construct the GetParameterRequest.
                .translateToServiceRequest(Translator::translateToGetParameterRequest)

                // Make the API call with the GetParameterRequest.
                .makeServiceCall((getParameterRequest, client) -> {
                    final SsmClient ssmClient = client.client();
                    GetParameterResponse getParameterResponse = null;
                    try {
                        getParameterResponse = client.injectCredentialsAndInvokeV2(
                                Translator.translateToGetParameterRequest(requestModel), ssmClient::getParameter);
                    } catch (final ParameterNotFoundException pnfe) {
                        throw new CfnNotFoundException(ResourceModel.TYPE_NAME, requestModel.getResourceLookupId());
                    } catch (final AwsServiceException e) {
                        throw new CfnGeneralServiceException(ResourceModel.TYPE_NAME, e);
                    }

                    logger.log(String.format("%s has successfully been read.", ResourceModel.TYPE_NAME));
                    return getParameterResponse;
                })

                // Gather all properties of the resource; call the
                // GetParameter API to fetch properties needed to
                // populate the model; note that here, when calling
                // translateFromGetParameterResponse() will also call
                // the ListTagsForResource API to get the tags for the
                // parameter, so to populate tag values as well. The
                // ResourceProperties field value is here retrieved
                // with a separate call to Cloud Control API.
                .done(getParameterResponse -> ProgressEvent.defaultSuccessHandler(
                        Translator.getModel(getParameterResponse, proxySsmClient, proxyCloudControlClient)));
    }
}
