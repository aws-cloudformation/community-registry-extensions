package com.awscommunity.appsync.breakingchangedetection.schema;

import graphql.language.ScalarTypeDefinition;

import java.util.Set;
import java.util.stream.Collectors;

public class AppSyncScalars {

    /**
     * Set of names for built in scalars for AppSync.
     */
    public static Set<String> APPSYNC_SCALAR_NAMES = Set.of("AWSDate", "AWSTime", "AWSDateTime", "AWSTimestamp",
        "AWSEmail", "AWSJSON", "AWSPhone", "AWSURL", "AWSIPAddress");

    /**
     * List of scalar type definitions for the built in scalars for AppSync.
     */
    public static Set<ScalarTypeDefinition> APPSYNC_SCALAR_DEFINITIONS =
        APPSYNC_SCALAR_NAMES.stream().map(n -> ScalarTypeDefinition.newScalarTypeDefinition().name(n).build())
            .collect(Collectors.toSet());
}
