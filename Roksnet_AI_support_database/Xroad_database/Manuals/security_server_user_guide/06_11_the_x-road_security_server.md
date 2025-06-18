### 1.1 The X-Road Security Server

The main function of a Security Server is to mediate requests in a way that preserves their evidential value.

The Security Server is connected to the public Internet from one side and to the information system within the organization's internal network from the other side. In a sense, the Security Server can be seen as a specialized application-level firewall that supports the SOAP and REST protocols; hence, it should be set up in parallel with the organization's firewall, which mediates other protocols.

The Security Server is equipped with the functionality needed to secure the message exchange between a client and a service provider.

-   Messages transmitted over the public Internet are secured using digital signatures and encryption.

-   The service provider's Security Server applies access control to incoming messages, thus ensuring that only those users that have signed an appropriate agreement with the service provider can access the data.

To increase the availability of the entire system, the service user's and service provider's Security Servers can be set up in a redundant configuration as follows.

-   One service user can use multiple Security Servers in parallel to perform requests.

-   If a service provider connects multiple Security Servers to the network to provide the same services, the requests are load-balanced between the Security Servers.

-   If one of the service provider's Security Servers goes offline, the requests are automatically redirected to other available Security Servers.

The Security Server also depends on a Central Server, which provides the global configuration.

### 1.2 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].