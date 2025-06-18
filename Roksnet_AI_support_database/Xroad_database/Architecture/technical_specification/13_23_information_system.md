### 2.3 Information System

The information system (IS) uses and/or provides services via the X-Road.

For the service client IS, the security server acts as an entry point to all the X-Road services (see Section [3.1](#31-x-road-message-protocol)). The client IS is responsible for implementing an user authentication and access control mechanism that complies with the requirements of the particular X-Road instance. The identity of the end user is made available to the service provider by including it in the service request. The client can discover the X-Road members and available services by using the X-Road metadata protocol (see Section [3.4](#34-service-metadata-protocol)).

The service provider information system implements a SOAP or a REST service and makes it available over the X-Road. For this purpose, the service must conform to the X-Road message protocol for SOAP or message protocol for REST (see Section [3.1](#31-x-road-message-protocol)). A SOAP service must be accompanied by a WSDL service description, and a REST service may be accompanied by an OpenAPI Specification v3.