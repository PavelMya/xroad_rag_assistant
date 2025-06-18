### 3.10 UC CP\_09: Add Configuration Source Signing Key

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator adds a configuration source
signing key to a particular configuration proxy instance.

**Preconditions**: A security token is connected to the system and is
logged in to.

**Postconditions**: -

**Trigger**: CP administrator wishes to add a signing key for a proxy
instance (e.g., as a part of performing a regular key change).

**Main Success Scenario**:

1.  CP administrator selects to add a new configuration source signing
    key to the specified configuration proxy instance from the given
    security token.

2.  System generates a new configuration signing key on the referred
    token and a corresponding self-signed certificate.

3.  System saves the generated key information and the certificate to
    the proxy instance settings file.

4.  CP administrator activates the generated key (see 3.11), if needed.

5.  CP administrator generates configuration anchor file (see 3.5).

**Extensions**:

- 2a. Key generation fails.
    - 2a.1. System displays an error message: “Failed to generate signing key: X”, where “X” is the description of the error. If the key generation failed on a hardware security token, then “X” is the error code from the PKCS \#11 cryptographic token interface \[PKCS11\].

- 2b. Generation of the self-signed certificate fails:
    - 2b.1. System deletes the generated key.
    - 2b.1a. Key deletion fails.
    - 2b.1a.1. Use case continues from step 2b.2.
    - 2b.2. System displays the error message: “Failed to generate signing  key: X”, where “X” is the description of the error.

**Related information**: -