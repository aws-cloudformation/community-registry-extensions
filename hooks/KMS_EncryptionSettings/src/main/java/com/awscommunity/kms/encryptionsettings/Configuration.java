package com.awscommunity.kms.encryptionsettings;

/**
 * Sets up this hook.
 */
class Configuration extends BaseHookConfiguration {

    /**
     * Set up the schema file for this hook.
     */
    Configuration() {
        super("awscommunity-kms-encryptionsettings.json");
    }
}
