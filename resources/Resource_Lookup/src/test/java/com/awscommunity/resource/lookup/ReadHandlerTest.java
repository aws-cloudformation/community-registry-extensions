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
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.GetParameterRequest;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceResponse;
import software.amazon.awssdk.services.ssm.model.Parameter;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.awssdk.services.ssm.model.Tag;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.exceptions.CfnNotFoundException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

@ExtendWith(MockitoExtension.class)
public class ReadHandlerTest extends AbstractTestBase {

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
    private ReadHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        proxyCloudControlClient = mockProxy(proxy, cloudControlClient);
        handler = spy(new ReadHandler());
    }

    @AfterEach
    public void tearDown() {
        verify(ssmClient, atLeastOnce()).serviceName();
        verifyNoMoreInteractions(proxySsmClient.client());
    }

    @Test
    public void handleRequestSuccess() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder()
                .parameter(Parameter.builder().type(ParameterType.STRING_LIST).name("test").value("test,test").build())
                .build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Collection<Tag> tagList = new ArrayList<Tag>();
        final ListTagsForResourceResponse listTagsForResourceResponse = ListTagsForResourceResponse.builder()
                .tagList(tagList).build();
        when(ssmClient.listTagsForResource(any(ListTagsForResourceRequest.class)))
                .thenReturn(listTagsForResourceResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();
        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

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

        final Map<String, String> resourceTags = new HashMap<String, String>();
        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        assertThatExceptionOfType(CfnNotFoundException.class).isThrownBy(() -> {
            handler.handleRequest(proxy, request, new CallbackContext(), proxySsmClient, proxyCloudControlClient,
                    LOGGER);
        });
    }

    @Test
    public void awsServiceExceptionThrown() {
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenThrow(AwsServiceException.builder().build());

        final Map<String, String> resourceTags = new HashMap<String, String>();
        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").resourceIdentifier("test")
                .typeName("test").tags(resourceTags).build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        assertThatExceptionOfType(CfnGeneralServiceException.class).isThrownBy(() -> {
            handler.handleRequest(proxy, request, new CallbackContext(), proxySsmClient, proxyCloudControlClient,
                    LOGGER);
        });
    }
}
