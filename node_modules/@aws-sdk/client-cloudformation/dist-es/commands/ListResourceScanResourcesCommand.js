import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListResourceScanResources } from "../schemas/schemas_0";
export { $Command };
export class ListResourceScanResourcesCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListResourceScanResources", {})
    .n("CloudFormationClient", "ListResourceScanResourcesCommand")
    .sc(ListResourceScanResources)
    .build() {
}
