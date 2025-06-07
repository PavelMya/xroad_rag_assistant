### 3.4 UC CP\_03: Edit Settings File

**System**: Configuration proxy

**Level**: User task

**Component**: Configuration proxy

**Actor**: CP administrator

**Brief Description**: CP administrator modifies settings of a
configuration proxy instance.

**Preconditions**: The given configuration proxy instance has been
created.

**Postconditions**: Changes made by CP administrator are reflected in
the operation of the configuration proxy.

**Trigger**: Step 1 of 3.11.

**Main Success Scenario**:

1.  CP administrator selects to edit a proxy instance settings file.

2.  CP administrator modifies the proxy instance settings file content.
    Possible setting keys are:

    -   validity-interval-seconds;

    -   active-signing-key-id;

    -   signing-key-id-\*.

3.  CP administrator saves the edited file.

4.  CP administrator generates configuration anchor file (see 3.5), in
    case signing keys were added or deleted.

**Extensions**: -

**Related information**:

-   By default the settings file is located at
    /etc/xroad/confproxy/&lt;INSTANCE&gt;/conf.ini, where
    &lt;INSTANCE&gt; is the name of the configuration proxy instance.
    See \[[UG-CP](#Ref_UG-CP)\] for details.