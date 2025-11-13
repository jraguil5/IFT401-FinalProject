import { StackResolver } from './nested_stack_resolver.js';
import { ConstructContainer, ConstructContainerEntryGenerator, ConstructFactory, ResourceProvider } from '@aws-amplify/plugin-types';
/**
 * Serves as a DI container and shared state store for initializing Amplify constructs
 */
export declare class SingletonConstructContainer implements ConstructContainer {
    private readonly stackResolver;
    private readonly providerCache;
    private readonly providerFactoryTokenMap;
    /**
     * Initialize the BackendBuildState with a root stack
     */
    constructor(stackResolver: StackResolver);
    /**
     * If generator has been seen before, the cached Construct instance is returned
     * Otherwise, the generator is called and the value is cached and returned
     */
    getOrCompute: (generator: ConstructContainerEntryGenerator) => ResourceProvider;
    /**
     * Gets a ConstructFactory that has previously been registered to a given token.
     * Returns undefined if no construct factory is found for the specified token.
     *
     * NOTE: The return type of this function cannot be guaranteed at compile time because factories are dynamically registered at runtime
     * The return type of the factory is a contract that must be negotiated by the entity that registers a token and the entity that retrieves a token.
     *
     * By convention, tokens should be the name of type T
     */
    getConstructFactory: <T extends ResourceProvider>(token: string) => ConstructFactory<T> | undefined;
    /**
     * Register a ConstructFactory to a specified token. This ConstructFactory can be retrieved later using getConstructFactory
     * Throws if the token is already registered to a different factory
     */
    registerConstructFactory: (token: string, provider: ConstructFactory) => void;
}
//# sourceMappingURL=singleton_construct_container.d.ts.map