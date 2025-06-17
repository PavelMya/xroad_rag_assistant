### 2.1 Prerequisites to Installation

The Central Server software assumes an existing installation of the Ubuntu 22.04 LTS or 24.04 LTS operating system, on an x86-64bit platform. To provide management services, a Security Server is installed alongside the Central Server.

The Central Server’s software can be installed both on physical and virtualized hardware (of the latter, Xen and Oracle VirtualBox have been tested).

There are many alternatives how the Central Server can be deployed. The options are described in [Annex C Deployment Options](#annex-c-deployment-options).

If the Central Server is a part of a cluster for achieving high availability (deployment option remote database cluster or cloud database cluster), the database cluster must be installed and configured before the Central Server itself can be installed. Please refer to the Central Server High Availability Installation Guide [IG-CSHA](#Ref_IG-CSHA) for details.