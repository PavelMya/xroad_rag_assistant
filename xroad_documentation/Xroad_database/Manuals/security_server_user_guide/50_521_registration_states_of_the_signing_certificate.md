#### 5.2.1 Registration States of the Signing Certificate

A Security Server signing certificate can be in one of the following registration states.

-   **Registered** – the certificate has been imported to the Security Server and saved to its configuration. A signing certificate in a "Registered" state can be used for signing X-Road messages.

-   **Deleted** – the certificate has been deleted from the server configuration. If the certificate is in the "Deleted" state and stored on a soft token key, the certificate will not be displayed in the table. If the certificate is in the "Deleted" state and stored on a hardware key device connected to the Security Server, the certificate status will be displayed with a **red circle** and a text **ONLY IN TOKEN**.