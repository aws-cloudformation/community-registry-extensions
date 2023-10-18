package com.awscommunity.appsync.breakingchangedetection.schema;

import com.awscommunity.appsync.breakingchangedetection.model.aws.appsync.graphqlschema.AwsAppsyncGraphqlschema;
import graphql.schema.GraphQLSchema;
import graphql.schema.diff.SchemaDiff;
import graphql.schema.diff.SchemaDiffSet;
import graphql.schema.idl.RuntimeWiring;
import graphql.schema.idl.SchemaGenerator;
import graphql.schema.idl.SchemaParser;
import graphql.schema.idl.TypeDefinitionRegistry;
import java.util.Objects;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;

import static com.awscommunity.appsync.breakingchangedetection.schema.AppSyncDirectives.APPSYNC_DIRECTIVE_DEFINITIONS;
import static com.awscommunity.appsync.breakingchangedetection.schema.AppSyncScalars.APPSYNC_SCALAR_DEFINITIONS;

public class AppSyncSchemaDiffUtil {

    private static final String DEFINITION_S3_LOCATION = "DefinitionS3Location";

    /**
     * Diffs the previous AppSync schema with the new version and returns a reporter which breaks down the changes
     * into different categories including breaking, dangerous, and info.
     * @param previousResourceProperties Previous resource properties.
     * @param resourceProperties Resource properties.
     * @param proxy CloudFormation proxy client.
     * @param logger Logger.
     * @return AppSyncSchemaDiffReporter which captures the differents events of interest.
     */
    public static AppSyncSchemaDiffReporter diffSchema(final AwsAppsyncGraphqlschema previousResourceProperties,
                                                       final AwsAppsyncGraphqlschema resourceProperties,
                                                       final AmazonWebServicesClientProxy proxy,
                                                       final Logger logger) {
        final SchemaDiff schemaDiff = new SchemaDiff(SchemaDiff.Options.defaultOptions().enforceDirectives());
        final GraphQLSchema currentSchema = getGraphQLSchema(previousResourceProperties, proxy);
        final GraphQLSchema newSchema = getGraphQLSchema(resourceProperties, proxy);
        final SchemaDiffSet diffset = SchemaDiffSet.diffSetFromSdl(currentSchema, newSchema);

        final AppSyncSchemaDiffReporter reporter = new AppSyncSchemaDiffReporter(logger, resourceProperties.getApiId());
        schemaDiff.diffSchema(diffset, reporter);
        return reporter;
    }

    /**
     * This method gets the GraphQLSchema required for the SchemaDiff operation by loading the definitions,
     * parsing them, and building the schema object.
     * @param schemaConfig The schema definition to use for getting the SDL.
     * @param proxy The CloudFormation proxy.
     * @return
     */
    private static GraphQLSchema getGraphQLSchema(final AwsAppsyncGraphqlschema schemaConfig,
                                                  final AmazonWebServicesClientProxy proxy) {
        final String definition = getSdlString(schemaConfig, proxy);
        final TypeDefinitionRegistry registry = parseSchema(definition);
        return buildSchemaFromDefinitions(registry);
    }

    /**
     * This method is responsible for getting the schema SDL as a String. If the schema is defined directly in the Definition property,
     * it simply return its contents. Otherwise, if the DefinitionS3Location property is used, it loads the schema from S3 and returns it
     * as a String.
     * @param schemaConfig The schema definition to use for getting the SDL.
     * @param proxy The CloudFormation proxy.
     * @return SDL String
     */
    private static String getSdlString(final AwsAppsyncGraphqlschema schemaConfig,
                                final AmazonWebServicesClientProxy proxy) {
        final String definition = Objects.toString(schemaConfig.get("Definition"), null);
        if (definition != null) {
            return definition;
        } else {
            final String s3Location = Objects.toString(schemaConfig.get(DEFINITION_S3_LOCATION), null);
            if (null == s3Location) {
                throw new IllegalArgumentException("No schema definition property found!");
            }

            final String s3Bucket = S3DefinitionUtil.getS3Bucket(s3Location, DEFINITION_S3_LOCATION);
            final String s3Key = S3DefinitionUtil.getS3Key(s3Location, DEFINITION_S3_LOCATION);
            return S3DefinitionUtil.readStringFromS3(proxy, s3Bucket, s3Key);
        }
    }

    /**
     * Parse the SDL into a type definition registry. Note that we append the built in AppSync directive definitions.
     * @param definition The SDL definition String.
     * @return TypeDefinitionRegistry for use in generating the Schema object.
     */
    private static TypeDefinitionRegistry parseSchema(final String definition) {
        final SchemaParser schemaParser = new SchemaParser();
        final TypeDefinitionRegistry registry = schemaParser.parse(definition);
        APPSYNC_DIRECTIVE_DEFINITIONS.forEach(registry::add);
        APPSYNC_SCALAR_DEFINITIONS.forEach(registry::add);
        return registry;
    }

    /**
     * Build the Schema object given the registry of type definitions.
     * @param registry The type definition registry.
     * @return GraphQLSchema
     */
    private static GraphQLSchema buildSchemaFromDefinitions(final TypeDefinitionRegistry registry) {
        final SchemaGenerator schemaGenerator = new SchemaGenerator();
        return schemaGenerator.makeExecutableSchema(
                SchemaGenerator.Options.defaultOptions(),
                registry,
                RuntimeWiring.MOCKED_WIRING);
    }
}
