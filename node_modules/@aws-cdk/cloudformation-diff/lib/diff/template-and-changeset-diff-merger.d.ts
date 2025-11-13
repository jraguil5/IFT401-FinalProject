import type { DescribeChangeSetOutput as DescribeChangeSet, ResourceChangeDetail as RCD } from '@aws-sdk/client-cloudformation';
import * as types from '../diff/types';
export type DescribeChangeSetOutput = DescribeChangeSet;
type ChangeSetResourceChangeDetail = RCD;
interface TemplateAndChangeSetDiffMergerOptions {
    readonly changeSetResources?: types.ChangeSetResources;
}
export interface TemplateAndChangeSetDiffMergerProps extends TemplateAndChangeSetDiffMergerOptions {
    readonly changeSet: DescribeChangeSetOutput;
}
/**
 * The purpose of this class is to include differences from the ChangeSet to differences in the TemplateDiff.
 */
export declare class TemplateAndChangeSetDiffMerger {
    static determineChangeSetReplacementMode(propertyChange: ChangeSetResourceChangeDetail): types.ReplacementModes;
    private static UNKNOWN_RESOURCE_TYPE;
    changeSet: DescribeChangeSetOutput | undefined;
    changeSetResources: types.ChangeSetResources;
    constructor(props: TemplateAndChangeSetDiffMergerProps);
    /**
     * Read resources from the changeSet, extracting information into ChangeSetResources.
     */
    private convertDescribeChangeSetOutputToChangeSetResources;
    /**
     * This is writing over the "ChangeImpact" that was computed from the template difference, and instead using the ChangeImpact that is included from the ChangeSet.
     * Using the ChangeSet ChangeImpact is more accurate. The ChangeImpact tells us what the consequence is of changing the field. If changing the field causes resource
     * replacement (e.g., changing the name of an IAM role requires deleting and replacing the role), then ChangeImpact is "Always".
     */
    overrideDiffResourceChangeImpactWithChangeSetChangeImpact(logicalId: string, change: types.ResourceDifference): void;
    addImportInformationFromChangeset(resourceDiffs: types.DifferenceCollection<types.Resource, types.ResourceDifference>): void;
    findResourceImports(): (string | undefined)[];
}
export {};
