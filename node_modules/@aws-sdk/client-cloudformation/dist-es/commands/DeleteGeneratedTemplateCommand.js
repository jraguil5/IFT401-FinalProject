import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeleteGeneratedTemplate } from "../schemas/schemas_0";
export { $Command };
export class DeleteGeneratedTemplateCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DeleteGeneratedTemplate", {})
    .n("CloudFormationClient", "DeleteGeneratedTemplateCommand")
    .sc(DeleteGeneratedTemplate)
    .build() {
}
