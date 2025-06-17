#### 2.17.2 Attributes

| Name           | Type           | Modifiers   | Description     |
|:-------------- |:--------------:|:----------- |:----------------|
| id [PK]        | bigint         | NOT NULL    | Primary key.    |
| client_id [FK] | bigint         |         | The security server client who provides the service. References id attribute of CLIENT entity.          |
| servicecode    | character varying(255)  | NOT NULL | The service code part of the service identifier. |
| method         | character varying(255)  | NOT NULL | The allowed HTTP method (REST services) |
| path           | character varying(2048) | NOT NULL | Allowed URL path (REST services) |
| generated      | boolean        | NOT NULL | Is the endpoint automatically generated (true) or manually added (false) |