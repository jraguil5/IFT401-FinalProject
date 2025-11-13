import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { CancelUpdateStack } from "../schemas/schemas_0";
export { $Command };
export class CancelUpdateStackCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "CancelUpdateStack", {})
    .n("CloudFormationClient", "CancelUpdateStackCommand")
    .sc(CancelUpdateStack)
    .build() {
}
