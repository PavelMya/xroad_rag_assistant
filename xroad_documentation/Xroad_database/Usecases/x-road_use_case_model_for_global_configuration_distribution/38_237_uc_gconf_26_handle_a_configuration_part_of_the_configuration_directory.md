#### 2.3.7 UC GCONF\_26: Handle a Configuration Part of the Configuration Directory

**System**: Security server

**Level**: Subfunction

**Component:** Security server, central server, configuration proxy

**Actor**: Configuration source

**Brief Description**: System checks if the configuration file described
in the configuration directory part is missing from the system or
differs from the one stored in the system. If the file is missing or
needs to be updated, the system downloads the file from the
configuration source and verifies the integrity of the downloaded file.

**Preconditions**: -

**Postconditions**: The system has verified that the configuration file
corresponding to the configuration part is up to date or has downloaded
the latest version of the file from the configuration source.

**Trigger**: Step 5 of 2.3.5.

**Main Success Scenario**:

1.  System finds a configuration file stored in the system that
    corresponds to the file name part of the value of the
    *Content-location* MIME header of the configuration part. System
    calculates the hash value for the found file using the hash
    algorithm stated in the *Hash-algorithm-id* MIME header of the
    configuration part.

2.  System verifies that the hash value given as the contents of the
    configuration part is different from the hash value calculated for
    the configuration file stored in the system.

3.  System downloads the configuration file from the URL provided by the
    *Content-location* MIME header in the configuration part.

4.  System calculates the hash value of the downloaded file using the
    algorithm defined by the *Hash-algorithm-id* MIME header and
    verifies that the hash value of the downloaded file matches the hash
    value in the configuration part.

5.  In case the *Content-identifier* MIME header value of the downloaded
    configuration part is either *PRIVATE-PARAMETERS* or
    *SHARED-PARAMETERS*, the system verifies that the instance
    identifier stated in the downloaded file matches the *instance*
    parameter value of the *Content-identifier* MIME header.

**Extensions**:

- 1a. System cannot find a stored file corresponding to the configuration part.
    -  1a.1. Use case continues from step 3.

- 2a. The hash values are equal.
    - 2a.1. Use-case terminates.

- 3a. The downloading of the file failed.
    - 3a.1. System logs the error message describing the reason of the failure. Use-case terminates.

- 4a. The hash values differ.
    - 4a.1. System logs the error message: “Failed to verify content integrity X” (where “X” is the *Content-identifier* or *Content-location* MIME header value of the configuration part). Use case terminates.

- 5a. The *Content-identifier* value is neither *PRIVATE-PARAMETERS* nor *SHARED-PARAMETERS*.
    - 5a.1. Use-case terminates.

- 5b. The instance identifier value in the downloaded configuration file differs from the *instance* parameter value of the *Content-identifier* MIME header.
    - 5b.1. System logs the error message: “Content part X has invalid instance identifier (expected Y, but was Z)” (where “X” is the *Content-identifier* or *Content-location* MIME header value of the configuration part; “Y” is the *instance* parameter value; and “Z” is the instance identifier value in the downloaded configuration file). Use case terminates.

**Related information**:

-   The error messages are logged to
    /var/log/xroad/configuration-client.log.