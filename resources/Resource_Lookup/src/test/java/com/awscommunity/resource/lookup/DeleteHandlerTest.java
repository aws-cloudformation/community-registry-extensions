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
import software.amazon.awssdk.services.ssm.model.DeleteParameterRequest;
import software.amazon.awssdk.services.ssm.model.DeleteParameterResponse;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.cloudformation.exceptions.CfnGeneralServiceException;
import software.amazon.cloudformation.exceptions.CfnNotFoundException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

@ExtendWith(MockitoExtension.class)
public class DeleteHandlerTest extends AbstractTestBase {

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
    private DeleteHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        proxyCloudControlClient = mockProxy(proxy, cloudControlClient);
        handler = spy(new DeleteHandler());
    }

    @AfterEach
    public void tearDown() {
        verify(ssmClient, atLeastOnce()).serviceName();
        verifyNoMoreInteractions(ssmClient);
    }

    @Test
    public void handleRequestSuccess() {
        final DeleteParameterResponse deleteParameterResponse = DeleteParameterResponse.builder().build();
        when(ssmClient.deleteParameter(any(DeleteParameterRequest.class))).thenReturn(deleteParameterResponse);

        final ResourceModel model = ResourceModel.builder().build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                new CallbackContext(), proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isNull();
        assertThat(response.getResourceModels()).isNull();
    }

    @Test
    public void parameterNotFoundExceptionThrown() {
        when(ssmClient.deleteParameter(any(DeleteParameterRequest.class)))
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
        when(ssmClient.deleteParameter(any(DeleteParameterRequest.class)))
                .thenThrow(AwsServiceException.builder().build());

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
