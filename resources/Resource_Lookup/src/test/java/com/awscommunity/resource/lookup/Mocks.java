package com.awscommunity.resource.lookup;

import java.util.ArrayList;
import java.util.List;

public final class Mocks {

    private Mocks() {
    }

    public static String getResourcePropertiesMock() {
        return "{\"VpcId\":\"vpc-abcd0123456789abc\",\"InstanceTenancy\":\"default\",\"CidrBlockAssociations\":[\"vpc-cidr-assoc-abcd0123456789abc\"],\"CidrBlock\":\"10.0.0.0/16\",\"DefaultNetworkAcl\":\"acl-abcd0123456789abc\",\"EnableDnsSupport\":true,\"Ipv6CidrBlocks\":[\"2001:db8::/56\"],\"DefaultSecurityGroup\":\"sg-abcd0123456789abc\",\"EnableDnsHostnames\":false,\"Tags\":[{\"Value\":\"contract-test-only-test-team\",\"Key\":\"Owner\"},{\"Value\":\"dev\",\"Key\":\"Env\"}]}";
    }

    public static List<String> getIdentifiersBufferMock(final int maxEntries) {
        final List<String> identifiersBuffer = new ArrayList<String>();

        for (int entryCounter = 0; entryCounter < maxEntries; entryCounter++) {
            identifiersBuffer.add("test" + entryCounter);
        }

        return identifiersBuffer;
    }
}
