package com.awscommunity.resource.lookup;

/**
 * Constants used in this resource type.
 */
public final class Constants {

    private Constants() {
    }

    /**
     *
     * Defines a number of retries for the
     * {@link software.amazon.awssdk.core.client.config.ClientOverrideConfiguration}
     * {@link software.amazon.awssdk.core.retry.RetryPolicy} used by the
     * {@link software.amazon.awssdk.services.cloudcontrol.CloudControlClient} in
     * {@link ClientBuilder}.
     */
    public static final int CLOUDCONTROL_CLIENT_NUM_RETRIES = 15;

    /**
     *
     * Defines a number of retries for the
     * {@link software.amazon.awssdk.core.client.config.ClientOverrideConfiguration}
     * {@link software.amazon.awssdk.core.retry.RetryPolicy} used by the
     * {@link software.amazon.awssdk.services.ssm.SsmClient} in
     * {@link ClientBuilder}.
     */
    public static final int SSM_CLIENT_NUM_RETRIES = 15;

    /**
     * Defines a prefix for the primary identifier.
     */
    public static final String PRIMARY_IDENTIFIER_PREFIX = "resource-lookup-id-";

    /**
     * Defines a callback delay, in seconds, for in-progress event operations.
     */
    public static final int CALLBACK_DELAY_SECONDS = 1;

    /**
     * Defines a max value of iterations for each search in the identifiers buffer.
     */
    public static final int IDENTIFIER_ITERATOR_COUNTER_MAX = 20;
}
