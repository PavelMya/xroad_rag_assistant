### 3.39 UC SS\_38: Unregister an Authentication Certificate

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator, management service's security server

**Brief Description**: SS administrator unregisters a registered
authentication certificate.

**Preconditions**: The registration status of the authentication
certificate is “registered” or “registration in progress”.

**Postconditions**: -

**Trigger**:

-   SS administrator wants to unregister the registered authentication
    certificate.

-   SS administrator wants to delete a key from the system
    configuration.

**Main Success Scenario**:

1.  SS administrator selects to unregister an authentication
    certificate.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System verifies that there is a valid authentication certificate for
    the security server.

5.  System creates an X-Road SOAP request containing the authentication
    certificate deletion request for the certificate. The contents of
    the request is described in \[PR-MSERV\].

6.  System sends the request to the management services' security
    server: see UC MESS\_02 \[UC-MESS\], where this system acts as both
    the Client IS and the System; the owner of this security server acts
    as the service client; and the central server acts as the Provider
    IS.

7.  System receives the response from the management services' security
    server and verifies that the response is not an error message.

8.  System displays the message “Request sent” to the SS administrator.

9.  System sets the registration status of the authentication
    certificate to “deletion in progress”.

10. System logs the event “Unregister authentication certificate” to the
    audit log.

**Extensions**:

- 3a. SS administrator terminates the use case.

- 4a. There is no valid authentication certificate for the security server.
    - 4a.1. System displays the error message “Failed to unregister certificate: Security server has no valid authentication certificate”
    - 4a.2. System logs the event “Unregister authentication certificate failed” to the audit log.
    - 4a.3. Use case terminates.

- 5-7a. The creating or sending of the deletion request failed, or the response was an error message.
    - 5-7a.1. System displays the warning message: “Failed to send certificate deletion request. Continue with certificate deletion anyway?” and the error message “Failed to unregister certificate: 'X'”, where “X” is the description of the encountered error, and prompts for confirmation.
    - 5-7a.2. System logs the event “Unregister authentication certificate failed” to the audit log.
    - 5-7a.3. SS administrator confirms.
        - 5-7a.3a. SS administrator terminates the use case.
    - 5-7a.4. System sets the registration status of the authentication certificate to “deletion in progress”.
    - 5-7a.5. System logs the event “Skip unregistration of authentication certificate” to the audit log.
    - 5-7a.6. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.