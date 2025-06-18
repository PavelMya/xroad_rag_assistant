### 3.28 UC SS\_27: Log Out of a Hardware Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator logs out of a hardware token.

**Preconditions**: The token is in logged in state.

**Postconditions**: The token is in logged out state. The system cannot
use the keys and certificates on the token.

**Trigger**: SS administrator wants to log out of a hardware token.

**Main Success Scenario**:

1.  SS administrator selects to log out of a hardware token.

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

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.