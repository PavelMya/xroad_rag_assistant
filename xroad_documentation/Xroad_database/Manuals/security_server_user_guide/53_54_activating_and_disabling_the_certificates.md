### 5.4 Activating and Disabling the Certificates

**Access rights**

-   For authentication certificates: [Security Officer](#xroad-security-officer)

-   For signing certificates: [Security Officer](#xroad-security-officer), [Registration Officer](#xroad-registration-officer)

Disabled certificates are not used for signing messages or for establishing secure channels between Security Servers (authentication). If a certificate is disabled, its status in the "OCSP" column in the "Keys and Certificates" table is "Disabled". Certificate can be activated only when OCSP responses are valid.

To activate or disable a certificate, follow these steps.

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  To activate a certificate, click on the desired certificate's name.

    3.1 In the opening **Certificate** dialog, click **Activate**. To deactivate a certificate, click **DISABLE** in the **Certificate** dialog.