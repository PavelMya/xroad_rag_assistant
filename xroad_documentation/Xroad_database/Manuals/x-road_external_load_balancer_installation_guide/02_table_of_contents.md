## Table of Contents




- [X-Road: External Load Balancer Installation Guide](#x-road-external-load-balancer-installation-guide)
  - [Table of Contents](#table-of-contents)
  - [License](#license)
  - [1. Introduction](#1-introduction)
    - [1.1 Target Audience](#11-target-audience)
    - [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
    - [1.3 References](#13-references)
  - [2. Overview](#2-overview)
    - [2.1 Goals and assumptions](#21-goals-and-assumptions)
      - [2.1.1 Basic assumptions about the load balanced environment](#211-basic-assumptions-about-the-load-balanced-environment)
      - [2.1.2 Consequences of the selected implementation model](#212-consequences-of-the-selected-implementation-model)
    - [2.2 Communication with external servers and services: The cluster from the point of view of a client or service](#22-communication-with-external-servers-and-services-the-cluster-from-the-point-of-view-of-a-client-or-service)
    - [2.3 State replication from the primary to the secondaries](#23-state-replication-from-the-primary-to-the-secondaries)
      - [2.3.1 Replicated state](#231-replicated-state)
        - [2.3.1.1 `serverconf` database replication](#2311-serverconf-database-replication)
        - [2.3.1.2 Key configuration and software token replication from `/etc/xroad/signer/*`](#2312-key-configuration-and-software-token-replication-from-etcxroadsigner)
        - [2.3.1.3 Other server configuration parameters from `/etc/xroad/*`](#2313-other-server-configuration-parameters-from-etcxroad)
      - [2.3.2 Non-replicated state](#232-non-replicated-state)
        - [2.3.2.1 `messagelog` database](#2321-messagelog-database)
        - [2.3.2.2 OCSP responses from `/var/cache/xroad/`](#2322-ocsp-responses-from-varcachexroad)
  - [3. X-Road Installation and configuration](#3-x-road-installation-and-configuration)
    - [3.1 Prerequisites](#31-prerequisites)
    - [3.2 Primary installation](#32-primary-installation)
    - [3.3 Secondary installation](#33-secondary-installation)
    - [3.4 Health check service configuration](#34-health-check-service-configuration)
      - [3.4.1 Known check result inconsistencies vs. actual state](#341-known-check-result-inconsistencies-vs-actual-state)
      - [3.4.2 Health check examples](#342-health-check-examples)
      - [3.4.3 Proxy memory health check](#343-proxy-memory-health-check)
  - [4. Database replication setup](#4-database-replication-setup)
    - [4.1 Setting up TLS certificates for database authentication](#41-setting-up-tls-certificates-for-database-authentication)
    - [4.2 Creating a separate PostgreSQL instance for the `serverconf` database](#42-creating-a-separate-postgresql-instance-for-the-serverconf-database)
      - [4.2.1 on RHEL](#421-on-rhel)
        - [4.2.1.1 on RHEL 7](#4211-on-rhel-7)
        - [4.2.1.2 on RHEL 8 and 9](#4212-on-rhel-8-and-9)
      - [4.2.2 on Ubuntu](#422-on-ubuntu)
    - [4.3 Configuring the primary instance for replication](#43-configuring-the-primary-instance-for-replication)
    - [4.4 Configuring the secondary instance for replication](#44-configuring-the-secondary-instance-for-replication)
  - [5. Configuring data replication with rsync over SSH](#5-configuring-data-replication-with-rsync-over-ssh)
    - [5.1 Set up SSH between secondaries and the primary](#51-set-up-ssh-between-secondaries-and-the-primary)
    - [5.2 Set up periodic configuration synchronization on the secondary nodes](#52-set-up-periodic-configuration-synchronization-on-the-secondary-nodes)
      - [5.2.1 Use systemd for configuration synchronization](#521-use-systemd-for-configuration-synchronization)
    - [5.3 Set up log rotation for the sync log on the secondary nodes](#53-set-up-log-rotation-for-the-sync-log-on-the-secondary-nodes)
  - [6. Verifying the setup](#6-verifying-the-setup)
    - [6.1 Verifying rsync+ssh replication](#61-verifying-rsyncssh-replication)
    - [6.2 Verifying database replication](#62-verifying-database-replication)
    - [6.3 Verifying replication from the admin user interface](#63-verifying-replication-from-the-admin-user-interface)
  - [7. Upgrading a clustered X-Road Security Server installation](#7-upgrading-a-clustered-x-road-security-server-installation)
    - [7.1 Offline upgrade](#71-offline-upgrade)
    - [7.2 Online rolling upgrade](#72-online-rolling-upgrade)
      - [7.2.1 Pausing the database and configuration synchronization](#721-pausing-the-database-and-configuration-synchronization)
      - [7.2.2 Upgrading the primary](#722-upgrading-the-primary)
      - [7.2.3 Upgrade a single secondary node](#723-upgrade-a-single-secondary-node)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this
license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1. Introduction