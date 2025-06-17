### 2.7 Disable the Messagelog Addon before Installation (optional)

It is possible to preconfigure the Security Server installation so that the messagelog addon will be automatically disabled after the installation process is done. This also skips the creation of the messagelog database.

In order to skip messagelog database creation and disable the messagelog addon, run the following command to add a boolean value into the debconf database before installing the Security Server 

```bash
sudo debconf-set-selections [k|m|g] [k|m|g]` - custom values, which will be transformed to `-Xms[k|m|g] -Xmx[k|m|g]`.
  
  Note that in all cases `/etc/xroad/services/local.properties` file is updated so that `XROAD_PROXY_PARAMS` property contains new memory configs in the end of any other already present options there.

The meta-package `xroad-securityserver` also installs metaservices module `xroad-addon-metaservices`, messagelog module `xroad-addon-messagelog` and WSDL validator module `xroad-addon-wsdlvalidator`. The meta-packages `xroad-securityserver-ee`, `xroad-securityserver-fi`, `xroad-securityserver-is`, and `xroad-securityserver-fo` install operational data monitoring module `xroad-addon-opmonitoring`.

**N.B.** In case configuration specific to Estonia (package `xroad-securityserver-ee`) is installed, connections from client applications are restricted to localhost by default. To enable client application connections from external sources, the value of the `connector-host` property must be overridden in the `/etc/xroad/conf.d/local.ini` configuration file. Changing the system parameter values is explained in the System Parameters User Guide \[[UG-SS](#Ref_UG-SS)\].