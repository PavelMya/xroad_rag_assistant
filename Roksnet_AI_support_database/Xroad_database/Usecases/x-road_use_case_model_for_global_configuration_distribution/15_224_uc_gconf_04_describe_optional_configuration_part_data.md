#### 2.2.4 UC GCONF\_04: Describe Optional Configuration Part Data

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator creates a file in the system
configuration that contains information needed for the system to
recognize, validate and distribute an optional configuration part.

**Preconditions**: -

**Postconditions**: A file describing an optional configuration part has
been saved in the system configuration. The option to upload the
optional configuration part file is enabled in the GUI.

**Trigger**: Information not contained in the shared or private
parameters parts needs to be added to the global configuration.

**Main Success Scenario**:

1.  CS administrator creates an INI file (see \[[INI](#Ref_INI)\]) in the
    /etc/xroad/configuration-parts directory containing the following
    key-value pairs:

    a.  content-identifier = &lt;value&gt; (e.g., FOO)

    b.  file-name = &lt;value&gt; (e.g., foo.xml)

2.  CS administrator saves the created file.

**Extensions**: -

**Related information**:

-   The description file must be a valid INI file and the read
    permission of the created description file must be given to the
    “xroad” group.

-   The system uses the values of the content-identifier and file-name
    keys respectively as *Content-identifier* and *Content-file-name*
    MIME header values in the configuration directory (for further
    information, please see the document “X-Road: Protocol for
    Downloading Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\]) and also for displaying
    configuration part information in the GUI.

-   Editing or deleting the INI file manually is currently not supported
    and may result in inconsistent system behavior. The current solution
    assumes that the INI files describing optional configuration
    parameters are added, edited and deleted by software installation or
    update packages.