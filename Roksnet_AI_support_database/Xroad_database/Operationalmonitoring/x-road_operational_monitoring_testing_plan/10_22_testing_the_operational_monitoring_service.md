### 2.2 Testing the Operational Monitoring Service

The operational monitoring service receives and processes operational and health data requests via the Operational Monitoring Query interface. This service is used by the security server. This service is tested at the following levels:

* Build-time unit tests are used for testing the conversion of query criteria in SOAP requests to the corresponding criteria of database queries.
* At system integration level, the operational monitoring service is tested directly as a central part of the automated integration tests.