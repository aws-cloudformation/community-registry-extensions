package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import io.burt.jmespath.Expression;
import io.burt.jmespath.JmesPath;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class LookupHelperTest {

    @Test
    public void generateResourceLookupIdMatchesExpectedPattern() {
        final Pattern pattern = Pattern
                .compile(Constants.PRIMARY_IDENTIFIER_PREFIX + "-[a-z0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}");
        final String response = LookupHelper.generateResourceLookupId();
        final Matcher matcher = pattern.matcher(response);

        assertThat(response).startsWith(Constants.PRIMARY_IDENTIFIER_PREFIX);
        assertTrue(matcher.find());
    }

    @Test
    public void escapeNoCommaDelimiters() {
        final String input = "test";
        final String output = LookupHelper.escapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test");
    }

    @Test
    public void escapeTwoCommaDelimiters() {
        final String input = "test,test,test";
        final String output = LookupHelper.escapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test\\,test\\,test");
    }

    @Test
    public void escapeTwoCommaDelimitersAndTrailingComma() {
        final String input = "test,test,test,";
        final String output = LookupHelper.escapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test\\,test\\,test\\,");
    }

    @Test
    public void unescapeNoCommaDelimiters() {
        final String input = "test";
        final String output = LookupHelper.unescapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test");
    }

    @Test
    public void unescapeTwoCommaDelimiters() {
        final String input = "test\\,test\\,test";
        final String output = LookupHelper.unescapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test,test,test");
    }

    @Test
    public void unescapeTwoCommaDelimitersAndTrailingComma() {
        final String input = "test\\,test\\,test\\,";
        final String output = LookupHelper.unescapeCommaDelimiters(input);

        assertThat(output).isEqualTo("test,test,test,");
    }

    @Test
    public void splitWithNoCommaDelimiters() {
        final String input = "test";
        final String[] output = LookupHelper.splitStringWithUnescapedCommaDelimiters(input);

        assertThat(output[0]).isEqualTo("test");
    }

    @Test
    public void splitWithUnescapedCommaDelimiters() {
        final String input = "test1,test2,test3";
        final String[] output = LookupHelper.splitStringWithUnescapedCommaDelimiters(input);

        assertThat(output[0]).isEqualTo("test1");
        assertThat(output[1]).isEqualTo("test2");
        assertThat(output[2]).isEqualTo("test3");
    }

    @Test
    public void splitWithUnescapedAndEscapedCommaDelimiters() {
        final String input = "test1,test2\\,test3,test4\\,test5";
        final String[] output = LookupHelper.splitStringWithUnescapedCommaDelimiters(input);

        assertThat(output[0]).isEqualTo("test1");
        assertThat(output[1]).isEqualTo("test2\\,test3");
        assertThat(output[2]).isEqualTo("test4\\,test5");
    }

    @Test
    public void splitWithUnescapedAndAdjacentEscapedCommaDelimiters() {
        final String input = "test1,test2\\,\\,test3,test4\\,\\,test5";
        final String[] output = LookupHelper.splitStringWithUnescapedCommaDelimiters(input);

        assertThat(output[0]).isEqualTo("test1");
        assertThat(output[1]).isEqualTo("test2\\,\\,test3");
        assertThat(output[2]).isEqualTo("test4\\,\\,test5");
    }

    @Test
    public void splitWithUnescapedAndNonAdjacentEscapedCommaDelimiters() {
        final String input = "test1,test\\,2\\,test3,test\\,4\\,test5";
        final String[] output = LookupHelper.splitStringWithUnescapedCommaDelimiters(input);

        assertThat(output[0]).isEqualTo("test1");
        assertThat(output[1]).isEqualTo("test\\,2\\,test3");
        assertThat(output[2]).isEqualTo("test\\,4\\,test5");
    }

    @Test
    public void isIdentifiersBufferNullOrEmptyBufferNull() {
        final List<String> input = null;

        final boolean response = LookupHelper.isIdentifiersBufferNullOrEmpty(input);

        assertTrue(response);
    }

    @Test
    public void isIdentifiersBufferNullOrEmptyBufferEmpty() {
        final List<String> input = new ArrayList<String>();

        final boolean response = LookupHelper.isIdentifiersBufferNullOrEmpty(input);

        assertTrue(response);
    }

    @Test
    public void isIdentifiersBufferNullOrEmptyBufferNotEmpty() {
        final List<String> input = new ArrayList<String>();
        input.add("test");

        final boolean response = LookupHelper.isIdentifiersBufferNullOrEmpty(input);

        assertFalse(response);
    }

    @Test
    public void isIdentifiersBufferNotEmptyBufferNull() {
        final List<String> input = null;

        final boolean response = LookupHelper.isIdentifiersBufferNotEmpty(input);

        assertFalse(response);
    }

    @Test
    public void isIdentifiersBufferNotEmptyBufferEmpty() {
        final List<String> input = new ArrayList<String>();

        final boolean response = LookupHelper.isIdentifiersBufferNotEmpty(input);

        assertFalse(response);
    }

    @Test
    public void isIdentifiersBufferNotEmptyBufferNotEmpty() {
        final List<String> input = new ArrayList<String>();
        input.add("test");

        final boolean response = LookupHelper.isIdentifiersBufferNotEmpty(input);

        assertTrue(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenNullAndBufferNull() {
        final String nextToken = null;
        final List<String> buffer = null;

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenEmptyAndBufferNull() {
        final String nextToken = "";
        final List<String> buffer = null;

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenEmptyAndBufferEmpty() {
        final String nextToken = "";
        final List<String> buffer = new ArrayList<String>();

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenNotEmptyAndBufferEmpty() {
        final String nextToken = "test";
        final List<String> buffer = new ArrayList<String>();

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertTrue(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenNotEmptyAndBufferNull() {
        final String nextToken = "test";
        final List<String> buffer = null;

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertTrue(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenNullAndBufferNotEmpty() {
        final String nextToken = null;
        final List<String> buffer = new ArrayList<String>();
        buffer.add("test");

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenEmptyAndBufferNotEmpty() {
        final String nextToken = "";
        final List<String> buffer = new ArrayList<String>();
        buffer.add("test");

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void isNextTokenNotEmptyAndIdentifiersBufferNullOrEmptyNextTokenNotEmptyAndBufferNotEmpty() {
        final String nextToken = "test";
        final List<String> buffer = new ArrayList<String>();
        buffer.add("test");

        final boolean response = LookupHelper.isNextTokenNotEmptyAndIdentifiersBufferNullOrEmpty(nextToken, buffer);

        assertFalse(response);
    }

    @Test
    public void jmesPathQueryMatchesResultNull() throws JsonMappingException, JsonProcessingException {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final String jmesPathQuery = "Tags[200]";

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        final boolean response = LookupHelper.jmesPathQueryMatches(resourceProperties, expression);

        assertFalse(response);
    }

    @Test
    public void jmesPathQueryMatchesResultFalse() throws JsonMappingException, JsonProcessingException {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final String jmesPathQuery = "InstanceTenancy == 'invalid'";

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        final boolean response = LookupHelper.jmesPathQueryMatches(resourceProperties, expression);

        assertFalse(response);
    }

    @Test
    public void jmesPathQueryMatchesResultTrue() throws JsonMappingException, JsonProcessingException {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final String jmesPathQuery = "InstanceTenancy == 'default'";

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        final boolean response = LookupHelper.jmesPathQueryMatches(resourceProperties, expression);

        assertTrue(response);
    }

    @Test
    public void jmesPathQueryMatchesResultEmpty() throws JsonMappingException, JsonProcessingException {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final String jmesPathQuery = "Tags[?Key == 'invalid' && Value == 'invalid']";

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        final boolean response = LookupHelper.jmesPathQueryMatches(resourceProperties, expression);

        assertFalse(response);
    }

    @Test
    public void jmesPathQueryMatchesResultNotEmpty() throws JsonMappingException, JsonProcessingException {
        final String resourceProperties = Mocks.getResourcePropertiesMock();

        final String jmesPathQuery = "Tags";

        final JmesPath<JsonNode> jmespath = LookupHelper.getJacksonRuntimeForJmesPath();
        final Expression<JsonNode> expression = jmespath.compile(jmesPathQuery);

        final boolean response = LookupHelper.jmesPathQueryMatches(resourceProperties, expression);

        assertTrue(response);
    }
}
