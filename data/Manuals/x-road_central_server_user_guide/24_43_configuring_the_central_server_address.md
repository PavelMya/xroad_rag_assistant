### 4.3 Configuring the Central Server Address

Access rights: Security Officer

In the System Settings view (Settings tab --> System Settings), the Central Server's public DNS name or its external IP address is displayed. This address is used by the Security Servers to access the services provided by the Central Server (configuration download, management services).

**ATTENTION!** When the Central Server address is changed,

- the management services address in the management services’ Security Server needs to be reconfigured,
- the internal configuration anchor need to be redistributed to the Security Server administrators and
- the external configuration anchor needs to be redistributed to the federation partners.

The services provided by the Central Server must be available from both the new and old address, until all servers using the services have uploaded the configuration anchor containing the new address.