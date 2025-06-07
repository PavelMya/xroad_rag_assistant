### 3.4 Federated Installation with Proxies

Scenario from the simple federated installation can be further developed by using configuration proxies. The figure below shows a setup where one X-Road installation uses proxies to cache both the incoming and outgoing shared parameters. Proxy is configured with a configuration anchor and it downloads and caches configuration from the source described by the anchor. Additionally, proxy acts as a configuration source and allows clients to download the cached configuration.

![Two federated X-Road installations with configuration proxies](img/pr-gconf-federated-installation-with-proxies.png)

Instead of direct references from private parameters of one installation to shared configuration source of the other installation, the X-Road installation 2 sets up two proxies. Proxy 1 downloads shared parameters of X-Road installation 2 and redistributes them to other X-Road installations. Proxy 2 downloads shared parameters of another X-Road installation (1 in this example) and distributes them to members of X-Road installation 2.

In this setup, the X-Road 2 has complete control over configuration that is exchanged with other X-Road installations – both incoming and outgoing. Using a proxy can improve availability of the shared parameters and reduce load on shared configuration sources of both X-Road installations. In addition, the proxies can transform the configuration, e.g. by filtering out some member classes. However, the filtering should be declared in the federation agreement to avoid any confusion among the members of the federated X-Road installations.

## Annex A. Examples

### A.1 Example of Configuration Anchor

```xml


    2014-05-20T16:42:55Z
    EE
    
        http://10.10.10.10/conf
        ZGVmYXVsdA==
    

```