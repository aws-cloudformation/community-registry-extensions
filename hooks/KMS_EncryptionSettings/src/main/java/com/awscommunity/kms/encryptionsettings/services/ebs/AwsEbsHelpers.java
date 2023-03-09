package com.awscommunity.kms.encryptionsettings.services.ebs;

import com.awscommunity.kms.encryptionsettings.Translator;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultRequest;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultResponse;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;

/**
 * Validation helpers for KMS-related properties of Amazon EBS resource type
 * properties specified by the user.
 */
public final class AwsEbsHelpers {

    private AwsEbsHelpers() {
    }

    /**
     * Whether or not EBS encryption by default is enabled.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @return Boolean A {@link Boolean} object set to `true` if EBS encryption by
     *         default is enabled, or set to `false` otherwise.
     */
    public static Boolean isEbsEncryptionByDefaultEnabled(final AmazonWebServicesClientProxy proxy,
            final Ec2Client ec2Client) {
        final GetEbsEncryptionByDefaultRequest getEbsEncryptionByDefaultRequest = Translator
                .translateToGetEbsEncryptionByDefaultRequest();
        final GetEbsEncryptionByDefaultResponse getEbsEncryptionByDefaultResponse = Translator
                .translateFromGetEbsEncryptionByDefaultResponse(proxy, ec2Client, getEbsEncryptionByDefaultRequest);
        if (getEbsEncryptionByDefaultResponse.ebsEncryptionByDefault()) {
            return true;
        }
        return false;
    }
}
