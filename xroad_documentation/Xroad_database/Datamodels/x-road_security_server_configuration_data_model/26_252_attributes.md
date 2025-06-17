#### 2.5.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | bigint | NOT NULL | Primary key |
| conf_id [FK] | bigint |  | Identifies the serverconf. References id attribute of SERVERCONF entity. |
| identifier [FK] | bigint |  | Identifies the security server client. References id attribute of IDENTIFIER entity. |
| clientstatus | character varying(255) |  | Current status of the client. Possible values are “saved”, “registration in progress”, “registered”, “deletion in progress”, “global error” |
| isauthentication | character varying(255) |  | Type of HTTPS authentication that is used with the client's information systems. Possible values are the following “NOSSL” -- the client can connect with HTTP or HTTPS protocol. For HTTPS connection, no authentication is used.“SSLNOAUTH” -- the client can only connect with HTTPS protocol. No certificate-based authentication is used.“SSLAUTH” -- the client can only connect with HTTPS protocol. The client must authenticate the connection with certificate.|