import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { CreateStackRefactor } from "../schemas/schemas_0";
export { $Command };
export class CreateStackRefactorCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "CreateStackRefactor", {})
    .n("CloudFormationClient", "CreateStackRefactorCommand")
    .sc(CreateStackRefactor)
    .build() {
}
