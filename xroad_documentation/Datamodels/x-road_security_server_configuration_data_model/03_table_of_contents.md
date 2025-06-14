## Table of Contents


* [License](#license)
* [1 General](#1-general)
  * [1.1 Preamble](#11-preamble)
  * [1.2 Database Version](#12-database-version)
  * [1.3 Creating, Backing Up and Restoring the Database](#13-creating-backing-up-and-restoring-the-database)
  * [1.4 Saving Database History](#14-saving-database-history)
  * [1.5 Entity-Relationship Diagram](#15-entity-relationship-diagram)
  * [1.6 List of Stored Procedures](#16-list-of-stored-procedures)
  * [1.7 List of Triggers](#17-list-of-triggers)
* [2 Description of Entities](#2-description-of-entities)
  * [2.1 ACCESSRIGHT](#21-accessright)
    * [2.1.1 Indexes](#211-indexes)
    * [2.1.2 Attributes](#212-attributes)
  * [2.2 APIKEY](#22-apikey)
    * [2.2.1 Attributes](#221-attributes)
  * [2.3 APIKEY_ROLES](#23-apikey_roles)
    * [2.3.1 Indexes](#231-indexes)
    * [2.3.2 Attributes](#232-attributes)
  * [2.4 CERTIFICATE](#24-certificate)
    * [2.4.1 Attributes](#241-attributes)
  * [2.5 CLIENT](#25-client)
    * [2.5.1 Indexes](#251-indexes)
    * [2.5.2 Attributes](#252-attributes)
  * [2.6 DATABASECHANGELOG](#26-databasechangelog)
    * [2.6.1 Attributes](#261-attributes)
  * [2.7 DATABASECHANGELOGLOCK](#27-databasechangeloglock)
    * [2.7.1 Attributes](#271-attributes)
  * [2.8 GROUPMEMBER](#28-groupmember)
    * [2.8.1 Indexes](#281-indexes)
    * [2.8.2 Attributes](#282-attributes)
  * [2.9 HISTORY](#29-history)
    * [2.9.1 Attributes](#291-attributes)
  * [2.10 IDENTIFIER](#210-identifier)
    * [2.10.1 Attributes](#2101-attributes)
  * [2.11 LOCALGROUP](#211-localgroup)
    * [2.11.1 Indexes](#2111-indexes)
    * [2.11.2 Attributes](#2112-attributes)
  * [2.12 SERVERCONF](#212-serverconf)
    * [2.12.1 Indexes](#2121-indexes)
    * [2.12.2 Attributes](#2122-attributes)
  * [2.13 SERVICE](#213-service)
    * [2.13.1 Indexes](#2131-indexes)
    * [2.13.2 Attributes](#2132-attributes)
  * [2.14 TSP](#214-tsp)
    * [2.14.1 Indexes](#2141-indexes)
    * [2.14.2 Attributes](#2142-attributes)
  * [2.15 UIUSER](#215-uiuser)
    * [2.15.1 Attributes](#2151-attributes)
  * [2.16 SERVICEDESCRIPTION](#216-servicedescription)
    * [2.16.1 Indexes](#2161-indexes)
    * [2.16.2 Attributes](#2162-attributes)
  * [2.17 ENDPOINT](#217-endpoint)
    * [2.17.1 Indexes](#2171-indexes)
    * [2.17.2 Attributes](#2172-attributes)

## License

This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported Li-cense. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1 General

### 1.1 Preamble

This document describes database model of X-Road security server.

### 1.2 Database Version

This database assumes PostgreSQL version 9.2 or later.