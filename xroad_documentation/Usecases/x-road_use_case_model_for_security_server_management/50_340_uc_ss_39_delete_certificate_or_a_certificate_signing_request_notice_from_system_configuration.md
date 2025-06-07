### 3.40 UC SS\_39: Delete Certificate or a Certificate Signing Request Notice from System Configuration

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator deletes a certificate or
certificate signing request notice from the system configuration.

**Preconditions**:

-   Authentication certificates can be deleted if the registration
    status is “saved”, “global error” or “deletion in progress”.

-   The certificate or the certificate signing request notice is saved
    to system configuration.

**Postconditions**: -

**Trigger**: SS administrator wants to delete a certificate or
certificate signing request notice from system configuration.

**Main Success Scenario**:

1.  SS administrator selects to delete a certificate or a certificate
    signing request notice.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System verifies that the key has more certificates and/or
    certificate signing request notices that are saved in system
    configuration and deletes the certificate or CSR from system
    configuration.

5.  System logs the event “Delete certificate from configuration” or
    “Delete CSR”, depending on the deleted object, to the audit log.

**Extensions**:

- 3a. SS administrator terminates the use case.

- 4a. The key has no more certificates and/or certificate signing request notices that are saved in system configuration.
    - 4a.1. System deletes the certificate or CSR and key from system configuration.
    - 4a.2. Use case continues form step 5.

- 4b. The key has no more certificates and/or certificate signing request notices that are saved in system configuration and the token has no more keys that are saved in system configuration.
    - 4b.1. System deletes the certificate or CSR, the key and the token from system configuration.
    - 4b.2. Use case continues form step 5.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.