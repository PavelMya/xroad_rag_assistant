### 3.4 UC FED\_03: Download and Validate Configuration

**System**: Central server

**Level**: Subfunction

**Component:** Central server, configuration proxy

**Actor**: Configuration source

**Brief Description**: System downloads the configuration directory
describing the configuration provided by the configuration source and
verifies the integrity of the directory. System downloads the
configuration files described in the configuration directory.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Step 7 of 3.3.

**Main Success Scenario**:

1.  System finds configuration source addresses from the configuration
    anchor.

2.  System downloads the signed configuration directory by making a HTTP
    GET request to a randomly chosen configuration source address found
    in the configuration anchor.

3.  System parses the downloaded configuration directory and verifies
    that the configuration directory is signed and not expired (compares
    the *Expire-date* header value of the configuration directory to
    current date).

4.  System verifies the signature of the configuration directory: 3.5.

5.  System downloads the configuration part files found in the
    configuration directory: 3.6.

**Extensions**:

- 2a. Download from a configuration source address fails.
    - 2a.1. System downloads the signed configuration directory by making aHTTP GET request to the next randomly chosen configuration source address found in the configuration anchor.
        - 2a.1a. Downloading failed from every configuration source addresses listed in the configuration anchor.
        - 2a.1a.1. System logs the error message: “Failed to download configuration from any configuration location: X” (where “X” is the list of configuration source addresses that were tried). Use case terminates.
    -  2a.2. Use case continues from step 3.

- 3a. Parsing of the configuration directory resulted in an error (e.g., the value of the MIME header *Content-transfer-encoding* was found not to be “base64”).
    - 3a.1. System logs the error message. Use case terminates.

- 3b. The configuration directory is missing the *Expire-date* header.
    - 3b.1. System logs the error message: “Configuration instance X is missing signed data expiration date” (where “X” is the instance identifier of the configuration). Use case terminates.

- 3c. The downloaded configuration is not signed. System logs the error message: “Configuration instance X is missing  signed data” (where “X” is the instance identifier of the configuration). Use case terminates.

- 3d. The downloaded configuration is expired.
    - 3d.1. System logs the error message: “Configuration instance X expired on Y” (where “X” is the instance identifier of the configuration and “Y” is the expiration date and time of the downloaded configuration directory). Use case terminates.

- 4a. The signature verification process terminated with an error
condition.
    -  4a.1. Use case terminates.

- 5a. The downloading of a configuration part terminated with an error condition.
    - 5a.1. Use case terminates.

**Related information**:

-   The error messages are logged to
    /var/log/xroad/configuration-client.log.