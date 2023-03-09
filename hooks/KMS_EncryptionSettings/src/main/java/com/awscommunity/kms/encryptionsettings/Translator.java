package com.awscommunity.kms.encryptionsettings;

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeImagesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeImagesResponse;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultRequest;
import software.amazon.awssdk.services.ec2.model.GetEbsEncryptionByDefaultResponse;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;

/**
 * Centralized placeholder for API requests construction, and for object
 * translations to/from the AWS SDK.
 */
public final class Translator {

    private Translator() {
    }

    /**
     * Build and return a GetEbsEncryptionByDefaultRequest.
     *
     * @return GetEbsEncryptionByDefaultRequest A
     *         {@link GetEbsEncryptionByDefaultRequest} object.
     */
    public static GetEbsEncryptionByDefaultRequest translateToGetEbsEncryptionByDefaultRequest() {
        return GetEbsEncryptionByDefaultRequest.builder().build();
    }

    /**
     * Make a GetEbsEncryptionByDefaultRequest, and return a
     * GetEbsEncryptionByDefaultResponse.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @param getEbsEncryptionByDefaultRequest
     *            A {@link GetEbsEncryptionByDefaultRequest} object.
     * @return GetEbsEncryptionByDefaultResponse A
     *         {@link GetEbsEncryptionByDefaultResponse} object.
     */
    public static GetEbsEncryptionByDefaultResponse translateFromGetEbsEncryptionByDefaultResponse(
            final AmazonWebServicesClientProxy proxy, final Ec2Client ec2Client,
            final GetEbsEncryptionByDefaultRequest getEbsEncryptionByDefaultRequest) {
        return proxy.injectCredentialsAndInvokeV2(getEbsEncryptionByDefaultRequest,
                ec2Client::getEbsEncryptionByDefault);
    }

    /**
     * Build and return a DescribeImagesRequest.
     *
     * @param imageId
     *            A {@link String} object.
     * @return DescribeImagesRequest A {@link DescribeImagesRequest} object.
     */
    public static DescribeImagesRequest translateToDescribeImagesRequest(final String imageId) {
        return DescribeImagesRequest.builder().imageIds(imageId).build();
    }

    /**
     * Make a DescribeImagesRequest, and return a DescribeImagesResponse.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @param describeImagesRequest
     *            A {@link DescribeImagesRequest} object.
     * @return DescribeImagesResponse A {@link DescribeImagesResponse} object.
     */
    public static DescribeImagesResponse translateFromDescribeImagesResponse(final AmazonWebServicesClientProxy proxy,
            final Ec2Client ec2Client, final DescribeImagesRequest describeImagesRequest) {
        return proxy.injectCredentialsAndInvokeV2(describeImagesRequest, ec2Client::describeImages);
    }

    /**
     * Build and return a DescribeInstancesRequest.
     *
     * @param instanceIds
     *            A {@link String} object.
     * @return DescribeInstancesRequest A {@link DescribeInstancesRequest} object.
     */
    public static DescribeInstancesRequest translateToDescribeInstancesRequest(final String instanceIds) {
        return DescribeInstancesRequest.builder().instanceIds(instanceIds).build();
    }

    /**
     * Make a DescribeInstancesRequest, and return a DescribeInstancesResponse.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @param describeInstancesRequest
     *            A {@link DescribeInstancesRequest} object.
     * @return DescribeInstancesResponse A {@link DescribeInstancesResponse} object.
     */
    public static DescribeInstancesResponse translateFromDescribeInstancesResponse(
            final AmazonWebServicesClientProxy proxy, final Ec2Client ec2Client,
            final DescribeInstancesRequest describeInstancesRequest) {
        return proxy.injectCredentialsAndInvokeV2(describeInstancesRequest, ec2Client::describeInstances);
    }
}
