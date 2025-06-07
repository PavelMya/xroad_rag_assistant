#### 3.2.2 Generating a Certificate Signing Request for an Authentication Key

**Access rights:** [Security Officer](#xroad-security-officer)

To generate a certificate signing request (CSR) for the authentication key, follow these steps.

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  On the row of the desired key, click **Generate CSR**. In the dialog that opens

    2.1  Select the certificate usage policy from the **Usage** drop down list (AUTH for authentication certificates);

    2.2  select the issuer of the certificate from the **Certification Service** drop-down list;

    2.3  select the format of the certificate signing request (PEM or DER), according to the certification service provider's requirements

    2.4  click **CONTINUE**;

3.  In the form that opens, review the information that will be included in the CSR and fill in the empty fields, if needed.

4.  Click **GENERATE CSR** to complete the generation of the CSR and save the prompted file to the local file system.

    1. Or click **ORDER CERTIFICATE** to also use the CSR to immediately make an order to the ACME server if the chosen Certification Service supports it.

5. Click **DONE**

After the generation of the CSR, a "Request" record is added under the key's row in the table, indicating that a certificate signing request has been created for this key. The record is added even if the request file was not saved to the local file system. (In case of a successful ACME order, the certificate will also be imported to the Security Server and be shown under the key's row instead of the CSR.)

**To certify the authentication key, transmit the certificate signing request to the approved certification service provider and accept the authentication certificate created from the certificate signing request.**