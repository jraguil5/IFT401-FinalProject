import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeactivateType } from "../schemas/schemas_0";
export { $Command };
export class DeactivateTypeCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DeactivateType", {})
    .n("CloudFormationClient", "DeactivateTypeCommand")
    .sc(DeactivateType)
    .build() {
}
