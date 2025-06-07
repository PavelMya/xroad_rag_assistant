### 2.8 Security Server Installation

Issue the following command to install the Security Server packages (use package `xroad-securityserver-fi` to include configuration specific to Finland; use package `xroad-securityserver-is` to include configuration specific to Iceland; there's no Estonia-specific package for RHEL):

  ```bash
  sudo yum install xroad-securityserver
  ```

The meta-package `xroad-securityserver` also installs metaservices module `xroad-addon-metaservices`, messagelog module `xroad-addon-messagelog` and WSDL validator module `xroad-addon-wsdlvalidator`. The meta-packages `xroad-securityserver-fi`, `xroad-securityserver-is`, and `xroad-securityserver-fo` install operational data monitoring module `xroad-addon-opmonitoring`.

Add system user (**reference data: 1.3**) whom all roles in the user interface are granted to. Add a new user with the command

  ```bash
  sudo xroad-add-admin-user 
  ```

User roles are discussed in detail in X-Road Security Server User Guide \[[UG-SS](#Ref_UG-SS)\].

#### 2.8.1 Start Security Server

Once the installation is completed, start the Security Server

  ```bash
  sudo systemctl start xroad-proxy
  ```