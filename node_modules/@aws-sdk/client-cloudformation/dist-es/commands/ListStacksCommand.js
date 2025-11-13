import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListStacks } from "../schemas/schemas_0";
export { $Command };
export class ListStacksCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListStacks", {})
    .n("CloudFormationClient", "ListStacksCommand")
    .sc(ListStacks)
    .build() {
}
