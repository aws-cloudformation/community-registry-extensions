package com.awscommunity.appsync.breakingchangedetection;

import com.amazonaws.util.StringInputStream;
import org.junit.jupiter.api.Assertions;
import software.amazon.awssdk.awscore.AwsResponse;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import org.apache.commons.io.IOUtils;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class PreUpdateHookHandlerTest {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private Logger logger;

    @BeforeEach
    public void setup() {
        proxy = mock(AmazonWebServicesClientProxy.class);
        logger = mock(Logger.class);
    }

    @Test
    public void handleRequest_UnsupportedTarget() throws IOException {
        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AppSync::GraphqlApi").targetModel(HookTargetModel.of(new HashMap<>())).build())
                .build();

        Assertions.assertThrows(UnsupportedTargetException.class, () -> {
            new PreUpdateHookHandler().handleRequest(proxy, request, null, logger,
                    TypeConfigurationModel.builder().build());
        });
    }

    @Test
    public void handleRequest_Success() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "original-schema.graphql",
                "schema-update-non-breaking.graphql");

        final String expectedMessage = "Successfully verified there are no breaking changes for AWS::AppSync::GraphQLSchema.\n"
                + "API Id: 1 [INFO] [ADDITION] - The new API adds the field 'test.name'\n"
                + "API Id: 1 [INFO] [ADDITION] - The new API adds the field 'Query.getTest'\n";
        assertResponse(response, OperationStatus.SUCCESS, expectedMessage, null);
    }

    @Test
    public void handleRequest_Breaking() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "original-schema.graphql",
                "schema-update-breaking.graphql",
                false,
                true);

        final String expectedMessage = "Breaking changes have been detected for this AWS::AppSync::GraphQLSchema:\n"
                + "API Id: 1 [BREAKING] [INVALID] - The new API has changed field 'test.version' from type 'String!' to 'ID!'\n";

        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_Dangerous() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "original-schema.graphql",
                "schema-update-dangerous.graphql");

        final String expectedMessage = "Successfully verified there are no breaking changes for AWS::AppSync::GraphQLSchema.\n"
                + "API Id: 1 [DANGEROUS] [ADDITION] - The new API has added a new enum value 'COMPOUND'\n";

        assertResponse(response, OperationStatus.SUCCESS, expectedMessage, null);
    }

    @Test
    public void handleRequest_DangerousBreaking() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "original-schema.graphql",
                "schema-update-dangerous.graphql",
                false,
                true);

        final String expectedMessage = "Breaking changes have been detected for this AWS::AppSync::GraphQLSchema:\n"
                + "API Id: 1 [DANGEROUS] [ADDITION] - The new API has added a new enum value 'COMPOUND'\n";

        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_FailedToParse() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "original-schema.graphql",
                "schema-update-additional-sdl.graphql");

        final String expectedMessage = "Unable to parse the new schema with the following errors: "
                + "['additionalField' [@4:3] tried to use an undeclared directive 'newDirective']";
        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.InvalidRequest);
    }

    @Test
    public void handleRequest_BuiltInTypes() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "schema-with-appsync-built-in-defs.graphql",
                "schema-with-appsync-built-in-defs.graphql");

        final String expectedMessage = "Successfully verified there are no breaking changes for AWS::AppSync::GraphQLSchema.\n";
        assertResponse(response, OperationStatus.SUCCESS, expectedMessage, null);
    }

    @SuppressWarnings("unchecked")
    @Test
    public void handleRequest_GetDefinitionFromS3Succeeds() throws IOException {
        final GetObjectRequest originalRequest = GetObjectRequest.builder()
                .key("original-schema.graphql")
                .bucket("schema")
                .build();

        final GetObjectRequest updateRequest = GetObjectRequest.builder()
                .key("schema-update-non-breaking.graphql")
                .bucket("schema")
                .build();

        GetObjectResponse getObjectResponse = GetObjectResponse.builder().build();
        ResponseBytes<AwsResponse> originalResponse = ResponseBytes.fromInputStream(getObjectResponse,
                new StringInputStream(getDefinition(originalRequest.key())));

        ResponseBytes<AwsResponse> updateResponse = ResponseBytes.fromInputStream(getObjectResponse,
                new StringInputStream(getDefinition(updateRequest.key())));

        when(proxy.injectCredentialsAndInvokeV2Bytes(eq(originalRequest), any())).thenReturn(originalResponse);
        when(proxy.injectCredentialsAndInvokeV2Bytes(eq(updateRequest), any())).thenReturn(updateResponse);

        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "s3://schema/original-schema.graphql",
                "s3://schema/schema-update-non-breaking.graphql",
                true,
                false);

        final String expectedMessage = "Successfully verified there are no breaking changes for AWS::AppSync::GraphQLSchema.\n"
                + "API Id: 1 [INFO] [ADDITION] - The new API adds the field 'test.name'\n"
                + "API Id: 1 [INFO] [ADDITION] - The new API adds the field 'Query.getTest'\n";

        assertResponse(response, OperationStatus.SUCCESS, expectedMessage, null);
        verify(proxy, times(1)).injectCredentialsAndInvokeV2Bytes(eq(originalRequest), any());
        verify(proxy, times(1)).injectCredentialsAndInvokeV2Bytes(eq(updateRequest), any());
    }

    @Test
    public void handleRequest_GetDefinitionFromS3Fails() throws IOException {
        when(proxy.injectCredentialsAndInvokeV2Bytes(any(), any())).thenThrow(S3Exception.builder().statusCode(503)
                .message("Test exception").build());

        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "s3://schema/original-schema.graphql",
                "s3://schema/schema-update-non-breaking.graphql",
                true,
                false);

        final String expectedMessage = "An unexpected error occurred validating the schema: "
            + "software.amazon.awssdk.services.s3.model.S3Exception: Test exception";

        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.HandlerInternalFailure);
        verify(proxy, times(1)).injectCredentialsAndInvokeV2Bytes(any(), any());
    }

    @Test()
    public void handleRequest_invalidDefinition() {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();
        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                .considerDangerousChangesBreaking(false)
                .build();

        final Map<String, Object> targetModel = new HashMap<>();

        final Map<String, Object> previousResourceProperties = new HashMap<>();
        previousResourceProperties.put("ApiId", "1");

        final Map<String, Object> resourceProperties = new HashMap<>();
        resourceProperties.put("ApiId", "1");

        targetModel.put("ResourceProperties", resourceProperties);
        targetModel.put("PreviousResourceProperties", previousResourceProperties);

        final HookTargetModel model = HookTargetModel.of(targetModel);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AppSync::GraphQLSchema").targetModel(model).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response =
                handler.handleRequest(proxy, request, null, logger, null);

        final String expectedMessage = "An unexpected error occurred validating the schema: "
            + "java.lang.IllegalArgumentException: No schema definition property found!";
        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.HandlerInternalFailure);
        verify(proxy, never()).injectCredentialsAndInvokeV2Bytes(any(), any());
    }

    @Test()
    public void handleRequest_invalidS3Definition() throws IOException {
        final ProgressEvent<HookTargetModel, CallbackContext> response = executeSchemaDiffHook(
                "s1",
                "s2",
                true,
                false);

        final String expectedMessage = "An unexpected error occurred validating the schema: "
            + "java.lang.IllegalArgumentException: S3 location not valid for DefinitionS3Location";

        assertResponse(response, OperationStatus.FAILED, expectedMessage, HandlerErrorCode.HandlerInternalFailure);
        verify(proxy, never()).injectCredentialsAndInvokeV2Bytes(any(), any());
    }

    private ProgressEvent<HookTargetModel, CallbackContext> executeSchemaDiffHook(final String oldSchemaDefinitionLocation,
                                                                                  final String newSchemaDefinitionLocation) throws IOException {
        return executeSchemaDiffHook(oldSchemaDefinitionLocation, newSchemaDefinitionLocation, false, false);
    }

    private ProgressEvent<HookTargetModel, CallbackContext> executeSchemaDiffHook(final String oldSchemaDefinitionLocation,
                                                                                  final String newSchemaDefinitionLocation,
                                                                                  boolean useS3,
                                                                                  boolean considerDangerousChangesBreaking) throws IOException {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();
        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder()
                .considerDangerousChangesBreaking(considerDangerousChangesBreaking)
                .build();

        final HookTargetModel targetModel = getTargetModel(
                useS3 ? oldSchemaDefinitionLocation : getDefinition(oldSchemaDefinitionLocation),
                useS3 ? newSchemaDefinitionLocation : getDefinition(newSchemaDefinitionLocation),
                useS3);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AppSync::GraphQLSchema").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        return handler.handleRequest(proxy, request, null, logger, typeConfiguration);
    }

    private void assertResponse(final ProgressEvent<HookTargetModel, CallbackContext> response,
                                final OperationStatus expectedStatus,
                                final String expectedMsg,
                                final HandlerErrorCode errorCode) {
        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(expectedStatus);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage()).isEqualTo(expectedMsg);
        assertThat(response.getErrorCode()).isEqualTo(errorCode);
    }

    private String getDefinition(final String fileName) {
        final ClassLoader classLoader = getClass().getClassLoader();
        final InputStream inputStream = classLoader.getResourceAsStream(fileName);
        try {
            return IOUtils.toString(inputStream, StandardCharsets.UTF_8);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private HookTargetModel getTargetModel(final String previousSDL, final String newSdl, boolean useS3) {
        final Map<String, Object> targetModel = new HashMap<>();
        final String definitionProperty = useS3 ? "DefinitionS3Location" : "Definition";

        final Map<String, Object> previousResourceProperties = new HashMap<>();
        previousResourceProperties.put(definitionProperty, previousSDL);
        previousResourceProperties.put("ApiId", "1");

        final Map<String, Object> resourceProperties = new HashMap<>();
        resourceProperties.put(definitionProperty, newSdl);
        resourceProperties.put("ApiId", "1");


        targetModel.put("ResourceProperties", resourceProperties);
        targetModel.put("PreviousResourceProperties", previousResourceProperties);
        return HookTargetModel.of(targetModel);
    }
}
