### 3.6 Management Services Protocol

The management services are called by security servers to perform management tasks such as registering a security server client or deleting an authentication certificate.

The management service protocol is a synchronous RPC-style protocol that is offered by the member management and registration web services. The services are called by security servers.

The management services are implemented as standard X-Road services (see Section 3.1 for details) that are offered by the organization managing the X-Road instance. The exception is the authentication certificate registration service that, for technical reasons, is implemented directly by the registration web service. Full details of the management services are described in \[[PR-MSERV](#Ref_PR-MSERV)\].

In general, the management services are not critical to operation of X-Road and therefore their availability is not paramount. If the management services are unavailable, the security servers cannot manage their clients and authentication certificates. Some actions (such as removing clients and certificates) can be performed manually by central server administrator, without using the management services. The management service operations are not time-critical (the security server user explicitly chooses to send the management request and the user interface does not imply that this operation is instantaneous).