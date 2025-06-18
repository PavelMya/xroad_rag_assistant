##### 4.4.1.1 Necessary activities after changing certificate

When the key and certificate are rotated, and mTLS is enabled between the management Security Server and the management services, the new certificate must be updated to the management Security Server. To add new certificate follow Security Server User Guide [UG-SS](#13-references) instruction in section "Managing Information System TLS Certificates".

**ATTENTION!**
- The changed TLS certificate is added in the global configuration `private-params.xml` part. The global configuration generation interval on the Central Server and the global configuration fetching interval on the Security Server depend on the system parameters. The system parameters are specified in the [UG-SYSPAR](#13-references) section "Center parameters: [admin-service]" and "Configuration Client parameters: [configuration-client]". With the default values, a new Registration and Management service TLS certificate is usable for the authentication certificate registration request on the Security Server side after ~1.5 min.
- The changed TLS certificate is automatically detected by Nginx within five minutes after the change.

## 5. Configuration Management