### 3.11 UC CP\_10: Activate Configuration Source Signing Key

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator activates an existing
configuration source signing key for a particular configuration proxy
instance.

**Preconditions**: A security token containing an inactive signing key
associated with the configuration source is connected to the system.

**Postconditions**: System is using a different key for signing
configuration.

**Triggers**:

-   CP administrator wishes to change the key that the system uses for
    signing configuration provided by the source.

-   Step 4 of 3.10.

**Main Success Scenario**:

1.  CP administrator edits the active key identifier in the
    configuration proxy instance settings file (see 3.4).

2.  System starts using the activated key.

**Extensions**: -

**Related information**:

-   By default the settings file is located at
    /etc/xroad/confproxy/&lt;INSTANCE&gt;/conf.ini, where
    &lt;INSTANCE&gt; is the name of the configuration proxy instance.
    See \[[UG-CP](#Ref_UG-CP)\] for details.