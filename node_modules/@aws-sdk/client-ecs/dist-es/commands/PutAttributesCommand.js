import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { PutAttributes } from "../schemas/schemas_0";
export { $Command };
export class PutAttributesCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("AmazonEC2ContainerServiceV20141113", "PutAttributes", {})
    .n("ECSClient", "PutAttributesCommand")
    .sc(PutAttributes)
    .build() {
}
