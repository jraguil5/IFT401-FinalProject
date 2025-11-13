import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListResourceScanRelatedResources } from "../schemas/schemas_0";
export { $Command };
export class ListResourceScanRelatedResourcesCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ListResourceScanRelatedResources", {})
    .n("CloudFormationClient", "ListResourceScanRelatedResourcesCommand")
    .sc(ListResourceScanRelatedResources)
    .build() {
}
