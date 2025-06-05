## 4 Configuration Creation Workflow

X-Road Central Server periodically assembles the global configuration, consisting of XML files describing private and shared parameters, as well as any additional configuration parts installed by add-ons (see \[[PR-GCONF](#Ref_PR-GCONF)\] for detailed information about configuration structure).

Configuration files are distributed in accordance with the protocol for downloading configuration (see [Section 3.2](#32-download-configuration)). MIME messages are generated to represent internal and external configuration directories of the X-Road instance.

The Central Server implements two configuration sources. The internal source distributes files to Security Servers belonging to the same X-Road instance as the Central Server. The external source distributes configuration files to Security Servers of other federated X-Road instances. Both sources can contain different set of configuration files, depending on the Central Server's configuration.

The process of generating and distributing the configuration is the same for both configuration sources.

1.  A scheduled task initiates the global configuration generation.

2.  The contents of the files are taken from Central Server's database. The files are saved to a temporary location.

3.  Administration service component generates configuration directory referencing the generated files.

4.  Administration service component sends a signing request (containing hash of the directory) to the signer component. Signer signs the hash and responds with the signature.

5.  Administration service component updates the configuration directory to contain the received signature.

6.  Administration service component moves the configuration files to the distribution directory of the web server.

7.  Security servers make HTTP requests and download the configuration.

This process is illustrated in the sequence diagram in [Figure 2](#Ref_The_process_of_global_configuration_and_distribution).


<a id="Ref_The_process_of_global_configuration_and_distribution" class="anchor"></a>
![](img/arc-cs_the_process_of_global_configuration_and_distribution.svg)

Figure 2. The process of global configuration generation and distribution