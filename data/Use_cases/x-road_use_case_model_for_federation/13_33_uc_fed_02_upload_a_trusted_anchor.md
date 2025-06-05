### 3.3 UC FED\_02: Upload a Trusted Anchor

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator uploads a trusted anchor to the
system. The system validates the anchor file and downloads configuration
from the source pointed by the anchor to verify that the source is
functional. The system includes the uploaded anchor to the list of
configuration sources distributed to the security servers of this X-Road
instance via the global configuration.

**Preconditions**: CS administrator has received an external
configuration anchor file from a federation partner and validated the
integrity of the anchor.

**Postconditions**: -

**Trigger**: CS administrator receives an external configuration anchor
file from a federation partner. The external anchor file should be
distributed (via out of band means) to the federation partners when the
federation is first set up or in case the contents of the external
configuration anchor are updated (e.g., due to external configuration
signing key changes, central server address changes, central server high
availability setup changes).

**Main success scenario**:

1.  CS administrator selects to upload a trusted anchor.

2.  CS administrator selects the anchor file from the local file system.

3.  System verifies that the selected file is a valid configuration
    anchor file by validating the uploaded file against the
    configuration anchor schema.

4.  System verifies that the configuration anchor does not point to a
    configuration source of this X-Road instance.

5.  System calculates and displays the SHA-224 hash value and the
    generation time of the selected anchor file and prompts for
    confirmation.

6.  CS administrator confirms.

7.  System downloads the signed configuration from the source defined by
    the uploaded anchor and validates the configuration: 3.4.

8.  System verifies that an anchor with the same instance identifier as
    the uploaded one exists in the system configuration and replaces the
    existing anchor with the uploaded one.

9.  System logs the event “Add trusted anchor” to the audit log.

**Extensions**:

- 3a. The selected file is not a valid configuration anchor file.
    - 3a.1. System displays the error message: “Failed to upload trusted anchor: Incorrect file structure.”.
    - 3a.2. CS administrator selects to reselect the configuration anchor file. Use case continues from step 3.
    - 3a.2a. CS administrator selects to terminate the use case.

- 4a. The anchor points to a configuration source of the local X-Road instance.
    - 4a.1. System displays the error message: “Failed to upload trusted anchor: Anchors originating from this instance are not supported as trusted anchors.”.
    - 4a.2. CS administrator selects to reselect the configuration anchor file. Use case continues from step 3.
    - 4a.2a. CS administrator selects to terminate the use case.

- 6a. CS administrator selects to terminate the use case.

- 7a. Downloading of the configuration fails.
    - 7a.1. System displays the error message: “Failed to save uploaded trusted anchor: Configuration source cannot be reached, check source URL in uploaded anchor file”.
    - 7a.2. System logs the event “Add trusted anchor failed” the audit log.
    - 7a.3. Use case terminates.

- 7b. The downloaded configuration is expired.
    - 7b.1. System displays the error message: “Failed to save uploaded trusted anchor: Configuration from source is out of date”.
    - 7b.2. System logs the event “Add trusted anchor failed” the audit log.
    - 7b.3. Use case terminates.

- 7c. Verification of the signature value of the downloaded configuration failed.
    - 7c.1. System displays the error message: “Failed to save uploaded trusted anchor: Signature of configuration cannot be verified”.
    - 7c.2. System logs the event “Add trusted anchor failed” the audit log.
    - 7c.3. Use case terminates.

- 7d. The downloaded configuration directory contains private parameters configuration part (i.e., the configuration anchor points to an internal configuration source).
    - 7d.1. System displays the error message: “Failed to upload trusted anchor: Anchor points to an internal configuration source. Only external configuration source anchors are supported as trusted anchors.”.
    - 7d.2. System logs the event “Add trusted anchor failed” the audit log.
    - 7d.3. Use case terminates.

- 7e. Verification of the downloaded configuration fails for reasons other than the ones listed in extensions 7b-d.
    - 7e.1. System displays the error message: “Failed to save uploaded trusted anchor: Configuration from source failed verification”.
    - 7e.2. System logs the event “Add trusted anchor failed” the audit log.
    - 7e.3. Use case terminates.

- 8a. No anchor with the same instance identifier as the uploaded one exists in the system configuration.
    - 8a.1. System saves the uploaded anchor to system configuration.

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The format of the configuration anchor and the configuration
    directory and the protocol for downloading the configuration are
    described in the document “X-Road: Protocol for Downloading
    Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\].