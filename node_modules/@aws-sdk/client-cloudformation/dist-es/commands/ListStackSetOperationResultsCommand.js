import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListStackSetOperationResults } from "../schemas/schemas_0";
export { $Command };
export class ListStackSetOperationResultsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListStackSetOperationResults", {})
    .n("CloudFormationClient", "ListStackSetOperationResultsCommand")
    .sc(ListStackSetOperationResults)
    .build() {
}
