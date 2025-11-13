import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListResourceScans } from "../schemas/schemas_0";
export { $Command };
export class ListResourceScansCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListResourceScans", {})
    .n("CloudFormationClient", "ListResourceScansCommand")
    .sc(ListResourceScans)
    .build() {
}
