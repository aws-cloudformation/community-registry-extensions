package com.awscommunity.appsync.breakingchangedetection.schema;

import com.awscommunity.appsync.breakingchangedetection.ClientBuilder;
import org.apache.commons.lang3.ArrayUtils;
import org.apache.commons.lang3.StringUtils;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;

public class S3DefinitionUtil {

    /**
     * The S3 path delimiter.
     */
    public static final String S3_PATH_DELIMITER = "/";

    /**
     * The S3 min file length.
     */
    public static final int S3_MIN_FILE_LENGTH = 3;

    /**
     * Given a S3 original file path like "s3://bucket/folder/file", returns S3
     * compatible file key, and in this case it is "folder/file".
     *
     * @param path
     *            Raw file path
     * @param fieldName
     *            The field we are trying to parse
     * @return S3 compatible file key
     */
    public static String getS3Key(final String path, final String fieldName) {
        final String[] arr = StringUtils.splitByWholeSeparator(path,
                S3_PATH_DELIMITER);
        if (arr.length < S3_MIN_FILE_LENGTH) {
            // invalid file location
            throw new IllegalArgumentException("S3 location not valid for " + fieldName);
        }

        // Remove the first segment "s3:"
        final String[] pathArr = ArrayUtils.removeAll(arr, 0, 1);
        final String key = StringUtils.join(pathArr, S3_PATH_DELIMITER);
        return key;
    }

    /**
     * Given an original file path like "s3://bucket/folder/file", returns its
     * bucket, and in this case it is "bucket".
     *
     * @param path
     *            Raw file path
     * @param fieldName
     *            The field we are trying to parse
     * @return bucket name
     */
    public static String getS3Bucket(final String path, final String fieldName) {
        final String[] arr = StringUtils.splitByWholeSeparator(path,
                S3_PATH_DELIMITER);
        if (arr.length < S3_MIN_FILE_LENGTH) {
            throw new IllegalArgumentException("S3 location not valid for " + fieldName);
        }

        final String bucketName = arr[1];
        return bucketName;
    }

    /**
     * Read a string from an s3 object at the given bucket and key.
     * @param proxy Cloudformation Proxy.
     * @param s3Bucket S3 bucket name.
     * @param s3Key S3 Key name.
     * @return String
     */
    public static String readStringFromS3(final AmazonWebServicesClientProxy proxy,
                                           final String s3Bucket,
                                           final String s3Key) {
        final S3Client s3Client = ClientBuilder.getS3Client();
        final GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(s3Bucket)
                .key(s3Key)
                .build();
        return proxy.injectCredentialsAndInvokeV2Bytes(getObjectRequest, s3Client::getObjectAsBytes)
                .asUtf8String();
    }
}
