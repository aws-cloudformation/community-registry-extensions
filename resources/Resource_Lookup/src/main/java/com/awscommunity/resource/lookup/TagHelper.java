package com.awscommunity.resource.lookup;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;
import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.collections.MapUtils;
import software.amazon.awssdk.services.ssm.model.Tag;

/**
 * Centralized placeholder for tag-related utilities.
 */
public final class TagHelper {

    private TagHelper() {
    }

    /**
     * Combines tags from the request (stack-level), and from the model
     * (resource-level).
     *
     * @param requestTags
     *            {@link Map} of {@link String}
     * @param resourceTags
     *            {@link Map} of {@link String}
     * @return Map {@link Map} of {@link String}
     */
    public static Map<String, String> combineTags(final Map<String, String> requestTags,
            final Map<String, String> resourceTags) {
        final Map<String, String> combinedTags = new HashMap<String, String>();

        if (requestTags != null && !requestTags.isEmpty()) {
            combinedTags.putAll(requestTags);
        }

        if (resourceTags != null && !resourceTags.isEmpty()) {
            combinedTags.putAll(resourceTags);
        }

        return combinedTags;
    }

    /**
     * Converts a map of strings for tag key/value pairs to a list of tag objects.
     *
     * @param tagMap
     *            {@link Map} of {@link String}
     * @return List {@link List} of {@link Tag}
     */
    public static List<Tag> convertToList(final Map<String, String> tagMap) {
        if (MapUtils.isEmpty(tagMap)) {
            return Collections.emptyList();
        }

        return tagMap.entrySet().stream().filter(tag -> tag.getValue() != null)
                .map(tag -> Tag.builder().key(tag.getKey()).value(tag.getValue()).build()).collect(Collectors.toList());
    }

    /**
     * Converts a list of tag objects to a map of strings for tag key/value pairs.
     *
     * @param tagList
     *            {@link List} of {@link Tag}
     * @return Map {@link Map} of {@link String}
     */
    public static Map<String, String> convertToMap(final Collection<Tag> tagList) {
        if (CollectionUtils.isEmpty(tagList)) {
            return Collections.emptyMap();
        }

        return tagList.stream().filter(tag -> tag.value() != null).collect(Collectors.toMap(Tag::key, Tag::value));
    }

    /**
     * Returns a map of tags to add, by comparing previous and new tags.
     *
     * @param previousTags
     *            {@link Map} of {@link String}
     * @param tags
     *            {@link Map} of {@link String}
     * @return Map {@link Map} of {@link String}
     */
    public static Map<String, String> generateTagsToAdd(final Map<String, String> previousTags,
            final Map<String, String> tags) {
        return tags.entrySet().stream().filter(tag -> !Objects.equals(previousTags.get(tag.getKey()), tag.getValue()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    /**
     * Returns a map of tags to remove, by comparing previous and new tags.
     *
     * @param previousTags
     *            {@link Map} of {@link String}
     * @param tags
     *            {@link Map} of {@link String}
     * @return Map {@link Map} of {@link String}
     */
    public static Map<String, String> generateTagsToRemove(final Map<String, String> previousTags,
            final Map<String, String> tags) {
        return previousTags.entrySet().stream().filter(tag -> !Objects.equals(tags.get(tag.getKey()), tag.getValue()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    /**
     * Returns a list of tag keys from a map of given tags.
     *
     * @param tags
     *            {@link Map} of {@link String}
     * @return List {@link List} of {@link String}
     */
    public static List<String> getTagKeysFromMapOfStrings(final Map<String, String> tags) {
        final List<Tag> tagList = convertToList(tags);
        return tagList.stream().map(tag -> tag.key()).collect(Collectors.toList());
    }
}
