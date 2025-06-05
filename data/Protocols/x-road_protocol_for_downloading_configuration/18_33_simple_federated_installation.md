### 3.3 Simple Federated Installation

This scenario involves two federated X-Road installations. Both installations are set up according to "Detached Shared Parameters". Figure below describes the setup. Both X-Road installations maintain two configuration sources, one for private parameters, the other one for shared parameters. For both installations, the private parameters part contains configuration anchors for both of the sources that distribute shared parameters.

![Two federated X-Road installations](img/pr-gconf-simple-federated-installation.png)

Members of the X-Road installations are initialized with configuration anchor pointing to private configuration source of their governing installation. This source is then used to download private parameters that contains configuration anchors for the sources that distribute shared parameters.