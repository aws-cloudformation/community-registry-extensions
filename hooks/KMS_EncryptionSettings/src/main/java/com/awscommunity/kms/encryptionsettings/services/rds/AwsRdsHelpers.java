package com.awscommunity.kms.encryptionsettings.services.rds;

/**
 * Validation helpers for KMS-related properties of Amazon RDS resource type
 * properties specified by the user.
 */
public final class AwsRdsHelpers {

    private AwsRdsHelpers() {
    }

    /**
     * Whether or not the RDS engine is Aurora.
     *
     * @param engine
     *            A {@link String} object.
     * @return Boolean A {@link Boolean} object set to `true` if the RDS engine is
     *         Aurora, or set to `false` otherwise.
     */
    public static Boolean isAuroraEngine(final String engine) {
        if (engine == null) {
            return false;
        }
        return engine.startsWith("aurora");
    }
}
