package com.awscommunity.kms.encryptionsettings;

/**
 * Default values for this hook to use when a relevant
 * {@link TypeConfigurationModel} value is not specified by the user.
 */
public final class HookDefaultConfigurationValues {

    private HookDefaultConfigurationValues() {
    }

    /**
     * Whether or not to instruct this hook to call the `GetEbsEncryptionByDefault`
     * API to determine if EBS encryption by default is enabled for your account in
     * the current Region. If EBS encryption by default is enabled for your account
     * in the current Region, this hook does not perform additional policy-as-code
     * validation checks for a number of resource type properties, except for
     * certain regular expression pattern checks or for certain missing mandatory
     * property checks. For more information on which resource type properties use
     * this configuration option, see `Supported resource types and properties` in
     * this hook's documentation. If you wish to activate this policy-as-code
     * validation as a fallback strategy, choose `yes`; otherwise, choose `no`
     * (default). Use the variable below to set the default value to use when a
     * value is not specified.
     */
    public static final String USE_GET_EBS_ENCRYPTION_BY_DEFAULT_AS_FALLBACK = "no";

    /**
     * When you specify an Amazon Machine Image (AMI) ID for the `ImageId` property,
     * whether to validate its BlockDeviceMapping encryption settings. Use the
     * variable below to set the default value to use when a value is not specified.
     */
    public static final String VALIDATE_AMI_BLOCK_DEVICE_MAPPING_ENCRYPTION_SETTINGS = "no";

    /**
     * Whether to validate if the BucketKeyEnabled property for the Amazon S3 bucket
     * resource type is set to `true`. Use the variable below to set the default
     * value to use when a value is not specified.
     */
    public static final String VALIDATE_BUCKET_KEY_ENABLED = "no";
}
