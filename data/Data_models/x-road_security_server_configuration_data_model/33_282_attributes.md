#### 2.8.2 Attributes

| Name               |            Type             | Modifiers | Description                                                                                                                 |
|:-------------------|:---------------------------:|:----------|:----------------------------------------------------------------------------------------------------------------------------|
| id [PK]            |           bigint            | NOT NULL  | Primary key.                                                                                                                |
| groupmemberid [FK] |           bigint            | NOT NULL  | Identifier of the member or the subsystem who is a member of the local group. References id attribute of IDENTIFIER entity. |
| added              | timestamp without time zone | NOT NULL  | The time when the group member  was added.                                                                                  |
| localgroup_id [FK] |           bigint            |           | The local group. References id attribute of LOCALGROUP entity.                                                              |