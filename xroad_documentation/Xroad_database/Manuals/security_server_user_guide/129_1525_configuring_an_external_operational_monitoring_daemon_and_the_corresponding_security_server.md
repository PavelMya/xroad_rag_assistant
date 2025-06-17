#### 15.2.5 Configuring an External Operational Monitoring Daemon and the Corresponding Security Server

To make a Security Server communicate with an external operational monitoring daemon, it is necessary to configure both the daemon and the Security Server.

By default, the operational monitoring daemon listens on localhost. To make the daemon available to Security Servers on other hosts, the listening address must be set to the IP address that is relevant in the particular network, as described in the previous section.

As advised, the scheme parameter should be set to "https". For communication over HTTPS, the Security Server and the operational monitoring daemon must know each other's TLS certificates to enable the Security Server to authenticate to the monitoring daemon successfully.

**NOTE:** If an external operational monitoring daemon is used, the host, scheme (and optionally, port) parameters must be changed at both hosts.

The internal TLS certificate of the Security Server is used for authenticating the Security Server to the operational monitoring daemon. This certificate has been generated beforehand, during the installation process of the Security Server, and is available in PEM format in the file `/etc/xroad/ssl/internal.crt`. Please refer to Section [10.4](#104-changing-the-internal-tls-key-and-certificate) for the instructions on exporting the internal TLS certificate from UI. The file must be copied to the host running the operational monitoring daemon. The system user xroad must have permissions to read this file.

In the configuration of the external daemon, the corresponding path must be set in `/etc/xroad/conf.d/local.ini`:

    [op-monitor]
    client-tls-certificate = 

Next, a TLS key and the corresponding certificate must be generated on the host of the external monitoring daemon as well, using the command

    generate-opmonitor-certificate

The script will prompt you for standard fields for input to TLS certificates and its output (key files and the certificate) will be generated to the directory `/etc/xroad/ssl`.

The generated certificate, in the file `opmonitor.crt`, must be copied to the corresponding Security Server. The system user `xroad` must have permissions to read this file. Its path at the Security Server must be written to the configuration (note the name of the section, although it is the proxy service that will read the configuration):

    [op-monitor]
    tls-certificate = 

For the external operational daemon to be used, the proxy service at the Security Server must be restarted:

    service xroad-proxy restart

In addition, on the host running the corresponding Security Server, the operational monitoring daemon must be stopped:

    service xroad-opmonitor stop

For the service to stay stopped after reboot the following command should be run:

    echo manual > /etc/init/xroad-opmonitor.override

The configuration anchor (renamed as `configuration-anchor.xml`) file must be manually copied into the directory `/etc/xroad` of the external monitoring daemon in order for configuration client to be able to download the global configuration (by default configuration download interval is 60 seconds). The system user xroad must have permissions to read this file.