#### 2.3.4 UC GCONF\_23: Update Configuration 

**System**: Security server

**Level**: System task

**Component:** Security server

**Actor**: -

**Brief Description**: System updates configuration by downloading
global configuration from every known configuration source and updating
the states of system configuration objects based on information found in
the downloaded configuration files.

**Preconditions**: Configuration anchor is saved in the system
configuration.

**Postconditions**: -

**Triggers**:

-   Step 7 of 2.3.3.

-   Timer defined by the security server system parameter
    *configuration-client.update-interval*.

**Main Success Scenario**:

1.  System downloads internal configuration: 2.3.5.

2.  System finds configuration anchors pointing to external
    configuration sources from the private parameters part of the
    internal configuration and downloads configuration from each source
    pointed by the anchors: 2.3.5.

3.  System verifies that the state values of one or more system
    configuration objects (i.e. authentication certificates, security
    server clients) need to be updated and updates the values.

**Extensions**:

- 1a. Internal configuration download terminates with an error.
    - 1a.1. Use case terminates.

- 2a. System did not find any configuration anchors pointing to external configuration sources from the private parameters part (i.e., the X-Road instance is not currently federated with any other X-Road instances).
    - 2a.1. Use case continues from step 3.

- 2b. Downloading configuration from one or more external configuration sources terminated with an error.
    - 2b.1. Use case continues from step 3.

**Related information**:

-   The system parameters are described in document “X-Road: System
    Parameters” \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].

-   The format of the configuration anchor and configuration directory,
    and the protocol for downloading the configuration are described in
    the document “X-Road: Protocol for Downloading Configuration”
    \[[PR-GCONF](#Ref_PR-GCONF)\].