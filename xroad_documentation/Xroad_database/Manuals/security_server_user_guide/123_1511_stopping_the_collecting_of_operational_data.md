#### 15.1.1 Stopping the Collecting of Operational Data

If, for any reason, operational data should not be collected and forwarded to the operational monitoring daemon, the parameter size can be set to 0:

    [op-monitor-buffer]
    size = 0

After the configuration change, the xroad-proxy service must be restarted:

    service xroad-proxy restart

In addition, the operational monitoring daemon should be stopped:

    service xroad-opmonitor stop

For the service to stay stopped after reboot the following command should be run:

    echo manual > /etc/init/xroad-opmonitor.override