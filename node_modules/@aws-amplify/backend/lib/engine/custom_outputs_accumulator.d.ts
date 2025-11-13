import { BackendOutputStorageStrategy, DeepPartialAmplifyGeneratedConfigs } from '@aws-amplify/plugin-types';
import { ClientConfig } from '@aws-amplify/client-config';
import { CustomOutput } from '@aws-amplify/backend-output-schemas';
import { ObjectAccumulator } from '@aws-amplify/platform-core';
/**
 * Accumulates custom outputs as they're added to the backend.
 */
export declare class CustomOutputsAccumulator {
    private readonly outputStorageStrategy;
    private readonly clientConfigAccumulator;
    private hasBackendOutputEntry;
    /**
     * Creates custom outputs accumulator.
     */
    constructor(outputStorageStrategy: BackendOutputStorageStrategy<CustomOutput>, clientConfigAccumulator: ObjectAccumulator<ClientConfig>);
    addOutput: (clientConfigPart: DeepPartialAmplifyGeneratedConfigs<ClientConfig>) => void;
    private ensureBackendOutputEntry;
}
//# sourceMappingURL=custom_outputs_accumulator.d.ts.map