## 3 X-Road message logging and the security token
By default, if the message logging add-on (package `xroad-addon-messagelog`) is installed on a security server, all X-Road SOAP messages are logged
with all their SOAP headers, including the security token. You can read more about the message logging in [Chapter 11](../../Manuals/ug-ss_x-road_6_security_server_user_guide.md#11-message-log)
of the  the Security Server User Guide \[[UG-SS](#Ref_UG-SS)\].

In case the security token contains sensitive data that should not be logged, the message logging can be configured to not log the SOAP body, which also drops the `securityToken` SOAP header. You can
read more about the SOAP body logging options in the [Message log add-on parameters section](../../Manuals/ug-syspar_x-road_v6_system_parameters.md#message-log-add-on-parameters-message-log) of the X-Road System Parameters User
Guide \[[UG-SYSPAR](#Ref_UG-SYSPAR)\].