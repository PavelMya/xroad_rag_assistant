#### 2.4.4 UC MEMBER\_47: Add a Client to the Security Server

**System**: Security server

**Level**: User task

**Component**: Security server

**Actor**: SS administrator

**Brief description**: SS administrator adds a client to the security server.

**Precondition**: The desired client does not exist in the Security Server

**Postcondition**: -

**Trigger**: -

**Main success scenario**:

SS administrator selects to add a security server client.

1. SS administrator inserts the parameters of the client (manually or from the Global list).

- System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input);

- System verifies that a client with the inserted identifier does not already exist in the system configuration.

- System verifies that an X-Road member with the inserted identifier exists by looking the member up from the global configuration.

2. If there are two or more security tokens on the Security Server, the SS administrator selects selects the one on which the client is added

3. SS administrator selects to generate a key

- SS administrator inserts the label value (not required, may be left blank)

4. SS administrator selects to generate a certificate signing request for a key

- system prefills the intended usage of the certificate (signing)

- system prefills the security server client the certificate will be issued for

- SS administrator selects the certification service from the list of approved certification services that will issue the certificate and

- SS administrator selects the format of the certificate signing request (PEM or DER)

- System uses the certificate profile info class described for the selected CA to display the subject distinguished name fields of the CSR, prefilling the values available for the system

- User inserts the values of the subject distinguished name that were not prefilled by the system

- System parses the user input: [2.5.1](#251-uc-member_54-parse-user-input)

- System verifies, that information of the token holding the key the CSR was generated for has not been previously saved to the system configuration and saves the token information.

- System verifies, that the key the CSR was generated for has not been previously saved to the system configuration and saves the key information, assigning the key usage according to the certificate usage selected for the generated CSR.

5. SS administrator can:

- abort the operation: the system terminates client, key and certificate generation

- continue the operation: the operation continues to step 6

6. System creates a new key, generates the certificate signing request and prompts the request file for downloading.

- SS administrator saves the CSR file to the local file system

7.  System saves the client to the system configuration and sets the status of the client to *saved*

8. System generates a key with the inserted label on the token

9. System shows the CSR next to related key and sets the status of the certificate to *requested*

10. System logs the event “Generate key” to the audit log.

11. System logs the event “Add client” to the audit log.

**Extensions**:

1a. The parsing of the user input terminated with an error.

  - 1a.1. System displays the termination message of the parsing process.

  - 1a.2. System logs the event “Add client failed” to the audit log.

  - 1a.3. SS administrator selects to reinsert the client identifier. Use case continues from step 1.

    - 1a.3a. SS administrator selects to terminate the use case.
    
1b. SS administrator selected to add new subsystem to an existing member. _Member details are prefilled and are not editable_

  - 1b.1. SS administrator inputs the subsystem code OR

  - 1b.2. SS administrator selects the subsystem code by searching form existing subsystems    

2a. A client with the inserted identifier already exists in the system configuration.

  - 2a.1. System displays the error message: “Client already exists”.

  - 2a.2. System logs the event “Add client failed” to the audit log.

  - 2a.3. SS administrator selects to reinsert the client identifier. Use case continues from step 1.

    - 2a.3a. SS administrator selects to terminate the use case.

3a. An X-Road member with the inserted identifier does not exist.

  - 3a.1. System prompts the message “The person/organisation 'X' is not registered as X-Road member” (where “X” is the entered identifier) and asks for confirmation for continuing.

  - 3a.2. SS administrator selects not to continue and reinserts the client identifier. Use case continues from step 1.

    - 3a.2a. SS administrator selects not to continue and terminates the use case.
    
4a. SS administrator cancels the new client addition. Use case terminates client, key and certificate generation.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The security server client state machine model is described in the document “Security Server User Guide” \[[UG-SS](#Ref_UG-SS)\].

-   Details on generating a key: see UC SS\_28 \[[UC-SS](#Ref_UC-SS)\].

-   Details on generating a CSR: see UC SS\_29 \[[UC-SS](#Ref_UC-SS)\].