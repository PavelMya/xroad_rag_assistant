### 3.13 UC SS\_12: Export the TLS Certificate of the Security Server

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator exports the internal TLS
certificate of the security server to the local file system.

**Preconditions**: An internal TLS certificate has been created.

**Postconditions**: The internal TLS certificate has been exported.

**Trigger**: SS administrator wants to export an internal TLS
certificate.

**Main Success Scenario**:

1.  SS administrator selects to export the internal TLS certificate of
    the security server.

2.  System prompts a tar.qz file for downloading, that contains the TLS
    certificate in PEM and CER format.

3.  SS administrator saves the file to the local file system.

**Extensions**: -

**Related information**: -