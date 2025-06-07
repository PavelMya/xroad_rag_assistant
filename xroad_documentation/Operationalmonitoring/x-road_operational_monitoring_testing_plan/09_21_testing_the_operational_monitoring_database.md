### 2.1 Testing the Operational Monitoring Database

The operational monitoring database component collects operational data of the X-Road security server(s) via the Store Operational Data interface. The requirements for data stored in the database are defined in \[[HD_1](#HD_1)\].

The database is tested at the following levels:
* Direct SQL is used by the developers and testers for ad-hoc queries during development and testing. The source code of the operational monitoring daemon does not make any raw SQL queries, however.
* Build-time unit tests written in Java 8 are used for testing the behaviour of the Hibernate library in Java code using the HSQLDB in-memory database, for checking the access to, and operations with the database records as Java objects.
* Also, build-time unit tests are used for testing transactional operations on the database in Java code.
* Conversion of operational monitoring data from the JSON representation to objects encapsulating database records, is covered by build-time unit tests in Java 8.
* The behaviour of the database component is tested during automated integration testing and load testing as part of the message exchange carried out.
* Creation and upgrades of the database schema using the combination of Hibernate and the PostgreSQL database are tested manually during the installation and upgrades of the testing environment. The source code of the operational monitoring daemon does not (and cannot) alter the database schema at runtime.