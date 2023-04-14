/**
 * This resource uses the `ListResources` and `GetResource` actions of AWS Cloud
 * Control API to perform a lookup of a resource of a given type (such as,
 * `AWS::EC2::VPC`) in your AWS account -and current region if you are using a
 * regional AWS service- based on a query you specify. If only one match is
 * found, this resource returns the primary identifier of the resource (in the
 * `AWS::EC2::VPC` example, the ID of the VPC), that you can then consume by
 * referencing it in your template with the `Fn::GetAtt` intrinsic function.
 * Note: as this resource type uses Cloud Control API, you can specify resource
 * type search targets -like `AWS::EC2::VPC`- that are supported by Cloud
 * Control API; for more information, see `Determining if a resource type
 * supports Cloud Control API`:
 * https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-types.html#resource-types-determine-support
 * .
 */
package com.awscommunity.resource.lookup;
