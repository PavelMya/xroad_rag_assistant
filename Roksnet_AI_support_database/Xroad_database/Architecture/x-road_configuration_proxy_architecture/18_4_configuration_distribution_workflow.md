## 4 Configuration Distribution Workflow

X-Road configuration proxy periodically downloads the global configuration from configured sources. Each global configuration consists of a number of XML files (see \[[PR-GCONF](#Ref_PR-GCONF)\] for detailed information about configuration structure). The configuration proxy then redistributes the downloaded configuration files to other configuration clients.

Configuration files are distributed in accordance with the protocol for downloading configuration (see [Section 3.1](#31-downloading-configuration)). MIME messages are generated to represent configuration directories of the global configurations being distributed.

The configuration proxy can distribute files from as many configuration sources as necessary. For each configuration source a configuration proxy instance is configured.

The following process is performed for each configuration proxy instance.

1.  A cron job sends a request to start the configuration processor for the given configuration proxy instance.

2.  Configuration processor component calls the configuration client to download the global configuration files from the configured source.

3.  Configuration processor component generates configuration directory referencing the downloaded files.

4.  Configuration processor component sends a signing request (containing hash of the directory) to the signer component. Signer signs the hash and responds with the signature.

5.  Configuration processor component updates the configuration directory to contain the received signature.

6.  Configuration processor component moves the configuration files to the distribution directory of the web server.

7.  Security servers make HTTP requests and download the configuration.

This process is illustrated in the sequence diagram in [figure 2](#Ref_Configuration_creation_sequence_diagram).



![](img/arc-cp_configuration_creation_sequence_diagram.png)

Figure 2. Configuration creation sequence diagram