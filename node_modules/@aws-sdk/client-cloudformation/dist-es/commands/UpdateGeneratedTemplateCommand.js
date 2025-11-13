import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { UpdateGeneratedTemplate } from "../schemas/schemas_0";
export { $Command };
export class UpdateGeneratedTemplateCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "UpdateGeneratedTemplate", {})
    .n("CloudFormationClient", "UpdateGeneratedTemplateCommand")
    .sc(UpdateGeneratedTemplate)
    .build() {
}
