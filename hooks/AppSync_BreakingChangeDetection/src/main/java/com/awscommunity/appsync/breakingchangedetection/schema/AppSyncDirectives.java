package com.awscommunity.appsync.breakingchangedetection.schema;

import com.google.common.collect.ImmutableSet;
import graphql.introspection.Introspection;
import graphql.language.DirectiveDefinition;
import graphql.language.DirectiveLocation;
import graphql.language.TypeName;
import graphql.language.InputValueDefinition;
import graphql.language.ListType;

import java.util.List;
import java.util.Set;

/**
 * A class which contains set of all in built directives currently supported by AppSync.
 */
public class AppSyncDirectives {

    /**
     * Cognito groups auth directive name.
     */
    public static final String AUTH_DIRECTIVE_NAME = "aws_auth";

    /**
     * Multi-auth Cognito auth directive name.
     */
    public static final String COGNITO_AUTH_DIRECTIVE_NAME = "aws_cognito_user_pools";

    /**
     * IAM auth directive name.
     */
    public static final String IAM_AUTH_DIRECTIVE_NAME = "aws_iam";

    /**
     * API key directive name.
     */
    public static final String API_KEY_AUTH_DIRECTIVE_NAME = "aws_api_key";

    /**
     * OIDC directive name.
     */
    public static final String OIDC_AUTH_DIRECTIVE_NAME = "aws_oidc";

    /**
     * Lambda auth directive name.
     */
    public static final String LAMBDA_AUTH_DIRECTIVE_NAME = "aws_lambda";

    /**
     * Cognito groups argument name.
     */
    public static final String AUTH_DIRECTIVE_COGNITO_GROUP_ARG = "cognito_groups";

    /**
     * Name of the publish directive which notifies the service which subscription to publish to.
     */
    public static final String PUBLISH_DIRECTIVE_NAME = "aws_publish";

    /**
     * The name of the publish argument.
     */
    public static final String PUBLISH_DIRECTIVE_SUBSCRIPTION_ARG = "subscriptions";

    /**
     * Name of the subscribe directive which notifies the service which mutations trigger this subscription.
     */
    public static final String SUBSCRIBE_DIRECTIVE_NAME = "aws_subscribe";

    /**
     * The name of the subscribe argument.
     */
    public static final String SUBSCRIBE_DIRECTIVE_MUTATIONS_ARG = "mutations";

    /**
     * Name of the hidden directive for AppSync Merged APIs.
     */
    public static final String HIDDEN_DIRECTIVE_NAME = "hidden";

    /**
     * Name of the canonical directive for AppSync Merged APIs.
     */
    public static final String CANONICAL_DIRECTIVE_NAME = "canonical";

    /**
     * Name of the renamed directive for AppSync Merged APIs.
     */
    public static final String RENAMED_DIRECTIVE_NAME = "renamed";

    /**
     * Name of the renamed to argument for the renamed directive for AppSync Merged APIs.
     */
    public static final String RENAMED_TO_ARG_NAME = "to";

    /**
     * Directive on Field definition.
     */
    private static final DirectiveLocation FIELD_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.FIELD_DEFINITION.name())
            .build();

    /**
     * Directive on Object definition.
     */
    private static final DirectiveLocation OBJECT_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.OBJECT.name())
            .build();

    /**
     * Directive on Interface definition.
     */
    private static final DirectiveLocation INTERFACE_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.INTERFACE.name())
            .build();

    /**
     * Directive on Union definition.
     */
    private static final DirectiveLocation UNION_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.UNION.name())
            .build();

    /**
     * Directive on Enum definition.
     */
    private static final DirectiveLocation ENUM_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.ENUM.name())
            .build();

    /**
     * Directive on Enum Value definition.
     */
    private static final DirectiveLocation ENUM_VALUE_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.ENUM_VALUE.name())
            .build();

    /**
     * Directive on Input Object definition.
     */
    private static final DirectiveLocation INPUT_OBJECT_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.INPUT_OBJECT.name())
            .build();

    /**
     * Directive on Input Field definition.
     */
    private static final DirectiveLocation INPUT_FIELD_DEFINITION_DIRECTIVE_LOCATION = DirectiveLocation.newDirectiveLocation()
            .name(Introspection.DirectiveLocation.INPUT_FIELD_DEFINITION.name())
            .build();

    /**
     * List of all valid locations for the AppSync Merged APIs conflict resoluition directives.
     */
    private static final List<DirectiveLocation> CONFLICT_RESOLUTION_DIRECTIVE_LOCATIONS =
            List.of(FIELD_DIRECTIVE_LOCATION, OBJECT_DIRECTIVE_LOCATION, INTERFACE_DIRECTIVE_LOCATION,
                    UNION_DIRECTIVE_LOCATION, ENUM_DIRECTIVE_LOCATION, ENUM_VALUE_DIRECTIVE_LOCATION,
                    INPUT_OBJECT_DIRECTIVE_LOCATION, INPUT_FIELD_DEFINITION_DIRECTIVE_LOCATION);

    /**
     * The api key directive
     */
    public static final DirectiveDefinition API_KEY_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(API_KEY_AUTH_DIRECTIVE_NAME)
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .directiveLocation(OBJECT_DIRECTIVE_LOCATION)
            .build();

    /**
     * The iam auth directive definition.
     */
    public static final DirectiveDefinition IAM_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(IAM_AUTH_DIRECTIVE_NAME)
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .directiveLocation(OBJECT_DIRECTIVE_LOCATION)
            .build();

    /**
     * The cognito auth directive definition.
     */
    public static final DirectiveDefinition COGNITO_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(COGNITO_AUTH_DIRECTIVE_NAME)
            .inputValueDefinition(InputValueDefinition.newInputValueDefinition()
                    .name(AUTH_DIRECTIVE_COGNITO_GROUP_ARG)
                    .type(new ListType(new TypeName("String")))
                    .build())
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .directiveLocation(OBJECT_DIRECTIVE_LOCATION)
            .build();

    /**
     * The oidc auth directive definition.
     */
    public static final DirectiveDefinition OIDC_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(OIDC_AUTH_DIRECTIVE_NAME)
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .directiveLocation(OBJECT_DIRECTIVE_LOCATION)
            .build();

    /**
     * The lambda auth directive definition.
     */
    public static final DirectiveDefinition LAMBDA_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(LAMBDA_AUTH_DIRECTIVE_NAME)
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .directiveLocation(OBJECT_DIRECTIVE_LOCATION)
            .build();

    /**
     * The aws-auth directive.
     */
    public static final DirectiveDefinition AUTH_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(AUTH_DIRECTIVE_NAME)
            .inputValueDefinition(new InputValueDefinition(AUTH_DIRECTIVE_COGNITO_GROUP_ARG, new ListType(new TypeName("String"))))
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .build();

    /**
     * A directive which can be applied to mutations. This directive tells us the mutation will publish to a
     * subscription.
     */
    public static final DirectiveDefinition PUBLISH_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(PUBLISH_DIRECTIVE_NAME)
            .inputValueDefinition(new InputValueDefinition(PUBLISH_DIRECTIVE_SUBSCRIPTION_ARG, new ListType(new TypeName("String"))))
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .build();

    /**
     * A directive which can be applied to subscriptions. This directive tells us the mutation which triggers this
     * subscription.
     */
    public static final DirectiveDefinition SUBSCRIBE_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(SUBSCRIBE_DIRECTIVE_NAME)
            .inputValueDefinition(new InputValueDefinition(SUBSCRIBE_DIRECTIVE_MUTATIONS_ARG, new ListType(new TypeName("String"))))
            .directiveLocation(FIELD_DIRECTIVE_LOCATION)
            .build();

    /**
     * Hidden directive for AppSync Merged APIs.
     */
    public static final DirectiveDefinition HIDDEN_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(HIDDEN_DIRECTIVE_NAME)
            .directiveLocations(CONFLICT_RESOLUTION_DIRECTIVE_LOCATIONS)
            .build();

    /**
     * Canonical directive for AppSync Merged APIs.
     */
    public static final DirectiveDefinition CANONICAL_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(CANONICAL_DIRECTIVE_NAME)
            .directiveLocations(CONFLICT_RESOLUTION_DIRECTIVE_LOCATIONS)
            .build();

    /**
     * Renamed directive for AppSync Merged APIs.
     */
    public static final DirectiveDefinition RENAMED_DIRECTIVE = DirectiveDefinition.newDirectiveDefinition()
            .name(RENAMED_DIRECTIVE_NAME)
            .inputValueDefinition(new InputValueDefinition(RENAMED_TO_ARG_NAME, new TypeName("String")))
            .directiveLocations(CONFLICT_RESOLUTION_DIRECTIVE_LOCATIONS)
            .build();

    /**
     * A list of built in AppSync Directives.
     */
    public static final Set<DirectiveDefinition> APPSYNC_DIRECTIVE_DEFINITIONS = ImmutableSet.of(
            AUTH_DIRECTIVE,
            PUBLISH_DIRECTIVE,
            SUBSCRIBE_DIRECTIVE,
            API_KEY_DIRECTIVE,
            OIDC_DIRECTIVE,
            IAM_DIRECTIVE,
            COGNITO_DIRECTIVE,
            LAMBDA_DIRECTIVE,
            HIDDEN_DIRECTIVE,
            CANONICAL_DIRECTIVE,
            RENAMED_DIRECTIVE
    );
}
