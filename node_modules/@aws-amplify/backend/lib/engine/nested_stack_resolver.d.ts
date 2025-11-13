import { Stack } from 'aws-cdk-lib';
import { AttributionMetadataStorage } from '@aws-amplify/backend-output-storage';
/**
 * Vends stacks for a resource grouping
 */
export type StackResolver = {
    getStackFor: (resourceGroupName: string) => Stack;
    createCustomStack: (name: string) => Stack;
};
/**
 * Vends and caches nested stacks under a provided root stack
 */
export declare class NestedStackResolver implements StackResolver {
    private readonly rootStack;
    private readonly attributionMetadataStorage;
    private readonly stacks;
    /**
     * Initialize with a root stack
     */
    constructor(rootStack: Stack, attributionMetadataStorage: AttributionMetadataStorage);
    /**
     * Proxy to getStackFor that appends attribution metadata for custom stacks
     */
    createCustomStack: (name: string) => Stack;
    /**
     * Returns a cached NestedStack if resourceGroupName has been seen before
     * Otherwise, creates a new NestedStack, caches it and returns it
     */
    getStackFor: (resourceGroupName: string) => Stack;
}
//# sourceMappingURL=nested_stack_resolver.d.ts.map