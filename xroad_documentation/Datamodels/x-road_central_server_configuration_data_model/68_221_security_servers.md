### 2.21 SECURITY_SERVERS

Information about a Security Server registered in this X-Road instance. Security Server always belongs to a particular X-Road member. For Security Server to function properly, it needs at least one authentication certificate. Security Server may have clients (subsystems).

A prerequisite for creating the record is that the authentication certificate registration request for not yet existing Security Server are approved (see also documentation of tables requests and request_processings). The record is created when request is approved by an X-Road registration officer in the user interface. The record is modified when an X-Road registration officer edits Security Server address in the user interface. The record can be deleted in the user interface by an X-Road registration officer.

#### 2.21.1 Indexes

| Name                                      |     Columns     |
|:------------------------------------------|:---------------:|
| index_security_servers_on_xroad_member_id | xroad_member_id |