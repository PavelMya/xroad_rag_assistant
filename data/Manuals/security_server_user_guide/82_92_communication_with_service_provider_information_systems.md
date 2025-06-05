### 9.2 Communication with Service Provider Information Systems


The connection method for information systems in the **service provider role** is determined by the protocol in the URL. To change the connection method, follow these steps.

1.  In the **Navigation tabs**, select **CLIENTS**, select a Security Server owner or a client from the table.

2.  In the view that opens, select the **SERVICES** tab.

3.  Click the caret next to the desired service description to show all services related to it.

4.  Click on a service code in the table.

5.  In the view that opens, change the protocol (a.k.a. scheme) part in the Service URL to either **http://** or **https://**.

- HTTP – the service/adapter URL begins with "**http:**//...".

- HTTPS – the service/adapter URL begins with "**https**://".
  - If **Verify TLS certificate** checkbox is left unchecked it means that service provider information system's TLS certificate is not verified and trusted by default.
  - If **Verify TLS certificate** checkbox is checked it means that service provider information system's TLS certificate is verified. In order to make the information system's TLS certificate trusted, it must be added into Security Server's **Information System TLS certificate** list (see section [9.3](#93-managing-information-system-tls-certificates)).
  - When the service provider information system needs to verify the Security Server's internal TLS certificate, the certificate must be first exported and then imported into the service provider information system's truststore (see section [9.3](#93-managing-information-system-tls-certificates)).