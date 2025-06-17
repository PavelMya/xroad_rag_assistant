### 2.16 SERVICEDESCRIPTION

Pointer to a SERVICEDESCRIPTION containing the descriptions of services provided by a security server client. A SERVICEDESCRIPTION record is created when the administrator adds a new service description to a security server client in the user interface. The record is modified when the administrator refreshes, enables or disables the service description. The record is deleted when the administrator deletes the service description or the security server client owning the service description.

#### 2.16.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| WSDL_CLIENT_ID_fkey | client_id |