import { getEndpointPlugin } from "@smithy/middleware-endpoint";
import { Command as $Command } from "@smithy/smithy-client";
import { commonParams } from "../endpoint/EndpointParameters";
import { ListTasks } from "../schemas/schemas_0";
export { $Command };
export class ListTasksCommand extends $Command
    .classBuilder()
    .ep(commonParams)
    .m(function (Command, cs, config, o) {
    return [getEndpointPlugin(config, Command.getEndpointParameterInstructions())];
})
    .s("AmazonEC2ContainerServiceV20141113", "ListTasks", {})
    .n("ECSClient", "ListTasksCommand")
    .sc(ListTasks)
    .build() {
}
