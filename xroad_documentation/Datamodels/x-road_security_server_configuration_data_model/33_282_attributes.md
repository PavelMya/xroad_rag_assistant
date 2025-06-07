#### 2.8.2 Attributes

| Name               |            Type             | Modifiers | Description                                                                                                                 |
|:-------------------|:---------------------------:|:----------|:----------------------------------------------------------------------------------------------------------------------------|
| id [PK]            |           bigint            | NOT NULL  | Primary key.                                                                                                                |
| groupmemberid [FK] |           bigint            | NOT NULL  | Identifier of the member or the subsystem who is a member of the local group. References id attribute of IDENTIFIER entity. |
| added              | timestamp without time zone | NOT NULL  | The time when the group member  was added.                                                                                  |
| localgroup_id [FK] |           bigint            |           | The local group. References id attribute of LOCALGROUP entity.                                                              |

### 2.9 HISTORY

Operations (insertions, updates and deletions of records) on the tables of this database, for the purpose of auditing. Each record corresponds to the change of a single field. The record is created in the manner described in section 1.4. The record is never modified or deleted.