package com.awscommunity.kms.encryptionsettings.services.ec2;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.Translator;
import java.util.List;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeImagesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeImagesResponse;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.EbsBlockDevice;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * Validation helpers for KMS-related properties of Amazon EC2 resource type
 * properties you specify.
 */
public final class AwsEc2Helpers {

    private AwsEc2Helpers() {
    }

    /**
     * Runs the KMS settings validation of `BlockDeviceMappings` for a specified
     * Amazon Machine Image (AMI).
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @param imageId
     *            A String object.
     * @return ProgressEvent A {@link ProgressEvent} object.
     */
    public static ProgressEvent<HookTargetModel, CallbackContext> runAmiBlockDeviceMappingsValidation(
            final AmazonWebServicesClientProxy proxy, final Ec2Client ec2Client, final String imageId) {
        final DescribeImagesRequest describeImagesRequest = Translator.translateToDescribeImagesRequest(imageId);
        final DescribeImagesResponse describeImagesResponse = Translator.translateFromDescribeImagesResponse(proxy,
                ec2Client, describeImagesRequest);
        final List<software.amazon.awssdk.services.ec2.model.BlockDeviceMapping> amiBlockDeviceMappings = describeImagesResponse
                .images().get(0).blockDeviceMappings();

        EbsBlockDevice amiEbs = null;
        Boolean amiEbsEncrypted = null;
        for (final software.amazon.awssdk.services.ec2.model.BlockDeviceMapping amiBlockDeviceMapping : amiBlockDeviceMappings) {
            amiEbs = amiBlockDeviceMapping.ebs();
            amiEbsEncrypted = amiEbs.encrypted();
            if (!amiEbsEncrypted) {
                return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .message("`Ebs` properties in `BlockDeviceMappings`"
                                + " for the specified Amazon Machine Image (AMI):"
                                + " an `Encrypted` property value is not set to a boolean value of `true`.")
                        .build();
            }
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("The resource is compliant.").build();
    }

    /**
     * Returns the ID of the Amazon Machine Image (AMI) for the EC2 instance whose
     * ID is provided as an input by the user.
     *
     * @param proxy
     *            An {@link AmazonWebServicesClientProxy} object.
     * @param ec2Client
     *            An {@link Ec2Client} object.
     * @param instanceId
     *            A String object.
     * @return String A {@link String} image ID object.
     */
    public static String getImageIdFromInstanceId(final AmazonWebServicesClientProxy proxy, final Ec2Client ec2Client,
            final String instanceId) {
        final DescribeInstancesRequest describeInstancesRequest = Translator
                .translateToDescribeInstancesRequest(instanceId);
        final DescribeInstancesResponse describeInstancesResponse = Translator
                .translateFromDescribeInstancesResponse(proxy, ec2Client, describeInstancesRequest);
        return describeInstancesResponse.reservations().get(0).instances().get(0).imageId();
    }
}
