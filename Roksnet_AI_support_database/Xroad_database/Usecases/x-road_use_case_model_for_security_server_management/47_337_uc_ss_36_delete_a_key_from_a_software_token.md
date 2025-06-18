### 3.37 UC SS\_36: Delete a Key from a Software Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator deletes a key from a software
token.

**Preconditions**: The key information is not saved to the system
configuration.

**Postconditions**: -

**Trigger**: SS administrator wants to delete a key.

**Main Success Scenario**:

1.  SS administrator selects to delete a key.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System deletes the key and associated certificates and certificate signing request notices from token.

5.  System logs the event “Delete key from token and configuration” to the audit log.

**Extensions**:

- 3a. SS administrator terminates the use case.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.