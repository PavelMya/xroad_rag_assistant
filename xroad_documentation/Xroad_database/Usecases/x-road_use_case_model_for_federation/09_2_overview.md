## 2 Overview

The trust federation of X-Road instances allows for the members of one
X-Road instance to use the services provided by members of the other
instance, thus making the X-Road systems interoperable.

To make the federating systems aware of each other, the external
configuration anchor of the federation partner must be uploaded as a
trusted anchor to the central servers of the federating X-Road
instances.

The trusted anchors are distributed to the security servers as a part of
the internal configuration. The security servers use the trusted anchors
to download external configuration from the federation partners. The
external configuration contains the information that the security
servers of the partner instances need to communicate with each other.

To end a federation relationship with an X-Road instance, the trusted
anchor of that instance must be deleted from the central server.

For more information on configuration distribution please see the
documents “X-Road: Protocol for Downloading Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\]
and “X-Road: Use Case Model for Global Configuration Distribution”
\[[UC-GCONF](#Ref_UC-GCONF)\].

## 3 Use Case Model