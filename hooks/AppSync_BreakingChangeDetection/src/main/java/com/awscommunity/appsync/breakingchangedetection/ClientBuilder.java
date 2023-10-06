package com.awscommunity.appsync.breakingchangedetection;

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.cloudformation.LambdaWrapper;

public class ClientBuilder {

    public static S3Client getS3Client() {
        return S3Client.builder()
            .httpClient(LambdaWrapper.HTTP_CLIENT)
            .build();
    }
}