### 3.2 Detached Shared Parameters

This scenario involves a standalone X-Road instance that uses different configuration sources for private and shared parameters.

In this case the X-Road governing authority manages two configuration sources. The first source contains the private parameters and, optionally, other configuration parts that are specific to this X-Road instance. The second source contains shared parameters. The private parameters part contains anchor for the second configuration source. Figure below illustrates this situation.

![X-Road installation with detached shared parameters](img/pr-gconf-detached-shared-parameters.png)

Compared to the simplest case, the configuration authority must maintain two separate configuration sources. Additionally, the configuration clients must make additional HTTP requests to download the directory from *Source 2*. For a non-federated installation, this solution does not offer significant benefits, but it is a good starting point for building a federated X-Road infrastructure.