### 3.14 UC CP\_13: Upload Trusted Anchor

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator places the configuration
provider's anchor file into the configuration proxy instance settings
directory.

**Preconditions**: -

**Postconditions**: An anchor file has been saved to the system.

**Trigger**: Configuration proxy initialization; trusted configuration
provider sends updated configuration anchor.

**Main Success Scenario**:

1.  CP administrator copies the anchor file to configuration proxy
    instance settings directory.

**Extensions**: -

**Related information**:

-   By default the anchor file is located at
    /etc/xroad/confproxy/&lt;INSTANCE&gt;/anchor.xml, where
    &lt;INSTANCE&gt; is the name of the configuration proxy instance.
    See \[[UG-CP](#Ref_UG-CP)\] for details.