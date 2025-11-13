import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DeleteTaskSet } from "../schemas/schemas_0";
export { $Command };
export class DeleteTaskSetCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("AmazonEC2ContainerServiceV20141113", "DeleteTaskSet", {})
    .n("ECSClient", "DeleteTaskSetCommand")
    .sc(DeleteTaskSet)
    .build() {
}
