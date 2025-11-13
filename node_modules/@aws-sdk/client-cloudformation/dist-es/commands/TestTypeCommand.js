import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { TestType } from "../schemas/schemas_0";
export { $Command };
export class TestTypeCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "TestType", {})
    .n("CloudFormationClient", "TestTypeCommand")
    .sc(TestType)
    .build() {
}
