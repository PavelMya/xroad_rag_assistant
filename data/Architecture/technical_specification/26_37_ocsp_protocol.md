### 3.7 OCSP Protocol

The OCSP protocol (see \[[OCSP](#Ref_OCSP)\]) is used by the security servers to query the validity information about the signing and authentication certificates.

OCSP protocol is synchronous protocol that is offered by the OCSP responder belonging to a certification authority.

In X-Road, each security server is responsible for downloading and caching the validity information about its certificates. The OCSP responses are sent to the other security servers as part of the message transport protocol (see Section [3.3](#33-message-transport-protocol)). This ensures that the security servers do not need to discover the OCSP service used by the other party. Additionally, this arrangement supports the situation where access to the OCSP service is either restricted to certificate owners or is subject to charges.

The security servers never include nonce field in the OCSP request. This allows the OCSP service to employ various optimization strategies, such as pre-creating the OCSP responses.

Because OCSP responses are used in the process of certificate validation, failure of the OCSP service effectively disables X-Road message exchange. When the cached OCSP responses cannot be refreshed, the security servers are unable to communicate. Thus, the lifetime of the OCSP responses determines the maximum amount of time that the OCSP service can be unavailable. The lifetime is defined by the owner of the central server and can vary between different instances of X-Road.