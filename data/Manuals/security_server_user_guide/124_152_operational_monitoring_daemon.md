### 15.2 Operational Monitoring Daemon

The configuration parameters available for configuring the operational monitoring daemon have been documented in \[[UG-OPMONSYSPAR](#Ref_UG-OPMONSYSPAR)\].

Similarly to the operational monitoring buffer, the default values of the parameters have been chosen to be sufficient under expected average load using the minimum recommended hardware.

All overrides to the default configuration values must be made in the file `/etc/xroad/conf.d/local.ini`, in the `[op-monitor]` section.

In the following sections, some parameters are described which may be required to be changed more likely.