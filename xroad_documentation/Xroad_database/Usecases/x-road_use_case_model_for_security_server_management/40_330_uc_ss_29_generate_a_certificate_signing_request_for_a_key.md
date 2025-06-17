### 3.30 UC SS\_29: Generate a Certificate Signing Request for a Key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator generates a certificate signing
request for a key and saves the request file to the local file system.
The token, key (if not already saved to the system configuration) and a
notice about the certificate signing request is saved to the system
configuration.

**Preconditions**: The key is accessible for the system. The token
holding the key is in logged in state.

**Postconditions**: -

**Trigger**: SS administrator wants to generate a certificate signing
request.

**Main Success Scenario**:

1.  SS administrator selects to generate a certificate signing request
    for a key.

2.  SS administrator

    -   selects the intended usage of the certificate (signing or
        authentication) if the usage of the key the CSR is generated for
        has not been assigned before,

    -   selects the security server client the certificate will be
        issued for (only for signing certificates) from the list of this
        security server's clients,

    -   selects the certification service from the list of approved
        certification services that will issue the certificate and

    -   selects the format of the certificate signing request (PEM or
        DER).

3.  System uses the certificate profile info class described for the
    selected CA to display the subject distinguished name fields of the
    CSR, prefilling the values available for the system.

4.  User inserts the values of the subject distinguished name that were
    not prefilled by the system.

5.  System parses the user input: 3.42.

6.  System generates the certificate signing request and prompts the
    request file for downloading.

7.  System verifies, that information of the token holding the key the
    CSR was generated for has not been previously saved to the system
    configuration and saves the token information.

8.  System verifies, that the key the CSR was generated for has not been
    previously saved to the system configuration and saves the key
    information, assigning the key usage according to the certificate
    usage selected for the generated CSR.

9.  System saves a notice about the generated CSR to the system
    configuration.

10. System logs the event “Generate CSR” to the audit log.

11. SS administrator saves the CSR file to the local file system.

**Extensions**:

- 4a. All the required fields of the distinguished name are prefilled by the system. Use case continues from step 6.

- 4b. SS administrator cancels the generation of the CSR. Use case terminates.

- 5a. The process of parsing the user input terminated with an error message.
    - 5a.1. System displays the termination message from the parsing process.
    - 5a.2. System logs the event “Generate CSR failed” to the audit log.
    - 5a.3. SS administrator selects to reinsert the distinguished name. Use case continues form step 5.
        - 5a.3a. SS administrator selects to terminate the use case.

- 6a. The generation of the CSR failed (e.g., token is inaccessible).
    - 6a.1. System displays the error message describing the encountered error. If the key which the CSR was to be generated for is stored on a hardware token, then the error message might be an error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 6a.2. System logs the event “Generate CSR failed” to the audit log.
    - 6a.3. Use case terminates.

- 7a. The token information is already saved in the system configuration. Use case continues from step 8.

- 8a. The key information is already saved in the system configuration. Use case continues from step 9.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.

-   The filename of the CSR is in the following format:
    &lt;usage&gt;\_csr\_&lt;date&gt;\_&lt;identifier&gt;.pem/.der. For
    an authentication certificate signing request the identifier of the
    security server the CSR was generated for in the format
    securityserver\_&lt;*instance identifier&gt;\_&lt;owner
    class&gt;\_&lt;owner code&gt;\_&lt;security server code&gt;*; for a
    signing certificate signing request the identifier of the X-Road
    member the CSR was generated for in the format member\_&lt;*instance
    identifier&gt;\_&lt;member class&gt;\_&lt;member code&gt;*.