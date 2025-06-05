### 1.1 Purpose

The purpose of this document is to describe:

-   the management of X-Road members and security servers in the central server and

-   the management of security server clients in the security server.

This document does not include

-   use cases for service and access right management – these use cases are described in the document “X-Road: Use Case Model for Service Management” \[[UC-SERVICE](#Ref_UC-SERVICE)\];

-   use cases for security token, key and certificate management in the security server – these use cases are described in the document “X-Road: Use Case Model for Security Server Management” \[[UC-SS](#Ref_UC-SS)\].

The use cases include verifications that take place, and the main error conditions that may be encountered during the described process. The general system errors that may be encountered in most of the use cases (e.g., database connection errors or out of memory errors) are not described in this document.

The use cases assume that the X-Road software components involved in the use cases are installed and initialised (see \[[IG-CS](#Ref_IG-CS)\] and \[[IG-SS](#Ref_IG-SS)\]).

The use cases including a human actor (the *level* of the use case is *user task*) assume that the actor is logged in to the system and has the access rights required to carry out the use case.