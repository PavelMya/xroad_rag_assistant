### 3.2 UC FED\_01: View Trusted Anchors

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of trusted
anchors.

**Preconditions**: -

**Postconditions**: The list of trusted anchors has been displayed to CS
administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view trusted anchors.

2.  System displays the list of trusted anchors uploaded to the central
    server. For each anchor, the following information is displayed:

    -   the instance identifier of the X-Road instance the trusted
        anchor originates from;

    -   the SHA-224 hash value of the trusted anchor file;

    -   the generation date and time (UTC) of the trusted anchor file.
        
         The following user action options are displayed:

    -   upload a trusted anchor: 3.3;
    
    -   download a trusted anchor: 3.7;
    
    -   delete a trusted anchor: 3.8.

**Extensions**: -

**Related information**: -