### 1.1 Overview

The Central Server manages the database of X-Road members and Security Servers. In addition, the Central Server contains the security policy of the X-Road instance. The security policy consists of the following items:

-   list of trusted certification authorities,

-   list of trusted time-stamping authorities,

-   tunable parameters such as maximum allowed lifetime of an OCSP response.

Both the member database and the security policy are made available to the Security Servers via HTTP protocol (see [Section 3.2](#32-download-configuration)). This distributed set of data forms the global configuration.

In addition to configuration distribution, the Central Server provides interface for performing management tasks such as adding and removing Security Server clients. These tasks are invoked from the user interface of the Security Servers. The management services are implemented as standard X-Road services and are offered via the central Security Server. See [Section 3.1](#31-management-services) for details.