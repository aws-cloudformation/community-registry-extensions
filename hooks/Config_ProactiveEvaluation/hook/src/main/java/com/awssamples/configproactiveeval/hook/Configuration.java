package com.awssamples.configproactiveeval.hook;

/**
 * Handle the configuration.
 */
class Configuration extends BaseHookConfiguration {

  /**
   * Initialize with the hook schema configuration file.
   */
  public Configuration() {
    super("awssamples-configproactiveeval-hook.json");
  }
}
