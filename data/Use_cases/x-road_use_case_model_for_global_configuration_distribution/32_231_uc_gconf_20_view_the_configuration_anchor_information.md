#### 2.3.1 UC GCONF\_20: View the Configuration Anchor Information

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator views the information regarding
the configuration anchor used by the system to download global
configuration.

**Preconditions**: A configuration anchor is saved in the system
configuration (see 2.3.3).

**Postconditions**: The configuration anchor information is displayed to
SS administrator.

**Trigger**: SS administrator wishes to view the configuration anchor
information e.g., to verify that the system is using the latest anchor
provided by the governing agency.

**Main Success Scenario**:

1.  SS administrator selects to view the configuration anchor.

2.  System displays the following information.

    -   The SHA-224 hash value of the configuration anchor.

    -   The generation date and time (UTC) of the configuration anchor.
    
    The following user action options are displayed:

    -   download the configuration anchor file: 2.3.2;

    -   upload a configuration anchor file: 2.3.3.

**Extensions**: -

**Related information**: -