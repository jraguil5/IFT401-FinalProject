import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStackInstance } from "../schemas/schemas_0";
export { $Command };
export class DescribeStackInstanceCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStackInstance", {})
    .n("CloudFormationClient", "DescribeStackInstanceCommand")
    .sc(DescribeStackInstance)
    .build() {
}
