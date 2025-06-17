### 3.4 UC MESS\_03: Process X-Road Request Message

**System**: Service provider's security server

**Level**: System

**Component**: Security server

**Actors**:

-   Client SS

-   Provider IS

**Brief Description**:

The system receives a communication request from Client SS; verifies that the system configuration allows X-Road message exchange; establishes a secure connection session with the Client SS; receives the X-Road service request; verifies the signature of the request; logs the request message and signature to the message log; forwards the request message to the Provider IS or to operational monitoring daemon (if the request is either operational monitoring data request or security server health data request) and waits for the response. Upon receiving the response from the Provider IS, system verifies that the response message composition conforms to the X-Road message protocol; signs the response message; logs the response message and signature to the message log and forwards the message and the signature to the Client SS. In case a verification or a validation fails or when the system encounters an error condition, the system sends a SOAP Fault message to the Client SS.

**Preconditions**:

-   Service provider's security server is running and able to receive messages.

**Postcondition**: -

**Trigger**: The service client's security server sends an X-Road service request to the service provider's security server.

**Main Success Scenario**:

1.  System receives the request and verifies that the request was sent using POST method.

2.  System verifies that the system configuration contains valid global configuration.

3.  System verifies that the Provider IS is in *Registered* state in the system configuration.

4.  System finds the signing information for the service provider. (The system does not accept the request if signing the respective response is not possible.)

5.  System establishes the secure connection initiated by Client SS: [3.7](#37-uc-mess_06-establish-the-secure-connection).

6.  System parses the request to verify that the message parts are well-formed.

7.  System verifies that the request does not contain a SOAP Fault message.

8.  System verifies that the request contains a SOAP message and a signature.

9.  System verifies that the requested service is configured in the system, allowed for the requesting information system and enabled.

10. System verifies the signature: [3.12](#312-uc-mess_11-verify-signature).

11. System logs the request message and signature to the message log: [3.10](#310-uc-mess_09-log-message-and-signature-to-message-log).

12. System looks up the address of the Provider IS form the system configuration.

13. System verifies that the Provider IS should be connected using HTTP protocol. System initiates a connection with the Provider IS.

14. System sends the request and waits for the response.

15. System receives a response from the Provider IS or operational monitoring daemon and verifies the SOAP message: [3.5](#35-uc-mess_04-verify-soap-message).

16. System verifies that the response is not a SOAP Fault message.

17. System adds the request message hash to the response message header.

18. System signs the response message: [3.9](#39-uc-mess_08-create-signature).

19. System logs the response message and signature to the message log: [3.10](#310-uc-mess_09-log-message-and-signature-to-message-log).

20. System stores operational monitoring data in operational monitoring buffer: [3.17](#317-uc-mess_16-store-operational-monitoring-data-and-forward-the-data-to-operational-monitoring-daemon).

21. System sends the response message to the Client SS.

**Extensions**:

1a. Request was sent using a method other than POST.

  - 1a1. System sends a SOAP Fault message with fault string “Must use POST request method instead of X” (where “X” is the used method) to the Client SS. The use case terminates.

2a. The global configuration is expired.

  - 2a.1. System sends a SOAP Fault message with fault string “Global configuration is expired” to the Client SS. The use case terminates.

3a. Client information system is not in *Registered* state.

  - 3a1. System sends a SOAP Fault message with fault string “Client 'X' not found” (where “X” is the service provider's information system X-Road identifier) to the Client SS. The use case terminates.

4a. System could not find signing information for the X-Road member.

  - 4a.1. System sends a SOAP Fault message with fault string “Failed to get signing info for member 'X': Y” (where “X” is the X-Road member's identifier and “Y” is the description of the encountered error) to the Client SS. The use case terminates.

5a. The establishment of the secure channel terminates with an exception message.

  - 5a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

6a. The parsing of the request message resulted in an error.

  - 6a.1. System sends a SOAP Fault message with fault string containing the encountered error details to the Client SS. The use case terminates.

7a. The request contains a fault message.

  - 7a.1. System discards the received message. The use case terminates.

8a. Request does not contain a SOAP message.

  - 8a.1. System sends a SOAP Fault message with fault string “Request does not have SOAP message” to the Client SS. The use case terminates.

8b. Request does not contain a signature.

  - 8b.1. System sends a SOAP Fault message with fault string “Request does not have signature” to the Client SS. The use case terminates.

9a. The requested service is not found in the system configuration.

  - 9a1. System sends a SOAP Fault message with fault string “Unknown service: X” (where “X” is the X-Road identifier of the requested service) to the Client SS. The use case terminates.

9b. The requesting information system does not have access rights for the requested service.

  - 9b1. System sends a SOAP Fault message with fault string “Request is not allowed: X” (where “X” is the X-Road identifier of the requested service) to the Client SS. The use case terminates.

9c. The requested service is disabled.

  - 9c1. System sends a SOAP Fault message with fault string “Service X is disabled: Y” (where “X” is the X-Road identifier of the requested service and “Y” is a notification message entered by the person who disabled the service) to the Client SS. The use case terminates.

10a. Signature verification process terminates with an exception message.

  - 10a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

11a. The logging process terminates with an exception message.

  - 11a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

12a. System cannot find the Provider IS address from the system configuration.

  - 12a.1. System sends a SOAP Fault message with fault string “Service address not specified for 'X'” (where “X” is the X-Road identifier of the requested service) to the Client SS. The use case terminates.

12b. The service provider information system's address found in the system configuration is malformed.

  - 12b1. System sends a SOAP Fault message with fault string “Malformed service address 'X': Y” (where “X” is the X-Road identifier of the requested service and Y is an exception message) to the Client SS. The use case terminates.

12c. The request is either operational monitoring data request or security server health data request. System looks up the address of the operational monitoring daemon form operational monitoring daemon configuration file.

  - 12c.1. Use case continues from step 13.

    - 12c.1a. The service operational monitoring daemon address found in the configuration file is malformed.

      - 12c.1a.1. System sends a SOAP Fault message with fault string to the Client SS. The use case terminates.

13a. System fails to initiate a connection with the Provider IS.

  - 13a.1. System sends a SOAP Fault message with fault string containing the error details to the Client SS. The use case terminates.

13b. Provider IS should be connected using HTTPS and the Provider IS certificate should not be verified.

  - 13b.1. System finds the Provider IS TLS certificate from the connection but does not verify the certificate. Use case continues from step 14.

    - 13b.1a. System fails to find the TLS certificate.

      - 13b.1a.1. System sends a SOAP Fault message with fault string “Could not get peer certificates” to the Client SS. The use case terminates.

13c. Provider IS should be connected using HTTPS and the Provider IS certificate should be verified.

  - 13c.1. System finds the Provider IS TLS certificate from the connection.

    - 13c.1a. System fails to find the TLS certificate.

      - 13c.1a.1. System sends a SOAP Fault message with fault string “Could not get peer certificates” to the Client SS. The use case terminates.

  - 13c.2. System verifies that the TLS certificate sent by the Provider IS matches one of the TLS certificates configured for the Provider IS in the system configuration. Use case continues from step 14.

    - 13c.2a. System does not find any TLS certificates for the Provider IS from the system configuration.

      - 13c.2a.1. System sends a SOAP Fault message with fault string “Client 'X' has no IS certificates” (where “X” is the identifier of the Provider IS) to the Client SS. The use case terminates.

    - 13c.2b. None of the TLS certificates configured for the Provider IS match the certificate the Provider IS presented for TLS authentication.

      - 13c.2b.1. System sends a SOAP Fault message with fault string “Server certificate is not trusted” to the Client SS. The use case terminates.

13d. The request is either operational monitoring data request or security server health data request. System verifies that the operational monitoring daemon should be connected using HTTP protocol. System initiates a connection with the operational monitoring daemon.

  - 13d.1. Use case continues from step 14.

    - 13d.1a. System fails to initiate a connection with the operational monitoring daemon.

      - 13d.1a.1. System sends a SOAP Fault message with fault string containing the error details to the Client SS. The use case terminates.

13e. The request is either operational monitoring data request or security server health data request. System verifies that the operational monitoring daemon should be connected using HTTPS and the operational monitoring daemon certificate should be verified.

  - 13e.1. System uses the internal TLS certificate of the security server for connection.

  - 13e.2. System finds the operational monitoring daemon TLS certificate from the connection.

    - 13e.2a. System fails to find the TLS certificate.

      - 13e.2a.1. System sends a SOAP Fault message with fault string to the Client SS. The use case terminates.

  - 13e.3. System verifies that the TLS certificate sent by the operational monitoring daemon matches the TLS certificate configured for the operational monitoring daemon in the system configuration. Use case continues from step 14.

    - 13e.3a. System does not find TLS certificate for the operational monitoring daemon from the system configuration.

      - 13e.3a.1. System sends a SOAP Fault message with fault string to the Client SS. The use case terminates.

    - 13e.3b. The TLS certificate configured for the operational monitoring daemon does not match the certificate the operational monitoring daemon presented for TLS authentication.

      - 13e.3b.1. System sends a SOAP Fault message with fault string to the Client SS. The use case terminates.

14a. System does not receive a response within the timeout period configured for the service in the system configuration.

  - 14a.1. System sends a SOAP Fault message containing the fault details to the Client SS. The use case terminates.

15a. The validation process terminates with an exception message.

  - 15a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

16a. The response is a SOAP Fault message.

  - 16a1. System sends a SOAP Fault message with fault string containing the received Fault message content to the Client SS. The use case terminates.

18a. The signature creation process terminates with an exception message.

  - 18a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

19a. The logging process terminates with an exception message.

  - 19a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client SS. The use case terminates.

20a. The size of the operational monitoring buffer defined with a system parameter is 0.

  - 20a.1. The operational monitoring data is not stored in operational monitoring buffer and will not be sent to the operational monitoring daemon.

**Related information**:

-   All fault strings are logged to `/var/log/xroad/proxy.log`.

-   The system parameters are described in document “X-Road: System Parameters” \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].