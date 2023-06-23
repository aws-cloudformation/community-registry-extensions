package com.awscommunity.resource.lookup;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
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
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.GetParameterRequest;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.Parameter;
import software.amazon.awssdk.services.ssm.model.ParameterNotFoundException;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.ProxyClient;

@ExtendWith(MockitoExtension.class)
public class CreateHandlerStabilizeTest extends AbstractTestBase {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private ProxyClient<SsmClient> proxySsmClient;

    @Mock
    private SsmClient ssmClient;

    @Mock
    private CreateHandler handler;

    @BeforeEach
    public void setup() {
        proxy = new AmazonWebServicesClientProxy(LOGGER, MOCK_CREDENTIALS, () -> Duration.ofSeconds(600).toMillis());
        ssmClient = mock(SsmClient.class);
        proxySsmClient = mockProxy(proxy, ssmClient);
        handler = spy(new CreateHandler());
    }

    @AfterEach
    public void tearDown() {
    }

    @Test
    public void isStabilizedExceptionThrown() {
        when(ssmClient.getParameter(any(GetParameterRequest.class)))
                .thenThrow(ParameterNotFoundException.builder().build());

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertFalse(response);
    }

    @Test
    public void isStabilizedNullResponse() {
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(null);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertFalse(response);
    }

    @Test
    public void isStabilizedNullParameter() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder().build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertFalse(response);
    }

    @Test
    public void isStabilizedNullParameterName() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder()
                .parameter(Parameter.builder().build()).build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertFalse(response);
    }

    @Test
    public void isNotStabilized() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder().parameter(
                Parameter.builder().type(ParameterType.STRING_LIST).name("test1").value("test,test,test").build())
                .build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertFalse(response);
    }

    @Test
    public void isStabilized() {
        final GetParameterResponse getParameterResponse = GetParameterResponse.builder().parameter(
                Parameter.builder().type(ParameterType.STRING_LIST).name("test").value("test,test,test").build())
                .build();
        when(ssmClient.getParameter(any(GetParameterRequest.class))).thenReturn(getParameterResponse);

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final String jmesPathQuery = "Tags[?Key=='Owner'&&Value=='contract-test-only-test-team']";

        final ResourceModel model = ResourceModel.builder().resourceLookupId("test").typeName("test")
                .jmesPathQuery(jmesPathQuery).resourceLookupRoleArn("test").tags(resourceTags).build();

        final boolean response = handler.isStabilized(model, proxySsmClient, LOGGER);

        assertTrue(response);
    }
}
