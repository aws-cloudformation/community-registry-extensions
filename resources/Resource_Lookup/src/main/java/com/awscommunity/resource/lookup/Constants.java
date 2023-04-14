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
     * Defines a namespace to prepend to PRIMARY_IDENTIFIER_NAME that, in
     * conjunction with PRIMARY_IDENTIFIER_NAMESPACE, should be used in
     * PRIMARY_IDENTIFIER_PREFIX to compose the names of AWS Systems Manager
     * Parameter Store parameter resources that this resource type uses to persist
     * lookup results in the user account. With Parameter Store as the backing
     * resource type, PRIMARY_IDENTIFIER_NAMESPACE should be composed using a
     * parameter hierarchy
     * (https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html)
     * to help with organizing parameters consistently. Choose the following pattern
     * for PRIMARY_IDENTIFIER_NAMESPACE:
     *
     * /CloudFormation/service-provider/service-name/data-type-name
     */
    public static final String PRIMARY_IDENTIFIER_NAMESPACE = "/CloudFormation/AwsCommunity/Resource/Lookup";

    /**
     * Defines a name for the primary identifier segment, that can be appended to
     * the PRIMARY_IDENTIFIER_NAMESPACE hierarchy.
     */
    public static final String PRIMARY_IDENTIFIER_NAME = "resource-lookup-id";

    /**
     * Defines the full prefix for the primary identifier, to create the name of AWS
     * Systems Manager Parameter Store parameter resources that the implementation
     * of this resource type creates in the user's account to persist lookup
     * results. The value for PRIMARY_IDENTIFIER_PREFIX should be following this
     * pattern:
     *
     * PRIMARY_IDENTIFIER_NAMESPACE/PRIMARY_IDENTIFIER_NAME.
     */
    public static final String PRIMARY_IDENTIFIER_PREFIX = PRIMARY_IDENTIFIER_NAMESPACE + "/" + PRIMARY_IDENTIFIER_NAME;

    /**
     * Defines a callback delay, in seconds, for in-progress event operations.
     */
    public static final int CALLBACK_DELAY_SECONDS = 1;

    /**
     * Defines a max value of iterations for each search in the identifiers buffer.
     */
    public static final int IDENTIFIER_ITERATOR_COUNTER_MAX = 20;
}
