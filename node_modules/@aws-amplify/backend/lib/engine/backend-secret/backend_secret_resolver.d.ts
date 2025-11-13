import { BackendIdentifier, BackendSecret, BackendSecretResolver, ResolvePathResult } from '@aws-amplify/plugin-types';
import { SecretValue } from 'aws-cdk-lib';
import { Construct } from 'constructs';
/**
 * DefaultBackendSecretResolver resolves a backend secret.
 */
export declare class DefaultBackendSecretResolver implements BackendSecretResolver {
    private readonly scope;
    private readonly backendId;
    /**
     * Creates a DefaultBackendSecretResolver instance.
     */
    constructor(scope: Construct, backendId: BackendIdentifier);
    resolveSecret: (backendSecret: BackendSecret) => SecretValue;
    resolvePath: (backendSecret: BackendSecret) => ResolvePathResult;
}
//# sourceMappingURL=backend_secret_resolver.d.ts.map