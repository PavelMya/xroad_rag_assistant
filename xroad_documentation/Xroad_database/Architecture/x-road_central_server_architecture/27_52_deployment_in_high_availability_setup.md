### 5.2 Deployment in High Availability Setup

This section describes the deployment of the Central Server in a cluster, for achieving high availability.

The High Availability (HA) solution for the X-Road Central Server relies on a shared, optionally highly available database. There can be multiple Central Server nodes each connecting to the same database instance. Furthermore, the database can be set up in high-availability mode where there is the primary node with read/write access and one or more secondary read-only nodes replicating the primary data as it changes.

In a high availability setup, the configuration clients can use any of the nodes for downloading configuration. It is up to the client implementations to choose the algorithm for selecting this node at each particular download attempt.

The Central Server's high availability is described in more detail in the document \[[IG-CSHA](#Ref_IG-CSHA)\].