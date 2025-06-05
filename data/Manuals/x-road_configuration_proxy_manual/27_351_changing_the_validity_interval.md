#### 3.5.1 Changing the Validity Interval

There is an additional property in the configuration file of the proxy instance (/etc/xroad/confproxy/&lt;PROXY_NAME&gt;/conf.ini) that determines the validity interval of the generated global configuration for a given instance.

The default value is 10 minutes (600 seconds). The property is set by modifying the following field in the configuration file:

```ini
[configuration-proxy]
...
validity-interval-seconds=600
```

Notice that when the Configuration Proxy instance is started, it deletes all the previously generated global configuration directories that are older than the currently configured validity interval for that instance.