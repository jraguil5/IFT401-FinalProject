import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ExecuteStackRefactor } from "../schemas/schemas_0";
export { $Command };
export class ExecuteStackRefactorCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ExecuteStackRefactor", {})
    .n("CloudFormationClient", "ExecuteStackRefactorCommand")
    .sc(ExecuteStackRefactor)
    .build() {
}
