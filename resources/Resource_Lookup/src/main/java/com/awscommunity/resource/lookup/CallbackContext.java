package com.awscommunity.resource.lookup;

import java.util.List;
import software.amazon.cloudformation.proxy.StdCallbackContext;

/**
 * Callback context POJO.
 */
@lombok.Getter
@lombok.Setter
@lombok.ToString
@lombok.EqualsAndHashCode(callSuper = true)
public class CallbackContext extends StdCallbackContext {

    /**
     * Defines a field for the primary identifier.
     */
    private String resourceLookupId;

    /**
     * Defines a nextToken string field for the
     * {@link software.amazon.awssdk.services.cloudcontrol.model.ListResourcesRequest}.
     */
    private String listResourcesNextToken;

    /**
     * Defines a {@link List} of {@link String} objects representing a buffer with
     * identifiers of resources to be searched for matches.
     */
    private List<String> identifiersBuffer;
}
