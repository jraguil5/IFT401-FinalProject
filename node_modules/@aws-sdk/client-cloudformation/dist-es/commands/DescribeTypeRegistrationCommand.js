import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeTypeRegistration } from "../schemas/schemas_0";
export { $Command };
export class DescribeTypeRegistrationCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeTypeRegistration", {})
    .n("CloudFormationClient", "DescribeTypeRegistrationCommand")
    .sc(DescribeTypeRegistration)
    .build() {
}
