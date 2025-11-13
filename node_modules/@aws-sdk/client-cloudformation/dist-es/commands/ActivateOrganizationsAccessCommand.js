import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ActivateOrganizationsAccess } from "../schemas/schemas_0";
export { $Command };
export class ActivateOrganizationsAccessCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("CloudFormation", "ActivateOrganizationsAccess", {})
    .n("CloudFormationClient", "ActivateOrganizationsAccessCommand")
    .sc(ActivateOrganizationsAccess)
    .build() {
}
