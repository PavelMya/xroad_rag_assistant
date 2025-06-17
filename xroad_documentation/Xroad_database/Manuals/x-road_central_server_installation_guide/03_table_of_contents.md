## Table of Contents 




- [License](#license)
- [1. Introduction](#1-introduction)
  - [1.1 Target Audience](#11-target-audience)
  - [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
  - [1.3 References](#13-references)
- [2. Installation](#2-installation)
  - [2.1 Prerequisites to Installation](#21-prerequisites-to-installation)
  - [2.2 Reference Data](#22-reference-data)
    - [2.2.1 Network Diagram](#221-network-diagram)
  - [2.3 Requirements to the Central Server](#23-requirements-to-the-central-server)
  - [2.4 Preparing OS](#24-preparing-os)
  - [2.5 Setup Package Repository](#25-setup-package-repository)
  - [2.6 Remote Database Setup (optional)](#26-remote-database-setup-optional)
  - [2.7 Package Installation](#27-package-installation)
    - [2.7.1 Configuring TLS Certificates](#271-configuring-tls-certificates)
  - [2.8 Installing the Support for Hardware Tokens](#28-installing-the-support-for-hardware-tokens)
  - [2.9 Installing the Support for Monitoring](#29-installing-the-support-for-monitoring)
  - [2.10 Pre-configuration for Registration Web Service](#210-pre-configuration-for-registration-web-service)
  - [2.11 Pre-configuration for Management Web Service](#211-pre-configuration-for-management-web-service)
  - [2.12 Post-Installation Checks](#212-post-installation-checks)
- [3 Initial Configuration](#3-initial-configuration)
  - [3.1 Reference Data](#31-reference-data)
  - [3.2 Initializing the Central Server](#32-initializing-the-central-server)
  - [3.3 Configuring the Central Server and the Management Services' Security Server](#33-configuring-the-central-server-and-the-management-services-security-server)
  - [3.4 Backup Encryption Configuration](#34-backup-encryption-configuration)
- [4 Additional configuration](#4-additional-configuration)
  - [4.1 Global configuration V1 support](#41-global-configuration-v1-support)
  - [4.2 Global configuration V2 support](#42-global-configuration-v2-support)
  - [4.3 Global configuration V3 support](#43-global-configuration-v3-support)
- [5 Installation Error Handling](#5-installation-error-handling)
  - [5.1 Cannot Set LC\_ALL to Default Locale](#51-cannot-set-lc_all-to-default-locale)
  - [5.2 PostgreSQL Is Not UTF8 Compatible](#52-postgresql-is-not-utf8-compatible)
  - [5.3 Could Not Create Default Cluster](#53-could-not-create-default-cluster)
  - [5.4 Is Postgres Running on Port 5432?](#54-is-postgres-running-on-port-5432)
  - [5.5 Upgrade supported from version X.Y.Z or newer](#55-upgrade-supported-from-version-xyz-or-newer)
  - [5.6 Data quality issues in the database](#56-data-quality-issues-in-the-database)
- [Annex A Central Server Default Database Properties](#annex-a-central-server-default-database-properties)
- [Annex B Database Users](#annex-b-database-users)
- [Annex C Deployment Options](#annex-c-deployment-options)
  - [C.1 General](#c1-general)
  - [C.2 Local Database](#c2-local-database)
  - [C.3 Remote Database](#c3-remote-database)
  - [C.4 Remote Database Cluster](#c4-remote-database-cluster)
  - [C.5 Cloud Database Cluster](#c5-cloud-database-cluster)
  - [C.6 Summary](#c6-summary)
- [Annex D Create Database Structure Manually](#annex-d-create-database-structure-manually)
- [Annex E Run Database Migrations Manually](#annex-e-run-database-migrations-manually)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1. Introduction