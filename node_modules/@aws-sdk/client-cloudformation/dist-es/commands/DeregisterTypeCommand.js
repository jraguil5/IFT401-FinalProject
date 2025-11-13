import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeregisterType } from "../schemas/schemas_0";
export { $Command };
export class DeregisterTypeCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DeregisterType", {})
    .n("CloudFormationClient", "DeregisterTypeCommand")
    .sc(DeregisterType)
    .build() {
}
