### 3.16 UC TRUST\_15: View Approved Timestamping Services

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the approved timestamping
services configured for this X-Road instance.

**Preconditions**: -

**Postconditions**: The list of approved timestamping services has been
displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view approved timestamping services.

2.  System displays the list of timstamping services. The following
    information is displayed for each timestamping service.

    -   The value of the subject common name (CN) element from the TSA
        certificate is displayed as the name of the timestamping
        service.

    -   The validity period of the certificate of the TSA.

    The following user action options are displayed:

    -   add an approved timestamping service: 3.17;
    
    -   view the details of a TSA certificate: 3.4;
    
    -   edit the timestamping server URL of an approved timestamping
        service: 3.18;
    
    -   delete an approved timestamping service: 3.19.

**Extensions**: -

**Related information**: -