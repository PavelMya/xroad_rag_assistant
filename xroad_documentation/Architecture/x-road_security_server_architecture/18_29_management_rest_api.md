### 2.9 Management REST API

The management REST API offers endpoints that can be used to read and modify the security server configuration.
These endpoints are used by the user interface frontend, and can be used by standalone API clients.
The management REST API is packaged in an executable Spring Boot\[[2](#Ref_2)\] *jar* archive.
This Spring Boot application starts an embedded Tomcat\[[3](#Ref_3)\] servlet engine, which also serves the resources for the user interface frontend.
Embedded Tomcat listens on a fixed port that is configured in internal configuration files.
In addition, the application listens to incoming \[[ACME](#Ref_ACME)\] challenge requests from the ACME server on port 80.

Management REST API endpoints are documented using an OpenAPI 3 definition: \[[REST_UI-API](#Ref_REST_UI-API)\].
For more information on OpenAPI 3, see \[[OPENAPI](#Ref_OPENAPI)\].


Certain API operations attempt to modify the X-Road global configuration and require management requests to be sent to the X-Road central server. These requests need to be approved by the central server administrator before they are reflected in the global configuration.

Some operations might also trigger sending an e-mail notification to the mail server which must be configured beforehand in /etc/xroad/conf.d/mail.yml (e.g. host, port, username etc.).

User action events that change the system state or configuration are logged into the audit log. The actions are logged regardless of whether the outcome was a success or a failure. The complete list of the audit log events is described in \[[SPEC-AL](#Ref_SPEC-AL)\].


\[2\] See  for details.


\[3\] See  for details.