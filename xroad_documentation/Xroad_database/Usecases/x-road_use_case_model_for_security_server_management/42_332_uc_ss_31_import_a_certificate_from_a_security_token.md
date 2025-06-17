### 3.32 UC SS\_31: Import a Certificate from a Security Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator imports a certificate from a
security token.

**Preconditions**: -

**Postconditions**: An audit log record for the event is created.

**Trigger**: SS administrator wants to import a certificate from the
security token.

**Main Success Scenario**:

1.  SS administrator selects to import a certificate from a security
    token.

2.  System verifies that the global configuration is not expired.

3.  System verifies that the imported certificate is a signing
    certificate and uses the identifier decoder described for the
    certification service that issued the certificate to decode the
    X-Road identifier of the security server client the certificate was
    issued for.

4.  System verifies that the member, whom the certificate is issued to,
    is the owner of the security server or has a subsystem registered as
    a client of the security server.

5.  System verifies that the private key, associated with the public key
    in the certificate, is not deleted from token.

6.  System verifies that this certificate is not already saved in the
    system configuration.

7.  System verifies that certificate usage is in accordance with the key
    usage.

8.  System verifies that the certificate is issued by an approved
    certification service by confirming that the issuer is listed in the
    global configuration.

9.  System verifies that the certificate is not expired.

10. System verifies that the usage of the key is defined and saves the
    certificate to the system configuration.

11. System sets the registration state of the signing certificate to
    “registered”.

12. System gets the OCSP response for the imported certificate (see UC
    MESS\_15 \[[UC-MESS](#Ref_UC-MESS)\] for details).

13. System verifies that a certificate signing request notice
    corresponding to the imported certificate exists in the system
    configuration and deletes the certificate signing request
    information.

14. System logs the event “Import certificate from token” to the audit
    log.

**Extensions**:

- 2a. Global configuration is expired.
    - 2a.1. System displays the error message “Global configuration is expired”.
    - 2a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 2a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 2a.3a. SS administrator selects to terminate the use case.

- 3a. Identifier decoder encountered an error.
    - 3a.1. System displays the error message describing the encountered error.
    - 3a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 3a.3. SS administrator selects to reselect the file. Use case continues from step 3.
       - 3a.3a. SS administrator selects to terminate the use case.

- 3b. The imported certificate is an authentication certificate. Use case continues from step 5.

- 4a. The member, whom the certificate is issued to, is not a client of the security server.
    - 4a.1. System displays the error message “Failed to import certificate: Certificate issued to an unknown member 'X'” (where “X” is the identifier of the member).
    - 4a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 4a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. System could not find key corresponding to the certificate.
    - 5a.1. System displays the error message “Failed to import certificate: Could not find key corresponding to the certificate.”.
    - 5a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 5a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 5a.3a. SS administrator selects to terminate the use case.

- 6a. The certificate already exists under the key.
    - 6a.1. System displays the error message “Failed to import certificate: Certificate already exists under key 'X'” (where “X” is the friendly name of the key).
    - 6a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 6a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 6a.3a. SS administrator selects to terminate the use case.

- 7a. SS administrator tried to import an authentication certificate for a signing key.
    - 7a.1. System displays the error message “Failed to import certificate: Authentication certificate cannot be imported to signing keys”.
    - 7a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 7a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 7a.3a. SS administrator selects to terminate the use case.

- 7b. SS administrator tried to import a signing certificate for an authentication key.
    - 7b.1. System displays the error message “Failed to import certificate: 'X'” (where 'X' is the reason of the failure).
    - 7b.2. System logs the event “Import certificate from token failed” to the audit log.
    - 7b.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 7b.3a. SS administrator selects to terminate the use case.

- 7c. The usage of the key is undefined.
    - 7c.2. Use case continues from step 8.

- 8a. SS administrator tried to import a certificate that is not issued by an approved certification service.
    - 8a.1. System displays the error message “Failed to import certificate: Certificate is not issued by approved certification service provider.”.
    - 8a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 8a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 8a.3a. SS administrator selects to terminate the use case.

- 9a. The certificate is expired.
    - 9a.1. System displays the error message “Failed to import certificate: Certificate is not valid”.
    - 9a.2. System logs the event “Import certificate from token failed” to the audit log.
    - 9a.3. SS administrator selects to reselect the file. Use case continues from step 3.
        - 9a.3a. SS administrator selects to terminate the use case.

- 10a. The usage of the key is undefined.
    - 10a.1. System assigns the usage of the key according to the usage of the imported certificate and saves the certificate to the system configuration.
    - 10a.2. Use case continues from step 11.

- 11a. The imported certificate is an authentication certificate.
    - 11a.1. System sets the certificate to disabled state and sets the registration state to “saved”.
    - 11a.2. Use case continues from step 12.

- 13a. No certificate signing request notice corresponding to the imported certificate exist in the system configuration. Use case continues from step 14.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.