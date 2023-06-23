package com.awscommunity.resource.lookup;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import software.amazon.awssdk.services.cloudcontrol.CloudControlClient;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceRequest;
import software.amazon.awssdk.services.cloudcontrol.model.GetResourceResponse;
import software.amazon.awssdk.services.cloudcontrol.model.ListResourcesRequest;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.AddTagsToResourceRequest;
import software.amazon.awssdk.services.ssm.model.DeleteParameterRequest;
import software.amazon.awssdk.services.ssm.model.DescribeParametersRequest;
import software.amazon.awssdk.services.ssm.model.DescribeParametersResponse;
import software.amazon.awssdk.services.ssm.model.GetParameterRequest;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.ssm.model.ListTagsForResourceResponse;
import software.amazon.awssdk.services.ssm.model.ParameterStringFilter;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.awssdk.services.ssm.model.PutParameterRequest;
import software.amazon.awssdk.services.ssm.model.RemoveTagsFromResourceRequest;
import software.amazon.awssdk.services.ssm.model.ResourceTypeForTagging;
import software.amazon.cloudformation.proxy.ProxyClient;

/**
 * Centralized placeholder for API requests construction, for object
 * translations to/from the AWS SDK, and for resource model construction for
 * read/list handlers.
 */
public final class Translator {

    private Translator() {
    }

    /**
     * Translates to a {@link ListResourcesRequest}.
     *
     * @param typeName
     *            {@link String}
     * @param resourceLookupRoleArn
     *            {@link String}
     * @param resourceModel
     *            {@link String}
     * @param nextToken
     *            {@link String}
     * @return ListResourcesRequest {@link ListResourcesRequest}
     */
    public static ListResourcesRequest translateToListResourcesRequest(final String typeName,
            final String resourceLookupRoleArn, final String resourceModel, final String nextToken) {
        final ListResourcesRequest listResourcesRequest = ListResourcesRequest.builder().typeName(typeName)
                .roleArn(resourceLookupRoleArn).resourceModel(resourceModel).nextToken(nextToken).build();
        return listResourcesRequest;
    }

    /**
     * Translates to a {@link GetResourceRequest}.
     *
     * @param typeName
     *            {@link String}
     * @param resourceLookupRoleArn
     *            {@link String}
     * @param identifier
     *            {@link String}
     * @return GetResourceRequest {@link GetResourceRequest}
     */
    public static GetResourceRequest translateToGetResourceRequest(final String typeName,
            final String resourceLookupRoleArn, final String identifier) {
        final GetResourceRequest getResourceRequest = GetResourceRequest.builder().typeName(typeName)
                .roleArn(resourceLookupRoleArn).identifier(identifier).build();
        return getResourceRequest;
    }

    /**
     * Translates to a {@link PutParameterRequest}.
     *
     * @param model
     *            {@link ResourceModel}
     * @param tags
     *            {@link Map} of {@link String}
     * @return PutParameterRequest {@link PutParameterRequest}
     */
    public static PutParameterRequest translateToPutParameterRequest(final ResourceModel model,
            final Map<String, String> tags) {
        final String parameterName = model.getResourceLookupId();
        final String typeName = model.getTypeName();

        // Before storing typeName and resourceIdentifier as a
        // Parameter Store parameter value delimited by a comma,
        // escape comma(s) that might be present in
        // resourceIdentifier; an example is the resource identifier
        // for `AWS::IAM::Role`, whereas a comma is allowed in the
        // role name. The same applies to the resource role ARN.
        final String resourceIdentifier = LookupHelper.escapeCommaDelimiters(model.getResourceIdentifier());
        final String resourceLookupRoleArn = LookupHelper.escapeCommaDelimiters(model.getResourceLookupRoleArn());

        // Compose the parameter value.
        final String parameterValue = typeName + "," + resourceIdentifier + "," + resourceLookupRoleArn;

        final PutParameterRequest putParameterRequest = PutParameterRequest.builder().type(ParameterType.STRING)
                .name(parameterName).value(parameterValue).description(parameterName)
                .tags(TagHelper.convertToList(tags)).build();
        return putParameterRequest;
    }

    /**
     * Translates to a {@link GetParameterRequest}.
     *
     * @param model
     *            {@link ResourceModel}
     * @return GetParameterRequest {@link GetParameterRequest}
     */
    public static GetParameterRequest translateToGetParameterRequest(final ResourceModel model) {
        return GetParameterRequest.builder().name(model.getResourceLookupId()).build();
    }

    /**
     * Translates to a {@link ListTagsForResourceRequest}.
     *
     * @param resourceId
     *            {@link String}
     * @return ListTagsForResourceRequest {@link ListTagsForResourceRequest}
     */
    public static ListTagsForResourceRequest translateToListTagsForResourceRequest(final String resourceId) {
        return ListTagsForResourceRequest.builder().resourceType(ResourceTypeForTagging.PARAMETER)
                .resourceId(resourceId).build();
    }

    /**
     * Returns the model by consuming from Parameter Store and Cloud Control API.
     *
     * @param getParameterResponse
     *            {@link GetParameterResponse}
     * @param proxySsmClient
     *            {@link ProxyClient} for {@link SsmClient}
     * @param proxyCloudControlClient
     *            {@link ProxyClient} for {@link CloudControlClient}
     * @return ResourceModel {@link ResourceModel}
     */
    public static ResourceModel getModel(final GetParameterResponse getParameterResponse,
            final ProxyClient<SsmClient> proxySsmClient,
            final ProxyClient<CloudControlClient> proxyCloudControlClient) {
        final String parameterName = getParameterResponse.parameter().name();
        final String parameterValue = getParameterResponse.parameter().value();
        final String typeName = parameterValue.split(",")[0];

        // When reading typeName and resourceIdentifier from a
        // Parameter Store parameter value delimited by a comma, first
        // split the string when an unescaped comma is found to get
        // resourceIdentifier, and then unescape
        // resourceIdentifier. An example use case is the resource
        // identifier for `AWS::IAM::Role`, whereas a comma is allowed
        // in the role name. The same applies to the resource role
        // ARN.
        final String resourceIdentifier = LookupHelper
                .unescapeCommaDelimiters(LookupHelper.splitStringWithUnescapedCommaDelimiters(parameterValue)[1]);
        final String resourceLookupRoleArn = LookupHelper
                .unescapeCommaDelimiters(LookupHelper.splitStringWithUnescapedCommaDelimiters(parameterValue)[2]);

        // Call ListTagsForResource to get the tags for the parameter.
        final SsmClient ssmClient = proxySsmClient.client();
        final ListTagsForResourceResponse listTagsForResourceResponse = proxySsmClient.injectCredentialsAndInvokeV2(
                translateToListTagsForResourceRequest(parameterName), ssmClient::listTagsForResource);
        // Convert tags into a map of strings.
        final Map<String, String> tags = TagHelper.convertToMap(listTagsForResourceResponse.tagList());

        // Call GetResource to get the resource properties.
        final CloudControlClient cloudControlClient = proxyCloudControlClient.client();

        final GetResourceResponse getResourceResponse = proxyCloudControlClient.injectCredentialsAndInvokeV2(
                translateToGetResourceRequest(typeName, resourceLookupRoleArn, resourceIdentifier),
                cloudControlClient::getResource);
        final String resourceProperties = getResourceResponse.resourceDescription().properties();

        return ResourceModel.builder().resourceLookupId(parameterName).typeName(typeName)
                .resourceIdentifier(resourceIdentifier).tags(tags).resourceProperties(resourceProperties)
                .resourceLookupRoleArn(resourceLookupRoleArn).build();
    }

    /**
     * Translates to a {@link DeleteParameterRequest}.
     *
     * @param model
     *            {@link ResourceModel}
     * @return DeleteParameterRequest {@link DeleteParameterRequest}
     */
    public static DeleteParameterRequest translateToDeleteParameterRequest(final ResourceModel model) {
        final DeleteParameterRequest deleteParameterRequest = DeleteParameterRequest.builder()
                .name(model.getResourceLookupId()).build();
        return deleteParameterRequest;
    }

    /**
     * Translates to a {@link DescribeParametersRequest}.
     *
     * @param nextToken
     *            {@link String}
     * @return DescribeParametersRequest {@link DescribeParametersRequest}
     */
    public static DescribeParametersRequest translateToDescribeParametersRequest(final String nextToken) {
        final ParameterStringFilter parameterStringFilter = ParameterStringFilter.builder().key("Name")
                .values(Constants.PRIMARY_IDENTIFIER_PREFIX).option("BeginsWith").build();
        final DescribeParametersRequest describeParametersRequest = DescribeParametersRequest.builder()
                .nextToken(nextToken).parameterFilters(parameterStringFilter).build();
        return describeParametersRequest;
    }

    /**
     * Translates from a List request.
     *
     * @param describeParametersResponse
     *            {@link DescribeParametersResponse}
     * @return List {@link List} of {@link ResourceModel}
     */
    public static List<ResourceModel> translateFromListRequest(
            final DescribeParametersResponse describeParametersResponse) {
        return streamOfOrEmpty(describeParametersResponse.parameters()).map(resource -> ResourceModel.builder()
                // Include only the primary identifier.
                .resourceLookupId(resource.name()).build()).collect(Collectors.toList());
    }

    /**
     * Returns a stream of type T.
     *
     * @param <T>
     *            T type
     * @param collection
     *            {@link Collection} of T
     * @return stream {@link Stream} of T
     */
    private static <T> Stream<T> streamOfOrEmpty(final Collection<T> collection) {
        return Optional.ofNullable(collection).map(Collection::stream).orElseGet(Stream::empty);
    }

    /**
     * Translates to a {@link RemoveTagsFromResourceRequest}.
     *
     * @param resourceId
     *            {@link String}
     * @param tags
     *            {@link Map} of {@link String}
     * @return RemoveTagsFromResourceRequest {@link RemoveTagsFromResourceRequest}
     */
    public static RemoveTagsFromResourceRequest translateToRemoveTagsFromResourceRequest(final String resourceId,
            final Map<String, String> tags) {
        return RemoveTagsFromResourceRequest.builder().resourceType(ResourceTypeForTagging.PARAMETER)
                .resourceId(resourceId).tagKeys(TagHelper.getTagKeysFromMapOfStrings(tags)).build();
    }

    /**
     * Translates to an {@link AddTagsToResourceRequest}.
     *
     * @param resourceId
     *            {@link String}
     * @param tags
     *            {@link Map} of {@link String}
     * @return AddTagsToResourceRequest {@link AddTagsToResourceRequest}
     */
    public static AddTagsToResourceRequest translateToAddTagsToResourceRequest(final String resourceId,
            final Map<String, String> tags) {
        return AddTagsToResourceRequest.builder().resourceType(ResourceTypeForTagging.PARAMETER).resourceId(resourceId)
                .tags(TagHelper.convertToList(tags)).build();
    }
}
