#### 2.2.11 UC GCONF\_11: Add a Configuration Source Signing Key

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator generates a configuration source
signing key on a security token. System creates a self-signed
certificate containing the public key part of the generated key and
generates the configuration anchor containing the created certificate.

**Preconditions**: A security token is initialised and connected to the
system.

**Postconditions**: -

**Trigger**: CS administrator wishes to add a signing key for a
configuration source (e.g., as a part of performing a regular key
change).

**Main Success Scenario**:

1.  CS administrator selects to add a configuration source signing key
    for a configuration source (either internal or external).

2.  System displays the list of available security tokens.

3.  CS administrator selects a security token and enters the label of
    the key.

4.  System generates a new configuration signing key with the inserted
    label on the selected token.

5.  System creates a self-signed certificate containing the public key
    part of the generated key.

6.  System saves the generated key information and the created
    certificate to system configuration.

7.  System verifies that the selected configuration source already has
    an active key.

8.  System logs the event “Generate internal configuration signing key”
    or “Generate external configuration signing key”, depending of the
    configuration source, to the audit log.

9.  System generates the configuration anchor for the configuration
    source: 2.2.17.

**Extensions**:

- 3a. The desired token is not on the list:
    - 3a.1. CS administrator terminates the use case.

- 4a. Key generation fails because the token is not logged in to.
    - 4a.1. System initiates the use case 2.2.7 or 2.2.8, depending on the type of the selected token.
    - 4a.2. System verifies that the log in process ended successfully. Use case continues from step 4.
        - 4a.2a. The log in process terminated with an error condition.
            - 4a.2a.1. CS administrator selects to reselect a security token. Use case continues from step 4.
                - 4a.2a.1a. CS administrator selects to terminate the use case.

- 4b. Key generation fails.
    - 4b.1. System displays an error message: “Failed to generate signing key: X”, where “X” is the description of the error. If the key generation failed on a hardware security token, then “X” is the error code from the PKCS \#11 cryptographic token interface \[PKCS11\].
    - 4b.2. System logs the event “Generate internal configuration signing key failed” or “Generate external configuration signing key failed”, depending of the configuration source, to the audit log.
    - 4b.3. CS administrator selects to reselect a security token. Use case continues from step 4.
        - 4b.3a. CS administrator selects to terminate the use case.

- 5a. Generation of the self-signed certificate fails:
    - 5a.1. System deletes the generated key.
        - 5a.1a. Key deletion fails.
            - 5a.1a.1. Use case continues from step 5a.2.
    - 5a.2. System displays the error message: “Failed to generate signing key: X”, where “X” is the description of the error.
    - 5a.3. System logs the event “Generate internal configuration signing key failed” or “Generate external configuration signing key failed”, depending of the configuration source, to the audit log.
    - 5a.4. CS administrator selects to reselect a security token. Use case continues from step 4.
        - 5a.4a. CS administrator selects to terminate the use case.

- 7a. The selected source does not have an active key.
    - 7a.1. System marks the key as active and starts using the key for signing the configuration provided by the source.
    - 7a.2. Use case continues from step 8.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].