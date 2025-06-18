#### 2.2.9 UC GCONF\_09: Log Out of a Software Security Token

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator logs out of a software security
token.

**Preconditions**:

-   The software security token is holding one or more configuration
    signing keys.

-   The software security token is in logged in state.

**Postconditions**:

-   The token is in logged out state.

-   The system cannot use the keys on the token for signing
    configuration.

-   An audit log record for the event has been created.

**Trigger**: CS administrator wishes to log out of a software security
token.

**Main Success Scenario**:

1.  CS administrator selects to log out of a token.

2.  System logs out of the token.

3.  System logs the event “Log out from token” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].