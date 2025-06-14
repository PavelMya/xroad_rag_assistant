## Table of Contents

- [X-Road: Central Server Configuration Data Model](#x-road-central-server-configuration-data-model)
	- [Table of Contents](#table-of-contents)
	- [License](#license)
- [1 General](#1-general)
	- [1.1 Preamble](#11-preamble)
	- [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
    - [1.3 References](#13-references)
	- [1.4 Database Version](#14-database-version)
	- [1.5 Creating, Backing Up and Restoring the Database](#15-creating-backing-up-and-restoring-the-database)
	- [1.6 Saving Database History](#16-saving-database-history)
	- [1.7 High Availability Support](#17-high-availability-support)
	- [1.8 Entity-Relationship Diagram](#18-entity-relationship-diagram)
	- [1.9 List of Stored Procedures](#19-list-of-stored-procedures)
	- [1.10 List of Triggers](#110-list-of-triggers)
- [2 Description of Entities](#2-description-of-entities)
	- [2.1 ANCHOR_URL_CERTS](#21-anchor_url_certs)
		- [2.1.1 Indexes](#211-indexes)
		- [2.1.2 Attributes](#212-attributes)
	- [2.2 ANCHOR_URLS](#22-anchor_urls)
		- [2.2.1 Indexes](#221-indexes)
		- [2.2.2 Attributes](#222-attributes)
    - [2.3 APIKEY](#23-apikey)
		- [2.3.1 Attributes](#231-attributes)
    - [2.4 APIKEY_ROLES](#24-apikey_roles)
        - [2.4.1 Indexes](#241-indexes)
		- [2.4.2 Attributes](#242-attributes)
	- [2.5 APPROVED_CAS](#25-approved_cas)
		- [2.5.1 Indexes](#251-indexes)
		- [2.5.2 Attributes](#252-attributes)
	- [2.6 APPROVED_TSAS](#26-approved_tsas)
		- [2.6.1 Attributes](#261-attributes)
	- [2.7 AUTH_CERTS](#27-auth_certs)
		- [2.7.1 Indexes](#271-indexes)
		- [2.7.2 Attributes](#272-attributes)
	- [2.8 CA_INFOS](#28-ca_infos)
		- [2.8.1 Indexes](#281-indexes)
		- [2.8.2 Attributes](#282-attributes)
	- [2.9 CONFIGURATION_SIGNING_KEYS](#29-configuration_signing_keys)
		- [2.9.1 Indexes](#291-indexes)
		- [2.9.2 Attributes](#292-attributes)
	- [2.10 CONFIGURATION_SOURCES](#210-configuration_sources)
		- [2.10.1 Indexes](#2101-indexes)
		- [2.10.2 Attributes](#2102-attributes)
	- [2.11 DISTRIBUTED_FILES](#211-distributed_files)
		- [2.11.1 Attributes](#2111-attributes)
	- [2.12 GLOBAL_GROUP_MEMBERS](#212-global_group_members)
		- [2.12.1 Indexes](#2121-indexes)
		- [2.12.2 Attributes](#2122-attributes)
	- [2.13 GLOBAL_GROUPS](#213-global_groups)
		- [2.13.1 Attributes](#2131-attributes)
	- [2.14 HISTORY](#214-history)
		- [2.14.1 Attributes](#2141-attributes)
	- [2.15 IDENTIFIERS](#215-identifiers)
		- [2.15.1 Attributes](#2151-attributes)
	- [2.16 MEMBER_CLASSES](#216-member_classes)
		- [2.16.1 Attributes](#2161-attributes)
	- [2.17 OCSP_INFOS](#217-ocspinfos)
		- [2.17.1 Indexes](#2171-indexes)
		- [2.17.2 Attributes](#2172-attributes)
	- [2.18 REQUEST_PROCESSINGS](#218-request_processings)
		- [2.18.1 Attributes](#2181-attributes)
	- [2.19 REQUESTS](#219-requests)
		- [2.19.1 Indexes](#2191-indexes)
		- [2.19.2 Attributes](#2192-attributes)
	- [2.20 SECURITY_SERVER_CLIENTS](#220-security_server_clients)
		- [2.20.1 Indexes](#2201-indexes)
		- [2.20.2 Attributes](#2202-attributes)
	- [2.21 SECURITY_SERVERS](#221-security_servers)
		- [2.21.1 Indexes](#2211-indexes)
		- [2.21.2 Attributes](#2212-attributes)
	- [2.22 SERVER_CLIENTS](#222-server_clients)
		- [2.22.1 Indexes](#2221-indexes)
		- [2.22.2 Attributes](#2222-attributes)
	- [2.23 SYSTEM_PARAMETERS](#223-system_parameters)
		- [2.23.1 Attributes](#2231-attributes)
	- [2.24 TRUSTED_ANCHORS](#224-trusted_anchors)
		- [2.24.1 Attributes](#2241-attributes)
	- [2.25 UI_USERS](#225-ui_users)
		- [2.25.1 Attributes](#2251-attributes)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1 General

### 1.1 Preamble

This document describes the database model of the X-Road Central Server.

### 1.2 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].

### 1.3 References

1. \[TA-TERMS\] X-Road Terms and Abbreviations. Document ID: [TA-TERMS](../terms_x-road_docs.md).

### 1.4 Database Version

This database assumes PostgreSQL version 12 or later. Default settings are used in simple setup, while a custom configuration is used in HA setup.