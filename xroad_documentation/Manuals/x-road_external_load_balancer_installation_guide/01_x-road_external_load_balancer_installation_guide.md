# X-Road: External Load Balancer Installation Guide

Version: 1.28
Doc. ID: IG-XLB


| Date       | Version | Description                                                                                                              | Author                      |
|------------|---------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 22.3.2017  | 1.0     | Initial version                                                                                                          | Jarkko Hyöty, Olli Lindgren |
| 27.4.2017  | 1.1     | Added slave node user group instructions                                                                                 | Tatu Repo                   |
| 15.6.2017  | 1.2     | Added health check interface maintenance mode                                                                            | Tatu Repo                   |
| 21.6.2017  | 1.3     | Added chapter 7 on [upgrading the Security Server cluster](#7-upgrading-a-clustered-x-road-security-server-installation) | Olli Lindgren               |
| 02.03.2018 | 1.4     | Added uniform terms and conditions reference                                                                             | Tatu Repo                   |
| 15.11.2018 | 1.5     | Updates for Ubuntu 18.04 support                                                                                         | Jarkko Hyöty                |
| 20.12.2018 | 1.6     | Update upgrade instructions                                                                                              | Jarkko Hyöty                |
| 11.09.2019 | 1.7     | Remove Ubuntu 14.04 support                                                                                              | Jarkko Hyöty                |
| 08.10.2020 | 1.8     | Added notes about API keys and caching                                                                                   | Janne Mattila               |
| 19.10.2020 | 1.9     | Remove xroad-jetty and nginx mentions and add xroad-proxy-ui-api                                                         | Caro Hautamäki              |
| 19.10.2020 | 1.10    | Added information about management REST API permissions                                                                  | Petteri Kivimäki            |
| 23.12.2020 | 1.11    | Updates for Ubuntu 20.04 support                                                                                         | Jarkko Hyöty                |
| 02.07.2021 | 1.12    | Updates for state sync                                                                                                   | Jarkko Hyöty                |
| 25.08.2021 | 1.13    | Update X-Road references from version 6 to 7                                                                             | Caro Hautamäki              |
| 17.09.2021 | 1.14    | Add note about the proxy health check now also checking global conf validity                                             | Caro Hautamäki              |
| 17.06.2022 | 1.15    | Replace the word "replica" with "secondary"                                                                              | Petteri Kivimäki            |
| 26.09.2022 | 1.16    | Remove Ubuntu 18.04 support                                                                                              | Andres Rosenthal            |
| 01.03.2023 | 1.17    | Updates for user groups in secondary nodes                                                                               | Petteri Kivimäki            |
| 20.12.2023 | 1.18    | Added RHEL 9                                                                                                             | Justas Samuolis             |
| 12.01.2024 | 1.19    | RHEL PostgreSQL 12 support                                                                                               | Eneli Reimets               |
| 16.02.2024 | 1.20    | RHEL PostgreSQL 13 support                                                                                               | Eneli Reimets               |
| 19.04.2024 | 1.21    | Simplified creation of PostgreSQL serverconf service for RHEL 8, 9 and added warning about SELinux policy                | Eneli Reimets               |
| 26.04.2024 | 1.22    | Added Ubuntu 24.04 support                                                                                               | Madis Loitmaa               |
| 16.08.2024 | 1.23    | Added assumption that the load balancer supports TLS passthrough                                                         | Petteri Kivimäki            |
| 06.09.2024 | 1.24    | Updated RHEL default configuration files location                                                                        | Eneli Reimets               |
| 17.12.2024 | 1.25    | When adding user xroad-slave, the home directory must be explicitly added for Ubuntu                                     | Eneli Reimets               |
| 17.03.2025 | 1.26    | Syntax and styling                                                                                                       | Pauline Dimmek              |
| 02.04.2025 | 1.27    | Added Proxy memory health check paragraph                                                                                | Mikk-Erik Bachmann          |
| 06.05.2025 | 1.28    | Added more details about the soft token status check result caching                                                      | Petteri Kivimäki            |