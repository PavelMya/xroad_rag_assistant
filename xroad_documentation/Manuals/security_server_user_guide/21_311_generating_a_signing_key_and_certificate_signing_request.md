#### 3.1.1 Generating a Signing Key and Certificate Signing Request

**Access rights:**

-   All activities: [Security Officer](#xroad-security-officer)

-   All activities except logging into the key device: [Registration Officer](#xroad-registration-officer)

-   Logging in to the key device: [System Administrator](#xroad-system-administrator)

To generate a Signing key and a Certificate Signing Request, follow these steps.

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  If you are using a hardware security token, ensure that the device is connected to the Security Server. The device information must be displayed in the **SIGN AND AUTH KEYS** table.

3.  To log in to the token, click **LOG IN** on the token's row in the table and enter the PIN code. Once the correct PIN is entered, the **LOG IN** button changes to **LOG OUT**.

4.  To generate a signing key and CSR for it, expand the token's information by clicking the caret next to the token name and click **ADD KEY**. In the wizard that opens

    1. Define a label for the newly created signing key (not mandatory) and click **NEXT**.

    2. In the dialog page that opens

       1. Select the certificate usage policy from the **Usage** drop down list (SIGNING for signing certificates)

       2. Select the X-Road member the certificate will be issued for from the **Client** drop-down list

       3. Select the issuer of the certificate from the **Certification Service** drop-down list

       4. Select the format of the certificate signing request (PEM or DER) from the **CSR Format** drop-down list, according to the certification service provider's requirements

       5. Click **CONTINUE**

    3. In the dialog that opens

       1. Review the certificate owner's information that will be included in the CSR and fill in the empty fields, if needed

       2. Click **GENERATE CSR**

       3. Click **DONE**

After the generation of the CSR, a "Request" record is added under the key's row in the table, indicating that a certificate signing request has been created for this key. The record is added even if the request file was not saved to the local file system.

**To certify the signing key, transmit the certificate signing request to the approved certification service provider and accept the signing certificate created from the certificate signing request.**