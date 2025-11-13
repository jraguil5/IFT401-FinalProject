import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStacks } from "../schemas/schemas_0";
export { $Command };
export class DescribeStacksCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStacks", {})
    .n("CloudFormationClient", "DescribeStacksCommand")
    .sc(DescribeStacks)
    .build() {
}
