#### 2.2.17 UC GCONF\_17: Generate a Configuration Anchor

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actor**: -

**Brief Description**: System generates for a configuration source a
configuration anchor containing the information needed for the
configuration clients for downloading and verifying configuration from
the configuration source.

**Preconditions**: The instance identifier and central server address
are saved in the system configuration.

**Postconditions**: -

**Triggers**:

-   Step 2 of 2.2.3.

-   Step 9 of 2.2.11.

-   Step 5 of 2.2.13.

-   Step 7 of 2.2.15.

**Main Success Scenario**:

1.  System verifies that at least one signing key with the corresponding
    certificate is saved in the system configuration for the
    configuration source.

2.  System generates the anchor file and calculates the file hash.

3.  System saves the anchor file, file hash and file generation time to
    system configuration.

4.  System displays the message: “Internal configuration anchor
    generated successfully” or “External configuration anchor generated
    successfully”, depending on the configuration source.

**Extensions**:

- 1a. System did not find any configuration signing keys for the configuration source.
    - 1a.1. System displays the error message: “X configuration anchor generation failed: No configuration signing keys configured”, where “X” stands for either “Internal” or “External”, depending on the configuration source. Use case terminates.

**Related information**:

-   The schema for the configuration anchor file can be found in the
    document “X-Road: Protocol for Downloading Configuration”
    \[[PR-GCONF](#Ref_PR-GCONF)\].