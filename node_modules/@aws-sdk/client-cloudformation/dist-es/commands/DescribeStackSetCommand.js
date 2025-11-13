import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStackSet } from "../schemas/schemas_0";
export { $Command };
export class DescribeStackSetCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStackSet", {})
    .n("CloudFormationClient", "DescribeStackSetCommand")
    .sc(DescribeStackSet)
    .build() {
}
