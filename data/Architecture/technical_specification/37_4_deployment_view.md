## 4 Deployment View

[Figure 2](#Deployment_view_of_X_Road) shows deployment view of a basic X-Road instance. In practice, all the components can use redundancy to improve availability and throughput. The deployment options for various components are described in the detailed architecture documents.

The diagram also shows what components are installed and hosted by any given organization. The governing authority installs and maintains central server and central security server. The configuration proxy is an optional component that is typically used for distributing configuration to federated X-Road instances. The service client and service provider organizations host their information system and security server that connects the information system to the X-Road.

<a id="Deployment_view_of_X_Road" class="anchor"></a>
![](img/arc-g_deployment_view_of_x_road.svg)

Figure 2. Deployment view of X-Road