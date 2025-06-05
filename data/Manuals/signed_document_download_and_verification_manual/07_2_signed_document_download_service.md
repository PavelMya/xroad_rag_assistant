## 2 Signed Document Download Service

The security server offers the asic web service for downloading its signed documents. The service is used via HTTP GET requests to the service URL: 

    http://SECURITYSERVER/asic

where `SECURITYSERVER` is the actual address of the security server.

Signed documents are available via the service until they are archived and removed from the message log database (by default 30 days). This time period is configurable in the security server (messagelog parameter `keep-records-for`). If messagelog parameter `archive-encryption-enabled` is true, the messages are returned in encrypted format (OpenPGP/GnuPG, see [UG-SS] for archive encryption details).