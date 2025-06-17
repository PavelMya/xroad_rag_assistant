#### 2.24.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK]  | integer | NOT NULL | Primary key |
| instance_identifier | character varying(255) |  | Instance identifier of the trusted anchor. Cannot be NULL. |
| trusted_anchor_file  | bytea |  | Trusted anchor file (in XML format). Cannot be NULL. |
| trusted_anchor_hash  | text |  | Hash of the trusted anchor file. Cannot be NULL. |
| created_at  | timestamp without time zone |  | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone |  | Record last modified time, managed automatically.  |
| generated_at  | timestamp without time zone |  | Anchor generation time (read from the anchor file).  |