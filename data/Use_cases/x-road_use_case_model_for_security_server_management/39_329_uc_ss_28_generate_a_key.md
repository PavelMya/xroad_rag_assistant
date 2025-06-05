### 3.29 UC SS\_28: Generate a Key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator generates a key on a security
token.

**Preconditions**: The token is in logged in state.

**Postconditions**: -

**Trigger**: SS administrator wants to generate a key on a security
token.

**Main Success Scenario**:

1.  SS administrator selects to generate a key on a security token.

2.  System prompts for the label of the key.

3.  SS administrator inserts the label value (not required, may be left
    blank).

4.  System parses the user input: 3.42.

5.  SS administrator

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

6.  System uses the certificate profile info class described for the
    selected CA to display the subject distinguished name fields of the
    CSR, prefilling the values available for the system.

7.  User inserts the values of the subject distinguished name that were
    not prefilled by the system.

8.  System parses the user input: 3.42.

9.  SS administrator either

    -   selects to cancel the key creation: process aborted
    
    -   selects to generate the key creation: process continue to step 10

10.  System generates a key with the inserted label on the token.

11.  System verifies, that information of the token holding the key the
    CSR was generated for has not been previously saved to the system
    configuration and saves the token information.

12.  System verifies, that the key the CSR was generated for has not been
    previously saved to the system configuration and saves the key
    information, assigning the key usage according to the certificate
    usage selected for the generated CSR.

13.  System saves a notice about the generated CSR to the system
    configuration.

14. System logs the event “Generate CSR” to the audit log.

15.  System generates the certificate signing request and prompts the
    request file for downloading.

16. SS administrator saves the CSR file to the local file system.


**Extensions**:

- 4a. The process of parsing the user input terminated with an error message.
    - 4a.1. System displays the termination message from the parsing process.
    - 4a.2. System logs the event “Generate key failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the label. Use case continues form step 2.
    - 4a.3a. SS administrator selects to terminate the use case.
    
- 8a. The process of parsing the user input terminated with an error message.
    - 8a.1. System displays the termination message from the parsing process.
    - 8a.2. System logs the event “Generate CSR failed” to the audit log.
    - 8a.3. SS administrator selects to reinsert the distinguished name. Use case continues form step 5.
        - 5a.3a. SS administrator selects to terminate the use case.

- 10a. The generation of the key failed (e.g., token is inaccessible).
    - 10a.1. System displays the error message describing the encountered error. If the key generation failed on a hardware token, then the error message is an error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 10a.2. System logs the event “Generate key failed” to the audit log.
    - 10a.3. Use case terminates.

- 15a. The generation of the CSR failed (e.g., token is inaccessible).
    - 15a.1. System displays the error message describing the encountered error. If the key which the CSR was to be generated for is stored on a hardware token, then the error message might be an error code from the PKCS \#11 cryptographic token interface (see \[PKCS11\]).
    - 15a.2. System logs the event “Generate CSR failed” to the audit log.
    - 15a.3. Use case terminates.


**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].