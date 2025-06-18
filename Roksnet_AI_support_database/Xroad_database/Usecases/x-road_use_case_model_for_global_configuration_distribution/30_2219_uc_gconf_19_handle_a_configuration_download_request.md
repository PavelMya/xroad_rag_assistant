#### 2.2.19 UC GCONF\_19: Handle a Configuration Download Request 

**System**: Central server

**Level**: System task

**Component:** Central server, security server, configuration proxy

**Actor**: Configuration client

**Brief Description**: System receives a configuration download request
from a configuration client and responds.

**Preconditions**: Signed configuration directory and configuration part
files have been made available for downloading.

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
    - 2a1. System responds with an error message.

**Related information**: -

### 2.3 Security Server Use Cases