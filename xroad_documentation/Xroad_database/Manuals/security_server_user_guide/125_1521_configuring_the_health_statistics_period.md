#### 15.2.1 Configuring the Health Statistics Period

By default, health statistics are provided for a period of 600 seconds (10 minutes). This means that if no request exchange has taken place for 10 minutes, all the statistical metrics are reset. Please refer to \[[PR-OPMON](#Ref_PR-OPMON)\] for a detailed overview of the health metrics available.

To change the health statistics period, the value of the parameter health-statistics-period-seconds should be set or edited in the `[op-monitor]`
section of the file `/etc/xroad/conf.d/local.ini`.