#### 2.2.2 UC GCONF\_02: Download a Configuration Source Anchor File

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator downloads the configuration
anchor of a configuration source.

**Preconditions**: The anchor file has been generated.

**Postconditions**: CS administrator has downloaded the anchor file.

**Trigger**: CS administrator wishes to download the configuration
anchor, either to view its contents or to distribute the anchor to
configuration clients.

**Main Success Scenario**:

1.  CS administrator selects to download the configuration anchor of a
    configuration source (internal or external).

2.  System presents the configuration anchor file for downloading.

3.  CS administrator saves the anchor file to the file system of the
    local computer.

**Extensions**: -

**Related information**:

-   The contents and format of the configuration anchor file is
    described in the document “X-Road: Protocol for Downloading
    Configuration” \[[PR-GCONF](#Ref_PR-GCONF)\].