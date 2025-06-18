### 2.2 Implementation details

* Creates a new service `xroad-autologin`
* Service is started after `xroad-signer` has started
* On RHEL/Ubuntu 20.04, service calls wrapper script `/usr/share/xroad/autologin/xroad-autologin-retry.sh` which in turn calls `autologin.expect`
  * Wrapper script handles retries in error situations.
* Service tries to enter the PIN code using script `signer-console`
  * If the PIN was correct or incorrect, it exits
  * If an error occurred (for example because `xroad-signer` has not yet fully started), it keeps retrying indefinitely