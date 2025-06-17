### 2.7 AUTH_CERTS

Authentication certificate that is used by a Security Server to establish secure connection. Each authentication certificate belongs to a particular Security Server.

The record is created when X-Road registration officer approves the request in the user interface. The record is removed whenever there is need to remove the Security Server the record belongs to or when the authentication certificate cannot be used any more. An X-Road registration officer can either remove Security Server or send authentication certificate deletion request for the Security Server in the user interface. The latter is done when only authentication certificate (without Security Server) is going to be deleted. The record is never modified. See also documentation of table security_servers.

#### 2.7.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_auth_certs_on_security_server_id | security_server_id |