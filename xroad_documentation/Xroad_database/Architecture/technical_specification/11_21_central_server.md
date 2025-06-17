### 2.1 Central Server

Central server (see \[[ARC-CS](#Ref_ARC-CS)\] for details) manages the database of X-Road members and security servers. In addition, the central server contains the security policy of the X-Road instance. The security policy consists of the following items:

-   list of trusted certification authorities,

-   list of trusted time-stamping authorities,

-   tunable parameters such as maximum allowed lifetime of an OCSP response.

Both the member database and the security policy are made available to the security servers via HTTP protocol (see Section [3.2](#32-protocol-for-downloading-configuration)). This distributed set of data forms the global configuration.

In addition to configuration distribution, the central server provides interface for performing management tasks such as adding and removing security server clients. These tasks are invoked from the user interface of the security servers. The management services are implemented as standard X-Road services and offered via central security server. See Section [3.6](#36-management-services-protocol) for details.