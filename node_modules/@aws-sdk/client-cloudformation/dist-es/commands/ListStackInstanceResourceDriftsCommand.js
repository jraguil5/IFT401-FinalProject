import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListStackInstanceResourceDrifts } from "../schemas/schemas_0";
export { $Command };
export class ListStackInstanceResourceDriftsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListStackInstanceResourceDrifts", {})
    .n("CloudFormationClient", "ListStackInstanceResourceDriftsCommand")
    .sc(ListStackInstanceResourceDrifts)
    .build() {
}
