#### 2.9.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| configuration_source_id [FK] | integer |  | ID of the configuration source that uses this signing key. References id attribute of configuration_sources entity. Cannot be NULL. |
| key_identifier  | character varying(255) |  | Contents of the configuration signing certificate (in DER encoding).  |
| cert | bytea |  |  |
| key_generated_at  | timestamp without time zone |  | The signing key generation time.  |
| token_identifier  | character varying(255) |  | Unique identifier of hardware or software token used for signing the configuration.  |