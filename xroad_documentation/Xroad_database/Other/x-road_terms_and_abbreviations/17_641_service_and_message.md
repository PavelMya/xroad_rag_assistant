#### 6.4.1 Service and message

**Dataservice** – web-service executed by a member of X-Road, in order to enable access to the resources of information system of X-Road dataservice provider. The predefined request-response, sent by the information system of a member to the information system of another member and receiving agreed data in response.

**Management service** – services provided by the X-Road governing organization to manage security servers and security server clients. Management services are implemented as standard X-Road services following X-Road message protocol.

**Message** – Data set meeting profile description and service description required by X-Road governing authority. Messages are divided into requests and responses. SOAP message consists of headers and a SOAP body that contains service specific content. REST message consists of HTTP verb, path, query parameters, HTTP headers and message body.

**Metadata service** – services between members executed by X-Road governing authority, enabling members of X-Road to get an overview of X-Road (e.g. enabling to get an overview of completed services and access rights needed for the consumption of services). Generally, it shall meet the description of X-Road service.

**Monitoring services** – The X-Road monitoring solution is conceptually split into two parts: environmental and operational monitoring. 

- **Environmental monitoring** – is the monitoring of the X-Road environment: details of the security servers such as operating system, memory, disk space, CPU load, running processes and installed packages, etc.

- **Operational monitoring** – is the monitoring of operational statistics such as which services have been called, how many times, what is the average response time, etc.
    + **Operational monitoring data** – contains operational data (such as which services have been called, how many times, what was the size of the response, etc.) of the X-Road security server(s).
    + **Operational monitoring daemon** – collects and shares operational monitoring data of the X-Road security server(s), calculates and shares health data of the X-Road security server(s) that is based on collected operational monitoring data.

**Service client** – is an X-Road member, subsystem, local access rights group or global access rights group that has access rights to one or more services of a security server client.

**X-Road service** – SOAP- or REST-based web service or API that is offered by an X-Road member or by a subsystem and that can be used by other X-Road members or subsystems.