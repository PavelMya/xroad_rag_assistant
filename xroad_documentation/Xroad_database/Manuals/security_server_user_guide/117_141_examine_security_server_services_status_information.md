### 14.1 Examine Security Server services status information

Security server services status information covers the following services:

| Service              | Status           | Message        | Previous Update                                        | Next Update                                                      |
|----------------------|------------------|----------------|--------------------------------------------------------|------------------------------------------------------------------|
| Global configuration | Green/yellow/red | Status message | The time of the global configuration client's last run | The estimated time of the global configuration client's next run |
| Timestamping         | Green/yellow/red | Status message | The time of the last timestamping operation            | Not used                                                         |
| OCSP-responders      | Green/yellow/red | Status message | The time of the last contact with the OCSP-responder   | The latest possible time for the next OCSP-refresh               |

To refresh the service statuses, refresh the page.

The status colors indicate the following:
- **Red indicator** – service cannot be contacted or is not operational
- **Yellow indicator** – service has been contacted but is yet to have been used to verify its status
- **Green indicator** – service has been successfully contacted and used to verify it is operational

The status message offers more detailed information on the current status.

If a section of the diagnostics view appears empty, it means that there either is no configured service available or that checking the service status has failed. If sections are empty, try refreshing the diagnostics view or check the service configuration.