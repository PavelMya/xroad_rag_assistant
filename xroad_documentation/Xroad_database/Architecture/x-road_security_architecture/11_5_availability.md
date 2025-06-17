## 5 Availability

For compliance with the security principle of availability, the objective is to ensure that X-Road assets are readily available to authorised X-Road actors that require them. With assurance of availability, the threat being mitigated is the denial to authorised actors of X-Road services.

Availability is a cornerstone of critical infrastructure. X-Road is designed so that no component is a system-wide bottleneck or point of failure. Security Servers remain operational even if Central Server, OCSP service and/or time-stamping service would fail. The grace period depends on the failing component and configuration of the X-Road instance.

X-Road Security Servers incorporate denial-of-service mitigation functionality. X-Road Linux services will automatically restart after a local system crash. 

To fortify the availability of the entire X-Road system, the service consumer’s/user's and service provider's Security Servers may be set up in a redundant configuration as follows:

  * One service user can use multiple Security Servers in parallel to perform requests.
  * If a service provider connects multiple Security Servers to the network to provide the same services, the requests are load-balanced amongst the Security Servers.
  * If one of the service provider's Security Servers goes offline, the requests are automatically redirected to other available Security Servers.