#### 2.3.5 UC GCONF\_24: Download Configuration from a Configuration Source

**System**: Security server

**Level**: Subfunction

**Component:** Security server, central server, configuration proxy

**Actor**: Configuration source

**Brief Description**: System downloads the configuration directory
describing the configuration provided by the configuration source and
verifies the integrity of the directory. System updates the
configuration files stored in the system to match the list of
configuration parts described in the configuration directory by
downloading the latest version of (or deleting) the obsolete or missing
files.

**Preconditions**: -

**Postconditions**: -

**Triggers**: Steps 1 and 2 of 2.3.4.

**Main Success Scenario**:

1.  System finds configuration source addresses from the configuration
    anchor.

2.  System downloads the signed configuration directory by making a HTTP
    GET request to the configuration source address found in the
    configuration anchor that successfully served the last configuration
    download request.

3.  System saves the information about the configuration source that
    successfully served the configuration download request.

4.  System parses the downloaded configuration directory and verifies
    that the configuration directory is signed and not expired (compares
    the *Expire-date* header value of the configuration directory to
    current date).

5.  System verifies the signature of the configuration directory: 2.3.6.

6.  System handles each configuration part found in the configuration
    directory: 2.3.7.

7.  System verifies, that one or more configuration files were
    downloaded and saves the files, replacing existing files (if such
    exist).

8.  System saves the expiry date of the downloaded configuration files.

9.  System verifies that every configuration file saved in the system
    configuration that originates from the used configuration source is
    described in the configuration directory.

**Extensions**:

- 1a. System cannot find the configuration anchor.
    - 1a.1. System logs the error message: “Cannot download configuration,anchor file X does not exist”, where “X” is the anchor file name.

- 2a. Download from the last successful configuration source address fails.
    - 2a.1. System downloads the signed configuration directory by making a HTTP GET request to a random configuration download address found in the configuration anchor, excluding the address(es) from where the configuration download failed.
        - 2a.1a. Downloading the configuration failed. Use case continues from step 2a.
        - 2a.1b. Downloading failed from every configuration source addresses listed in the configuration anchor.
            - 2a.1a.1. System logs the error message: “Failed to download configuration from any configuration location: X” (where “X” is the list of configuration source addresses that were tried). Use case terminates.
    - 2a.2. Use case continues from step 3.

- 4a. Parsing of the configuration directory resulted in an error (e.g., the value of the MIME header *Content-transfer-encoding* was found not to be “base64”).
    - 4a.1. System logs the error message. Use case terminates.

- 4b. The configuration directory is missing the *Expire-date* header.
    - 4b.1. System logs the error message: “Configuration instance X is missing signed data expiration date” (where “X” is the instance identifier of the configuration). Use case terminates.

- 4c. The downloaded configuration is not signed.
    - 4c.1. System logs the error message: “Configuration instance X is missing signed data” (where “X” is the instance identifier of the configuration). Use case terminates.

- 4d. The downloaded configuration is expired.
    - 4d.1. System logs the error message: “Configuration instance X expired on Y” (where “X” is the instance identifier of the configuration and “Y” is the expiration date and time of the downloaded configuration directory). Use case terminates.

- 5a. The signature verification process terminated with an error condition.
    - 5a.1. Use case terminates.

- 6a. The downloading of a configuration part file terminated with an error condition.
    - 6a.1. Use case terminates.

- 7a. System encounters an error while saving the downloaded files.
    - 7a.1. System logs the error message: “Failed to sync downloaded files list” and restores the previous state of the configuration file set. Use case terminates.

- 8b. No configuration files were downloaded.
    - 8b.1. Use case continues from step 9.

- 9a. System finds one or more configuration files that originate from the used configuration source but are not described in the configuration source.
    - 9a.1. System deletes the configuration files.

**Related information**:

-   The error messages are logged to
    /var/log/xroad/configuration-client.log.