### 3.6 UC FED\_05: Download a Configuration Part File

**System**: Central server

**Level**: Subfunction

**Component:** Central server, configuration proxy

**Actor**: Configuration source

**Brief Description**: System downloads a configuration part file from
the configuration source and verifies the integrity of the downloaded
file.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 5 of 3.4.

**Main Success Scenario**:

1.  System downloads the configuration file from the URL provided by the
    *Content-location* MIME header in the configuration part of the
    configuration directory.

2.  System calculates the hash value of the downloaded file using the
    algorithm defined by the *Hash-algorithm-id* MIME header and
    verifies that the hash value of the downloaded file matches the hash
    value in the configuration part.

3.  System verifies that the instance identifier stated in the
    downloaded file matches the *instance* parameter value of the
    *Content-identifier* MIME header of the configuration directory.

**Extensions**:

- 1a. The downloading of the file failed.
    - 1a.1. System logs the error message describing the reason of the failure. Use-case terminates.

- 2a. The hash values differ.
    - 2a.1. System logs the error message: “Failed to verify content integrity X” (where “X” is the *Content-identifier* or *Content-location* MIME header value of the configuration part). Use case terminates.

- 3a. The instance identifier value in the downloaded configuration file differs from the *instance* parameter value of the *Content-identifier* MIME header.
    - 3a.1. System logs the error message: “Content part X has invalid instance identifier (expected Y, but was Z)” (where “X” is the *Content-identifier* or *Content-location* MIME header value of the configuration part; “Y” is the *instance* parameter value; and “Z” is the instance identifier value in the downloaded configuration file). Use case terminates.

**Related information**:

- The error messages are logged to 
  /var/log/xroad/configuration-client.log.