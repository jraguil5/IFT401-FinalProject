import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeleteChangeSet } from "../schemas/schemas_0";
export { $Command };
export class DeleteChangeSetCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DeleteChangeSet", {})
    .n("CloudFormationClient", "DeleteChangeSetCommand")
    .sc(DeleteChangeSet)
    .build() {
}
