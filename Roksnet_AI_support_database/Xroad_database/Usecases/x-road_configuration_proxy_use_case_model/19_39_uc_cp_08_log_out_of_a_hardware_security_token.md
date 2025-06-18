### 3.9 UC CP\_08: Log Out of a Hardware Security Token

**System**: Configuration proxy

**Level**: User task

**Component:** Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator logs out of a hardware security
token.

**Preconditions**: The hardware security token is logged in to.

**Postconditions**: -

**Trigger**: CP administrator wishes to log out of a hardware security
token.

**Main Success Scenario**:

1.  CP administrator selects to log out of a security token.

2.  System logs out of the token.

**Extensions**:

- 2a. The logout attempt failed (e.g., token is inaccessible).
    - 2a.1. System displays the error message: “Logout failed: X”, where “X” is the error code from the PKCS \#11 cryptographic token interface \[[PKCS11](#Ref_PKCS11)\] and terminates the use case.

**Related information**: -