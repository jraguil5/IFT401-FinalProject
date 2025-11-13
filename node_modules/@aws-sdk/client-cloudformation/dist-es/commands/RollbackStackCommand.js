import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { RollbackStack } from "../schemas/schemas_0";
export { $Command };
export class RollbackStackCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "RollbackStack", {})
    .n("CloudFormationClient", "RollbackStackCommand")
    .sc(RollbackStack)
    .build() {
}
