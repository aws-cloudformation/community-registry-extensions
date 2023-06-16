# AwsCommunity::Lambda::Invoker

## Activation

To activate a hook in your account, use the following JSON as the `Configuration` request parameter for [`SetTypeConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) API request.

### Configuration

<pre>
{
    "CloudFormationConfiguration": {
        "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-hook-configuration" title="HookConfiguration">HookConfiguration</a>": {
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">TargetStacks</a>":  <a href="#footnote-1">"ALL" | "NONE"</a>,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>": <a href="#footnote-1">"FAIL" | "WARN"</a> ,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-properties" title="Properties">Properties</a>" : {
                "<a href="#registrationtablearn" title="RegistrationTableArn">RegistrationTableArn</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### RegistrationTableArn

Arn for the DynamoDB table that will hold the list of Lambda functions to invoke. The table must have a partition key called 'pk', and sort key called 'sk'. Entries should have a single additional attribute called 'lambda_arn'. You must create the table as a prerequisite to installing this hook.

_Required_: No

_Type_: String


---

## Targets

* `AWS::EC2::CapacityReservation`
* `AWS::EC2::CapacityReservationFleet`
* `AWS::EC2::CarrierGateway`
* `AWS::EC2::ClientVpnAuthorizationRule`
* `AWS::EC2::ClientVpnEndpoint`
* `AWS::EC2::ClientVpnRoute`
* `AWS::EC2::ClientVpnTargetNetworkAssociation`
* `AWS::EC2::CustomerGateway`
* `AWS::EC2::DHCPOptions`
* `AWS::EC2::EC2Fleet`
* `AWS::EC2::EIP`
* `AWS::EC2::EIPAssociation`
* `AWS::EC2::EgressOnlyInternetGateway`
* `AWS::EC2::EnclaveCertificateIamRoleAssociation`
* `AWS::EC2::FlowLog`
* `AWS::EC2::GatewayRouteTableAssociation`
* `AWS::EC2::Host`
* `AWS::EC2::IPAM`
* `AWS::EC2::IPAMAllocation`
* `AWS::EC2::IPAMPool`
* `AWS::EC2::IPAMPoolCidr`
* `AWS::EC2::IPAMResourceDiscovery`
* `AWS::EC2::IPAMResourceDiscoveryAssociation`
* `AWS::EC2::IPAMScope`
* `AWS::EC2::Instance`
* `AWS::EC2::InternetGateway`
* `AWS::EC2::KeyPair`
* `AWS::EC2::LaunchTemplate`
* `AWS::EC2::LocalGatewayRoute`
* `AWS::EC2::LocalGatewayRouteTable`
* `AWS::EC2::LocalGatewayRouteTableVPCAssociation`
* `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation`
* `AWS::EC2::NatGateway`
* `AWS::EC2::NetworkAcl`
* `AWS::EC2::NetworkAclEntry`
* `AWS::EC2::NetworkInsightsAccessScope`
* `AWS::EC2::NetworkInsightsAccessScopeAnalysis`
* `AWS::EC2::NetworkInsightsAnalysis`
* `AWS::EC2::NetworkInsightsPath`
* `AWS::EC2::NetworkInterface`
* `AWS::EC2::NetworkInterfaceAttachment`
* `AWS::EC2::NetworkInterfacePermission`
* `AWS::EC2::NetworkPerformanceMetricSubscription`
* `AWS::EC2::PlacementGroup`
* `AWS::EC2::PrefixList`
* `AWS::EC2::Route`
* `AWS::EC2::RouteTable`
* `AWS::EC2::SecurityGroup`
* `AWS::EC2::SecurityGroupEgress`
* `AWS::EC2::SecurityGroupIngress`
* `AWS::EC2::SpotFleet`
* `AWS::EC2::Subnet`
* `AWS::EC2::SubnetCidrBlock`
* `AWS::EC2::SubnetNetworkAclAssociation`
* `AWS::EC2::SubnetRouteTableAssociation`
* `AWS::EC2::TrafficMirrorFilter`
* `AWS::EC2::TrafficMirrorFilterRule`
* `AWS::EC2::TrafficMirrorSession`
* `AWS::EC2::TrafficMirrorTarget`
* `AWS::EC2::TransitGateway`
* `AWS::EC2::TransitGatewayAttachment`
* `AWS::EC2::TransitGatewayConnect`
* `AWS::EC2::TransitGatewayMulticastDomain`
* `AWS::EC2::TransitGatewayMulticastDomainAssociation`
* `AWS::EC2::TransitGatewayMulticastGroupMember`
* `AWS::EC2::TransitGatewayMulticastGroupSource`
* `AWS::EC2::TransitGatewayPeeringAttachment`
* `AWS::EC2::TransitGatewayRoute`
* `AWS::EC2::TransitGatewayRouteTable`
* `AWS::EC2::TransitGatewayRouteTableAssociation`
* `AWS::EC2::TransitGatewayRouteTablePropagation`
* `AWS::EC2::TransitGatewayVpcAttachment`
* `AWS::EC2::VPC`
* `AWS::EC2::VPCCidrBlock`
* `AWS::EC2::VPCDHCPOptionsAssociation`
* `AWS::EC2::VPCEndpoint`
* `AWS::EC2::VPCEndpointConnectionNotification`
* `AWS::EC2::VPCEndpointService`
* `AWS::EC2::VPCEndpointServicePermissions`
* `AWS::EC2::VPCGatewayAttachment`
* `AWS::EC2::VPCPeeringConnection`
* `AWS::EC2::VPNConnection`
* `AWS::EC2::VPNConnectionRoute`
* `AWS::EC2::VPNGateway`
* `AWS::EC2::VPNGatewayRoutePropagation`
* `AWS::EC2::VerifiedAccessEndpoint`
* `AWS::EC2::VerifiedAccessGroup`
* `AWS::EC2::VerifiedAccessInstance`
* `AWS::EC2::VerifiedAccessTrustProvider`
* `AWS::EC2::Volume`
* `AWS::EC2::VolumeAttachment`
* `AWS::Lambda::Alias`
* `AWS::Lambda::CodeSigningConfig`
* `AWS::Lambda::EventInvokeConfig`
* `AWS::Lambda::EventSourceMapping`
* `AWS::Lambda::Function`
* `AWS::Lambda::LayerVersion`
* `AWS::Lambda::LayerVersionPermission`
* `AWS::Lambda::Permission`
* `AWS::Lambda::Url`
* `AWS::Lambda::Version`
* `AWS::S3::AccessPoint`
* `AWS::S3::Bucket`
* `AWS::S3::BucketPolicy`
* `AWS::S3::MultiRegionAccessPoint`
* `AWS::S3::MultiRegionAccessPointPolicy`
* `AWS::S3::StorageLens`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

