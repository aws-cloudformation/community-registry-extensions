package com.awscommunity.kms.encryptionsettings.factory;

/**
 * AwsKmsIntegratedService factory interface.
 */
public interface AwsKmsIntegratedServiceFactory {

    /**
     * Returns a specified factory based on a given AWS KMS-integrated service
     * resource type.
     *
     * @return AwsKmsIntegratedService The {@link AwsKmsIntegratedService}
     *         service-specific factory to use.
     */
    AwsKmsIntegratedService getFactory();
}
