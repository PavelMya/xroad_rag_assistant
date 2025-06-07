### 3.21 UC SS\_20: View the Details of a Token

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator views the details of a security
token.

**Preconditions**: -

**Postconditions**: The details of the security token are displayed to
SS administrator.

**Trigger**: SS administrator wants to view the details of a security
token.

**Main Success Scenario**:

1.  SS administrator selects to view the details of a token.

2.  System displays the details of the token:

    -   the friendly name of the token;
    
    -   the identifier of the token;

    -   the technical token status information.

    The SS administrator has a possibility to choose amongst the following actions:

    -   edit the friendly name of the token: 3.23.

**Extensions**: -

**Related information**:

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.