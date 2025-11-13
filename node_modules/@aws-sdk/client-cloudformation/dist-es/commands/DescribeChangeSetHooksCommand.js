import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeChangeSetHooks } from "../schemas/schemas_0";
export { $Command };
export class DescribeChangeSetHooksCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeChangeSetHooks", {})
    .n("CloudFormationClient", "DescribeChangeSetHooksCommand")
    .sc(DescribeChangeSetHooks)
    .build() {
}
