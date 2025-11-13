import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { GetGeneratedTemplate } from "../schemas/schemas_0";
export { $Command };
export class GetGeneratedTemplateCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "GetGeneratedTemplate", {})
    .n("CloudFormationClient", "GetGeneratedTemplateCommand")
    .sc(GetGeneratedTemplate)
    .build() {
}
