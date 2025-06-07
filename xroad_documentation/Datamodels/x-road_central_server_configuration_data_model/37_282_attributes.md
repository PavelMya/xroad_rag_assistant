#### 2.8.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| cert | bytea |  | Contents of the CA certificate (in DER encoding). Cannot be NULL. |
| intermediate_ca_id [FK] | integer |  | Used to associate the ca_info record with a top-level CA record. This field is present only for intermediate-level CAs (top-level CA is referenced directly by the ca_info table. References to id attribute of approved_cas entity. |
| valid_from | timestamp without time zone |  | Start of validity period of the CA's certificate. Extracted from the certificate. |
| valid_to | timestamp without time zone |  | End of validity period of the CA's certificate. Extracted from the certificate. |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |