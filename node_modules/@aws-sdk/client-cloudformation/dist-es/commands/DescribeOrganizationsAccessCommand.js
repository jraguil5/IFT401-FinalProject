import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { DescribeOrganizationsAccess } from "../schemas/schemas_0";
export { $Command };
export class DescribeOrganizationsAccessCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "DescribeOrganizationsAccess", {})
    .n("CloudFormationClient", "DescribeOrganizationsAccessCommand")
    .sc(DescribeOrganizationsAccess)
    .build() {
}
