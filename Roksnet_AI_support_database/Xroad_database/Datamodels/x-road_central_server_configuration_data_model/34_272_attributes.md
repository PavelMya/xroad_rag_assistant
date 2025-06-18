#### 2.7.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| security_server_id [FK] | integer |  | ID of the Security Server the authentication certificate belongs to. References id attribute of security_servers entity. Cannot be NULL. |
| cert | bytea |  | Authentication certificate contents (in DER encoding). Cannot be NULL. |
| created_at | timestamp without time zone | NOT NULL | Record creation time, managed automatically. |
| updated_at | timestamp without time zone | NOT NULL | Record last modified time, managed automatically. |