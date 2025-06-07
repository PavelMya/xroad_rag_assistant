### 3.14 UC MESS\_13: Validate an OCSP Response

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: System verifies that the OCSP response is valid and the OCSP response status is *good*.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 3 of [3.13](#313-uc-mess_12-verify-certificate-chain).

**Main Success Scenario**:

1.  System verifies that the certificate identified in a response received from the OCSP responder corresponds to the one identified in the corresponding request.

2.  System verifies that the signature on the OSCP response is valid.

3.  System verifies that the signer is currently authorized to sign the OCSP responses for the certificate authority that has issued the certificate the OCSP response was given to.

4.  System verifies that the OCSP response is not older than allowed by the global configuration. The validity period of OCSP responses is defined by the central server system parameter *ocspFreshnessSeconds*.

5.  System verifies (when available) that the time at or before which newer information will be available about the status of the certificate is greater than the current time.

6.  System verifies the OCSP response status value is *good*.

**Extensions**:

1a. The certificate in the OCSP response does not match the one in the request.

  - 1a.1. System creates an exception message: “OCSP response does not apply to certificate (sn = X)” (where “X” is the serial number of the certificate). The use case terminates.

2a. System cannot find the OCSP responder certificate needed to validate the signature.

  - 2a.1. System creates an exception message: “Could not find OCSP certificate for responder ID“. The use case terminates.

2b. The validation of the signature fails.

  - 2b.1. System creates an exception message: “Signature on OCSP response is not valid“. The use case terminates.

3a. The OCSP responder is not authorized to sign OCSP responses for the certificate authority that has issued the certificate.

  - 3a.1. System creates an exception message: “OCSP responder is not authorized for given CA“. The use case terminates.

4a. The OCSP status is too old.

  - 4a.1. System creates an exception message: “OCSP response is too old (thisUpdate: X)“, where “X” is a date representing the beginning time of validity of this response. The use case terminates.

5a. Newer information about the status of the certificate should be available.

  - 5a.1. System creates an exception message: “OCSP response is too old: newer information is available“. The use case terminates.

6a. The status of the OCSP response is not *good*.

  - 6a.1. System creates an exception message: “OCSP response indicates certificate status is X”, where “X” is the status (possible values: *unknown*, *revoked (date: &lt;revocation time&gt;)*, *invalid*) of the OCSP response. The use case terminates.

**Related information**: -