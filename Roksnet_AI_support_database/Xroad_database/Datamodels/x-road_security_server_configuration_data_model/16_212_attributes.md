#### 2.1.2 Attributes

| Name        | Type           | Modifiers        | Description          |
|:----------- |:--------------:|:----------------:|:--------------------|
| id [PK]     | bigint         | NOT NULL         | Primary key          |
| client_id [FK] | bigint         |         | The security server client who provides the service. References id attribute of CLIENT entity.          |
| subjectid [FK]     | bigint         | NOT NULL         | Identifier of a subject that is authorized to access the service. Can be either a member, a subsystem, global group or local group. References id attribute of IDENTIFIER entity.          |
| rightsgiven     | timestamp without time zone         | NOT NULL         | The time when the access right was granted.           |
| endpoint_id [FK]     | bigint         |         | The authorized endpoint. References id attribute of ENDPOINT entity. |

### 2.2 APIKEY

API key which grants access to REST API operations.