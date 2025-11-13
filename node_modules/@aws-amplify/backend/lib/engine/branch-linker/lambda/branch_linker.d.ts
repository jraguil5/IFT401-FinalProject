import { CloudFormationCustomResourceEvent, CloudFormationCustomResourceSuccessResponse } from 'aws-lambda';
import { AmplifyClient } from '@aws-sdk/client-amplify';
/**
 * Handles custom resource events.
 */
export declare class AmplifyBranchLinkerCustomResourceEventHandler {
    private readonly amplifyClient;
    /**
     * Creates the custom resource events handler.
     */
    constructor(amplifyClient: AmplifyClient);
    handleCustomResourceEvent: (event: CloudFormationCustomResourceEvent) => Promise<CloudFormationCustomResourceSuccessResponse>;
    private updateOrUnsetStackReference;
    private getBranch;
}
/**
 * Entry point for the lambda-backend custom resource to link deployment to branch.
 */
export declare const handler: (event: CloudFormationCustomResourceEvent) => Promise<CloudFormationCustomResourceSuccessResponse>;
//# sourceMappingURL=branch_linker.d.ts.map