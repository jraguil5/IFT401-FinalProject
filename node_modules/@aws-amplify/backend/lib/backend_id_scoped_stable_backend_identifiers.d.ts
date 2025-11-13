import { BackendIdentifier, StableBackendIdentifiers } from '@aws-amplify/plugin-types';
/**
 * Gets a stable hash value derived from BackendIdentifier
 */
export declare class BackendIdScopedStableBackendIdentifiers implements StableBackendIdentifiers {
    private readonly backendId;
    private hash;
    /**
     * Creates a StableBackendHashGetter instance.
     */
    constructor(backendId: BackendIdentifier);
    getStableBackendHash: () => string;
    private hashFromBackendId;
}
//# sourceMappingURL=backend_id_scoped_stable_backend_identifiers.d.ts.map