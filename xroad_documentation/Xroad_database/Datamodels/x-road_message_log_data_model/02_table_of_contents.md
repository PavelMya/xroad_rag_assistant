## Table of Contents


- [X-Road: Message Log Data Model](#x-road-message-log-data-model)
- [1. General](#1-general)
  - [1.1 Preamble](#11-preamble)
  - [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
    - [1.3 References](#13-references)
  - [1.4 Database Version](#14-database-version)
  - [1.5 Creating, Backing Up and Restoring the Database](#15-creating-backing-up-and-restoring-the-database)
  - [1.6 Message Logging and Timestamping](#16-message-logging-and-timestamping)
  - [1.7 Entity-Relationship Diagram](#17-entity-relationship-diagram)
- [2. Description of Entities](#2-description-of-entities)
  - [2.1 LOGRECORD](#21-logrecord)
    - [2.1.1 Indexes](#211-indexes)
    - [2.1.2 Attributes](#212-attributes)
  - [2.2 LAST_ARCHIVE_DIGEST](#22-last_archive_digest)
    - [2.2.1 Indexes](#221-indexes)
    - [2.2.2 Attributes](#222-attributes)
  - [2.3 DATABASECHANGELOG](#23-databasechangelog)
    - [2.3.1 Attributes](#231-attributes)
  - [2.4 DATABASECHANGELOGLOCK](#24-databasechangeloglock)
    - [2.4.1 Attributes](#241-attributes)

## 1. General

### 1.1 Preamble

This document describes database model of X-Road message log.

### 1.2 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].

### 1.3 References

1. \[TA-TERMS\] X-Road Terms and Abbreviations. Document ID: [TA-TERMS](../terms_x-road_docs.md).

### 1.4 Database Version

This database assumes PostgreSQL version 9.2 or later.