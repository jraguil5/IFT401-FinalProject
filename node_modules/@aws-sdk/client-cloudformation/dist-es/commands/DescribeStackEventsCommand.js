import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStackEvents } from "../schemas/schemas_0";
export { $Command };
export class DescribeStackEventsCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStackEvents", {})
    .n("CloudFormationClient", "DescribeStackEventsCommand")
    .sc(DescribeStackEvents)
    .build() {
}
