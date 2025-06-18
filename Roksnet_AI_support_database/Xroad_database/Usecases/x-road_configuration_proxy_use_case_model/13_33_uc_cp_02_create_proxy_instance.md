### 3.3 UC CP\_02: Create Proxy Instance

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator creates a new configuration
proxy instance for distributing configuration from a configuration
source.

**Preconditions**: -

**Postconditions**: Configuration files for a proxy instance with the
specified identifier are available on the file system.

**Trigger**: -

**Main Success Scenario**:

1.  CP administrator selects to create a new proxy instance with the
    specified identifier.

2.  System creates the settings directory for the new proxy instance and
    generates the initial configuration file 'conf.ini', containing a
    default value (600) for *validity-interval-seconds*, which describes
    the configuration validity interval.

**Extensions**:

- 1a. Proxy instance with the specified identifier already exists:
    - 1a.1. System notifies CP administrator with the error message “Configuration for instance '&lt;INSTANCE&gt;' already exists, aborting.”, &lt;INSTANCE&gt; being the provided instance identifier, and terminates the use case.

**Related information**:

-   By default the settings directory is located at
    /etc/xroad/confproxy/&lt;INSTANCE&gt;, where &lt;INSTANCE&gt; is the
    provided instance identifier. See \[[UG-CP](#Ref_UG-CP)\] for details.