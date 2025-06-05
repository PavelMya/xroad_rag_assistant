### 2.7 Disable the Messagelog Addon before Installation (optional)

It is possible to preconfigure the Security Server installation so that the messagelog addon will be automatically disabled after the installation process is done. This also skips the creation of the messagelog database.

In order to skip messagelog database creation and disable the messagelog addon, run the following command to add a boolean value into the debconf database before installing the Security Server 

```bash
sudo debconf-set-selections <<< 'xroad-addon-messagelog xroad-addon-messagelog/enable-messagelog boolean false'
```