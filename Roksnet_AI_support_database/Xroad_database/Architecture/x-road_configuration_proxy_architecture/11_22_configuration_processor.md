### 2.2 Configuration Processor

A configuration processor is responsible for initiating the download of global configuration files for the configured X-Road instance and preparing them for distribution to configuration clients.

A cron job configured on the server periodically (every minute) starts the configuration processor, which sequentially performs it's functions for all configured configuration proxy instances.

### 2.3 Signer

The signer component is responsible for managing the keys and certificates used for signing the global configuration. Signer is called from the configuration processor to create the signature for the configuration.

### 2.4 Configuration Client

The configuration client is responsible for downloading remote global configuration files. The source location of the global configuration is taken from the anchor file that the configuration processor provides when invoking the configuration client.

### 2.5 Password Store

Stores security token passwords in a shared memory segment of the operating system that can be accessed by the signer. Allows security token logins to persist, until the configuration proxy is restarted, without compromising the passwords.