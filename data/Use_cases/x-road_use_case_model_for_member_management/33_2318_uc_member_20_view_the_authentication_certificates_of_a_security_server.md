#### 2.3.18 UC MEMBER\_20: View the Authentication Certificates of a Security Server

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of authentication certificates registered for a security server.

**Preconditions**: -

**Postconditions**: The list of authentication certificates registered for the security server has been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the authentication certificates of a security server.

2.  System displays the list of authentication certificates registered for the security server. The following information is displayed for each certificate:

    -   the Common Name (CN) of the CA that issued the certificate;

    -   the serial number of the certificate;

    -   the Distinguished Name (DN) of the subject of the certificate;

    -   the expiry date of the certificate.

    The following user action options are displayed:

    -   view the details of an authentication certificate registered for the security server: [2.5.2](#252-uc-member_55-view-certificate-details);

    -   add an authentication certificate for the security server: [2.3.21](#2321-uc-member_23-create-an-authentication-certificate-registration-request);

    -   remove a registered authentication certificate of this security server: [2.3.22](#2322-uc-member_24-create-an-authentication-certificate-deletion-request).

**Extensions**: -

**Related information**: -