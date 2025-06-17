### 3.16 UC CP\_15: Update Configuration

**System**: Configuration proxy

**Level**: System

**Component**: Configuration proxy

**Actor**: -

**Brief Description**: System downloads the configuration and generates
the configuration directory distributed to the configuration clients.

**Preconditions**: Trusted configuration anchor exists.

**Postconditions**: -

**Triggers**:

-   Timer (defined by *cron* daemon).

-   Step 4 of 3.15.

**Main Success Scenario**:

1.  System downloads the configuration: UC GCONF\_21: Download
    Configuration from a Configuration Source \[[UC-GCONF](#Ref_UC-GCONF)\].

2.  System generates the configuration directory: 3.17.

**Extensions:**

- 1a. Configuration download terminates with an error.
    - 1a.1. Use case terminates.

**Related information**:

-   By default the *cron* job is executed every
    minute. 

-   The format of the configuration anchor and configuration directory,
    and the protocol for downloading the configuration are described in
    the document “X-Road: Protocol for Downloading Configuration”
    \[[PR-GCONF](#Ref_PR-GCONF)\].