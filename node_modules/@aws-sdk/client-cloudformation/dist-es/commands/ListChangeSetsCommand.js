import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListChangeSets } from "../schemas/schemas_0";
export { $Command };
export class ListChangeSetsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListChangeSets", {})
    .n("CloudFormationClient", "ListChangeSetsCommand")
    .sc(ListChangeSets)
    .build() {
}
