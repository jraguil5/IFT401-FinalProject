import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeType } from "../schemas/schemas_0";
export { $Command };
export class DescribeTypeCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeType", {})
    .n("CloudFormationClient", "DescribeTypeCommand")
    .sc(DescribeType)
    .build() {
}
