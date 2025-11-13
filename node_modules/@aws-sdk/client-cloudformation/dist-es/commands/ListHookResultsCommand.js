import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListHookResults } from "../schemas/schemas_0";
export { $Command };
export class ListHookResultsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListHookResults", {})
    .n("CloudFormationClient", "ListHookResultsCommand")
    .sc(ListHookResults)
    .build() {
}
