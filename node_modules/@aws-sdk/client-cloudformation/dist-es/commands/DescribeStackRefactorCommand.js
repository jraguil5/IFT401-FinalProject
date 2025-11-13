import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStackRefactor } from "../schemas/schemas_0";
export { $Command };
export class DescribeStackRefactorCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStackRefactor", {})
    .n("CloudFormationClient", "DescribeStackRefactorCommand")
    .sc(DescribeStackRefactor)
    .build() {
}
