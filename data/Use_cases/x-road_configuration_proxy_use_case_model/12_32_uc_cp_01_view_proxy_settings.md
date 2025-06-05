### 3.2 UC CP\_01: View Proxy Settings

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator views the settings of the
configured configuration proxy instances.

**Preconditions**: -

**Postconditions**: The settings are displayed to CP administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CP administrator selects to view all proxy instance settings.

2.  System displays list of proxy instances. For each instance, the
    following information is displayed:

    -   trusted anchor;

    -   configuration download URL;

    -   active signing key identifier and respective certificate;

    -   list of inactive signing key identifiers and respective
        certificates;

    -   configuration validity interval.

**Extensions**:

-  1a. CP administrator selects to view the settings for a specific proxy instance.
    - 1a.1. System displays information from step 2 for the requested instance only.

-  1b. CP administrator selects to view the settings for a proxy instance that does not exist.
    - 1b.1. System notifies CP administrator with the error message “Configuration for proxy instance '&lt;INSTANCE&gt;' does not exist.”, &lt;INSTANCE&gt; being the identifier of the proxy instance.

-  1c. The configuration file for a configuration proxy instance is missing:
    -  1c.1. System notifies CP administrator with the error message “'conf.ini' could not be loaded for proxy '&lt;INSTANCE&gt;': 'conf.ini' does not exist.”, &lt;INSTANCE&gt; being the identifier of the proxy instance.

-  2a. Only partial configuration information for a proxy instance is available.
    -  2a.1. The settings are displayed with additional error messages. The settings information may contain one or more of the following messages:
        -   trusted anchor is invalid or missing - “'anchor.xml' could not be loaded: IOError: /etc/xroad/confproxy/&lt;INSTANCE&gt;/anchor.xml (No such file or directory)”, &lt;INSTANCE&gt; being the identifier of the proxy instance;
        -   the active signing key has not been configured - “active-signing-key-id: NOT CONFIGURED (add 'active-signing-key-id' to 'conf.ini')”;
        -   configuration validity interval has not been configured - “Validity interval: NOT CONFIGURED (add 'validity-interval-seconds' to 'conf.ini')”;

**Related information**:
-   See \[[UG-CP](#Ref_UG-CP)\] for details.