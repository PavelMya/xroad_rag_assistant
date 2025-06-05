#### 2.2.12 UC GCONF\_12: Activate a Configuration Source Signing Key

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator activates a configuration
signing key. System uses the active key to sign configuration provided
by the configuration source.

**Preconditions**: A security token containing an inactive signing key
associated with the configuration source is connected to the system.

**Postconditions**: -

**Trigger**: CS administrator wishes to change the key that the system
uses for signing configuration provided by the source.

**Main Success Scenario**:

1.  CS administrator selects to activate an inactive configuration
    source signing key.

2.  System prompts for confirmation.

3.  CS administrator confirms.

4.  System verifies that the key to be activated is accessible, marks
    the key as active and starts using the key for signing the
    configuration provided by the source.

5.  System logs the event “Activate internal configuration signing key”
    or “Activate external configuration signing key”, depending of the
    configuration source, to the audit log.

**Extensions**:

- 3a. CS administrator cancels the key activation.
    - 3a.1. System terminates use case.

- 4a. The key to be activated is not accessible.
    - 4a.1. System displays the error message: “Failed to activate signing key: token or key not available”.
    - 4a.2. System logs the event “Activate internal configuration signing key failed” or “Activate external configuration signing key failed”, depending of the configuration source, to the audit log.
    - 4a.3. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].