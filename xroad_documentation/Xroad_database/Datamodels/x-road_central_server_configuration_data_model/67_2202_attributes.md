#### 2.20.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| member_code  | character varying(255) |  | Member code, unique inside member class. NULL if type is 'Subsystem'. |
| subsystem_code  | character varying(255) |  | Subsystem code, unique inside member, filled if type is 'Subsystem'. NULL if type is 'XroadMember'. |
| name  | character varying(255) |  | Member (human-readable) name.  |
| xroad_member_id [FK] | integer |  | ID of the member the subsystem record belongs to. Filled if type is 'Subsystem'. NULL if type is 'XroadMember'. References id attribute of security_server_clients entity.  |
| member_class_id [FK] | integer |  | ID of the the member record belongs to. Filled if type is 'XroadMember'.  References id attribute of member_classes entity. Cannot be NULL. |
| server_client_id [FK] | integer |  | Full identifier of the client. References id attribute of identifiers entity. Cannot be NULL. |
| type  | character varying(255) |  | Application model class type, managed automatically. Possible values are 'XroadMember' and 'Subsystem'. |
| administrative_contact  | character varying(255) |  | Administrative contact of the member, may be e-mail, phone etc. NB! Not used at the moment! |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |