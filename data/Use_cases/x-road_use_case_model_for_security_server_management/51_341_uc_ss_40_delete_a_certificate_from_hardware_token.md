### 3.41 UC SS\_40: Delete a Certificate from Hardware Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator deletes a certificate from a
hardware token.

**Preconditions**:

-   The certificate is not saved to system configuration.

-   The hardware token is in logged in state.

**Postconditions**: -

**Trigger**: SS administrator wants to delete a certificate from a
hardware token.

**Main Success Scenario**:

1.  SS administrator selects to delete a certificate from a hardware
    token.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System deletes the certificate from the token.

5.  System logs the event “Delete certificate from token” to the audit
    log.

**Extensions**:

- 3a. SS administrator terminates the use case.

- 4a. The deletion failed (e.g., certification deletion operation is not supported by the token).
    - 4a.1. System displays the error message: “Failed to delete certificate: 'X'”, where “X” is the error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 4a.2. System logs the event “Delete certificate from token failed” to the audit log.
    - 4a.3. Use case terminates.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.