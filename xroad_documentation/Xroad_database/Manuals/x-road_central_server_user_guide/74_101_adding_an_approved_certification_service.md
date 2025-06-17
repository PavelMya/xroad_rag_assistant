### 10.1 Adding an Approved Certification Service

Access rights: System Administrator

To add a certification service, follow these steps.
1. In the Trust Services tab, click Add certification service
2. Locate the certification service CA certificate file and click Upload.
3. Set the certification service settings as follows.
  - If the certification service issues only authentication certificates, check the "This CA can only be used for TLS authentication" checkbox. However, if the certification service issues additionally or only signing certificates, leave the checkbox empty.
  - Enter the fully qualified class name that implements the ee.ria.xroad.common.certificateprofile.CertificateProfileInfo interface to the field Certificate profile info (for example: ee.ria.xroad.common.certificateprofile.impl.SkKlass3CertificateProfileInfoProvider).
  - If the certification service supports ACME, then check the "This CA can be used for ACME" checkbox. This will reveal additional ACME specific fields:
    - ACME server directory URL (required): used by the Security Servers to do certificate related operations via the ACME Server API.
    - ACME server IP address(es): a list of ACME Server source IPs that are used to complete the ACME HTTP challenge with the Security Server. Multiple addresses are separated by a comma. This information is shown in the Security Server UI.
    - Authentication certificate profile ID: profile ID used for some ACME servers to let them know the certificate usage type when ordering an authentication certificate.
    - Signing certificate profile ID: profile ID used for some ACME servers to let them know the certificate usage type when ordering a signing certificate.
  - If the CA certificate contains the certification service CA’s OCSP service information, and the PKI does not have intermediate CAs, the procedure is complete.
4. If necessary, enter the certification service CA’s OCSP service URL and certificate in the OCSP Responders tab by clicking Add.
5. Information about intermediate CAs can be added in the Intermediate CAs tab.
To add a new intermediate CA
  - click Add;
  - in the window that opens, locate the certificate file of the intermediate CA and click Save;
  - to add OCSP service information to the new intermediate CA, click on the added intermediate CA, in the window that opens, locate OCSP Responders tab and click Add.