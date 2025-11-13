import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { RecordHandlerProgress } from "../schemas/schemas_0";
export { $Command };
export class RecordHandlerProgressCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "RecordHandlerProgress", {})
    .n("CloudFormationClient", "RecordHandlerProgressCommand")
    .sc(RecordHandlerProgress)
    .build() {
}
