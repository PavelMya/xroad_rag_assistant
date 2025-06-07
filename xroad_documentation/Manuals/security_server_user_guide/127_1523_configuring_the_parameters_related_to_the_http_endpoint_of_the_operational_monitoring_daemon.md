#### 15.2.3 Configuring the Parameters related to the HTTP Endpoint of the Operational Monitoring Daemon

For configuring the endpoint of the operational monitoring daemon, the following parameters are available in the `[op-monitor]` section of the configuration:

**host** – listening host of the daemon (by default the value is set to *localhost*).

**port** – listening port (by default the value is set to *2080*).

**scheme** – connection type (by default the value is set to *HTTP*).

If any of these values are changed, both the proxy and the operational monitoring daemon services must be restarted:

    service xroad-proxy restart
    service xroad-opmonitor restart