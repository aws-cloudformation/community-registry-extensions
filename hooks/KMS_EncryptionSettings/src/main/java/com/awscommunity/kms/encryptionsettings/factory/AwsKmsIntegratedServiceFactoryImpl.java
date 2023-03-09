package com.awscommunity.kms.encryptionsettings.factory;

import com.awscommunity.kms.encryptionsettings.CallbackContext;
import com.awscommunity.kms.encryptionsettings.TypeConfigurationModel;
import com.awscommunity.kms.encryptionsettings.services.autoscaling.AwsAutoScalingLaunchConfigurationKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.cloudtrail.AwsCloudTrailTrailKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.cloudwatchlogs.AwsLogsLogGroupKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.dynamodb.AwsDynamoDbGlobalTableKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.dynamodb.AwsDynamoDbTableKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.ebs.AwsEc2VolumeKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.ec2.AwsEc2InstanceKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.ec2.AwsEc2LaunchTemplateKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.efs.AwsEfsFileSystemKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.kinesis.AwsKinesisStreamKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.rds.AwsRdsDbClusterKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.rds.AwsRdsDbInstanceKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.rds.AwsRdsGlobalClusterKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.redshift.AwsRedshiftClusterKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.s3.AwsS3BucketKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.sns.AwsSnsTopicKmsSettingsValidationImpl;
import com.awscommunity.kms.encryptionsettings.services.sqs.AwsSqsQueueKmsSettingsValidationImpl;
import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;

/**
 * AwsKmsIntegratedService factory implementation class.
 */
@Builder
@EqualsAndHashCode
@ToString
public final class AwsKmsIntegratedServiceFactoryImpl implements AwsKmsIntegratedServiceFactory {

    /**
     * An {@link AmazonWebServicesClientProxy} object.
     */
    @NonNull
    private final AmazonWebServicesClientProxy proxy;

    /**
     * A {@link HookHandlerRequest} object.
     */
    @NonNull
    private final HookHandlerRequest request;

    /**
     * A {@link CallbackContext} object.
     */
    private final CallbackContext callbackContext;

    /**
     * A {@link Logger} object.
     */
    @NonNull
    private final Logger logger;

    /**
     * A {@link TypeConfigurationModel} object.
     */
    @NonNull
    private final TypeConfigurationModel typeConfiguration;

    /**
     * Returns a specified factory based on a given AWS KMS-integrated service
     * resource type.
     *
     * @return AwsKmsIntegratedService The {@link AwsKmsIntegratedService}
     *         service-specific factory to use.
     */
    public AwsKmsIntegratedService getFactory() {
        final String targetName = request.getHookContext().getTargetName();
        switch (targetName) {
            case "AWS::AutoScaling::LaunchConfiguration" :
                return AwsAutoScalingLaunchConfigurationKmsSettingsValidationImpl.builder().proxy(proxy)
                        .request(request).callbackContext(callbackContext).logger(logger)
                        .typeConfiguration(typeConfiguration).build();
            case "AWS::CloudTrail::Trail" :
                return AwsCloudTrailTrailKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::DynamoDB::GlobalTable" :
                return AwsDynamoDbGlobalTableKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::DynamoDB::Table" :
                return AwsDynamoDbTableKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::EC2::Instance" :
                return AwsEc2InstanceKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::EC2::LaunchTemplate" :
                return AwsEc2LaunchTemplateKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::EC2::Volume" :
                return AwsEc2VolumeKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::EFS::FileSystem" :
                return AwsEfsFileSystemKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::Kinesis::Stream" :
                return AwsKinesisStreamKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::Logs::LogGroup" :
                return AwsLogsLogGroupKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::RDS::DBCluster" :
                return AwsRdsDbClusterKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::RDS::DBInstance" :
                return AwsRdsDbInstanceKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::RDS::GlobalCluster" :
                return AwsRdsGlobalClusterKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::Redshift::Cluster" :
                return AwsRedshiftClusterKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::S3::Bucket" :
                return AwsS3BucketKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::SNS::Topic" :
                return AwsSnsTopicKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            case "AWS::SQS::Queue" :
                return AwsSqsQueueKmsSettingsValidationImpl.builder().proxy(proxy).request(request)
                        .callbackContext(callbackContext).logger(logger).typeConfiguration(typeConfiguration).build();
            default :
                throw new UnsupportedTargetException(targetName);
        }
    }
}
