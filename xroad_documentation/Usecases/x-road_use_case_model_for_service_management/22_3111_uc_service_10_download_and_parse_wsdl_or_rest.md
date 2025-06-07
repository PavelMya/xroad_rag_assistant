#### 3.1.11 UC SERVICE\_10: Download and Parse WSDL or REST

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief** **Description**: The system downloads the WSDL or REST file from the
given URL and reads the service descriptions from the WSDL or REST file.

**Preconditions**: -

**Postconditions**: -

**Trigger**:

-   Step 5 of 3.1.9.

-   Step 2 of 3.1.16.

**Main** **Success** **Scenario**:

1.  System verifies that the URL is well-formed.

2.  System verifies that the URL points to a valid XML or JSON file and
    downloads the file.

3.  System verifies that the downloaded file is a valid WSDL or REST file.

4.  System parses the WSDL or REST file for service descriptions. The following
    information is read for each service that has a port element with
    SOAP over HTTP binding described:

    -   service URL is read from the
        /definitions/service/port/address/@location attribute;

    -   service code is read from the
        /definitions/binding/operation/@name attribute;

    -   service version is read from the
        /definitions/binding/operation/xrd:version element;

    -   service title is read from the
        /definitions/portType/operation/documentation/xrd:title element.

**Extensions**:

- 1a. The URL is malformed.
    - 1a.1. Use case terminates with the error message “Malformed URL (or REST). WSDL (or REST) URL must point to a WSDL (or REST) file.”.

- 2a. Downloading of the WSDL or REST file failed.
    - 2a.1. Use case terminates with the error message “Downloading WSDL failed. WSDL or REST URL must point to a WSDL or REST file.”.

- 2b. The URL points to data that is not a valid XML or JSON file.
    - 2b.1. Use case terminates with the error message “Incorrect file structure. WSDL (or REST) URL must point to a WSDL (or REST) file.”.

- 3a. The validation of the WSDL or REST failed.
    - 3a.1. Use case terminates with an error message describing the validation exception.

**Related** **information**: -