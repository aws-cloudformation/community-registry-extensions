package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.atLeastOnce;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.verifyNoMoreInteractions;
import static org.mockito.Mockito.when;

import java.time.Duration;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceRequest;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceResponse;
import software.amazon.awssdk.services.cloudcontrol.model.ResourceDescription;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.AddTagsToResourceRequest;
import software.amazon.awssdk.services.ssm.model.AddTagsToResourceResponse;
import software.amazon.awssdk.services.ssm.model.GetParameterRequest;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceResponse;
import software.amazon.awssdk.services.ssm.model.Parameter;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.awssdk.services.ssm.model.RemoveTagsFromResourceRequest;
import software.amazon.awssdk.services.ssm.model.RemoveTagsFromResourceResponse;
import software.amazon.awssdk.services.ssm.model.Tag;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.exceptions.CfnNotFoundException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

@ExtendWith(MockitoExtension.class)
public class UpdateHandlerTest extends AbstractTestBase {

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
    private UpdateHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        proxyCloudControlClient = mockProxy(proxy, cloudControlClient);
        handler = spy(new UpdateHandler());
    }

    @AfterEach
    public void tearDown() {
        verify(ssmClient, atLeastOnce()).serviceName();
        verifyNoMoreInteractions(proxySsmClient.client());
    }

    @Test
    public void handleRequestSuccess() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder().parameter(
                Parameter.builder().type(ParameterType.STRING_LIST).name("test").value("test,test,test").build())
                .build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Collection<Tag> tagList = new ArrayList<Tag>();
        final ListTagsForResourceResponse listTagsForResourceResponse = ListTagsForResourceResponse.builder()
                .tagList(tagList).build();
        when(ssmClient.listTagsForResource(any(ListTagsForResourceRequest.class)))
                .thenReturn(listTagsForResourceResponse);

        final Map<String, String> tags = new HashMap<String, String>();

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(tags).resourceProperties(resourceProperties).resourceLookupRoleArn("test")
                .build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).desiredResourceTags(tags).previousResourceState(model)
                .previousResourceTags(tags).build();

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                new CallbackContext(), proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isEqualTo(request.getDesiredResourceState());
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void parameterNotFoundExceptionThrown() {
        when(ssmClient.getParameter(any(GetParameterRequest.class)))
                .thenThrow(ParameterNotFoundException.builder().build());

        final Map<String, String> tags = new HashMap<String, String>();

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(tags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).desiredResourceTags(tags).previousResourceState(model)
                .previousResourceTags(tags).build();

        assertThatExceptionOfType(CfnNotFoundException.class).isThrownBy(() -> {
            handler.handleRequest(proxy, request, new CallbackContext(), proxySsmClient, proxyCloudControlClient,
                    LOGGER);
        });
    }

    @Test
    public void awsServiceExceptionThrown() {
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenThrow(AwsServiceException.builder().build());

        final Map<String, String> tags = new HashMap<String, String>();

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(tags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).desiredResourceTags(tags).previousResourceState(model)
                .previousResourceTags(tags).build();

        assertThatExceptionOfType(CfnGeneralServiceException.class).isThrownBy(() -> {
            handler.handleRequest(proxy, request, new CallbackContext(), proxySsmClient, proxyCloudControlClient,
                    LOGGER);
        });
    }

    @Test
    public void removeAndAddTagsSuccess() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder().parameter(
                Parameter.builder().type(ParameterType.STRING_LIST).name("test").value("test,test,test").build())
                .build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final RemoveTagsFromResourceResponse removeTagsFromResourceResponse = RemoveTagsFromResourceResponse.builder()
                .build();
        when(ssmClient.removeTagsFromResource(any(RemoveTagsFromResourceRequest.class)))
                .thenReturn(removeTagsFromResourceResponse);

        final AddTagsToResourceResponse addTagsToResourceResponse = AddTagsToResourceResponse.builder().build();
        when(ssmClient.addTagsToResource(any(AddTagsToResourceRequest.class))).thenReturn(addTagsToResourceResponse);

        final Collection<Tag> tagList = new ArrayList<Tag>();
        tagList.add(Tag.builder().key("Test2").value("test2").build());
        tagList.add(Tag.builder().key("TestB").value("testB").build());
        final ListTagsForResourceResponse listTagsForResourceResponse = ListTagsForResourceResponse.builder()
                .tagList(tagList).build();
        when(ssmClient.listTagsForResource(any(ListTagsForResourceRequest.class)))
                .thenReturn(listTagsForResourceResponse);

        final Map<String, String> requestTags = new HashMap<String, String>();
        requestTags.put("Test2", "test2");
        final Map<String, String> resourceTags = new HashMap<String, String>();
        resourceTags.put("TestB", "testB");
        // Add the Test2 stack-level tag to the desired resource state: it will be set
        // in the model when reading from the read handler.
        resourceTags.put("Test2", "test2");

        final Map<String, String> previousRequestTags = new HashMap<String, String>();
        previousRequestTags.put("Test1", "test1");
        final Map<String, String> previousResourceTags = new HashMap<String, String>();
        previousResourceTags.put("TestA", "testA");

        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final GetResourceResponse getResourceResponse = GetResourceResponse.builder()
                .resourceDescription(ResourceDescription.builder().properties(resourceProperties).build()).build();
        when(cloudControlClient.getResource(any(GetResourceRequest.class))).thenReturn(getResourceResponse);

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(resourceTags).resourceProperties(resourceProperties)
                .resourceLookupRoleArn("test").build();

        final ResourceModel previousModel = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(previousResourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).desiredResourceTags(requestTags).previousResourceState(previousModel)
                .previousResourceTags(previousRequestTags).build();

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                new CallbackContext(), proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);

        // Also verify that the Test2 stack-level tag is set in the model when reading
        // from the read handler.
        assertThat(response.getResourceModel()).isEqualTo(request.getDesiredResourceState());

        assertThat(response.getResourceModels()).isNull();
    }
}
