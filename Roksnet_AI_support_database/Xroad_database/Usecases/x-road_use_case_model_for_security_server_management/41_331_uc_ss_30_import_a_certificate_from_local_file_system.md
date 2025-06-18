### 3.31 UC SS\_30: Import a Certificate from Local File System

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator imports a certificate from the
local file system.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to import a certificate from the
local file system.

**Main Success Scenario**:

1.  SS administrator selects to import a certificate file.

2.  SS administrator selects the file from the local file system.

3.  System verifies that the global configuration is not expired.

4.  System verifies that the file is in DER or PEM format.

5.  System verifies that the imported certificate is a signing
    certificate and uses the identifier decoder described for the
    certification service that issued the certificate to decode the
    X-Road identifier of the security server client the certificate was
    issued for.

6.  System verifies that the member, whom the certificate is issued to,
    is the owner of the security server or has a subsystem registered as
    a client of the security server.

7.  System verifies that the private key, associated with the public key
    in the certificate, is not deleted from token.

8.  System verifies that this certificate is not already saved in the
    system configuration.

9.  System verifies that certificate usage is in accordance with the key
    usage.

10. System verifies that the certificate is issued by an approved
    certification service by confirming that the issuer is listed in the
    global configuration.

11. System verifies that the certificate is not expired.

12. System verifies that the usage of the key is defined and saves the
    certificate to the system configuration.

13. System sets the registration state of the signing certificate to
    “registered”.

14. System gets the OCSP response for the imported certificate (see UC
    MESS\_15 \[UC-MESS\] for details).

15. System verifies that a certificate signing request notice
    corresponding to the imported certificate exists in the system
    configuration and deletes the certificate signing request
    information.

16. System logs the event “Import certificate from file” to the audit
    log.

**Extensions**:

- 3a. Global configuration is expired.
    - 3a.1. System displays the error message “Global configuration is expired”.
    - 3a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 3a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The file is not in valid format.
    - 4a.1. System displays the error message “Failed to import certificate: Incorrect file format. Only PEM and DER files allowed.”.
    - 4a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 4a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. Identifier decoder encountered an error.
    - 5a.1. System displays the error message describing the encountered error.
    - 5a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 5a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 5a.3a. SS administrator selects to terminate the use case.

- 5b. The imported certificate is an authentication certificate. Use case continues from step 7.

- 6a. The member, whom the certificate is issued to, is not a client of the security server.
    - 6a.1. System displays the error message “Failed to import certificate: Certificate issued to an unknown member 'X'” (where “X” is the identifier of the member).
    - 6a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 6a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 6a.3a. SS administrator selects to terminate the use case.

- 7a. System could not find key corresponding to the certificate
    - 7a.1. System displays the error message “Failed to import certificate: Could not find key corresponding to the certificate.”.
    - 7a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 7a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 7a.3a. SS administrator selects to terminate the use case.

- 8a. The certificate already exists under the key.
    - 8a.1. System displays the error message “Failed to import certificate: Certificate already exists under key 'X'” (where “X” is the friendly name of the key).
    - 8a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 8a.3. SS administrator selects to reselect the file. Use case continues from step 3.
    - 8a.3a. SS administrator selects to terminate the use case.

- 9a. SS administrator tried to import an authentication certificate for a signing key.
    - 9a.1. System displays the error message “Failed to import certificate: Authentication certificate cannot be imported to signing keys”.
    - 9a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 9a.3. SS administrator selects to reselect the file. Use case continuesfrom step 3.
        - 9a.3a. SS administrator selects to terminate the use case.

- 9b. SS administrator tried to import a signing certificate for an authentication key.
    - 9b.1. System displays the error message “Failed to import certificate: 'X'” (where 'X' is the reason of the failure).
    - 9b.2. System logs the event “Import certificate from token failed” to the audit log.
    - 9b.3. SS administrator selects to reselect the file. Use case continues from step 3.
    - 9b.3a. SS administrator selects to terminate the use case.
    
- 9c. The usage of the key is undefined.
    - 9c.2. Use case continues from step 10.

- 10a. SS administrator tried to import a certificate that is not issued by an approved certification service.
    - 10a.1. System displays the error message “Failed to import certificate: Certificate is not issued by approved certification service provider.”.
    - 10a.2. System logs the event “Import certificate from file failed” tothe audit log.
    - 10a.3. SS administrator selects to reselect the file. Use case continuesfrom step 3.
        - 10a.3a. SS administrator selects to terminate the use case.

- 11a. The certificate is expired.
    - 11a.1. System displays the error message “Failed to import certificate: Certificate is not valid”.
    - 11a.2. System logs the event “Import certificate from file failed” to the audit log.
    - 11a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 11a.3a. SS administrator selects to terminate the use case.

- 13a. The usage of the key is undefined.
    - 13a.1. System assigns the usage of the key according to the usage of the imported certificate and saves the certificate to the system configuration.
    - 13a.2. Use case continues from step 14.

- 14a. The imported certificate is an authentication certificate.
    - 14a.1. System sets the certificate to disabled state and sets the registration state to “saved”.
    - 14a.2. Use case continues from step 15.

- 15a. No certificate signing request notice corresponding to the imported certificate exist in the system configuration. Use case continues from step 16.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.