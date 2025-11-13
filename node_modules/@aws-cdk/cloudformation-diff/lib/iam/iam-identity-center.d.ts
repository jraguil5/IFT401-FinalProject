/**
 * This namespace should be a subset of the L1 CfnPermissionSet, other than
 * capitalization, since the values come from from a parsed CFN template.
 */
export declare namespace ISsoPermissionSet {
    interface Props {
        readonly name: string | undefined;
        readonly cfnLogicalId: string | undefined;
        readonly ssoInstanceArn: string | undefined;
        readonly ssoPermissionsBoundary: ISsoPermissionSet.PermissionsBoundary | undefined;
        readonly ssoCustomerManagedPolicyReferences: ISsoPermissionSet.CustomerManagedPolicyReference[] | undefined;
    }
    interface PermissionsBoundary {
        readonly CustomerManagedPolicyReference?: CustomerManagedPolicyReference;
        readonly ManagedPolicyArn?: string;
    }
    interface CustomerManagedPolicyReference {
        readonly Name: string | undefined;
        readonly Path: string | undefined;
    }
}
export declare class SsoPermissionSet implements ISsoPermissionSet.Props {
    readonly name: string | undefined;
    readonly cfnLogicalId: string | undefined;
    readonly ssoInstanceArn: string | undefined;
    readonly ssoPermissionsBoundary: ISsoPermissionSet.PermissionsBoundary | undefined;
    readonly ssoCustomerManagedPolicyReferences: ISsoPermissionSet.CustomerManagedPolicyReference[] | undefined;
    constructor(props: ISsoPermissionSet.Props);
    equal(other: SsoPermissionSet): boolean;
}
export declare namespace ISsoAssignment {
    interface Props {
        readonly ssoInstanceArn: string | undefined;
        readonly cfnLogicalId: string | undefined;
        readonly permissionSetArn: string | undefined;
        readonly principalId: string | undefined;
        readonly principalType: string | undefined;
        readonly targetId: string | undefined;
        readonly targetType: string | undefined;
    }
}
export declare class SsoAssignment implements ISsoAssignment.Props {
    readonly cfnLogicalId: string | undefined;
    readonly ssoInstanceArn: string | undefined;
    readonly permissionSetArn: string | undefined;
    readonly principalId: string | undefined;
    readonly principalType: string | undefined;
    readonly targetId: string | undefined;
    readonly targetType: string | undefined;
    constructor(props: ISsoAssignment.Props);
    equal(other: SsoAssignment): boolean;
}
/**
 * AWS::SSO::InstanceAccessControlAttributeConfiguration
 */
export interface ISsoInstanceACAConfigProps {
    ssoInstanceArn: string;
}
export declare namespace ISsoInstanceACAConfig {
    type AccessControlAttribute = {
        Key: string | undefined;
        Value: {
            Source: string[];
        } | undefined;
    } | undefined;
    interface Props {
        readonly ssoInstanceArn: string | undefined;
        readonly cfnLogicalId: string | undefined;
        readonly accessControlAttributes?: AccessControlAttribute[] | undefined;
    }
}
export declare class SsoInstanceACAConfig implements ISsoInstanceACAConfig.Props {
    readonly cfnLogicalId: string | undefined;
    readonly ssoInstanceArn: string | undefined;
    readonly accessControlAttributes?: ISsoInstanceACAConfig.AccessControlAttribute[] | undefined;
    constructor(props: ISsoInstanceACAConfig.Props);
    equal(other: SsoInstanceACAConfig): boolean;
}
