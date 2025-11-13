import { BackendIdentifier, MainStackCreator } from '@aws-amplify/plugin-types';
import { Construct } from 'constructs';
import { Stack } from 'aws-cdk-lib';
/**
 * Creates stacks that are tied to a given project environment via an SSM parameter
 */
export declare class ProjectEnvironmentMainStackCreator implements MainStackCreator {
    private readonly scope;
    private readonly backendId;
    private mainStack;
    /**
     * Initialize with a project environment
     */
    constructor(scope: Construct, backendId: BackendIdentifier);
    /**
     * Get a stack for this environment in the provided CDK scope
     */
    getOrCreateMainStack: () => Stack;
}
//# sourceMappingURL=project_environment_main_stack_creator.d.ts.map