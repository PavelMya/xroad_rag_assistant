### 2.2 Communication with external servers and services: The cluster from the point of view of a client or service

When external Security Servers communicate with the cluster, they see only the public IP address of the cluster which is
registered to the global configuration as the Security Server address. From the caller point of view, this case is analogous
to making a request to a single Security Server.

![inbound traffic](img/load_balancing_traffic.png)

When a Security Server makes a request to an external server (Security Server, OCSP, TSA or a Central Server), the
external server sees only the public IP address. Note that depending on the configuration, the public IP address
might be different from the one used in the previous scenario. It should also be noted that the Security Servers will
independently make requests to OCSP and TSA services as well as to the Central Server to fetch the global configuration
as needed.

![outbound traffic](img/load_balancing_traffic-2.png)

### 2.3 State replication from the primary to the secondaries

![state replication](img/load_balancing_state_replication.png)

#### 2.3.1 Replicated state