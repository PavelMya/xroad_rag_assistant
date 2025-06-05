### 2.19 REQUESTS

Management request for creating or deleting association between X-Road member and Security Server. Management requests are divided into registration and deletion requests.

- Registration requests are submitted through X-Road Security Server. The request can be either approved or declined in the user interface of the Central Server. There are two types of registration requests: registration of a Security Server client and registration of Security Server's authentication certificate.
- Deletion requests are there to delete associations between X-Road clients, Security Servers and authentication certificates. Deletion requests are not associated with request processing. There are two types of deletion requests: deletion of Security Server's authentication certificate and  deletion of Security Server' client. Deletion request can be sent for following purposes:
  - if a registration request is mistakenly sent (from user interface of the Security Server), respective (with the same client, Security Server and/or authentication certificate data) deletion request can be sent to delete the bad registration request;
  - if authentication certificate of Central Server needs to be deleted, respective authentication certificate deletion request is sent either from user interface of the Central Server or Security Server;
  - if client of a Security Server needs to be removed, respective deletion request can be sent.

The record is created in the manner described above in this section. Starting in X-Road version 7.3.0 the record is never modified.
The record is never deleted.