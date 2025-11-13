import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { GetTemplate } from "../schemas/schemas_0";
export { $Command };
export class GetTemplateCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "GetTemplate", {})
    .n("CloudFormationClient", "GetTemplateCommand")
    .sc(GetTemplate)
    .build() {
}
