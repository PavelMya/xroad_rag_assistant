### 3.34 UC SS\_33: Disable a Certificate

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator disables a certificate.
Certificates in disabled state are not used for signing or
authentication.

**Preconditions**: A certificate is in active state.

**Postconditions**: The certificate is disabled.

**Trigger**: SS administrator wants to disable a certificate.

**Main Success Scenario**:

1.  SS administrator selects to disable a certificate.

2.  System disables the certificate and sets the status of OCSP response
    to “disabled”. OCSP responders are not queried for disabled
    certificates.

3.  System logs the event “Disable certificate” to the audit log.

**Extensions**: -

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.