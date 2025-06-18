## 12 Trust Federation

The trust federation of X-Road instances allows for the members of one X-Road instance to use the services provided by members of the other instance, thus making the X-Road systems interoperable.

To make the federating systems aware of each other, the external configuration anchor of the federation partner must be uploaded as a trusted anchor to the Central Servers of the federating X-Road instances.

The trusted anchors are distributed to the Security Servers as a part of the internal configuration. The Security Servers use the trusted anchors to download external configuration from the federation partners. The external configuration contains the information that the Security Servers of the partner instances need to communicate with each other.

To end a federation relationship with an X-Road instance, the trusted anchor of that instance must be deleted from the Central Server.

For further information on X-Road Trust Federation, refer to \[[UC-FED](#Ref_UC-FED)\].