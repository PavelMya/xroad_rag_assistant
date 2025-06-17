### 10.4 Changing the Internal TLS Key and Certificate

**Access rights:** [Security Officer](#xroad-security-officer), [System Administrator](#xroad-system-administrator)

_To change the Security Server's internal TLS key and certificate_, follow these steps.

1. On the **Navigation tabs**, select **Keys and Certificates**

2. In the opening view, select **SECURITY SERVER TLS KEY** tab

3. In the opening view, click **GENERATE KEY** and in the dialog that opens, click **CONFIRM**.

   The Security Server generates a key used for communication with the client information systems, and the corresponding self-signed certificate. The Security Server's certificate fingerprint will also change. The Security Server's domain name is saved to the certificate's **Common Name** field, and the internal IP address to the **subjectAltName** extension field.

_To generate a new certificate request_, follow these steps.

1. On the **Navigation tabs**, select **KEYS AND CERTIFICATES**

2. In the opening view, select **SECURITY SERVER TLS KEY** tab

3. In the "TLS Key and Certificate" section, at the end of the key row, click **Generate CSR**

4. In the opening view, input the **Distinguished Name** and click **GENERATE CSR**. Save the certificate request file to the local file system and click **DONE**.

   The Security Server generates a certificate request using the current key and the provided **Distinguished Name**.

_To import a new TLS certificate_, follow these steps.

1. On the **Navigation tabs**, select **KEYS AND CERTIFICATES**

2. In the opening view, select **SECURITY SERVER TLS KEY** tab

3. In the opening view, click **IMPORT CERT.** and point to the file to be imported.

   The imported certificate must be in PEM-format to be accepted. Certificate chains are supported; concatenate possible intermediate certificate(s) to the server certificate before importing the file.

_To export the Security Server's internal TLS certificate_, follow these steps.

1. On the **Navigation tabs**, select **KEYS AND CERTIFICATES**

2. In the opening view, select **SECURITY SERVER TLS KEY** tab

3. In the opening view, click **EXPORT CERT.** and save the prompted file to the local file system.

   Note that only the internal server certificate is exported, not the possible intermediate certificates.

_To view the detailed information of the Security Server's internal TLS certificate_, follow these steps.

1. On the **Navigation tabs**, select **Keys and Certificates**

2. In the opening view, select **SECURITY SERVER TLS KEY** tab

3. In the "TLS Key and Certificate" section, click on the certificate hash.