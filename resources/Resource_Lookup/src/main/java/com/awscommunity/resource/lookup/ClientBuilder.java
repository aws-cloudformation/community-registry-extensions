package com.awscommunity.resource.lookup;

import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.core.retry.RetryPolicy;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.cloudformation.LambdaWrapper;

/**
 * Describes static HTTP clients (to consume less memory) for API calls that
 * this resource type makes to AWS services.
 */
public final class ClientBuilder {

    private ClientBuilder() {
    }

    /**
     * Creates an HTTP client for AWS Cloud Control API.
     *
     * @return CloudControlClient {@link CloudControlClient}
     */
    public static CloudControlClient getCloudControlClient() {
        return CloudControlClient.builder().httpClient(LambdaWrapper.HTTP_CLIENT)
                .overrideConfiguration(ClientOverrideConfiguration.builder()
                        .retryPolicy(
                                RetryPolicy.builder().numRetries(Constants.CLOUDCONTROL_CLIENT_NUM_RETRIES).build())
                        .build())
                .build();
    }

    /**
     * Creates an HTTP client for AWS Systems Manager.
     *
     * @return SsmClient {@link SsmClient}
     */
    public static SsmClient getSsmClient() {
        return SsmClient.builder().httpClient(LambdaWrapper.HTTP_CLIENT)
                .overrideConfiguration(ClientOverrideConfiguration.builder()
                        .retryPolicy(RetryPolicy.builder().numRetries(Constants.SSM_CLIENT_NUM_RETRIES).build())
                        .build())
                .build();
    }
}
