### 5.1 Simple Deployment

This section describes a simple scenario where the Central Server is installed on a standalone server without the use of redundancy. The signing key is stored on a HSM device. This setup is useful for testing environments and for X-Road instances where availability is not of critical concern.



![](img/arc-cs_simple_deployment_of_the_central_server.svg)

Figure 3. Simple deployment of the Central Server

Optionally, an SSCD can be connected with the Central Server if global configuration signatures are to be provided by a cryptographic hardware device.