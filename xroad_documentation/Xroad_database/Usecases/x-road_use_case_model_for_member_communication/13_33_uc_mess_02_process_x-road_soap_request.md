### 3.3 UC MESS\_02: Process X-Road SOAP Request

**System**: Service client's security server

**Level**: System

**Component**: Security server

**Actors**:

-   Client IS

-   Provider SS

**Brief Description**: The system receives a request message from Client IS; verifies that the system configuration allows X-Road message exchange and that the request message composition conforms to the X-Road message protocol; sets up a secure connection session with the Provider SS; signs the request message; logs the request message and the signature; sends the request message and signature to Provider SS and awaits for the response. After receiving the response from Provider SS, system validates the response composition and signature; logs the response message and signature and sends the response to the Client IS. In case a verification or a validation fails or when the system encounters an error condition, the system sends an error (SOAP Fault) message to the Client IS.

**Preconditions**:

-   Service client's security server is running and able to receive messages.

**Postconditions**: -

**Trigger**: Client IS sends a request to the system.

**Main Success Scenario**:

1.  System receives the request and verifies that the request was sent using POST method.

2.  System verifies that the system configuration contains valid global configuration.

3.  System verifies that the system configuration contains an authentication certificate that can be used for exchanging messages with another security server (the certificate must be active and valid).

4.  System verifies that the request contains a SOAP message and verifies the SOAP message: [3.5](#35-uc-mess_04-verify-soap-message).

5.  System verifies that SOAP request header contains X-Road service identifier.

6.  System verifies that the Client IS is in *Registered* state in the system configuration.

7.  System verifies that the communication type for the Client IS in the system configuration is set to “HTTPS” and that the Client IS has made the connection for sending the request using HTTPS protocol.

8.  System verifies that the Client IS provided a TLS certificate that matches a certificate saved for the Client IS in the system configuration.

9.  System looks up Provider SS addresses from the global configuration.

10. System prepares the authentication information that will be sent to the Provider SS while setting up a secure connection.

11. System verifies that no cached communication sessions with the found addresses exist and initiates a secure connection with the fastest responder: [3.6](#36-uc-mess_05-initiate-a-secure-connection).

12. System signs the request message: [3.9](#39-uc-mess_08-create-signature).

13. System logs the request message and signature to the message log: [3.10](#310-uc-mess_09-log-message-and-signature-to-message-log).

14. System sends the signed request and OCSP responses needed to verify the authentication certificate to the Provider SS and waits for the response.

15. System receives a response from the Provider SS and parses the response to verify that the message parts are well-formed.

16. System verifies that the response is not a SOAP Fault message.

17. System verifies that the response contains a SOAP message and a signature.

18. System verifies the signature: [3.12](#312-uc-mess_11-verify-signature).

19. System verifies that the SOAP response headers are consistent with the SOAP request headers.

20. System verifies that the request message hash is included in the response and that the hash matches the request message.

21. System logs the response message and signature to the message log: [3.10](#310-uc-mess_09-log-message-and-signature-to-message-log).

22. System stores operational monitoring data in operational monitoring buffer: [3.17](#317-uc-mess_16-store-operational-monitoring-data-and-forward-the-data-to-operational-monitoring-daemon).

23. System sends the response message to the Client IS.

**Extensions**:

1a. Request was sent using a method other than POST.

  - 1a.1. System sends a SOAP Fault message with fault string “Must use POST request method instead of X” (where “X” is the used method) to the Client IS. The use case terminates.

2a. The global configuration is expired.

  - 2a.1. System sends a SOAP Fault message with fault string “Global configuration is expired” to the Client IS. The use case terminates.

3a. Security server does not have usable authentication certificates.

  - 3a.1. System sends a SOAP Fault message with fault string “Security server has no valid authentication certificate” to the Client IS. The use case terminates.

4a. Request does not contain a SOAP message.

  - 4a.1. System sends a SOAP Fault message with fault string “Request does not contain SOAP message” to the Client IS. The use case terminates.

4b. The validation process terminates with an exception message.

  - 4b.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

6a. Client IS is not in *Registered* state.

  - 6a.1. System sends a SOAP Fault message with fault string “Client 'X' not found” (where “X” is the X-Road identifier of Client IS) to the Client IS. The use case terminates.

7a. Client IS connection type in the system configuration is “HTTP” and Client IS has made an HTTP connection.

  - 7a.1. The use case continues from step 9.

7b. Client IS connection type in the system configuration is “HTTP”, but Client IS has made an HTTPS connection.

  - 7b.1. The use case continues from step 9.

7c. Client IS connection type in the system configuration is “HTTPS NO AUTH”, but Client IS has made an HTTP connection.

  - 7c.1. System sends a SOAP Fault message with fault string “Client (X) specifies HTTPS NO AUTH but client made plaintext connection” (where “X” is the X-Road identifier of Client IS) to the Client IS. The use case terminates.

7d. Client IS connection type in the system configuration is “HTTPS”, but Client IS has made an HTTP connection.

  - 7d.1. System sends a SOAP Fault message with fault string “Client (X) specifies HTTPS but did not supply TLS certificate” (where “X” is the X-Road identifier of Client IS) to the Client IS. The use case terminates.

8a. No TLS certificates for the Client IS are found in the system configuration.

  - 8a.1. System sends a SOAP Fault message with fault string “Client (X) has no IS certificates” (where “X” is the X-Road identifier of Client IS) to the Client IS. The use case terminates.

8b. No matching TLS certificates for the Client IS are found in the system configuration.

  - 8b.1. System sends a SOAP Fault message with fault string “Client (X) TLS certificate does not match any IS certificates” (where “X” is the X-Road identifier of Client IS) to the Client IS. The use case terminates.

9a. No Provider SS addresses for the requested service are found.

  - 9a.1. System sends a SOAP Fault message with fault string “Could not find addresses for service provider “X”” (where “X” is the service provider's X-Road identifier) to the Client IS. The use case terminates.

10a. System cannot find an authentication key that can be used for establishing a secure connection.

  - 10a.1. System sends a SOAP Fault message with fault string “Could not find active authentication key for security server 'X'” (where “X” is the security server identifier) to the Client IS. The use case terminates.

11a. System finds a cached session with one of the found security servers.

  - 11a.1. System reuses the cached session information to set up a connection: [3.6](#36-uc-mess_05-initiate-a-secure-connection) from step 3.

    - 11a.1a. The process of initiating a secure connection using the cached session information terminates with an exception message.

      - 11a.1a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

  - 11a.2. The use case continues from step 12.

11b. The process of initiating a secure connection terminates with an exception message.

  - 11b.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

11c. System could not initiate contact with any of the found Provider SS addresses.

  - 11c.1. System sends a SOAP Fault message with fault string “Could not connect to any target host (X)” (where X is the list of Provider SS addresses). The use case terminates.

12a. The signature creation process terminates with an exception message.

  - 12a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

13a. The logging process terminates with an exception message.

  - 13a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

15a. System does not receive a response within the timeout period set by the security server system parameter *proxy.client-timeout*.

  - 15a.1. System sends a SOAP Fault message containing the fault detail to the Client IS. The use case terminates.

15b. The parsing of the response message resulted in an error.

  - 15b.1. System sends a SOAP Fault message with fault string containing the encountered error details to the Client IS. The use case terminates.

16a. The response is a Fault message.

  - 16a.1. System sends a SOAP Fault message with fault string containing the received fault message content to the Client IS. The use case terminates.

17a. Response does not contain a SOAP message.

  - 17a.1. System sends a SOAP Fault message with fault string “Response does not have SOAP message” to the Client IS. The use case terminates.

17b. Response does not contain a signature.

  - 17b.1. System sends a SOAP Fault message with fault string “Response does not have signature” to the Client IS. The use case terminates.

18a. Signature verification process terminates with an exception message.

  - 18a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

19a. Response headers are not consistent with the request headers.

  - 19a.1. System sends a SOAP Fault message with string “Response from server proxy is not consistent with request” to the Client IS. The use case terminates.

20a. Request message hash contained in the response does not match request message.

  - 20a.1. System sends a SOAP Fault message with fault string “Request message hash does not match request message” to the Client IS. The use case terminates.

20b. Response does not contain the request message hash.

  - 20b.1. System sends a SOAP Fault message with fault string “Response from server proxy is missing request message hash” to the Client IS. The use case terminates.

21a. The logging process terminates with an exception message.

  - 21a.1. System sends a SOAP Fault message with fault string containing the exception message to the Client IS. The use case terminates.

22a. The size of the operational monitoring buffer defined with a system parameter is 0.

  - 22a.1. The operational monitoring data is not stored in operational monitoring buffer and will not be sent to the operational monitoring daemon.

**Related information**:

-   All the fault strings are logged to `/var/log/xroad/proxy.log`.

-   The system parameters are described in document “X-Road: System Parameters” \[[UG-SYSPAR](#Ref_UG-SYSPAR)\]