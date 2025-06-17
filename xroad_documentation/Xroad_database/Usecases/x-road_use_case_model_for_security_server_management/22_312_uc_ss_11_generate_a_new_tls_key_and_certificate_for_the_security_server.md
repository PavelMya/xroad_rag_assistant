### 3.12 UC SS\_11: Generate a New TLS Key and Certificate for the Security Server

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator generates a TLS key
and respective self-signed certificate for the security server.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to change the key and certificate
used for TLS connections with the client information systems.

**Main Success Scenario**:

1.  SS administrator selects to generate a new TLS key.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System generates and saves the new TLS key and the respective
    self-signed certificate, replacing the existing key and certificate
    (if such exist) with the new ones.

5.  System calculates the SHA-1 hash value of the certificate (for
    displaying in the GUI).

6.  System logs the event “Generate new internal TLS key and
    certificate” to the audit log.

7. SS administrator selects to generate a new TLS certificate request.

8. System prompts for defining a Distinguished name.

9. SS administrator inserts a Distinguished name.

10. System prompts a request to download the generated certificate request.

11. The security server generates a certificate request using the current key and the provided Distinguished Name.

12. SS administrator downloads and saves the certificate request file to the local file system.

13. After a Certification Authority has issued a TLS certificate, SS administrator imports and saves the certificate file to the local file system.

**Extensions**:

- 3a. SS administrator cancels the generating of the new TLS key.
    - 3a.1. Use case terminates.

- 4a. System failed to generate the key or the respective self-signed certificate.
    - 4a.1. System displays an error message “Failed to generate new key: 'X'” (where “X” is the reason of the failure). Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].