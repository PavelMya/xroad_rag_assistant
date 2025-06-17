## 1 Introduction

The purpose of this document is to describe the general central server
use cases that do not fall under any of the following topics.

-   The use cases for global configuration management and distribution
    are described in the document “X-Road: Use Case Model for Global
    Configuration Distribution” \[[UC-GCONF](#Ref_UC-GCONF)\].

-   The use cases for federating X-Road instances are described in the
    document “X-Road: Use Case Model for Federation” \[UC-FED\].

-   The use cases for the management of X-Road members and security
    servers are described in the document “X-Road: Use Case Model for
    Member Management” \[[UC-MEMBER](#Ref_UC-MEMBER)\].

-   The use cases for the management of global groups and central
    services are described in the document “X-Road: Use Case Model for
    Service Management” \[[UC-SERVICE](#Ref_UC-SERVICE)\].

-   The use cases for the management of certification services and
    timestamping services are described in the document “X-Road: Use
    Case Model for Trust Service Management” \[[UC-TRUST](#Ref_UC-TRUST)\].

The use cases include verifications that take place, and the main error
conditions that may be encountered during the described process. The
general system errors that may be encountered in most of the use cases
(e.g., database connection errors or out of memory errors) are not
described in this document.

The use cases assume that the X-Road software components involved in the
use cases are installed and initialised (see \[[IG-CS](#Ref_IG-CS)\]).

The use cases (except for 2.2) including a human actor (the *level* of
the use case is *user task*) assume that the actor is logged in to the
system and has the access rights required to carry out the use case.

### 1.1 Terms and Abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].