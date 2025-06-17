### 2.1 Goals and assumptions

The primary goal of the load balancing support is, as the name suggests, load balancing, not fault tolerance.
A clustered environment increases fault tolerance but some X-Road messages can still be lost if a Security Server node fails.

The implementation does not include a load balancer component. It should be possible to use any external load balancer
component that supports HTTP-based health checks for the nodes, load balancing at the TCP level and TLS passthrough (e.g., haproxy, nginx,
AWS NLB or Classic Load Balancer, or a hardware appliance). A health check service is provided for monitoring a node's
status, this is described in more detail in section [3.4 Health check service configuration](#34-health-check-service-configuration).
The load balancer must be configured to use TSL passthrough so that TLS termination is performed by the Security Server and 
not by the load balancer.

The load balancing support is implemented with a few assumptions about the environment that users should be aware of.
Carefully consider these assumptions before deciding if the supported features are suitable for your needs.