package com.awscommunity.resource.lookup;

import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

/**
 * Functionality shared across Create/Read/Update/Delete/List Handlers.
 */
public abstract class BaseHandlerStd extends BaseHandler<CallbackContext> {

    /**
     * Defines a common request handler entry point method used by handler classes
     * (such as `CreateHandler`, et cetera) that extend this class. Note the
     * `callbackContext`, the `ProxyClient` for the `SsmClient`, and the
     * `ProxyClient` for the `CloudControlClient`, that are initialized on first
     * use, and reused across handler invocations. Note also the
     * `AmazonWebServicesClientProxy` object, that you'll need as part of making AWS
     * API calls: for more information, see `Permissions and authorization`:
     * https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-faq.html#resource-type-faq-permissions
     *
     * @param proxy
     *            {@link AmazonWebServicesClientProxy}
     * @param request
     *            {@link ResourceHandlerRequest}
     * @param callbackContext
     *            {@link CallbackContext}
     * @param logger
     *            {@link Logger}
     * @return progress {@link ProgressEvent}
     */
    @Override
    public final ProgressEvent<ResourceModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final ResourceHandlerRequest<ResourceModel> request, final CallbackContext callbackContext,
            final Logger logger) {
        return handleRequest(proxy, request, callbackContext != null ? callbackContext : new CallbackContext(),
                proxy.newProxy(ClientBuilder::getSsmClient), proxy.newProxy(ClientBuilder::getCloudControlClient),
                logger);
    }

    /**
     * Defines a method to handle requests; handler classes (such as
     * `CreateHandler`, et cetera) that extend this class must override and
     * implement this method as the entry point of their handler calls.
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
    protected abstract ProgressEvent<ResourceModel, CallbackContext> handleRequest(AmazonWebServicesClientProxy proxy,
            ResourceHandlerRequest<ResourceModel> request, CallbackContext callbackContext,
            ProxyClient<SsmClient> proxySsmClient, ProxyClient<CloudControlClient> proxyCloudControlClient,
            Logger logger);
}
