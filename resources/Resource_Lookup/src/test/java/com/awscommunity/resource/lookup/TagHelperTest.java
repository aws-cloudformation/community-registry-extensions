package com.awscommunity.resource.lookup;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.awssdk.services.ssm.model.Tag;

@ExtendWith(MockitoExtension.class)
public class TagHelperTest {

    @Test
    public void getCombineTagsStackLevelAndResourceLevelBothNull() {
        final Map<String, String> requestTags = null;

        final Map<String, String> resourceTags = null;

        final Map<String, String> response = TagHelper.combineTags(requestTags, resourceTags);

        assertThat(response).isEmpty();
    }

    @Test
    public void getCombineTagsStackLevelAndResourceLevelBothNotPresent() {
        final Map<String, String> requestTags = new HashMap<String, String>();

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final Map<String, String> response = TagHelper.combineTags(requestTags, resourceTags);

        assertThat(response).isEmpty();
    }

    @Test
    public void getCombineTagsStackLevelAndResourceLevelBothPresent() {
        final Map<String, String> requestTags = new HashMap<String, String>();
        requestTags.put("t1", "v1");

        final Map<String, String> resourceTags = new HashMap<String, String>();
        resourceTags.put("tA", "vA");

        final Map<String, String> response = TagHelper.combineTags(requestTags, resourceTags);

        assertThat(response.size()).isEqualTo(2);
        assertTrue(response.containsKey("t1"));
        assertTrue(response.containsValue("v1"));
        assertTrue(response.containsKey("tA"));
        assertTrue(response.containsValue("vA"));
    }

    @Test
    public void getCombineTagsStackLevelOnly() {
        final Map<String, String> requestTags = new HashMap<String, String>();
        requestTags.put("t1", "v1");

        final Map<String, String> resourceTags = new HashMap<String, String>();

        final Map<String, String> response = TagHelper.combineTags(requestTags, resourceTags);

        assertThat(response.size()).isEqualTo(1);
        assertTrue(response.containsKey("t1"));
        assertTrue(response.containsValue("v1"));
    }

    @Test
    public void getCombineTagsResourceLevelOnly() {
        final Map<String, String> requestTags = new HashMap<String, String>();

        final Map<String, String> resourceTags = new HashMap<String, String>();
        resourceTags.put("tA", "vA");

        final Map<String, String> response = TagHelper.combineTags(requestTags, resourceTags);

        assertThat(response.size()).isEqualTo(1);
        assertTrue(response.containsKey("tA"));
        assertTrue(response.containsValue("vA"));
    }

    @Test
    public void convertToListInputEmpty() {
        final Map<String, String> input = new HashMap<String, String>();

        final List<Tag> response = TagHelper.convertToList(input);

        assertTrue(response.isEmpty());
    }

    @Test
    public void convertToListInputNotEmpty() {
        final Map<String, String> input = new HashMap<String, String>();
        input.put("t1", "v1");

        final List<Tag> response = TagHelper.convertToList(input);

        assertThat(response.size()).isEqualTo(1);
        assertThat(response.get(0).key()).isEqualTo("t1");
        assertThat(response.get(0).value()).isEqualTo("v1");
    }

    @Test
    public void convertToListInputMapValueNull() {
        final Map<String, String> input = new HashMap<String, String>();
        input.put("t1", null);

        final List<Tag> response = TagHelper.convertToList(input);

        assertThat(response.size()).isEqualTo(0);
    }

    @Test
    public void convertToMapInputEmpty() {
        final List<Tag> input = new ArrayList<Tag>();

        final Map<String, String> response = TagHelper.convertToMap(input);

        assertTrue(response.isEmpty());
    }

    @Test
    public void convertToMapInputNotEmpty() {
        final List<Tag> input = new ArrayList<Tag>();
        input.add(Tag.builder().key("t1").value("v1").build());

        final Map<String, String> response = TagHelper.convertToMap(input);

        assertThat(response.size()).isEqualTo(1);
        assertTrue(response.containsKey("t1"));
        assertTrue(response.containsValue("v1"));
    }

    @Test
    public void convertToMapInputListValueNull() {
        final List<Tag> input = new ArrayList<Tag>();
        input.add(Tag.builder().key("t1").value(null).build());

        final Map<String, String> response = TagHelper.convertToMap(input);

        assertThat(response.size()).isEqualTo(0);
    }

    @Test
    public void generateTagsToAddRemovePreviousTagAndAddNewTag() {
        final Map<String, String> previousTags = new HashMap<String, String>();
        previousTags.put("t1", "v1");

        final Map<String, String> tags = new HashMap<String, String>();
        tags.put("t2", "v2");

        final Map<String, String> response = TagHelper.generateTagsToAdd(previousTags, tags);

        assertThat(response.size()).isEqualTo(1);
        assertFalse(response.containsKey("t1"));
        assertFalse(response.containsValue("v1"));
        assertTrue(response.containsKey("t2"));
        assertTrue(response.containsValue("v2"));
    }

    @Test
    public void generateTagsToAddPreserveOnePreviousTagAndAddAnotherTag() {
        final Map<String, String> previousTags = new HashMap<String, String>();
        previousTags.put("t1", "v1");

        final Map<String, String> tags = new HashMap<String, String>();
        tags.put("t1", "v1");
        tags.put("t2", "v2");

        final Map<String, String> response = TagHelper.generateTagsToAdd(previousTags, tags);

        assertThat(response.size()).isEqualTo(1);
        assertFalse(response.containsKey("t1"));
        assertFalse(response.containsValue("v1"));
        assertTrue(response.containsKey("t2"));
        assertTrue(response.containsValue("v2"));
    }

    @Test
    public void generateTagsToRemoveAddNewTagAndRemovePreviousTag() {
        final Map<String, String> previousTags = new HashMap<String, String>();
        previousTags.put("t1", "v1");

        final Map<String, String> tags = new HashMap<String, String>();
        tags.put("t2", "v2");

        final Map<String, String> response = TagHelper.generateTagsToRemove(previousTags, tags);

        assertThat(response.size()).isEqualTo(1);
        assertFalse(response.containsKey("t2"));
        assertFalse(response.containsValue("v2"));
        assertTrue(response.containsKey("t1"));
        assertTrue(response.containsValue("v1"));
    }

    @Test
    public void generateTagsToRemovePreserveOnePreviousTagAndRemoveAnotherTag() {
        final Map<String, String> previousTags = new HashMap<String, String>();
        previousTags.put("t1", "v1");
        previousTags.put("t2", "v2");

        final Map<String, String> tags = new HashMap<String, String>();
        tags.put("t2", "v2");

        final Map<String, String> response = TagHelper.generateTagsToRemove(previousTags, tags);

        assertThat(response.size()).isEqualTo(1);
        assertFalse(response.containsKey("t2"));
        assertFalse(response.containsValue("v2"));
        assertTrue(response.containsKey("t1"));
        assertTrue(response.containsValue("v1"));
    }

    @Test
    public void getTagKeysFromMapOfStrings() {
        final Map<String, String> input = new HashMap<String, String>();
        input.put("t1", "v1");
        input.put("t2", "v2");

        final List<String> response = TagHelper.getTagKeysFromMapOfStrings(input);

        assertThat(response.size()).isEqualTo(2);
        assertThat(response.get(0)).isEqualTo("t1");
        assertThat(response.get(1)).isEqualTo("t2");
    }
}
