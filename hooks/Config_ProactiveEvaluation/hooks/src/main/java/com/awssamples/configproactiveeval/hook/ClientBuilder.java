package com.awssamples.configproactiveeval.hook;

import software.amazon.awssdk.services.config.ConfigClient;
import software.amazon.cloudformation.HookLambdaWrapper;

/**
 * Build AWS Service Clients.
 */
public class ClientBuilder {

  /**
   * Create a static HTTP client for AWS Config.
   *
   * @return ConfigClient
   */
  public static ConfigClient getConfigClient() {
    return ConfigClient.builder()
        .httpClient(HookLambdaWrapper.HTTP_CLIENT)
        .build();
  }

}
