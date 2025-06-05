### 2.9 Post-Installation Checks

The installation is successful if system services are started and the user interface is responding.

* Ensure from the command line that X-Road services are in the `running` state (example output follows):

  ```bash
  sudo systemctl list-units "xroad-*"

  UNIT                           LOAD   ACTIVE SUB     DESCRIPTION
  xroad-addon-messagelog.service loaded active running X-Road Messagelog Archiver
  xroad-base.service             loaded active exited  X-Road initialization
  xroad-confclient.service       loaded active running X-Road confclient
  xroad-monitor.service          loaded active running X-Road Monitor
  xroad-proxy-ui-api.service     loaded active running X-Road Proxy UI REST API
  xroad-proxy.service            loaded active running X-Road Proxy
  xroad-signer.service           loaded active running X-Road signer
  ```

* Ensure that the Security Server user interface at https://SECURITYSERVER:4000/ (**reference data: 1.8; 1.6**) can be opened in a Web browser. To log in, use the account name chosen during the installation (**reference data: 1.3**). While the user interface is still starting up, the Web browser may display a connection refused -error.