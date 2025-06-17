### 2.6 Post-Installation Checks

The installation is successful if the 'xroad-signer' service is started, the 'xroad-confproxy' cron job is added, and the Configuration Proxy management utilities are available from the command line.

* Check from the command line that the 'xroad-signer' service is in the running state (example output follows). Notice that it is normal for the xroad-confclient to be in `stopped` state on the Configuration Proxy since it operates in one-shot mode.
  
  ```bash
  systemctl list-units "xroad*" 

  UNIT                     LOAD   ACTIVE SUB     DESCRIPTION
  xroad-signer.service     loaded active running X-Road signer
  ```

* Check from the command line that the 'xroad-confproxy' cron job is present (example output follows):

  ```bash
  sudo ls /etc/cron.d/ | grep "^xroad-"
 
  xroad-confproxy
  ```

* Make sure that the following commands are available from the command line:

  ```bash
  signer-console
  confproxy-view-conf
  confproxy-create-instance
  confproxy-add-signing-key
  confproxy-del-signing-key
  confproxy-generate-anchor
  ```