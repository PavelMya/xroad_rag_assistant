### 3.36 UC SS\_35: Delete a Key from the System Configuration and from a Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator deletes a key including the
associated certificates and/or certificate signing request notices, if
there are any, from the system configuration, and from a token.

**Preconditions**: Information about the key is saved in the system
configuration.

**Postconditions**: -

**Trigger**: SS administrator wants to delete a key.

**Main Success Scenario**:

1.  SS administrator selects to delete a key from the system
    configuration.

2.  System checks whether the key is associated with authentication certificates that have
    registration state “registered” or “registration in progress”
    imported for the key and if so, prompts for confirmation to continue with
    unregistration and deletion of associated certificates, certificate signing request notices, and the key.

3.  SS administrator confirms the unregistration and deletion actions.

4.  System unregisters each of the authentication certificates: see
    3.43.

5.  System deletes the key and the associated certificates and/or
    certificate signing request notices from system configuration and from token.

6.  System logs the event “Delete key from token and configuration” to the audit
    log.

**Extensions**:

- 2a. There are no authentication certificates that have registration state “registered” or “registration in progress” imported for the key.
    - 2a.1. System prompts for confirmation of deletion.
    - 2a.2. SS administrator confirms.
        - 2a.2a. SS administrator terminates the use case.
    - 2a.3. Use case continues from step 5.

- 3a. SS administrator terminates the use case.

- 4a. The process of unregistering authentication certificates terminated with an error message.
    - 4a.1. System displays the message: “Failed to delete key: X”, where “X” is the termination message from the unregistration process.
    - 4a.2. System logs the event “Delete key failed” to the audit log.
    - 4a.3. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.