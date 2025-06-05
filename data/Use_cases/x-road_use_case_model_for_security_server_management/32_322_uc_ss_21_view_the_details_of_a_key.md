### 3.22 UC SS\_21: View the Details of a Key

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator views the details of a key.

**Preconditions**: -

**Postconditions**: The details of the key are displayed to SS
administrator.

**Trigger**: SS administrator wants to view the details of a key.

**Main Success Scenario**:

1.  SS administrator selects to view the details of a key.

2.  System displays the following information:

    -   the friendly name of the key;
    
    -   the identifier of the key;
    
    -   the label of the key;
    
    -   the information, whether the key is read-only or not.

    The SS administrator has a possibility to choose amongst the following actions:

    -   edit the friendly name of the key: 3.24.

**Extensions**: -

**Related information**:

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.