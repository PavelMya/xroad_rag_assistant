#### 2.6.1 Attributes

| Name        | Columns           | Name        | Columns           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| name | character varying(255) |  | Name of the TSA, used in user interfaces. Technically, this is the subject name of the TSA certificate. |
| url | character varying(255) |  | URL that is used for sending time-stamping requests. Must correspond to the URL format. Cannot be NULL. |
| cert | bytea |  | TSA certificate that is used to verify issued time stamps. Stored in DER-encoded form. Cannot be NULL. |
| valid_from | timestamp without time zone |  | Start of validity period of the TSA's certificate. Extracted from the uploaded certificate. |
| valid_to | timestamp without time zone |  | End of validity period of the TSA's certificate. Extracted from the uploaded certificate. |
| created_at | timestamp without time zone | NOT NULL | Record creation time, managed automatically. |
| updated_at | timestamp without time zone | NOT NULL | Record last modified time, managed automatically. |