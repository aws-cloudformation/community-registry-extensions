package com.awscommunity.appsync.breakingchangedetection;

import com.awscommunity.appsync.breakingchangedetection.schema.S3DefinitionUtil;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class S3DefinitionUtilTest {

    @Test
    public void testValidS3BucketLocation() {
        Assertions.assertEquals("schema", S3DefinitionUtil.getS3Bucket("s3://schema/original-schema.graphql",
                "DefinitionS3Location"));
    }

    @Test
    public void testValidS3KeyLocation() {
        Assertions.assertEquals("original-schema.graphql", S3DefinitionUtil.getS3Key("s3://schema/original-schema.graphql",
                "DefinitionS3Location"));
    }

    @Test
    public void testInvalidS3Key() {
        Assertions.assertThrows(IllegalArgumentException.class, () ->
                S3DefinitionUtil.getS3Key("s3://", "DefinitionS3Location"));
    }

    @Test
    public void testInvalidS3Bucket() {
        Assertions.assertThrows(IllegalArgumentException.class, () ->
                S3DefinitionUtil.getS3Bucket("s3://", "DefinitionS3Location"));
    }
}
