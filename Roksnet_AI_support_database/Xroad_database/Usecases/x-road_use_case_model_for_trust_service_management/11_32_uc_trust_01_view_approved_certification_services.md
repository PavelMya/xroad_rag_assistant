### 3.2 UC TRUST\_01: View Approved Certification Services

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of certification
services that have been approved and described for this X-Road instance.

**Preconditions**: -

**Postconditions**: The list of approved certification services has been
displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the list of approved certification
    services.

2.  System displays the list of approved certification services. The
    following information is displayed for each certification service.

    -   The value of the subject common name (CN) element from the
        certification service CA certificate is displayed as the name of
        the certification service.

    -   The validity period of the service CA certificate.

    The following user action options are displayed:
    
    -   add an approved certification service: 3.9;
    
    -   view the details of an approved certification service: 3.3;
    
    -   delete an approved certification service: 3.15.

**Extensions**: -

**Related information**: -