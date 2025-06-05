### 2.8 Security Server Installation

Issue the following command to install the Security Server packages (use package `xroad-securityserver-ee` to include configuration specific to Estonia; use package `xroad-securityserver-fi` to include configuration specific to Finland; use package `xroad-securityserver-is` to include configuration specific to Iceland):

```bash
sudo apt install xroad-securityserver
```

Upon the first installation of the packages, the system asks for the following information.

* Account name for the user who will be granted the rights to perform all activities in the user interface (**reference data: 1.3**).
* Database server URL. Locally installed database is suggested as default but remote databases can be used as well. In case remote database is used, one should verify that the version of the local PostgreSQL client matches the version of the remote PostgreSQL server.
* The Distinguished Name of the owner of the **user interface's and management REST API's** self-signed TLS certificate (*Subject DN*) and its alternative names (*subjectAltName*) (**reference data: 1.8; 1.10**). The certificate is used for securing connections to the user interface and to the management REST API.
  The name and IP addresses detected from the operating system are suggested as default values.

  * The *Subject DN* must be entered in the format:

            /CN=server.domain.tld

  * All IP addresses and domain names in use must be entered as alternative names in the format:

            IP:1.2.3.4,IP:4.3.2.1,DNS:servername,DNS:servername2.domain.tld

* The Distinguished Name of the owner of the TLS certificate that is used for securing the HTTPS access point of information systems (**reference data: 1.8; 1.11**).
    The name and IP addresses detected from the system are suggested as default values.

    * The *Subject DN* must be entered in the format:

            /CN=server.domain.tld

    * All IP addresses and domain names in use must be entered as alternative names in the format:

            IP:1.2.3.4,IP:4.3.2.1,DNS:servername,DNS:servername2.domain.tld

* The memory allocation configuration for the Java Virtual Machine (JVM) used by the proxy service.
  Allowed values are:
    * *d* - default, adds `-Xms100m -Xmx512m` config to the JVM options in `XROAD_PROXY_PARAMS` in `/etc/xroad/services/local.properties` file;
  
    * *r* - recommended, adds recommended Xms and Xmx values based on total memory in current server to the JVM options in `XROAD_PROXY_PARAMS` in `/etc/xroad/services/local.properties` file;
  
    * `<initialSize>[k|m|g] <maxSize>[k|m|g]` - custom values, which will be transformed to `-Xms<initialSize>[k|m|g] -Xmx<maxSize>[k|m|g]`.
  
  Note that in all cases `/etc/xroad/services/local.properties` file is updated so that `XROAD_PROXY_PARAMS` property contains new memory configs in the end of any other already present options there.

The meta-package `xroad-securityserver` also installs metaservices module `xroad-addon-metaservices`, messagelog module `xroad-addon-messagelog` and WSDL validator module `xroad-addon-wsdlvalidator`. The meta-packages `xroad-securityserver-ee`, `xroad-securityserver-fi`, `xroad-securityserver-is`, and `xroad-securityserver-fo` install operational data monitoring module `xroad-addon-opmonitoring`.

**N.B.** In case configuration specific to Estonia (package `xroad-securityserver-ee`) is installed, connections from client applications are restricted to localhost by default. To enable client application connections from external sources, the value of the `connector-host` property must be overridden in the `/etc/xroad/conf.d/local.ini` configuration file. Changing the system parameter values is explained in the System Parameters User Guide \[[UG-SS](#Ref_UG-SS)\].