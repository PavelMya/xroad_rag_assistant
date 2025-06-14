## Table of Contents 




- [License](#license)
- [1 Introduction](#1-introduction)
  - [1.1 The X-Road Security Server](#11-the-x-road-security-server)
  - [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
  - [1.3 References](#13-references)
- [2 User Management](#2-user-management)
  - [2.1 User Roles](#21-user-roles)
  - [2.2 Managing the Users](#22-managing-the-users)
    - [2.2.1 Adding and Removing Users](#221-adding-and-removing-users)
  - [2.3 LDAP user authentication](#23-ldap-user-authentication)
    - [2.3.1 Setting up LDAP User Authentication for X-Road Security Server using SSSD](#231-setting-up-ldap-user-authentication-for-x-road-security-server-using-sssd)
  - [2.4 Managing API Keys](#24-managing-api-keys)
    - [2.4.1 Creating a new API key](#241-creating-a-new-api-key)
    - [2.4.2 Editing the roles of an API key](#242-editing-the-roles-of-an-api-key)
    - [2.4.3 Revoking an API key](#243-revoking-an-api-key)
- [3 Security Server Registration](#3-security-server-registration)
  - [3.1 Configuring the Signing Key and Certificate for the Security Server Owner](#31-configuring-the-signing-key-and-certificate-for-the-security-server-owner)
    - [3.1.1 Generating a Signing Key and Certificate Signing Request](#311-generating-a-signing-key-and-certificate-signing-request)
    - [3.1.2 Importing a Certificate from the Local File System](#312-importing-a-certificate-from-the-local-file-system)
    - [3.1.3 Importing a Certificate from a Security Token](#313-importing-a-certificate-from-a-security-token)
  - [3.2 Configuring the Authentication Key and Certificate for the Security Server](#32-configuring-the-authentication-key-and-certificate-for-the-security-server)
    - [3.2.1 Generating an Authentication Key](#321-generating-an-authentication-key)
    - [3.2.2 Generating a Certificate Signing Request for an Authentication Key](#322-generating-a-certificate-signing-request-for-an-authentication-key)
    - [3.2.3 Importing an Authentication Certificate from the Local File System](#323-importing-an-authentication-certificate-from-the-local-file-system)
  - [3.3 Registering the Security Server in the X-Road Governing Authority](#33-registering-the-security-server-in-the-x-road-governing-authority)
    - [3.3.1 Registering an Authentication Certificate](#331-registering-an-authentication-certificate)
  - [3.4 Changing the Security Server Owner](#34-changing-the-security-server-owner)
- [4 Security Server Clients](#4-security-server-clients)
  - [4.1 Security Server Client States](#41-security-server-client-states)
  - [4.2 Adding a Security Server Client](#42-adding-a-security-server-client)
  - [4.3 Adding a Security Server Member Subsystem](#43-adding-a-security-server-member-subsystem)
  - [4.4 Configuring a Signing Key and Certificate for a Security Server Client](#44-configuring-a-signing-key-and-certificate-for-a-security-server-client)
  - [4.5 Registering a Security Server Client in the X-Road Governing Authority](#45-registering-a-security-server-client-in-the-x-road-governing-authority)
    - [4.5.1 Registering a Security Server Client](#451-registering-a-security-server-client)
  - [4.6 Deleting a Client from the Security Server](#46-deleting-a-client-from-the-security-server)
    - [4.6.1 Unregistering a Client](#461-unregistering-a-client)
    - [4.6.2 Deleting a Client](#462-deleting-a-client)
  - [4.7 Disabling Client Subsystem Temporarily](#47-disabling-client-subsystem-temporarily)
    - [4.7.1 Disabling Client Subsystem](#471-disabling-client-subsystem)
    - [4.7.2 Enabling Client Subsystem](#472-enabling-client-subsystem)
  - [4.8 Renaming Client Subsystem](#48-renaming-client-subsystem)
- [5 Security Tokens, Keys, and Certificates](#5-security-tokens-keys-and-certificates)
  - [5.1 Availability States of Security Tokens](#51-availability-states-of-security-tokens)
  - [5.2 Registration States of Certificates](#52-registration-states-of-certificates)
    - [5.2.1 Registration States of the Signing Certificate](#521-registration-states-of-the-signing-certificate)
    - [5.2.2 Registration States of the Authentication Certificate](#522-registration-states-of-the-authentication-certificate)
  - [5.3 Validity States of Certificates](#53-validity-states-of-certificates)
  - [5.4 Activating and Disabling the Certificates](#54-activating-and-disabling-the-certificates)
  - [5.5 Configuring and Registering an Authentication key and Certificate](#55-configuring-and-registering-an-authentication-key-and-certificate)
  - [5.6 Deleting a Certificate](#56-deleting-a-certificate)
    - [5.6.1 Unregistering an Authentication Certificate](#561-unregistering-an-authentication-certificate)
    - [5.6.2 Deleting a Certificate or a certificate Signing Request notice](#562-deleting-a-certificate-or-a-certificate-signing-request-notice)
  - [5.7 Deleting a Key](#57-deleting-a-key)
  - [5.8 Deleting an inactive Token](#58-deleting-an-inactive-token)
- [6 X-Road Services](#6-x-road-services)
  - [6.1 Adding a service description](#61-adding-a-service-description)
    - [6.1.1 SOAP](#611-soap)
    - [6.1.2 REST](#612-rest)
  - [6.2 Refreshing a service description](#62-refreshing-a-service-description)
  - [6.3 Enabling and Disabling a service description](#63-enabling-and-disabling-a-service-description)
  - [6.4 Changing the Address of a service description](#64-changing-the-address-of-a-service-description)
  - [6.5 Deleting a service description](#65-deleting-a-service-description)
  - [6.6 Changing the Parameters of a Service](#66-changing-the-parameters-of-a-service)
  - [6.7 Managing REST Endpoints](#67-managing-rest-endpoints)
  - [6.8 Configuring a Minimum Required Client Security Server Version](#68-configuring-a-minimum-required-client-security-server-version)
- [7 Access Rights](#7-access-rights)
  - [7.1 Changing the Access Rights of a Service](#71-changing-the-access-rights-of-a-service)
  - [7.2 Adding a Service Client](#72-adding-a-service-client)
  - [7.3 Changing the Access Rights of a Service Client](#73-changing-the-access-rights-of-a-service-client)
- [8 Local Access Right Groups](#8-local-access-right-groups)
  - [8.1 Adding a Local Group](#81-adding-a-local-group)
  - [8.2 Displaying and Changing the Members of a Local Group](#82-displaying-and-changing-the-members-of-a-local-group)
  - [8.3 Changing the description of a Local Group](#83-changing-the-description-of-a-local-group)
  - [8.4 Deleting a Local Group](#84-deleting-a-local-group)
- [9 Communication with Information Systems](#9-communication-with-information-systems)
  - [9.1 Communication with Service Consumer Information Systems](#91-communication-with-service-consumer-information-systems)
  - [9.2 Communication with Service Provider Information Systems](#92-communication-with-service-provider-information-systems)
  - [9.3 Managing Information System TLS Certificates](#93-managing-information-system-tls-certificates)
- [10 System Parameters](#10-system-parameters)
  - [10.1 Managing the Security Server address](#101-managing-the-security-server-address)
  - [10.2 Managing the Configuration Anchor](#102-managing-the-configuration-anchor)
  - [10.3 Managing the Timestamping Services](#103-managing-the-timestamping-services)
  - [10.4 Changing the Internal TLS Key and Certificate](#104-changing-the-internal-tls-key-and-certificate)
  - [10.5 Approved Certificate Authorities](#105-approved-certificate-authorities)
  - [10.6 Enable/Disable maintenance mode for the Security Server](#106-enabledisable-maintenance-mode-for-the-security-server)
- [11 Message Log](#11-message-log)
  - [11.1 Changing the Configuration of the Message Log](#111-changing-the-configuration-of-the-message-log)
    - [11.1.1 Common Parameters](#1111-common-parameters)
    - [11.1.2 Logging Parameters](#1112-logging-parameters)
    - [11.1.3 Message Log Encryption](#1113-message-log-encryption)
    - [11.1.4 Timestamping Parameters](#1114-timestamping-parameters)
    - [11.1.5 Archiving Parameters](#1115-archiving-parameters)
    - [11.1.6 Archive Files](#1116-archive-files)
    - [11.1.7 Archive Encryption and Grouping](#1117-archive-encryption-and-grouping)
  - [11.2 Transferring the Archive Files from the Security Server](#112-transferring-the-archive-files-from-the-security-server)
  - [11.3 Using a Remote Database](#113-using-a-remote-database)
- [12 Audit Log](#12-audit-log)
  - [12.1 Changing the Configuration of the Audit Log](#121-changing-the-configuration-of-the-audit-log)
  - [12.2 Archiving the Audit Log](#122-archiving-the-audit-log)
- [13 Back up and restore](#13-back-up-and-restore)
  - [13.1 Back up and Restore in the User Interface](#131-back-up-and-restore-in-the-user-interface)
  - [13.2 Restore from the Command Line](#132-restore-from-the-command-line)
  - [13.3 Automatic Backups](#133-automatic-backups)
  - [13.4 Backup Encryption Configuration](#134-backup-encryption-configuration)
  - [13.5 Verifying Backup Archive Consistency](#135-verifying-backup-archive-consistency)
- [14 Diagnostics](#14-diagnostics)
  - [14.1 Examine Security Server services status information](#141-examine-security-server-services-status-information)
  - [14.2 Examine Security Server Java version information](#142-examine-security-server-java-version-information)
  - [14.3 Examine Security Server encryption status information](#143-examine-security-server-encryption-status-information)
  - [14.4 Download diagnostics report](#144-download-diagnostics-report)
- [15 Operational Monitoring](#15-operational-monitoring)
  - [15.1 Operational Monitoring Buffer](#151-operational-monitoring-buffer)
    - [15.1.1 Stopping the Collecting of Operational Data](#1511-stopping-the-collecting-of-operational-data)
  - [15.2 Operational Monitoring Daemon](#152-operational-monitoring-daemon)
    - [15.2.1 Configuring the Health Statistics Period](#1521-configuring-the-health-statistics-period)
    - [15.2.2 Configuring the Parameters Related to Database Cleanup](#1522-configuring-the-parameters-related-to-database-cleanup)
    - [15.2.3 Configuring the Parameters related to the HTTP Endpoint of the Operational Monitoring Daemon](#1523-configuring-the-parameters-related-to-the-http-endpoint-of-the-operational-monitoring-daemon)
    - [15.2.4 Installing an External Operational Monitoring Daemon](#1524-installing-an-external-operational-monitoring-daemon)
    - [15.2.5 Configuring an External Operational Monitoring Daemon and the Corresponding Security Server](#1525-configuring-an-external-operational-monitoring-daemon-and-the-corresponding-security-server)
    - [15.2.6 Monitoring Health Data over JMXMP](#1526-monitoring-health-data-over-jmxmp)
- [16 Environmental Monitoring](#16-environmental-monitoring)
  - [16.1 Usage via SOAP API](#161-usage-via-soap-api)
  - [16.2 Usage via JMX API](#162-usage-via-jmx-api)
  - [16.3 Limiting environmental monitoring remote data set](#163-limiting-environmental-monitoring-remote-data-set)
- [17 Logs and System Services](#17-logs-and-system-services)
  - [17.1 System Services](#171-system-services)
  - [17.2 Logging configuration](#172-logging-configuration)
  - [17.3 Fault Detail UUID](#173-fault-detail-uuid)
- [18 Federation](#18-federation)
- [19 Management REST API](#19-management-rest-api)
  - [19.1 API key management operations](#191-api-key-management-operations)
    - [19.1.1 Creating new API keys](#1911-creating-new-api-keys)
    - [19.1.2 Listing API keys](#1912-listing-api-keys)
    - [19.1.3 Updating API keys](#1913-updating-api-keys)
    - [19.1.4 Revoking API keys](#1914-revoking-api-keys)
    - [19.1.5 API key caching](#1915-api-key-caching)
  - [19.2 Executing REST calls](#192-executing-rest-calls)
  - [19.3 Correlation ID HTTP header](#193-correlation-id-http-header)
  - [19.4 Validation errors](#194-validation-errors)
  - [19.5 Warning responses](#195-warning-responses)
- [20 Migrating to Remote Database Host](#20-migrating-to-remote-database-host)
- [21 Adding command line arguments](#21-adding-command-line-arguments)
    - [21.1 Updating Proxy Service's memory allocation command line arguments](#211-updating-proxy-services-memory-allocation-command-line-arguments)
- [22 Additional Security Hardening](#22-additional-security-hardening)
- [23 Passing additional parameters to psql](#23-passing-additional-parameters-to-psql)
- [24 Configuring ACME](#24-configuring-acme)
- [25 Migrating to EC Based Authentication and Signing Certificates](#25-migrating-to-ec-based-authentication-and-signing-certificates)
  - [25.1 Steps to Enable EC Based Certificates](#251-Steps-to-enable-EC-based-certificates)
  - [25.2 Backwards Compatibility](#252-Backwards-compatibility)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/

## 1 Introduction

This document describes the management and maintenance of an X-Road version 7 Security Server.