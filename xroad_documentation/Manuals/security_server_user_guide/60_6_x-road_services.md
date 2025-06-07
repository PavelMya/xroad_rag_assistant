## 6 X-Road Services

X-Road supports both SOAP and REST services. The services are managed on two levels:

-   the addition, deletion, and deactivation of services is carried out on the WSDL / REST API / OpenAPI 3 level;

-   the service address, internal network connection method, and the service timeout values are configured at the service level for SOAP services and at the API level for REST / OpenAPI 3 services. In addition, for SOAP / WSDL, it is easy to extend the configuration of one service to all the other services.

### 6.1 Adding a service description

**Access rights:** [Service Administrator](#xroad-service-administrator)