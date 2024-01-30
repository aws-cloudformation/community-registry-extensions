package com.awscommunity.config.proactiveeval;

/**
 * Handle the configuration.
 */
class Configuration extends BaseHookConfiguration {

  /**
   * Initialize with the hook schema configuration file.
   */
  public Configuration() {
    super("awscommunity-config-proactiveeval.json");
  }
}
