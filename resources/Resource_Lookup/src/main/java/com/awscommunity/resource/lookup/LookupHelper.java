package com.awscommunity.resource.lookup;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.burt.jmespath.Expression;
import io.burt.jmespath.JmesPath;
import io.burt.jmespath.RuntimeConfiguration;
import io.burt.jmespath.jackson.JacksonRuntime;
import java.util.List;
import java.util.UUID;

/**
 * Centralized placeholder for lookup-related utilities.
 */
public final class LookupHelper {

    private LookupHelper() {
    }

    /**
     * Generates a primary identifier with a UUID of type 4 value as a suffix.
     *
     * @return string {@link String}
     */
    public static String generateResourceLookupId() {
        // Set a UUID of type 4 value as a suffix.
        return Constants.PRIMARY_IDENTIFIER_PREFIX + "-" + UUID.randomUUID();
    }

    /**
     * Determines whether the Identifiers Buffer is null or empty.
     *
     * @param identifiersBuffer
     *            {@link List} of {@link String}
     * @return boolean `true` if the Identifiers Buffer is null or empty
     */
    public static boolean isIdentifiersBufferNullOrEmpty(final List<String> identifiersBuffer) {
        return identifiersBuffer == null || identifiersBuffer.isEmpty();
    }

    /**
     * Determines whether the Identifiers Buffer is not empty.
     *
     * @param identifiersBuffer
     *            {@link List} of {@link String}
     * @return boolean `true` if the Identifiers Buffer is not empty
     */
    public static boolean isIdentifiersBufferNotEmpty(final List<String> identifiersBuffer) {
        return identifiersBuffer != null && !identifiersBuffer.isEmpty();
    }

    /**
     * Determines whether NextToken is not empty, and IdentifiersBuffer is null or
     * empty.
     *
     * @param nextToken
     *            {@link String}
     * @param identifiersBuffer
     *            {@link List} of {@link String}
     * @return boolean `true` if NextToken is not empty, and IdentifiersBuffer is
     *         null or empty.
     */
    public static boolean isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(final String nextToken,
            final List<String> identifiersBuffer) {
        return nextToken != null && !nextToken.isEmpty() && (identifiersBuffer == null || identifiersBuffer.isEmpty());
    }

    /**
     * Sets up a {@link RuntimeConfiguration} for the {@link JmesPath} runtime, and
     * returns it.
     *
     * @return JmesPath {@link JmesPath} runtime
     */
    public static JmesPath<JsonNode> getJacksonRuntimeForJmesPath() {
        final boolean silentTypeErrors = true;

        return new JacksonRuntime(new RuntimeConfiguration.Builder().withSilentTypeErrors(silentTypeErrors).build());
    }

    /**
     * Searches resource properties using an input JMESPath query, and returns a
     * boolean value on whether a match is found or not.
     *
     * @param resourcePropertiesString
     *            {@link String}
     * @param expression
     *            {@link JsonNode} {@link Expression}
     * @return boolean `true` if the JMESPath query matches
     * @throws JsonProcessingException
     *             JsonProcessingException
     */
    public static boolean jmesPathQueryMatches(final String resourcePropertiesString,
            final Expression<JsonNode> expression) throws JsonProcessingException {
        final ObjectMapper objectMapper = new ObjectMapper();

        final JsonNode resourcePropertiesJsonNode = objectMapper.readTree(resourcePropertiesString);

        final JsonNode result = expression.search(resourcePropertiesJsonNode);

        return result.asBoolean() || !result.isEmpty();
    }
}
