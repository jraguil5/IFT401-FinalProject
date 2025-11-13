import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ValidateTemplate } from "../schemas/schemas_0";
export { $Command };
export class ValidateTemplateCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ValidateTemplate", {})
    .n("CloudFormationClient", "ValidateTemplateCommand")
    .sc(ValidateTemplate)
    .build() {
}
