package com.awscommunity.appsync.breakingchangedetection.schema;

import graphql.schema.diff.DiffEvent;
import graphql.schema.diff.reporting.DifferenceReporter;
import software.amazon.cloudformation.proxy.Logger;

import java.util.ArrayList;
import java.util.List;

/**
 * This class handles the reporting of breaking changes. It receives a callback during schema diff to be able to log
 * and return the changes that were detected with a new version of the AppSync GraphQL Schema.
 */
public class AppSyncSchemaDiffReporter implements DifferenceReporter {

    private final List<DiffEvent> breakingChanges;
    private final List<DiffEvent> dangerousChanges;
    private final List<DiffEvent> infoChanges;
    private final Logger logger;
    private final String apiId;


    /**
     * Schema diff reporter for logging and recording the change events reported by SchemaDiff
     * @param logger Logger
     * @param apiId Api Id.
     */
    public AppSyncSchemaDiffReporter(final Logger logger,
                                     final String apiId) {
        this.breakingChanges = new ArrayList<>();
        this.dangerousChanges = new ArrayList<>();
        this.infoChanges = new ArrayList<>();
        this.logger = logger;
        this.apiId = apiId;
    }

    /**
     * Reports the status of a comparison between a field in the new version and old version.
     * @param differenceEvent Difference event representing the potential change in a field.
     */
    @Override
    public void report(DiffEvent differenceEvent) {
        switch (differenceEvent.getLevel()) {
            case BREAKING:
                this.breakingChanges.add(differenceEvent);
                break;
            case DANGEROUS:
                this.dangerousChanges.add(differenceEvent);
                break;
            case INFO:
                // A non-null category in the event indicates there was actually a change.
                if (differenceEvent.getCategory() != null) {
                    this.infoChanges.add(differenceEvent);
                }

                break;
            default:
                logger.log(String.format("Unexpected event level: %s, ignoring", differenceEvent.getLevel()));
        }
    }

    @Override
    public void onEnd() {
    }

    /**
     * Determines whether a breaking change has occurred or not. There are some changes that are considered "DANGEROUS"
     * but not "BREAKING." Use can pass a flag indicating whether the "DANGEROUS" changes should be considered a failure or not.
     * @param allowDangerousChanges Whether to allow dangerous changes or consider them breaking.
     * @return Boolean indicating whether there was a breaking change or not.
     */
    public boolean validateChanges(boolean allowDangerousChanges) {
        boolean hasNoBreakingChanges = this.breakingChanges.isEmpty();
        boolean hasNoDangerousChanges = this.dangerousChanges.isEmpty();
        if (allowDangerousChanges) {
            return hasNoBreakingChanges;
        } else {
            return hasNoBreakingChanges && hasNoDangerousChanges;
        }
    }

    /**
     * Get the formatted report of all relevant changes between the two schema versions.
     * @return String containing the formatted change report.
     */
    public String getFormattedChangeReport() {
        final StringBuilder sb = new StringBuilder();
        appendChangeReports(sb, this.breakingChanges);
        appendChangeReports(sb, this.dangerousChanges);
        appendChangeReports(sb, this.infoChanges);
        return sb.toString();
    }

    /**
     * Append the formatted diff event reports to the input string builder.
     * @param sb String builder
     * @param changes Changes to append to the String.
     */
    private void appendChangeReports(final StringBuilder sb, List<DiffEvent> changes) {
        for (DiffEvent change : changes) {
            sb.append(String.format("API Id: %s [%s] [%s] - %s\n", this.apiId, change.getLevel(), change.getCategory(), change.getReasonMsg()));
        }
    }
}
