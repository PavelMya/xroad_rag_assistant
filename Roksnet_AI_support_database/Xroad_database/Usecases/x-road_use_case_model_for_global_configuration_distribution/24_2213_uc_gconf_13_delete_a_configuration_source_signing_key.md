#### 2.2.13 UC GCONF\_13: Delete a Configuration Source Signing Key

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator deletes a configuration source
signing key and the associated certificate. System generates the
configuration anchor that contains updated certificates for the
configuration source.

**Preconditions**: The signing key is not in active state (i.e., the
system is using another key for signing the configuration).

**Postconditions**: -

**Trigger**: CS administrator wishes to delete a configuration signing
key.

**Main Success Scenario**:

1.  CS administrator selects to delete a configuration source signing
    key.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System deletes the selected configuration signing key information
    and the associated certificate from system configuration and
    displays the message: “Key successfully deleted from central server
    configuration”.

5.  System generates the configuration anchor for the configuration
    source: 2.2.17.

6.  System logs the event “Delete internal configuration signing key” to
    the audit log.

7.  System deletes the signing key from the security token and displays
    the message: “Key successfully deleted from token 'X'”, where “X” is
    the identifier of the token.

**Extensions**:

- 3a. CS administrator cancels the key deletion.
    - 3a1. System terminates use case.

- 7a. System fails to delete the signing key form the security token.
    - 7a.1. System displays the error message: “Failed to delete key from token 'X': Y”, where “X” is the identifier of the token and “Y” is the error details.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].