### 2.7 Disable the Messagelog Addon before Installation (optional)

It is possible to preconfigure the Security Server installation so that the messagelog addon will be automatically disabled after the installation process is done. This also skips the creation of the messagelog database.

In order to skip messagelog database creation and disable the messagelog addon, run the following command to create a configuration file before installing the Security Server 

```bash
echo "ENABLE_MESSAGELOG=false" | sudo tee /etc/sysconfig/xroad-addon-messagelog
```