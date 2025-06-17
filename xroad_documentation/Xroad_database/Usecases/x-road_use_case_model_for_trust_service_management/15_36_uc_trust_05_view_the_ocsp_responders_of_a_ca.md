### 3.6 UC TRUST\_05: View the OCSP Responders of a CA

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the OCSP responders
configured for a CA.

**Preconditions**: -

**Postconditions**: The OCSP responders configured for a CA have been
displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the OCSP responders of a CA.

2.  System displays the list of configured OCSP responders. For each
    OCSP responder, the following information is displayed:

    -   the URL of the OCSP server.

    The following user action options are displayed:

    -   add an OCSP responder for the CA: 3.11;
    
    -   view the details of the OCSP responder certificate (if a certificate
        has been uploaded for this OCSP responder): 3.4;
    
    -   edit the information of an OCSP responder: 3.11;
    
    -   delete an OCSP responder from the CA: 3.12.

**Extensions**: -

**Related information**: -