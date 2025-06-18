#### 4.4.1 Registration and Management Service TLS certificate

Registration and Management Service TLS certificate is used to secure the communication between:
- the management Security Server and the member management web service;
- a Security Server and the registration web service.

To see Registration and Management Service TLS certificate info, follow these steps.

1. In the Navigation tabs, select Settings --> TLS certificates.
2. Locate the Management service TLS certificate section and click certificate hash.

To download Management Service TLS certificate, follow these steps.

1. In the Navigation tabs, select Settings --> TLS certificates.
2. Locate the Management service TLS certificate section.
3. Click button Download certificate and save the prompted file.

To re-create Management Service key and self-signed certificate, follow these steps.

1. In the Navigation tabs, select Settings --> TLS certificates.
2. Locate the Management service TLS certificate section and click button Re-create key.
3. Confirm the re-creating by clicking Confirm.
4. Complete the activities defined in section [4.4.1.1 Necessary activities after changing certificate](#4411-necessary-activities-after-changing-certificate)

To generate Management Service certificate signing request, follow these steps.

1. In the Navigation tabs, select Settings --> TLS certificates.
2. Locate the Management service TLS certificate section and click button Generate CSR.
3. Read the information and enter Distinguished name and click button Generate CSR.
4. Save prompted file into a safe place.
5. Apply for a TSL/SSL certificate from a trusted Certificate Authority (CA) using the CSR file.

To upload Management Service certificate, follow these steps.

1. In the Navigation tabs, select Settings --> TLS certificates.
2. Locate the Management service TLS certificate section and click button Upload certificate.
3. Find the proper certificate file and click Open, to finish certificate uploading click button Upload.
4. Complete the activities defined in section [4.4.1.1 Necessary activities after changing certificate](#4411-necessary-activities-after-changing-certificate)