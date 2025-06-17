#### 2.2.10 UC GCONF\_10: Log Out of a Hardware Security Token

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator logs out of a hardware security
token.

**Preconditions**:

-   The hardware security token is holding one or more configuration
    signing keys.

-   The hardware security token is logged in to.

**Postconditions**:

-   The system cannot use the keys on the token for signing
    configuration.

-   An audit log record for the event has been created.

**Trigger**: CS administrator wishes to log out of a software security
token.

**Main Success Scenario**:

1.  CS administrator selects to log out of a security token.

2.  System logs out of the token.

3.  System logs the event “Log out from token” to the audit log.

**Extensions**:

- 2a. The logout attempt failed (e.g., token is inaccessible).
    - 2a.1. System displays the error message: “Logout failed: X”, where “X” is the error code from the PKCS \#11 cryptographic token interface \[PKCS11\].
    - 2a.2. System logs the event “Log out from token failed” to the audit log.
    - 2a.3. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].