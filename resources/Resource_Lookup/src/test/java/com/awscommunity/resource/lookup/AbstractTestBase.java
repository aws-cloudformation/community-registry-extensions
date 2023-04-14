package com.awscommunity.resource.lookup;

import java.util.concurrent.CompletableFuture;
import java.util.function.Function;
import software.amazon.awssdk.awscore.AwsRequest;
import software.amazon.awssdk.awscore.AwsResponse;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.core.pagination.sync.SdkIterable;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Credentials;
import software.amazon.cloudformation.proxy.LoggerProxy;
import software.amazon.cloudformation.proxy.ProxyClient;

public abstract class AbstractTestBase {
    protected static final Credentials MOCK_CREDENTIALS;
    protected static final LoggerProxy LOGGER;

    static {
        MOCK_CREDENTIALS = new Credentials("accessKey", "secretKey", "token");
        LOGGER = new LoggerProxy();
    }

    static ProxyClient<SsmClient> mockProxy(final AmazonWebServicesClientProxy proxy, final SsmClient ssmClient) {
        return new ProxyClient<SsmClient>() {
            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseT injectCredentialsAndInvokeV2(
                    final RequestT request, final Function<RequestT, ResponseT> requestFunction) {
                return proxy.injectCredentialsAndInvokeV2(request, requestFunction);
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> CompletableFuture<ResponseT> injectCredentialsAndInvokeV2Async(
                    final RequestT request, final Function<RequestT, CompletableFuture<ResponseT>> requestFunction) {
                throw new UnsupportedOperationException();
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse, IterableT extends SdkIterable<ResponseT>> IterableT injectCredentialsAndInvokeIterableV2(
                    final RequestT request, final Function<RequestT, IterableT> requestFunction) {
                return proxy.injectCredentialsAndInvokeIterableV2(request, requestFunction);
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseInputStream<ResponseT> injectCredentialsAndInvokeV2InputStream(
                    final RequestT requestT, final Function<RequestT, ResponseInputStream<ResponseT>> function) {
                throw new UnsupportedOperationException();
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseBytes<ResponseT> injectCredentialsAndInvokeV2Bytes(
                    final RequestT requestT, final Function<RequestT, ResponseBytes<ResponseT>> function) {
                throw new UnsupportedOperationException();
            }

            @Override
            public SsmClient client() {
                return ssmClient;
            }
        };
    }

    static ProxyClient<CloudControlClient> mockProxy(final AmazonWebServicesClientProxy proxy,
            final CloudControlClient cloudControlClient) {
        return new ProxyClient<CloudControlClient>() {
            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseT injectCredentialsAndInvokeV2(
                    final RequestT request, final Function<RequestT, ResponseT> requestFunction) {
                return proxy.injectCredentialsAndInvokeV2(request, requestFunction);
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> CompletableFuture<ResponseT> injectCredentialsAndInvokeV2Async(
                    final RequestT request, final Function<RequestT, CompletableFuture<ResponseT>> requestFunction) {
                throw new UnsupportedOperationException();
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse, IterableT extends SdkIterable<ResponseT>> IterableT injectCredentialsAndInvokeIterableV2(
                    final RequestT request, final Function<RequestT, IterableT> requestFunction) {
                return proxy.injectCredentialsAndInvokeIterableV2(request, requestFunction);
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseInputStream<ResponseT> injectCredentialsAndInvokeV2InputStream(
                    final RequestT requestT, final Function<RequestT, ResponseInputStream<ResponseT>> function) {
                throw new UnsupportedOperationException();
            }

            @Override
            public <RequestT extends AwsRequest, ResponseT extends AwsResponse> ResponseBytes<ResponseT> injectCredentialsAndInvokeV2Bytes(
                    final RequestT requestT, final Function<RequestT, ResponseBytes<ResponseT>> function) {
                throw new UnsupportedOperationException();
            }

            @Override
            public CloudControlClient client() {
                return cloudControlClient;
            }
        };
    }
}
