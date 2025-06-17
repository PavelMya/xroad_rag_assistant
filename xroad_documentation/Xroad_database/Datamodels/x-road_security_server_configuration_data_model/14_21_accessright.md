### 2.1 ACCESSRIGHT

Access right of a security server client or a group of clients to use a particular service. An access right record is created when an access right for a service is granted. The record is deleted when the service is removed from the system configuration or the access right is forfeited. The record is never modified.

#### 2.1.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| ACCESSRIGHT_CLIENT_ID_fkey | client_id |
| AUTHORIZEDSUBJECT_SUBJECTID_fkey | subjectid |