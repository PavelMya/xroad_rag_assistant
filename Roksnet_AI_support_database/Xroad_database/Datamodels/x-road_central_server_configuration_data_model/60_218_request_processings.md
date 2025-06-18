### 2.18 REQUEST_PROCESSINGS

Processing status of the management request. Management requests are means of managing clients and authentication certificates of Security Servers. See also documentation of the table requests. 
- In older version request processing binds together two management requests that refer to the same data but have different origin (Security Server or user interface of the Central Server). If one request associated with the processing is from Central Server, the other one must be from Security Server and vice versa. 
- Starting in X-Road version 7.3.0 request_processing table contain only one record per request, there is no complementary request anymore.

Request processing can have one of following statuses:

- WAITING – Central Server has received a request. From this state, the user must either approve or decline the request.
- SUBMITTED FOR APPROVAL – Central Server has received two complementary requests from different sources. From this state, the user must either approve or decline the request. Starting in X-Road version 7.3.0 not used anymore.
- APPROVED – when the user approves the request, the processing enters APPROVED state. When entering this state the requested action (such as adding a client to a Security Server) is performed.
- REVOKED – when the processing is in WAITING state, respective deletion request can be sent to revoke the request. Deletion request can be sent from Security Server.
- DECLINED – when the processing is in WAITING state, it can be declined from the user interface if X-Road registration officer decides so.

Request processing record is created (registration requests for X-Road client and Security Server authentication certificate) from Security Server. Modifications to the record are related to changes of the request processing status and are described above in this section. The record is never deleted.