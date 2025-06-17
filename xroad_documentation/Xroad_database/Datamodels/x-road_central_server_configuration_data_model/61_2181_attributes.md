#### 2.18.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| type  | character varying(255) |  | Application model class type, managed automatically.  Possible values are 'ClientRegProcessing' and 'AuthCertRegProcessing'. |
| status | character varying(255) |  | Current status of the request processing. Possible values are 'NEW', 'WAITING', 'EXECUTING', 'SUBMITTED FOR APPROVAL', 'APPROVED', 'DECLINED' and 'REVOKED'.  |
| created_at | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |