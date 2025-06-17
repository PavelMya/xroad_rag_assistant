### 3.9 UC MESS\_08: Create Signature

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: The system signs the message using the signature key and certificate of the service client (in case the Client SS creates the signature) or the service provider (in case the Provider SS creates the signature).

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 12 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

-   Step 18 of [3.4](#34-uc-mess_03-process-x-road-request-message).

**Main Success Scenario**:

1.  System finds signing information (key, certificate, OCSP responses) for the X-Road member that sent the message to be signed.

2.  System creates the signature. Please see documents “Profile for High-Perfomance Digital Signature” \[[HPDS](#Ref_HPDS)\] and “Using Batch Hashing for Signing and Time-Stamping” \[[BATCH](#Ref_BATCH)\] for detailed description of X-Road signatures.

**Extensions**:

1a. System could not find signing info for the X-Road member.

  - 1a.1. System creates an exception message: “Failed to get signing info for member 'X': Y” (where “X” is the X-Road member's identifier and “Y” is the description of the encountered error). The use case terminates.

1b. System could not find any usable (active, valid) signature certificates for the X-Road member.

  - 1b.1. System creates an exception message: “Failed to get signing info for member 'X': Member 'X' has no suitable certificates” (where “X” is the X-Road member's identifier). The use case terminates.

2a. System could not build the certificate chain for the signature certificate.

  - 2a.1. System creates an exception message: “Got empty certificate chain for certificate X” (where X is the certificate serial number). The use case terminates

2b. System did not find an OCSP response for one or more certificates in the certificate chain.

  - 2b.1. System creates an exception message: “Could not get OCSP responses for certificates (X)” (where “X” is the list of certificates). The use case terminates.

**Related information**: -