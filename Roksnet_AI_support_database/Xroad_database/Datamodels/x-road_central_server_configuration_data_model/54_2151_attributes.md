#### 2.15.1 Attributes

| Name            | Type                        | Modifiers | Description           |
|:----------------|:---------------------------:|:--------- |:-----------------:|
| id [PK]         | integer                     | NOT NULL  | Primary key |
| object_type     | character varying(255)      |           | Specifies the type of the object that the identifier identifies. Possible values, defined in enum ee.ria.xroad.common.identifier.XroadObjectType, are 'MEMBER', 'SUBSYSTEM', 'SERVICE', 'CENTRALSERVICE', 'SERVER'. |
| xroad_instance  | character varying(255)      |           | X-Road instance identifier. Present (otherwise NULL) in identifiers of all types. |
| member_class    | character varying(255)      |           | Member class. Present in identifiers of 'MEMBER', 'SUBSYSTEM', 'SERVER' and 'SERVICE' type.  |
| member_code     | character varying(255)      |           | Member code. Present in identifiers of 'MEMBER', 'SUBSYSTEM, SERVER' and 'SERVICE' type.  |
| subsystem_code  | character varying(255)      |           | Subsystem code. Present in identifiers of 'SUBSYSTEM' and 'SERVICE' type. |
| service_code    | character varying(255)      |           | Service code. Present in identifiers of 'SERVICE' type.  |
| server_code     | character varying(255)      |           | Security Server code. Present in identifiers of 'SERVER' type.  |
| created_at      | timestamp without time zone | NOT NULL  | Record creation time, managed automatically.  |
| updated_at      | timestamp without time zone | NOT NULL  | Record last modified time, managed automatically.  |
| service_version | character varying(255)      |           | X-Road service version. May be present in identifiers of 'SERVICE' type. |