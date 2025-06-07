### 3.27 UC SS\_26: Log Out of a Software Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator logs out of a software token.

**Preconditions**: The token is in logged in state.

**Postconditions**: The token in logged out state. The system cannot use
the keys and certificates on the token.

**Trigger**: SS administrator wants to log out of a software token.

**Main Success Scenario**:

1.  SS administrator selects to log out of a software token.

2.  System logs out of the token.

3.  System logs the event “Log out from token” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.