### 3.2 UC MESS\_01: X-Road Service Call

**System**: X-Road

**Level**: Summary

**Component**: Security server

**Actors**:

-   Client IS

-   Client SS

-   Provider SS

-   Provider IS

**Brief Description**: A service client initiates a service call and receives a response. Both the request and the response are processed by the service client's and the service provider's security servers.

**Preconditions**:

-   Service provider and service client are affiliated to the X-Road.

-   Service provider and service client have entered into a service usage contract.

-   Service provider and service client have interfaced their information systems as subsystems to the X-Road system.

-   Service client's security server is running and able to receive messages.

**Postcondition**: Service client's information system has received either a service response or a SOAP Fault message.

**Trigger**: Service client's information system initiates an X-Road service call.

**Main Success Scenario**:

1.  Client IS forms and sends an X-Road SOAP request to the Client SS.

2.  Client SS processes the X-Road SOAP request and forwards the request as X-Road request message to the Provider SS: [3.3](#33-uc-mess_02-process-x-road-soap-request) (steps 1-14).

3.  Provider SS processes the X-Road request message and forwards the request as X-Road SOAP request to the Provider IS: [3.4](#34-uc-mess_03-process-x-road-request-message) (steps 1-14).

4.  Provider IS processes the received request, forms an X-Road SOAP response and sends the response to Provider SS.

5.  Provider SS processes the X-Road SOAP response and forwards the response as X-Road response message to the Client SS: [3.4](#34-uc-mess_03-process-x-road-request-message) (steps 15-20).

6.  Client SS processes the X-Road response message and forwards the response as X-Road SOAP response to the Client IS: [3.3](#33-uc-mess_02-process-x-road-soap-request) (steps 15-22).

7.  Client IS receives and processes the response.

**Extensions**:

2-6a. Processing or forwarding the message results in an error. Client IS receives a SOAP Fault message. The use case terminates.

**Related information**:

-   X-Road SOAP messages must conform to the profile described in document “X-Road: Message Protocol” \[[PR-MESS](#Ref_PR-MESS)\].

-   Messaging between security servers conforms to the protocol described in document “X-Road: Message Transport Protocol” \[[PR-MESSTRANSP](#Ref_PR-MESSTRANSP)\].