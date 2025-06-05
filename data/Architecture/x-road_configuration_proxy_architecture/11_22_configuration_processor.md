### 2.2 Configuration Processor

A configuration processor is responsible for initiating the download of global configuration files for the configured X-Road instance and preparing them for distribution to configuration clients.

A cron job configured on the server periodically (every minute) starts the configuration processor, which sequentially performs it's functions for all configured configuration proxy instances.