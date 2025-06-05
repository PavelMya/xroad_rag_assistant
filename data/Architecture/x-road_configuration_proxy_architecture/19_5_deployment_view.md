## 5 Deployment View

The configuration proxy is deployed on a separate server on the configuration provider's side and, optionally, on the configuration client's side as well.

[Figure 3](#Ref_Configuration_proxy_deployment_example) shows a possible deployment scenario for the configuration proxy. In the presented scenario the instance \#1 central server is distributing it's internal and external configuration through a configuration proxy to instance \#1 members and an instance \#2 configuration proxy, respectively. The instance \#2 central server distributes it's internal configuration directly to instance \#2 members and it's external configuration directly to instance \#1 members.


<a id="Ref_Configuration_proxy_deployment_example" class="anchor"></a>
![](img/arc-cp_configuration_proxy_deployment_example.png)

Figure 3. Configuration proxy deployment example

Optionally, an SSCD can be connected with the configuration proxy if global configuration signatures are to be provided by a cryptographic hardware device.

For detailed information on installing and configuring the configuration proxy refer to the configuration proxy manual \[[UG-CP](#Ref_UG-CP)\].