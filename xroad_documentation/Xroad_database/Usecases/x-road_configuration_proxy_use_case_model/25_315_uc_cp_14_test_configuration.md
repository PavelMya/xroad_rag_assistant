### 3.15 UC CP\_14: Test Configuration

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator executes a number of console
commands that let him verify the correctness of the configuration proxy
instance settings.

**Preconditions**: CP administrator has tested the system setup.

**Postconditions**: -

**Trigger**: CP administrator wishes to verify that a configuration
proxy instance has been setup correctly.

**Main Success Scenario**:

1.  CP administrator generates the proxy instance anchor file. (see
    3.5).

2.  CP administrator runs the configuration download script providing it
    with the generated anchor and a directory for placing the downloaded
    configuration (see \[[UG-CP](#Ref_UG-CP)\] for details).

3.  The configuration is downloaded from the configuration source: UC
    GCONF\_21: Download Configuration from a Configuration Source
   \[[UC-GCONF](#Ref_UC-GCONF)\].

4.  CP administrator verifies that configuration download (see 3.16) and
    configuration directory generation (see 3.17) were successful.

**Extensions:** -

**Related information**:

-   The specific commands used to test the configuration of a proxy
    instance are described in the configuration proxy manual \[UG-CP\].