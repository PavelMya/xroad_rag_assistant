### 3.12 UC MESS\_11: Verify Signature

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: System verifies that the signature is valid.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 18 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

-   Step 10 of [3.4](#34-uc-mess_03-process-x-road-request-message).

**Main Success Scenario**:

1.  System validates the signature against the XAdES schema \[UC-OPMON](#Ref_UC-OPMON)\]).

2.  System verifies that the signature is a batch signature and verifies the hash chain (hash chain verification steps are described in document “Using Batch Hashing for Signing and Time-Stamping” \[[BATCH](#Ref_BATCH)\]).

3.  System verifies that the signature contains a signature certificate (*keyUsage* extension of the certificate has *nonRepudiation* bit set).

4.  System verifies that the signature certificate was issued by an approved certification service.

5.  System verifies that the signing certificate was issued to the X-Road member who (or whose subsystem) sent the message the signature was attached to.

6.  System verifies the signature value.

7.  System verifies the certificate chain using the signature certificate, OCSP responses and any extra certificates: [3.13](#313-uc-mess_12-verify-certificate-chain).

**Extensions**:

1a. Validation against the schema fails.

  - 1a.1. System creates an exception message containing the validation errors. The use case terminates.

2a. The signature is not a batch signature.

  - 2a.1. The use case continues form step 3.

2b. Hash chain verification fails.

  - 2b.1. System creates an exception message containing the encountered verification error. The use case terminates.

3a. System did not find a signing certificate in the signature.

  - 3a.1. System creates an exception message: “Signature does not contain signing certificate“. The use case terminates.

3b. The signing certificate does not qualify as a signature certificate.

  - 3b.1. System creates an exception message: “Certificate X is not a signing certificate” (where “X” is the subject name of the certificate). The use case terminates.

4a. System did not find the issuer of the certificate from the list of approved certification services in the global configuration.

  - 4a.1. System creates an exception message: “Certificate is not issued by approved certification service provider“. The use case terminates.

5a. System fails to read the identifier of the subject of the certificate from the signature certificate.

  - 5a.1. System creates an exception message containing the encountered error. The use case terminates.

5b. The subject common name does not match the identifier of the sender of the message.

  - 5b.1. System creates an exception message: “Name in certificate (X) does not match name in message (Y)” (where “X” is the common name of the person the certificate was issued to and “Y” is the identifier of the X-Road member who sent the message). The use case terminates.

6a. Verification of the signature value failed.

  - 6a.1. System creates an exception message: “Signature is not valid“. The use case terminates.

7a. The certificate chain validation process terminates with an exception message.

  - 7a.1. The use case terminates with the exception message.

**Related information**: -