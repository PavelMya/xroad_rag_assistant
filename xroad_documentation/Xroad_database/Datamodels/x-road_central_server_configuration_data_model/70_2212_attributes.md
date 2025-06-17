#### 2.21.2 Attributes

| Name                     |            Type             | Modifiers | Description                                                                                                                       |
|:-------------------------|:---------------------------:|:----------|:----------------------------------------------------------------------------------------------------------------------------------|
| id [PK]                  |           integer           | NOT NULL  | Primary key                                                                                                                       |
| server_code              |   character varying(255)    |           | Security Server code, unique between Security Servers belonging to the same owner. Cannot be NULL.                                |
| owner_id [FK]            |           integer           |           | ID of the X-Road member that owns the Security Server. References id attribute of security_server_clients entity. Cannot be NULL. |
| address                  |   character varying(255)    |           | DNS name or IP-address of the Security Server.                                                                                    |
| in_maintenance_mode      |           boolean           | NOT NULL  | Indicates whether Security server is in maintenance mode (true) or not (false)                                                    |
| maintenance_mode_message |   character varying(255)    |           | Optional short message when in maintenance mod.                                                                                   |
| created_at               | timestamp without time zone | NOT NULL  | Record creation time, managed automatically.                                                                                      |
| updated_at               | timestamp without time zone | NOT NULL  | Record last modified time, managed automatically.                                                                                 |