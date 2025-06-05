### 3.17 UC CP\_16: Generate Configuration Directory

**System**: Configuration
proxy

**Level**: Subfunction

**Component**: Configuration proxy

**Actor**: -

**Brief Description**: The configuration proxy generates the
configuration directory that will be distributed to configuration
clients for a particular configuration proxy instance.

**Preconditions**: Active configuration signing key and downloaded
configuration files exist, downloaded configuration is not expired.

**Postconditions**: The configuration directory has been generated and
is being distributed to configuration clients.

**Triggers**:

-   Step 4 of 3.15.

-   Step 2 of 3.16.

**Main Success Scenario**:

1.  Systems adds information (content type, content transfer encoding,
    content file name, content identifier, content location, hash
    algorithm id, file digest) about configuration part files to
    configuration directory.

2.  System adds parameters (instance identifier, expire date) to the
    configuration directory.

3.  System signs the configuration directory.

4.  System makes the signed directory and configuration part files
    available to configuration clients.

**Extensions**: -

**Related information**: -