#### 3.2.1 Generating an Authentication Key

**Access rights**

-   All activities: [Security Officer](#xroad-security-officer)

-   Logging in to the key device: [System Administrator](#xroad-system-administrator)

**The Security Server's authentication keys can only be generated on software security tokens.**

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  To log in to the software token, click **LOG IN** on the token's row in the table and enter the token's PIN code. Once the correct PIN is entered, the **LOG IN** button changes to **LOG OUT**.

3.  Show more details about the token by clicking the caret next to the token name.

4.  To generate an authentication key and CSR for it, click the **ADD KEY** button below the token row. In the wizard that opens

    1. Define a label for the newly created authentication key (not mandatory) and click **NEXT**.

    2. In the dialog page that opens

       1. Select the certificate usage policy from the **Usage** drop down list (AUTHENTICATION for authentication certificates)

       2. Select the issuer of the certificate from the **Certification Service** drop-down list

       3. Select the format of the certificate signing request (PEM or DER) from the **CSR Format** drop-down list, according to the certification service provider's requirements

       4. Click **CONTINUE**

    3. In the dialog that opens

       1. Review the certificate owner's information that will be included in the CSR and fill in the empty fields, if needed

       2. Click **GENERATE CSR**

       3. Click **DONE**