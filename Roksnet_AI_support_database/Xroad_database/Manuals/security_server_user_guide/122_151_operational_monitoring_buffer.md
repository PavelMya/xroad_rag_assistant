### 15.1 Operational Monitoring Buffer

In general, the operational monitoring buffer is an internal component of the Security Server and thus being not directly used by the end user.

The configuration parameters available for configuring the operational monitoring buffer have been documented in \[[UG-OPMONSYSPAR](#Ref_UG-OPMONSYSPAR)\].

The default values of the parameters have been chosen to be sufficient under expected average load using the minimum hardware recommended.

All overrides to the default configuration values must be made in the file `/etc/xroad/conf.d/local.ini`, in the `[op-monitor-buffer]` section.