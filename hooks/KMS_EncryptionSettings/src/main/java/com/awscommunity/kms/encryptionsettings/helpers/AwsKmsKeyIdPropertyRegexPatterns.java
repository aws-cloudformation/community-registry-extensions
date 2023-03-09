package com.awscommunity.kms.encryptionsettings.helpers;

import lombok.AllArgsConstructor;
import lombok.Getter;

/**
 * Defines an enum for regular expression patterns for use with validation of
 * user-provided values for properties (such as, for example, `KmsKeyId`:
 * https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-kmskeyid).
 */
@AllArgsConstructor
public enum AwsKmsKeyIdPropertyRegexPatterns {

    /**
     * The key ID.
     */
    KEY_ID("^[a-f0-9]{8}(-[a-f0-9]{4}){3}-[a-f0-9]{12}$"),

    /**
     * The key alias.
     */
    KEY_ALIAS("^alias/[a-zA-Z0-9/_\\-]+$"),

    /**
     * The key ARN.
     */
    KEY_ARN("^arn:aws(-[a-z0-9]+)*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}(-[a-f0-9]{4}){3}-[a-f0-9]{12}$"),

    /**
     * The key alias ARN.
     */
    ALIAS_ARN("^arn:aws(-[a-z0-9]+)*:kms:[a-z0-9-]+:[0-9]{12}:alias/[a-zA-Z0-9/_\\-]+$");

    /**
     * Getter for the regex pattern.
     */
    @Getter
    private final String regexPattern;
}
