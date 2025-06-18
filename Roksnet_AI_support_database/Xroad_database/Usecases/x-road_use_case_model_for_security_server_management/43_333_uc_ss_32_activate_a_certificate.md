### 3.33 UC SS\_32: Activate a Certificate

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors**: SS administrator

**Brief Description**: SS administrator activates a certificate. The
security server can use active certificates for establishing a secure
data exchange channel between security servers (authentication
certificates) or for signing messages (signing certificates).

**Preconditions**: The certificate is in disabled state.

**Postconditions**: The certificate is activated.

**Trigger**: SS administrator wants to activate a certificate.

**Main Success Scenario**:

1.  SS administrator selects to activate a certificate.

2.  System activates the certificate and displays the latest OCSP
    response value (if such exists, otherwise the value “unknown”) for
    this certificate as the status of OCSP response.

3.  System logs the event “Enable certificate” to the audit log.

**Extensions**: -

**Related information:**

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.