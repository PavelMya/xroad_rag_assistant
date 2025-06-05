### 3.5 UC MESS\_04: Verify SOAP Message

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: The system verifies that the SOAP message received from an information system (Client IS or Provider IS) conforms to the X-Road message protocol \[[PR-MESS](#Ref_PR-MESS)\].

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 4 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

-   Step 14 of [3.4](#34-uc-mess_03-process-x-road-request-message).

**Main Success Scenario**:

1.  System verifies that the base content type of the message is either *text/xml* or *multipart/related*.

2.  System verifies that the SOAP message is well-formed.

**Extensions**:

1a. System fails to get the base content type from the message.

  - 1a.1. System creates an exception message: “Could not get content type from request”. The use case terminates.

1b. Base content type of the message is neither *text/xml* nor *multipart/related*.

  - 1b.1. System creates an exception message: “Invalid content type: X” (where “X” is the base content type). The use case terminates.

2a. The SOAP body element is missing from the message.

  - 2a.1. System creates an exception message: “Malformed SOAP message: body missing”. The use case terminates.

2b. The validation of the SOAP envelope against the SOAP envelope schema (<http://schemas.xmlsoap.org/soap/envelope/>) fails.

  - 2b.1. System creates an exception message containing the validation fault message. The use case terminates.

2c. The message is not a SOAP Fault and the SOAP header element is missing from the message.

  - 2c.1. System creates an exception message: “Malformed SOAP message: header missing”. The use case terminates.

2d. The message is not a SOAP Fault and the *service* header is empty.

  - 2d.1. System creates an exception message: “Message header must contain service id“. The use case terminates.

2e. The message is not a SOAP Fault and the SOAP header contains duplicate fields.

  - 2e.1. System creates an exception message: “SOAP header contains duplicate field 'X'” (where “X” is the duplicated header element name). The use case terminates.

2f. The message contains attachments and system fails to get the content type of an attachment part.

  - 2f.1. System creates an exception message: “Could not get content type for part“. The use case terminates.

2g. The *objectType* of the service client is MEMBER but the SOAP header contains the element *subsystemCode*.

  - 2g.1. System creates an exception message: “Redundant subsystem code”. The use case terminates.

2h. The *objectType* of the service client is SUBSYSTEM but the SOAP header does not contain the element *subsystemCode*.

  - 2h.1. System creates an exception message: “Missing required subsystem code”. The use case terminates.

**Related information**: -