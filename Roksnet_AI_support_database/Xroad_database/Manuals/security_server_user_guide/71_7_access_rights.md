## 7 Access Rights

Access rights can be granted to the following access right subjects.

-   **An X-Road member's subsystem.**

-   **A global access rights group.** Global groups are created in the X-Road governing authority. If a group is granted an access right, it extends to all group members.

-   **A local access rights group.** To simplify access rights management, each client in the Security Server can create local access rights groups (see section [8](#8-local-access-right-groups)). If a group is granted an access right, it extends to all group members.

There are two options for managing access rights in a Security Server.

-   Service-based access rights management – if a single service needs to be opened/closed to multiple service clients (see [7.1](#71-changing-the-access-rights-of-a-service)).

-   Service client-based access rights management – if a single service client needs multiple services opened/closed (see [7.2](#72-adding-a-service-client)).

It is possible to define access rights on two levels for REST services:

-   REST service level
-   endpoint level

In general, a REST service usually has multiple endpoints. When access rights are defined on the service level, they apply to all the endpoints of the REST service. Instead, defining access rights on the endpoint level gives access to specific endpoint(s) only. The service level access rights support both service-based and service client-based access rights management. The endpoint level access rights support only service based access rights management.