package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.verifyNoMoreInteractions;
import static org.mockito.Mockito.when;

import java.time.Duration;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceRequest;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceResponse;
import software.amazon.awssdk.services.cloudcontrol.model.ListResourcesRequest;
import software.amazon.awssdk.services.cloudcontrol.model.ListResourcesResponse;
import software.amazon.awssdk.services.cloudcontrol.model.ResourceDescription;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

@ExtendWith(MockitoExtension.class)
public class CreateHandlerResourceLookupTest extends AbstractTestBase {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private ProxyClient<SsmClient> proxySsmClient;

    @Mock
    private ProxyClient<CloudControlClient> proxyCloudControlClient;

    @Mock
    private SsmClient ssmClient;

    @Mock
    private CloudControlClient cloudControlClient;

    @Mock
    private CreateHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        proxyCloudControlClient = mockProxy(proxy, cloudControlClient);
        handler = spy(new CreateHandler());
    }

    @AfterEach
    public void tearDown() {
        verifyNoMoreInteractions(cloudControlClient);
        verifyNoMoreInteractions(ssmClient);
    }

    @Test
    public void firstHandlerInvocationShouldSetThePrimaryIdAndReinvoke() {
        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final CallbackContext currentContext = new CallbackContext();

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.IN_PROGRESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(Constants.CALLBACK_DELAY_SECONDS);
        assertThat(response.getResourceModel()).isEqualTo(request.getDesiredResourceState());
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void moreThanOneResultMatching() {
        final Collection<ResourceDescription> resourceDescriptions = new ArrayList<ResourceDescription>();
        resourceDescriptions.add(ResourceDescription.builder().identifier("test").build());
        resourceDescriptions.add(ResourceDescription.builder().identifier("test1").build());

        final ListResourcesResponse listResourcesResponse = ListResourcesResponse.builder()
                .resourceDescriptions(resourceDescriptions).build();
        when(cloudControlClient.listResources(any(ListResourcesRequest.class))).thenReturn(listResourcesResponse);

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo("The query returned more than one result; cannot provide a single resource identifier.");
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.GeneralServiceException);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isEqualTo(null);
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void identifiersBufferStillContainsData() {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "TestOnly";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final List<String> identifiersBuffer = Mocks.getIdentifiersBufferMock(21);

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");
        currentContext.setIdentifiersBuffer(identifiersBuffer);

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.IN_PROGRESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(Constants.CALLBACK_DELAY_SECONDS);
        assertThat(response.getResourceModel()).isEqualTo(request.getDesiredResourceState());
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void nextTokenSetInCallbackContextAndIdentifiersBufferEmpty() {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "TestOnly";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final List<String> identifiersBuffer = Mocks.getIdentifiersBufferMock(11);

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");
        currentContext.setIdentifiersBuffer(identifiersBuffer);
        currentContext.setListResourcesNextToken("test");

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.IN_PROGRESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(Constants.CALLBACK_DELAY_SECONDS);
        assertThat(response.getResourceModel()).isEqualTo(request.getDesiredResourceState());
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void noMatchesFound() {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "TestOnly";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final List<String> identifiersBuffer = Mocks.getIdentifiersBufferMock(11);

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");
        currentContext.setIdentifiersBuffer(identifiersBuffer);
        currentContext.setListResourcesNextToken(null);

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(
                "The provided search query did not return a matching result; cannot provide a single resource identifier.");
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.GeneralServiceException);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isEqualTo(null);
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void nextTokenFoundAndSetInCallbackContext() {
        final Collection<ResourceDescription> resourceDescriptions = new ArrayList<ResourceDescription>();
        resourceDescriptions.add(ResourceDescription.builder().identifier("test").build());
        resourceDescriptions.add(ResourceDescription.builder().identifier("test1").build());

        final ListResourcesResponse listResourcesResponse = ListResourcesResponse.builder()
                .resourceDescriptions(resourceDescriptions).nextToken("test").build();
        when(cloudControlClient.listResources(any(ListResourcesRequest.class))).thenReturn(listResourcesResponse);

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");

        handler.handleRequest(proxy, request, currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(currentContext.getListResourcesNextToken()).isEqualTo("test");
    }

    @Test
    public void nextTokenNullAndNotSetInCallbackContext() {
        final Collection<ResourceDescription> resourceDescriptions = new ArrayList<ResourceDescription>();
        resourceDescriptions.add(ResourceDescription.builder().identifier("test").build());
        resourceDescriptions.add(ResourceDescription.builder().identifier("test1").build());

        final ListResourcesResponse listResourcesResponse = ListResourcesResponse.builder()
                .resourceDescriptions(resourceDescriptions).nextToken(null).build();
        when(cloudControlClient.listResources(any(ListResourcesRequest.class))).thenReturn(listResourcesResponse);

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");

        handler.handleRequest(proxy, request, currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(currentContext.getListResourcesNextToken()).isNull();
    }

    @Test
    public void nextTokenEmptyAndNotSetInCallbackContext() {
        final Collection<ResourceDescription> resourceDescriptions = new ArrayList<ResourceDescription>();
        resourceDescriptions.add(ResourceDescription.builder().identifier("test").build());
        resourceDescriptions.add(ResourceDescription.builder().identifier("test1").build());

        final ListResourcesResponse listResourcesResponse = ListResourcesResponse.builder()
                .resourceDescriptions(resourceDescriptions).nextToken("").build();
        when(cloudControlClient.listResources(any(ListResourcesRequest.class))).thenReturn(listResourcesResponse);

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");

        handler.handleRequest(proxy, request, currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(currentContext.getListResourcesNextToken()).isNull();
    }

    @Test
    public void jsonProcessingExceptionThrown() {
        final String resourceProperties = "{";

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "TestOnly";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final List<String> identifiersBuffer = Mocks.getIdentifiersBufferMock(11);

        final CallbackContext currentContext = new CallbackContext();
        currentContext.setResourceLookupId("test");
        currentContext.setIdentifiersBuffer(identifiersBuffer);
        currentContext.setListResourcesNextToken(null);

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                currentContext, proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isEqualTo(
                "Unexpected end-of-input: expected close marker for Object (start marker at [Source: (String)\"{\"; line: 1, column: 1])"
                        + "\n" + " at [Source: (String)\"{\"; line: 1, column: 2]");
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.GeneralServiceException);
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isEqualTo(null);
        assertThat(response.getResourceModels()).isNull();
    }
}
