### 4.1 Minimum Supported Client Security Server Version

To increase the security of the X-Road ecosystem, it is recommended to limit the minimum version of the client Security Server that is allowed to access a service.

On the service provider side, the Security Server administrator can limit the minimum client version by configuring the system parameter `server-min-supported-client-version` as described in [UG-SYSPAR](#Ref_UG-SYSPAR) section 3.2 Proxy parameters.

For example, setting the value `server-min-supported-client-version = 7.3.1` means that client Security Server version should be at least `7.3.1`:

	[proxy]
	server-min-supported-client-version = 7.3.1