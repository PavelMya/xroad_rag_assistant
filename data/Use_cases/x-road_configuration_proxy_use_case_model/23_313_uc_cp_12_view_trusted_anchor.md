### 3.13 UC CP\_12: View Trusted Anchor

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator views the content of the
configuration anchor used by the configuration proxy to download the
global configuration for a particular instance.

**Preconditions**: Trusted anchor file exists.

**Postconditions**: The anchor file content has been displayed to CP
administrator.

**Trigger**: CP administrator wishes to view the configuration anchor
information e.g., to verify that the system is using the latest anchor
provided by the governing agency.

**Main Success Scenario**:

1.  CP administrator selects to view trusted anchor.

2.  System displays the anchor file content.

**Extensions**: -

**Related information**:

-   By default the anchor file is located at
    /etc/xroad/confproxy/&lt;INSTANCE&gt;/anchor.xml, where
    &lt;INSTANCE&gt; is the name of the configuration proxy instance.
    See \[[UG-CP](#Ref_UG-CP)\] for details.