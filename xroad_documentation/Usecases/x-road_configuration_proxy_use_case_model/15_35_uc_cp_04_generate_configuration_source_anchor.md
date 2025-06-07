### 3.5 UC CP\_04: Generate Configuration Source Anchor

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator generates a configuration source
anchor for a configuration proxy instance.

**Preconditions**: The configuration proxy instance has been configured.

**Postconditions**: -

**Triggers**:

-   Step 4 of 3.4.

-   Step 5 of 3.10.

-   Step 3 of 3.12.

-   Step 1 of 3.15.

**Main Success Scenario**:

1.  CP administrator selects to generate a configuration anchor (as a
    file with the given name) for the specified proxy instance.

2.  System verifies that the information needed to generate the anchor
    is present:

    -   configuration provider's source anchor is present;

    -   configuration proxy server address is configured;

    -   at least one signing key with corresponding certificate is
        configured.

3.  System generates and saves the anchor file.

**Extensions**:

- 1b. CP administrator selects to generate a configuration anchor for a proxy instance that does not exist:
    - 1b.1. System notifies CP administrator with the error message “Configuration for proxy instance '&lt;INSTANCE&gt;' does not exist.”, &lt;INSTANCE&gt; being the identifier of the proxy instance. The use case terminates.

- 2a. The source anchor for the proxy instance does not exist:
    - 2a.1. System notifies CP administrator with the error message “Could not load source anchor: IOError: /etc/xroad/confproxy/&lt;INSTANCE&gt;/anchor.xml (No such file or directory)”, &lt;INSTANCE&gt; being the identifier of the proxy instance. The use case terminates.

- 2b. The configuration proxy address has not been configured:
    - 2b.1. System notifies CP administrator with the error message “configuration-proxy.address has not been configured in 'local.ini'!”. The use case terminates.

- 2c. No signing keys have been configured for the proxy instance:
    - 2c.1. System notifies CP administrator with the error message “No signing keys configured!”. The use case terminates.

- 3a. CP administrator does not have permission to write to the file system:
    - 3a.1. System notifies CP administrator with the error message “Cannot write anchor to '&lt;FILE&gt;', permission denied.”, &lt;FILE&gt; being the file path provided by CP administrator. The use case terminates.

**Related information:**

-   See \[[UG-CP](#Ref_UG-CP)\] for details.