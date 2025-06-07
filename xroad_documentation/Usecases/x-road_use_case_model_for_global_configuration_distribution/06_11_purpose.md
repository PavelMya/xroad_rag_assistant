### 1.1 Purpose

The purpose of this document is to describe:

-   the management of configuration sources in central server and
    security server,

-   the generation and distribution of the global configuration in
    central server and

-   the downloading and verification of the global configuration in
    security server.

This document does not include use cases for

-   the federation of X-Road systems – these use cases are described in
    document “X-Road: Use Case Model for Federation” \[UC-FED\].

-   the functionality of the configuration proxy – these use cases are
    described in document “X-Road: Use Case Model for the Configuration
    Proxy” \[[UC-CP](#Ref_UC-CP)\].

The use cases include verifications that take place, and the main error
conditions that may be encountered during the described process. The
general system errors that may be encountered in most of the use cases
(e.g., database connection errors or out of memory errors) are not
described in this document.

The use cases assume that the X-Road software components involved in the
use cases are installed and initialised (see \[[IG-CS](#Ref_IG-CS)\] and \[[IG-SS](#Ref_IG-SS)\]).

The use cases including a human actor (the *level* of the use case is
*user task*) assume, that the actor is logged in to the system and has
the access rights required to carry out the use case.

### 1.2 Terms and Abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].