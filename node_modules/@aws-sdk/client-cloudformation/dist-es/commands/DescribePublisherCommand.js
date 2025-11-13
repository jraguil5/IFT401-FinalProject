import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribePublisher } from "../schemas/schemas_0";
export { $Command };
export class DescribePublisherCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribePublisher", {})
    .n("CloudFormationClient", "DescribePublisherCommand")
    .sc(DescribePublisher)
    .build() {
}
