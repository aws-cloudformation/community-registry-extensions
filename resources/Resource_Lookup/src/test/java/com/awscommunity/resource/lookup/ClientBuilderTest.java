package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.ssm.SsmClient;

@ExtendWith(MockitoExtension.class)
public class ClientBuilderTest {

    @Test
    public void getCloudControlClientSuccess() {
        final CloudControlClient cloudControlClient = ClientBuilder.getCloudControlClient();

        assertTrue(cloudControlClient.serviceClientConfiguration().overrideConfiguration().retryPolicy().isPresent());
        assertThat(cloudControlClient.serviceClientConfiguration().overrideConfiguration().retryPolicy().get()
                .numRetries()).isEqualTo(Constants.CLOUDCONTROL_CLIENT_NUM_RETRIES);
    }

    @Test
    public void getSsmClientSuccess() {
        final SsmClient ssmClient = ClientBuilder.getSsmClient();

        assertTrue(ssmClient.serviceClientConfiguration().overrideConfiguration().retryPolicy().isPresent());
        assertThat(ssmClient.serviceClientConfiguration().overrideConfiguration().retryPolicy().get().numRetries())
                .isEqualTo(Constants.SSM_CLIENT_NUM_RETRIES);
    }
}
