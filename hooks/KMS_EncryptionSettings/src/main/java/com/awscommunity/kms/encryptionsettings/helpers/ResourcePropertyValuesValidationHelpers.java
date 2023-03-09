package com.awscommunity.kms.encryptionsettings.helpers;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Resource property validation helpers.
 */
public final class ResourcePropertyValuesValidationHelpers {

    private ResourcePropertyValuesValidationHelpers() {
    }

    /**
     * Validates if an input string is null or empty.
     *
     * @param <T>
     *            A given type.
     * @param input
     *            An input to validate; this method checks if the input is null, and
     *            for empty values for {@link String}, {@link String}, {@link Set}
     *            objects.
     *
     * @return Boolean Return a {@link Boolean} `true` if the input string is null
     *         or empty, `false` otherwise.
     */
    public static <T> Boolean isNullOrEmpty(final T input) {
        if (input == null) {
            return true;
        } else if (input instanceof String) {
            if (input.toString().isEmpty()) {
                return true;
            }
        } else if (input instanceof List) {
            final List<?> objectToList = ((List<?>) input);
            if (objectToList.isEmpty()) {
                return true;
            }
        } else if (input instanceof Set) {
            final Set<?> objectToSet = ((Set<?>) input);
            if (objectToSet.isEmpty()) {
                return true;
            }
        }
        return false;
    }

    /**
     * Matches an input string against {@link AwsKmsKeyIdPropertyRegexPatterns}.
     *
     * @param inputString
     *            A user-provided input {@link String}.
     * @param ignoreKeyIdPattern
     *            A {@link Boolean} value for ignoring a relevant validation regex.
     * @param ignoreKeyAliasPattern
     *            A {@link Boolean} value for ignoring a relevant validation regex.
     * @param ignoreKeyArnPattern
     *            A {@link Boolean} value for ignoring a relevant validation regex.
     * @param ignoreAliasArnPattern
     *            A {@link Boolean} value for ignoring a relevant validation regex.
     * @return Boolean Whether the user-provided input matches or not against any of
     *         the {@link AwsKmsKeyIdPropertyRegexPatterns}.
     */
    public static Boolean awsKmsKeyIdRegexMatches(final String inputString, final Boolean ignoreKeyIdPattern,
            final Boolean ignoreKeyAliasPattern, final Boolean ignoreKeyArnPattern,
            final Boolean ignoreAliasArnPattern) {
        final List<String> regexPatternsToUse = new ArrayList<String>();

        if (!ignoreKeyIdPattern) {
            regexPatternsToUse.add(AwsKmsKeyIdPropertyRegexPatterns.KEY_ID.name());
        }

        if (!ignoreKeyAliasPattern) {
            regexPatternsToUse.add(AwsKmsKeyIdPropertyRegexPatterns.KEY_ALIAS.name());
        }

        if (!ignoreKeyArnPattern) {
            regexPatternsToUse.add(AwsKmsKeyIdPropertyRegexPatterns.KEY_ARN.name());
        }

        if (!ignoreAliasArnPattern) {
            regexPatternsToUse.add(AwsKmsKeyIdPropertyRegexPatterns.ALIAS_ARN.name());
        }

        String regexPattern = null;
        for (final AwsKmsKeyIdPropertyRegexPatterns awsKmsKeyIdPropertyRegexPattern : AwsKmsKeyIdPropertyRegexPatterns
                .values()) {
            final String regexName = awsKmsKeyIdPropertyRegexPattern.name();
            if (regexPatternsToUse.contains(regexName)) {
                regexPattern = awsKmsKeyIdPropertyRegexPattern.getRegexPattern();
                final Pattern pattern = Pattern.compile(regexPattern);
                final Matcher matcher = pattern.matcher(inputString);
                if (matcher.find()) {
                    return true;
                }
            }
        }
        return false;
    }
}
