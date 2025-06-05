### 1.1 Purpose

The purpose of this document is to describe the management of the
security server including:

-   the management of the graphical user interface;

-   the management of timestamping services,

-   the management of the security server's internal TLS certificate,

-   the management of keys and certificates and

-   the backing up and restoring the security server configuration.

The use cases include verifications that take place, and the main error
conditions that may be encountered during the described process. The
general system errors that may be encountered in most of the use cases
(e.g., database connection errors or out of memory errors) are not
described in this document.

The use cases assume that the X-Road software components involved in the
use cases are installed and initialised (see \[[IG-SS](#Ref_IG-SS)\]).

The use cases including a human actor (the *level* of the use case is
*user task*) assume, that the actor is logged in to the system and has
the access rights required to carry out the use case.