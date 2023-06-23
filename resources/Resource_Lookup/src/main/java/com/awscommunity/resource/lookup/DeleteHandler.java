package com.awscommunity.resource.lookup;

import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.DeleteParameterResponse;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.exceptions.CfnNotFoundException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

/**
 * DeleteHandler.
 */
public class DeleteHandler extends BaseHandlerStd {

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
        logger.log("*** DELETE handler ***");

        final ResourceModel requestModel = request.getDesiredResourceState();

        // Using a Progress Chain to perform operations shown next;
        // see:
        // https://github.com/aws-cloudformation/cloudformation-cli-java-plugin/blob/master/src/main/java/software/amazon/cloudformation/proxy/CallChain.java
        // for more information.
        return ProgressEvent.progress(requestModel, callbackContext)

                // Delete: progress chain.
                .then(progress ->

                // Initialize the proxy context.
                proxy.initiate("AwsCommunity-Resource-Lookup::Delete", proxySsmClient, progress.getResourceModel(),
                        progress.getCallbackContext())

                        // Construct the DeleteParameterRequest.
                        .translateToServiceRequest(Translator::translateToDeleteParameterRequest)

                        // Make the API call with the
                        // DeleteParameterRequest.
                        .makeServiceCall((deleteParameterRequest, client) -> {
                            final SsmClient ssmClient = client.client();
                            DeleteParameterResponse deleteParameterResponse = null;
                            try {
                                deleteParameterResponse = client.injectCredentialsAndInvokeV2(deleteParameterRequest,
                                        ssmClient::deleteParameter);
                            } catch (final ParameterNotFoundException pnfe) {
                                throw new CfnNotFoundException(ResourceModel.TYPE_NAME,
                                        progress.getResourceModel().getResourceLookupId());
                            } catch (final AwsServiceException e) {
                                throw new CfnGeneralServiceException(ResourceModel.TYPE_NAME, e);
                            }

                            logger.log(String.format("%s successfully deleted.", ResourceModel.TYPE_NAME));
                            return deleteParameterResponse;
                        })

                        .progress())

                // Return the successful progress event without the
                // resource model set.
                .then(progress -> ProgressEvent.defaultSuccessHandler(null));
    }
}
