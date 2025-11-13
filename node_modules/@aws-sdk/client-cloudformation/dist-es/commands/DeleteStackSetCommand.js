import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeleteStackSet } from "../schemas/schemas_0";
export { $Command };
export class DeleteStackSetCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DeleteStackSet", {})
    .n("CloudFormationClient", "DeleteStackSetCommand")
    .sc(DeleteStackSet)
    .build() {
}
