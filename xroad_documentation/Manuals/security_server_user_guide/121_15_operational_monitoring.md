## 15 Operational Monitoring

**Operational monitoring data** contains data about request exchange (such as the ID-s of the client and the service, various attributes of the message read from the message header, request and response timestamps, SOAP sizes etc.) of the X-Road Security Server(s).

**The operational monitoring daemon** collects and shares operational monitoring data of the X-Road Security Server(s) as part of request exchange, shares this data, calculates and shares health statistics (the timestamps and number of successful/unsuccessful requests, various metrics of the duration and the SOAP message size of the requests, etc.). The data fields that are stored and shared are described in \[[PR-OPMON](#Ref_PR-OPMON)\].

The Security Server caches operational monitoring data in the **operational monitoring buffer**. One operational data record is created for each request during the message exchange. Security server forwards operational data cached in the operational monitoring buffer to the operational monitoring daemon. Successfully forwarded records are removed from the operational monitoring buffer.

The operational monitoring daemon makes operational and health data available to the owner of the Security Server, regular clients and the central monitoring client via the Security Server. Local health data are available for external monitoring systems (e.g. Zabbix) over the JMXMP interface described in \[[PR-OPMONJMX](#Ref_PR-OPMONJMX)\].

The owner of the Security Server and the central monitoring client are able to query the records of all clients. For a regular client, only the records associated with that client are available. The internal IP of the Security Server is included in the response only for the owner of the Security Server and central monitoring client.

**NOTE:** All the commands in the following sections must be carried out using root permissions.