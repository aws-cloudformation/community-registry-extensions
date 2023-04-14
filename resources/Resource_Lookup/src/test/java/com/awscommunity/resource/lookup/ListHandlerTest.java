package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.verifyNoMoreInteractions;
import static org.mockito.Mockito.when;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.DescribeParametersRequest;
import software.amazon.awssdk.services.ssm.model.DescribeParametersResponse;
import software.amazon.awssdk.services.ssm.model.ParameterMetadata;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.ResourceHandlerRequest;

@ExtendWith(MockitoExtension.class)
public class ListHandlerTest extends AbstractTestBase {

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
    private ListHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        proxyCloudControlClient = mockProxy(proxy, cloudControlClient);
        handler = spy(new ListHandler());
    }

    @AfterEach
    public void tearDown() {
        verifyNoMoreInteractions(ssmClient);
    }

    @Test
    public void handleRequestSuccess() {
        final List<ParameterMetadata> parametersMetadata = new ArrayList<ParameterMetadata>();
        final ParameterMetadata parameterMetadata = ParameterMetadata.builder().type(ParameterType.STRING_LIST)
                .name("test").build();
        parametersMetadata.add(parameterMetadata);

        final DescribeParametersResponse describeParametersResponse = DescribeParametersResponse.builder()
                .parameters(parametersMetadata).build();
        when(ssmClient.describeParameters(any(DescribeParametersRequest.class))).thenReturn(describeParametersResponse);

        final ResourceModel model = ResourceModel.builder().build();

        final ResourceHandlerRequest<ResourceModel> request = ResourceHandlerRequest.<ResourceModel>builder()
                .desiredResourceState(model).build();

        final ProgressEvent<ResourceModel, CallbackContext> response = handler.handleRequest(proxy, request,
                new CallbackContext(), proxySsmClient, proxyCloudControlClient, LOGGER);

        assertThat(response).isNotNull();
        assertThat(response.getMessage()).isNull();
        assertThat(response.getErrorCode()).isNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getResourceModel()).isNull();
        assertThat(response.getResourceModels()).isNotNull();
    }
}
