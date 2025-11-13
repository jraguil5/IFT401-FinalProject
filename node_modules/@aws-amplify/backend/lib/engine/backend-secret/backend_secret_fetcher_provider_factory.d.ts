import { Construct } from 'constructs';
import { Provider } from 'aws-cdk-lib/custom-resources';
import { BackendIdentifier } from '@aws-amplify/plugin-types';
/**
 * The factory to create secret-fetcher provider.
 */
export declare class BackendSecretFetcherProviderFactory {
    /**
     * Returns a resource provider if it exists in the input scope. Otherwise,
     * creates a new provider.
     */
    getOrCreateInstance: (scope: Construct, providerId: string, backendIdentifier: BackendIdentifier) => Provider;
}
//# sourceMappingURL=backend_secret_fetcher_provider_factory.d.ts.map