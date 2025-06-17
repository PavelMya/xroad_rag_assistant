### 6.3 X-Road external components

**Adapter Service** – converts a request or response query to X-Road Message Protocol for SOAP or X-Road Message Protocol for REST. 

**Information system** – a system including technological as well as organizational information processing of a member of X-Road. The information system (IS) uses and/or provides services via the X-Road.

**Subsystem** – represents a part of an X-Road member's information system. X-Road members must declare parts of its information system as subsystems to use or provide X-Road services.

-   The access rights of an X-Road members’ subsystems are independent – access rights given to one subsystem do not affect the access rights of the members’ other subsystems.

-   Services provided by a subsystem are independent of the services provided by the members’ other subsystems.

-   To sign the messages sent by a subsystem when using or providing X-Road services, the signing certificate of the member that manages the subsystem is used. An X-Road member can associate several different subsystems with one security server, and one subsystem can be associated with several security servers.

### 6.4 Elements of X-Road software