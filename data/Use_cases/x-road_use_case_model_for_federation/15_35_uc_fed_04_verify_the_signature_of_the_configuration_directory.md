### 3.5 UC FED\_04: Verify the Signature of the Configuration Directory

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System verifies the signature of the
configuration directory using the configuration source anchor.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 4 of 3.4.

**Main Success Scenario**:

1.  System finds the configuration signature algorithm (value of the
    MIME header *Signature-algorithm-id*) and the hash value of the
    verification certificate (value of the MIME header
    *Verification-certificate-hash*) from the signature part of the
    downloaded configuration directory.

2.  System uses the found hash value to find the corresponding signature
    verification certificate from the configuration source anchor.

3.  System verifies the configuration signature value using the
    signature algorithm and the signature verification certificate.

**Extensions**:

- 2a. System cannot find the verification certificate needed to verify the signature.
    - 2a.1. System logs the error message: “Cannot verify signature of configuration instance X: could not find verification certificate for certificate hash Y” (where “X” is the instance identifier of the configuration and “Y” is the hash value of the verification certificate that was used to sign the configuration directory). Use case terminates.

- 3a. Signature verification fails.
    - 3a.1. System logs the error message: “Failed to verify signature of configuration instance X” (where “X” is the instance identifier of the configuration directory). Use case terminates.

**Related information**:

- The error messages are logged to
  /var/log/xroad/configuration-client.log.