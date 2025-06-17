### 3.12 UC CP\_11: Delete Configuration Source Signing Key

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator deletes a configuration source
signing key from a particular configuration proxy instance.

**Preconditions**: A security token containing an inactive signing key
associated with the configuration source is connected to the system.

**Postconditions**: -

**Trigger**: CP administrator wishes to delete a configuration signing
key.

**Main Success Scenario**:

1.  CP administrator selects to delete an inactive configuration source
    signing key.

2.  System deletes the selected configuration signing key from the
    security token and the corresponding certificate and key ID from the
    configuration proxy instance settings file.

3.  CP administrator generates configuration anchor file (see 3.5).

**Extensions**:

- 1a. CP administrator selects to delete an active configuration source signing key.
    - 1a.1. System notifies CP administrator with the error message “Not allowed to delete an active signing key!”. The use case terminates.

- 1b. CP administrator selects to delete a key that does not belong to this proxy instance.
    - 1b.1. System notifies CP administrator with the error message “The key ID '&lt;KEY\_ID&gt;' could not be found in 'conf.ini'.”, where &lt;KEY\_ID&gt; is the id of the key to be deleted. The use case terminates.

**Related information**:

-   See \[[UG-CP](#Ref_UG-CP)\] for details.