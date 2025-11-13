import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListTypeVersions } from "../schemas/schemas_0";
export { $Command };
export class ListTypeVersionsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListTypeVersions", {})
    .n("CloudFormationClient", "ListTypeVersionsCommand")
    .sc(ListTypeVersions)
    .build() {
}
