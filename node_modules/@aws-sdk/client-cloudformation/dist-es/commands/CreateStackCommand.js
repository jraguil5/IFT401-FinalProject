import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { CreateStack } from "../schemas/schemas_0";
export { $Command };
export class CreateStackCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "CreateStack", {})
    .n("CloudFormationClient", "CreateStackCommand")
    .sc(CreateStack)
    .build() {
}
