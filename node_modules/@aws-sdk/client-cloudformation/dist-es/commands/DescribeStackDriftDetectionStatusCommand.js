import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeStackDriftDetectionStatus } from "../schemas/schemas_0";
export { $Command };
export class DescribeStackDriftDetectionStatusCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeStackDriftDetectionStatus", {})
    .n("CloudFormationClient", "DescribeStackDriftDetectionStatusCommand")
    .sc(DescribeStackDriftDetectionStatus)
    .build() {
}
