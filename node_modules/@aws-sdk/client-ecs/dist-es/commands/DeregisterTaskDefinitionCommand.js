import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeregisterTaskDefinition } from "../schemas/schemas_0";
export { $Command };
export class DeregisterTaskDefinitionCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("AmazonEC2ContainerServiceV20141113", "DeregisterTaskDefinition", {})
    .n("ECSClient", "DeregisterTaskDefinitionCommand")
    .sc(DeregisterTaskDefinition)
    .build() {
}
