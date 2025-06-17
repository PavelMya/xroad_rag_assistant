### 3.7 UC CP\_06: Log In to a Hardware Security Token

**System**: Configuration proxy

**Level**: User task

**Component:** Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator logs in to a hardware token by
entering the token PIN code.

**Preconditions**:

-   The hardware security token is initialized and connected to the
    system.

-   The token has not been logged in to.

**Postconditions**: -

**Trigger**: CP administrator wishes to make the functionality of the
token available to the system.

**Main Success Scenario**:

1.  CP administrator selects log in to a hardware security token holding
    a configuration signing key.

2.  CP administrator inserts the token PIN code.

3.  System verifies that the token is not locked.

4.  System verifies that the inserted PIN code is correct and logs in to
    the token.

**Extensions**:

- 3-4a. The login attempt failed (e.g., incorrect PIN was inserted, token is inaccessible).
    - 3-4a.1. System displays the error message: “Login failed: X”, where “X” is the error code from the PKCS \#11 cryptographic token interface (see \[[PKCS11](#Ref_PKCS11)\]) and terminates the use case.

**Related information**: -