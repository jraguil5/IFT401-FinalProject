import { ImportPathVerifier } from '@aws-amplify/plugin-types';
/**
 * ImportPathVerifier that can be turned into a noop by passing `false` to the constructor
 */
export declare class ToggleableImportPathVerifier implements ImportPathVerifier {
    private readonly doVerify;
    /**
     * Defaults to verifying, but can be turned into a noop by passing in false.
     */
    constructor(doVerify?: boolean);
    /**
     * @inheritDoc
     */
    verify: (importStack: string | undefined, expectedImportSuffix: string, errorMessage: string) => void;
}
//# sourceMappingURL=toggleable_import_path_verifier.d.ts.map