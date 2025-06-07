### 3.13 UC MESS\_12: Verify Certificate Chain

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: System verifies the certificate chain.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 3 of [3.8](#38-uc-mess_07-verify-authentication-certificate).

-   Step 8 of [3.12](#312-uc-mess_11-verify-signature).

**Main Success Scenario**:

1.  System builds the certificate chain from the signature or authentication certificate (depending on the trigger of this use case) to a trusted certification authority (CA) certificate.

2.  System validates the certificate chain.

3.  System finds and validates the OCSP responses for each certificate in the certificate chain: [3.14](#314-uc-mess_13-validate-an-ocsp-response).

**Extensions**:

2a. Validation of the certificate chain failed.

  - 2a.1. System creates an exception message containing the details of the validation error. The use case terminates.

3a. System cannot find an OCSP response for a certificate in the certificate chain.

  - 3a.1. System creates an exception message: “Unable to find OCSP response for certificate X” (where “X” is the subject name of the certificate). The use case terminates.

3b. An OCSP response validation process terminates with an exception message.

  - 3b.1. The use case terminates with the exception message.

**Related information**: -