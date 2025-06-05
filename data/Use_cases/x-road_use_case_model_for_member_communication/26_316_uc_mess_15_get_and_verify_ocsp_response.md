### 3.16 UC MESS\_15: Get and Verify OCSP Response

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actor**: OCSP responder

**Brief Description**: System finds OCSP responders for a certificate, makes an OCSP request and validates the received response.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 3 of [3.15](#315-uc-mess_14-get-ocsp-responses).

-   Certificate import (see \[[UC-SS](#Ref_UC-SS)\]).

**Main Success Scenario**:

1.  System finds OCSP responder addresses from the global configuration.

2.  System gets an OCSP response from one of the found OCSP responders.

3.  System verifies the OCSP response:

    1.  System verifies that the certificate identified in a response received from the OCSP responder corresponds to the one in the corresponding request.

    2.  System verifies that the signature on the OSCP response is valid.

    3.  System verifies that the signer is currently authorized to sign the OCSP responses for the certificate authority that has issued the certificate the OCSP response was given to.

    4.  System verifies that the OCSP response is not older than allowed by the global configuration. The validity period of OCSP responses is defined by the central server system parameter *ocspFreshnessSeconds.*

    5.  System verifies (when available) that the time at or before which newer information will be available about the status of the certificate is greater than the current time.

**Extensions**:

1a. System cannot find any OCSP responders for a certificate.

  - 1a.1. System logs an error message: “No OCSP responder URIs available”. The use case terminates.

2a. System cannot get a response from an OCSP responder.

  - 2a.1. System logs an error message: “Unable to fetch response from responder at X” (where X is the OCSP responder address).

2b. System cannot get an OCSP response from any of the responders.

  - 2b.1. System logs an error message: “Unable to get valid OCSP response from any responders“. The use case terminates.

3a. Validation of the OCSP response fails.

  - 3a.1. System logs a warning message: “Received OCSP response that failed verification“. The use case terminates.

**Related information**: -