import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DetectStackResourceDrift } from "../schemas/schemas_0";
export { $Command };
export class DetectStackResourceDriftCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DetectStackResourceDrift", {})
    .n("CloudFormationClient", "DetectStackResourceDriftCommand")
    .sc(DetectStackResourceDrift)
    .build() {
}
