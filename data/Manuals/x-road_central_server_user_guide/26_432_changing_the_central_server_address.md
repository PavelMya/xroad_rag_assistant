#### 4.3.2 Changing the Central Server Address

To change the Central Server address, follow these steps.

1. In the Navigation tabs, select Settings --> System Settings.
2. Locate the System Parameters section and click Edit.
3. Enter the Central Server’s address and click Save. When the address is changed, the system:
  - changes the management services WSDL address,
  - changes the management services address,
  - changes the configuration source addresses,
  - generates new configuration anchors for the internal and external configuration sources.
4. After the Central Server address is changed, act as follows.
  - Download the internal configuration source anchor and distribute the anchor along with the anchor’s hash value to the Security Server administrators of the local X-Road infrastructure.
    > **NOTE**: Starting from version 7.5.0 new Central Server address is automatically distributed to Security Servers within the global configuration. Distribution will take place within two global configuration refresh cycles. However, the new Central Server address is not updated to the configuration anchor stored on the Security Server. If the Security Server's local copy of the global configuration expires, the Security Server returns using the Central Server address from the configuration anchor. Therefore, if the Security Server's local copy of the global configuration is expired, importing a new version of the configuration anchor is required if the current Central Server address doesn't match with the address in the original configuration anchor.
  - In case of federated X-Road systems, download the external configuration source anchor and distribute the anchor along with the anchor’s hash value to the federation partners.
    > **NOTE**: Starting from version 7.5.0 new Central Server address is automatically distributed to the federation partners within the global configuration. Distribution will take place within two global configuration refresh cycles. However, the new Central Server address is not updated to the configuration anchor stored on the Security Server. If the Security Server's local copy of the global configuration expires, the Security Server returns using the Central Server address from the configuration anchor. Therefore, if the Security Server's local copy of the global configuration is expired, importing a new version of the configuration anchor is required if the current Central Server address doesn't match with the address in the original configuration anchor.
  - Reconfigure the management services addresses in the management service Security Server.