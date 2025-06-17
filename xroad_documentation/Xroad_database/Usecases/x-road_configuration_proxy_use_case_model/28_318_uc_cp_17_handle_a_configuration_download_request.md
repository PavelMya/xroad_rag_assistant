### 3.18 UC CP\_17: Handle a Configuration Download Request

**System**: Configuration proxy

**Level**: System task

**Component:** Configuration proxy, security server, central server

**Actor**: Configuration client

**Brief Description**: System receives a configuration download request
from a configuration client and responds.

**Preconditions**: Signed configuration directory and configuration part
files are made available for downloading (see 3.17).

**Postconditions**: The configuration client has received either the
requested configuration item (signed configuration directory or a
configuration part file) or an error message.

**Trigger**: Download request from a configuration client.

**Main Success Scenario**:

1.  Configuration client requests to download the signed configuration
    directory or a configuration part file.
    
2.  System responds with the requested files.

**Extensions**:

- 2a. Request cannot be served.
    - 2a.1. System responds with an error message.

**Related information**: -