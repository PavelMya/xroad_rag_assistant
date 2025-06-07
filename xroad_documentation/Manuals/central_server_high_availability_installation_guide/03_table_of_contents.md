## Table of Contents 




- [License](#license)
- [1 Introduction](#1-introduction)
  - [1.1 High Availability for X-Road Central Server](#11-high-availability-for-x-road-central-server)
  - [1.2 Target Audience](#12-target-audience)
  - [1.3 Terms and abbreviations](#13-terms-and-abbreviations)
  - [1.4 References](#14-references)
- [2 Key Points and Known Limitations for X-Road Central Server HA Deployment](#2-key-points-and-known-limitations-for-x-road-central-server-ha-deployment)
- [3 Requirements and Workflows for HA Configuration](#3-requirements-and-workflows-for-ha-configuration)
  - [3.1 Requirements](#31-requirements)
  - [3.2 Workflow for a New X-Road Instance Setup](#32-workflow-for-a-new-x-road-instance-setup)
  - [3.3 Workflow for Upgrading an Existing X-Road Central Server to an HA Configuration](#33-workflow-for-upgrading-an-existing-x-road-central-server-to-an-ha-configuration)
  - [3.4 Workflow for Adding New Nodes to an Existing HA Configuration](#34-workflow-for-adding-new-nodes-to-an-existing-ha-configuration)
  - [3.5 Post-Configuration Steps](#35-post-configuration-steps)
- [4 General Installation of HA Support](#4-general-installation-of-ha-support)
- [5 Monitoring HA State on a Node](#5-monitoring-ha-state-on-a-node)
- [6 Recovery of the HA cluster](#6-recovery-of-the-ha-cluster)
  - [6.1 Configuration database (and possible replicas) is lost](#61-configuration-database-and-possible-replicas-is-lost)
  - [6.2 One or more cental server nodes lost, backup available](#62-one-or-more-cental-server-nodes-lost-backup-available)
  - [6.3 Some Central Server nodes lost, backup not available](#63-some-central-server-nodes-lost-backup-not-available)
- [Appendix A. Setting up a replicated PostgreSQL database](#appendix-a-setting-up-a-replicated-postgresql-database)
  - [Prerequisites](#prerequisites)
  - [PostgreSQL configuration (all database servers)](#postgresql-configuration-all-database-servers)
  - [Preparing the standby](#preparing-the-standby)
  - [Verifying replication](#verifying-replication)
  - [Configuring Central Servers](#configuring-central-servers)
  - [Fail-over](#fail-over)
    - [Automatic fail-over](#automatic-fail-over)
- [Appendix B. Central Server HA Migration](#appendix-b-central-server-ha-migration)
  - [Migrating from Standalone to HA Cluster](#migrating-from-standalone-to-ha-cluster)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/

## 1 Introduction