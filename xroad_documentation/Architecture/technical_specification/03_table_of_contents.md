## Table of Contents



- [Technical Specification](#technical-specification)
  - [Version history](#version-history)
  - [Table of Contents](#table-of-contents)
  - [License](#license)
  - [1 Introduction](#1-introduction)
    - [1.1 Overview](#11-overview)
    - [1.2 Design Goals](#12-design-goals)
  - [1.3 Terms and abbreviations](#13-terms-and-abbreviations)
    - [1.4 References](#14-references)
  - [2 System Components](#2-system-components)
    - [2.1 Central Server](#21-central-server)
    - [2.2 Security Server](#22-security-server)
    - [2.3 Information System](#23-information-system)
    - [2.4 Time-Stamping Authority](#24-time-stamping-authority)
    - [2.5 Certification Authority](#25-certification-authority)
    - [2.6 Configuration Proxy](#26-configuration-proxy)
    - [2.7 Operational Monitoring Daemon](#27-operational-monitoring-daemon)
    - [2.8 Environmental Monitoring Daemon](#28-environmental-monitoring-daemon)
  - [3 Protocols and Interfaces](#3-protocols-and-interfaces)
    - [3.1 X-Road Message Protocol](#31-x-road-message-protocol)
    - [3.2 Protocol for Downloading Configuration](#32-protocol-for-downloading-configuration)
    - [3.3 Message Transport Protocol](#33-message-transport-protocol)
    - [3.4 Service Metadata Protocol](#34-service-metadata-protocol)
    - [3.5 Download Signed Document](#35-download-signed-document)
    - [3.6 Management Services Protocol](#36-management-services-protocol)
    - [3.7 OCSP Protocol](#37-ocsp-protocol)
    - [3.8 Time-Stamping Protocol](#38-time-stamping-protocol)
    - [3.9 Security Server User Interface](#39-security-server-user-interface)
    - [3.10 Central Server User Interface](#310-central-server-user-interface)
    - [3.11 Store Operational Monitoring Data](#311-store-operational-monitoring-data)
    - [3.12 Operational Monitoring Query](#312-operational-monitoring-query)
    - [3.13 Operational Monitoring Protocol](#313-operational-monitoring-protocol)
    - [3.14 Operational Monitoring JMX](#314-operational-monitoring-jmx)
    - [3.15 Environmental Monitoring Protocol](#315-environmental-monitoring-protocol)
    - [3.16 Environmental Monitoring JMX](#316-environmental-monitoring-jmx)
    - [3.17 Environmental Monitoring Query](#317-environmental-monitoring-query)
  - [4 Deployment View](#4-deployment-view)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/

## 1 Introduction