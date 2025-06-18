#### 2.17.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key. |
| url  | character varying(255) |  | URL of the OCSP server. Must correspond to the URL format. Cannot be NULL. |
| cert  | bytea |  | Certificate used by the OCSP server to sign OCSP responses (in DER encoding). |
| ca_info_id [FK] | integer |  | ID of the CA info record this OCSP info belongs to. References id attribute of ca_infos entity. Cannot be NULL. |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |