#### 2.2.18 UC GCONF\_18: Generate Configuration

**System**: Central server

**Level**: System task

**Component:** Central server

**Actor**: -

**Brief Description**: System generates private and shared configuration
part files, builds and signs the configuration directories for
configuration sources, and makes the global configuration available for
configuration clients.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Configuration generation timer defined in the central
server configuration file /etc/cron.d/xroad-center*.*

**Main Success Scenario**:

1.  System verifies that the system configuration contains the data
    necessary for generating configuration and generates the private
    parameters and shared parameters configuration part files.

2.  System verifies the validity of the generated files against the
    respective schemas and saves the generated files to the system
    configuration.

3.  System

    -   calculates the configuration expiry time (by adding the value of
        the central server system parameter *confExpireIntervalSeconds*
        to current time);

    -   calculates the hash values of the generated configuration files
        using the algorithm defined by the value of the central server
        system parameter *confHashAlgoUri*; and

    -   builds the internal and external configuration directories.

4.  System signs the internal and external configuration directories
    using the active configuration signing keys of the respective
    configuration sources.

5.  System makes the signed configuration directories and configuration
    part files available to configuration clients.

**Extensions**:

- 1a. The generation of the configuration part files failed because the central server address is not configured.
    - 1a.1. System logs the error message “Failed to generate valid global configuration: No authentication service registration URL present. Central server may have not been initialized”.
    - 1a.2. System displays the error message “Global configuration generation failing since 'X'”, where “X” is the time and date since when the system has not been able to generate distributable global configuration.
    - 1a.3. Use case terminates.

- 1b. The generation of the configuration part files failed because the management service provider is not configured.
    - 1b.1. System logs the error message “Failed to generate valid global configuration: Management services provider is not configured”.
    - 1b.2. System displays the error message “Global configuration generation failing since 'X'”, where “X” is the time and date since when the system has not been able to generate distributable global configuration.
    - 1b.3. Use case terminates.

- 1c. The generation of the configuration part files failed for any other reason than the ones stated in extensions 1a and 1b.
    - 1c.1. System logs the error message “Failed to generate valid global configuration: X”, where “X” is the technical system error message.
    - 1c.2. System displays the error message “Global configuration generation failing since 'X'”, where “X” is the time and date since when the system has not been able to generate distributable global configuration.
    - 1c.3. Use case terminates.

- 2a. The validation of the configuration part files failed.
    - 2a.1. System logs the error message “Failed to generate valid global configuration: X”, where “X” is the XML Schema validator specific error message.
    - 2a.2. System displays the error message “Global configuration generation failing since 'X'”, where “X” is the time and date since when the system has not been able to generate distributable global configuration.
    - 2a.3. Use case terminates.

- 3-5a. The building or signing of the configuration directory failed.
    - 3-5a.1. System logs the error message “Failed to generate global configuration: X”, where “X” is the description of the error that occurred.
    - 3-5a.3. Use case terminates.

**Related information**:

-   The system parameters are described in document “X-Road: System
    Parameters” \[UG-SYSPAR\].

-   The contents of the signed directory and the schemas for private
    parameters and shared parameters are described in the document
    “X-Road: Protocol for Downloading Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\].

-   The error messages are logged to /var/log/xroad/jetty/jetty.log.