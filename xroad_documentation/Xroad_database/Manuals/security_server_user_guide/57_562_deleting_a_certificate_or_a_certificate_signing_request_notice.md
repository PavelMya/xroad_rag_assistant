#### 5.6.2 Deleting a Certificate or a certificate Signing Request notice

**Access rights**

-   For authentication certificates: [Security Officer](#xroad-security-officer)

-   For signing certificates: [Security Officer](#xroad-security-officer), [Registration Officer](#xroad-registration-officer)

An authentication certificate saved in the system configuration can be deleted if its state is "Saved", "Global error" or "Deletion in progress". The signing certificate and request notices can always be deleted from the system configuration.

**If a certificate is stored on a hardware security token, then the deletion works on two levels:**

-   if the certificate is saved in the server configuration, then the deletion **deletes the certificate from server configuration**, but not from the security token;

-   if the certificate is not saved in the server configuration (certificate's status has a red circle and status is "STORED IN TOKEN"), then the deletion deletes the certificate from the security token (assuming the token supports this operation).

**To delete a certificate, follow these steps.**

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  Click on the certificate that you want to delete.

    3.1 In the opening **Certificate** dialog, click **DELETE**. Confirm the deletion by clicking **YES**.

**To delete a certificate signing request notice (CSR), follow these steps.**

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  At the end of the desired CSR row click **Delete CSR**. Confirm the deletion by clicking **YES**.