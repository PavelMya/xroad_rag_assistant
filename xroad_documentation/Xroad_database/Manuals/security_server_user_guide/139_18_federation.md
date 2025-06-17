## 18 Federation

Federation allows Security Servers of two different X-Road instances to exchange messages with each other. The instances
are federated at the Central Server level. After this, Security Servers can be configured to opt-in to the federation.
By default, federation is disabled and configuration data for other X-Road instances will not be downloaded.

The federation can be allowed for all X-Road instances that the Central Server offers, or a list of specific
(comma-separated) instances. The default is to allow none. The values are case-insensitive.

To override the default value, edit the file `/etc/xroad/conf.d/local.ini` and add or change the value of the system
parameter `allowed-federations` for the server component `configuration-client`. To restore the default, either remove
the system parameter entirely or set the value to `none`. X-Road services `xroad-confclient` and `xroad-proxy` need to
be restarted (in that order) for any setting changes to take effect.

Below are some examples for `/etc/xroad/conf.d/local.ini`.

To allow federation with all offered X-Road instances:
```ini
[configuration-client]
allowed-federations=all
```

To allow federation with specific instances `xe-test` and `ee-test`:
```ini
[configuration-client]
allowed-federations=xe-test,ee-test
```

To disable federation, just remove the `allowed-federations` system parameter entirely or use:
```ini
[configuration-client]
allowed-federations=none
```

Please note that if the keyword `all` is present in the comma-separated list, it will override the single allowed
instances. The keyword `none` will override all other values. This means that the following setting will allow all
federations:
```ini
[configuration-client]
allowed-federations=xe-test, all, ee-test
```
And the following will allow none:
```ini
[configuration-client]
allowed-federations=xe-test, all, none, ee-test
```