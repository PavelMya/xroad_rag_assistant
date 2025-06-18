#### 3.4.1 Accepting Connections

The Security Server has a special `[proxy]` parameter [connector-host](ug-syspar_x-road_v6_system_parameters.md#32-proxy-parameters-proxy) which determines
the interfaces that the Security Server uses to listen for incoming connections. The default value for this parameter in the default X-Road packages is `0.0.0.0`,
which makes the Security Server accept connections from any server. For country-specific defaults, please refer to the system parameters documentation. 

The parameter can be changed by following the [System Parameters guide](ug-syspar_x-road_v6_system_parameters.md#21-changing-the-system-parameter-values-in-configuration-files).